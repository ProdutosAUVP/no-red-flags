#!/usr/bin/env python3
"""Build and validate the No Red Flags plugin package.

Usage:
    python scripts/build_plugin.py          # validate, build dist/no-red-flags-plugin-<version>.zip
    python scripts/build_plugin.py --check  # validate and build, then remove the build output
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
SKILL_DIR = ROOT / "skills" / "no-red-flags"
DIST = ROOT / "dist"

REQUIRED_MANIFEST_FIELDS = ("name", "version", "description", "author", "skills", "interface")
REQUIRED_INTERFACE_FIELDS = ("displayName", "shortDescription", "longDescription", "developerName", "category")
MAX_PROMPTS = 3
MAX_PROMPT_LENGTH = 128

PACKAGE_FILES = (
    ".codex-plugin/plugin.json",
    "skills/no-red-flags/SKILL.md",
    "skills/no-red-flags/eval.md",
    "README.md",
    "LICENSE",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and validate the plugin package.")
    parser.add_argument("--check", action="store_true", help="Validate and build, then delete the build output.")
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def load_manifest() -> dict:
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing manifest at {MANIFEST_PATH.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"manifest is not valid JSON: {exc}")
    return {}


def validate_source(manifest: dict) -> None:
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest or manifest[field] in ("", None, [], {}):
            fail(f"manifest is missing required field '{field}'")

    interface = manifest["interface"]
    for field in REQUIRED_INTERFACE_FIELDS:
        if not interface.get(field):
            fail(f"manifest interface is missing required field '{field}'")

    prompts = interface.get("defaultPrompt", [])
    if len(prompts) > MAX_PROMPTS:
        fail(f"defaultPrompt has {len(prompts)} entries, maximum is {MAX_PROMPTS}")
    for prompt in prompts:
        if len(prompt) > MAX_PROMPT_LENGTH:
            fail(f"defaultPrompt entry exceeds {MAX_PROMPT_LENGTH} characters: {prompt!r}")

    for relative in PACKAGE_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing package file {relative}")

    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = skill.split("---", 2)[1]
    if "name: no-red-flags" not in frontmatter:
        fail("SKILL.md frontmatter must declare 'name: no-red-flags'")
    if "description:" not in frontmatter:
        fail("SKILL.md frontmatter must declare a description")


def build_plugin(manifest: dict) -> Path:
    package_name = f"{manifest['name']}-plugin-{manifest['version']}"
    package_dir = DIST / package_name
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True)

    for relative in PACKAGE_FILES:
        target = package_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)

    archive = DIST / f"{package_name}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(package_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(package_dir))
    return archive


def validate_build(manifest: dict, archive: Path) -> None:
    package_dir = DIST / f"{manifest['name']}-plugin-{manifest['version']}"
    for relative in PACKAGE_FILES:
        built = package_dir / relative
        if not built.is_file():
            fail(f"built package is missing {relative}")
        if not filecmp.cmp(ROOT / relative, built, shallow=False):
            fail(f"built file differs from source: {relative}")

    with zipfile.ZipFile(archive) as zf:
        bad = zf.testzip()
        if bad is not None:
            fail(f"zip archive is corrupt at {bad}")
        names = set(zf.namelist())
    missing = [relative for relative in PACKAGE_FILES if relative not in names]
    if missing:
        fail(f"zip archive is missing: {', '.join(missing)}")


def main() -> None:
    args = parse_args()
    manifest = load_manifest()
    validate_source(manifest)
    archive = build_plugin(manifest)
    validate_build(manifest, archive)
    print(f"built {archive.relative_to(ROOT)}")
    if args.check:
        shutil.rmtree(DIST)
        print("check passed, build output removed")


if __name__ == "__main__":
    main()
