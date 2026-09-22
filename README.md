# No Red Flags

Remove 40+ design red flags that make an interface look AI-generated, without flattening the product's own brand.

## Problem

AI makes it easy to generate clean interfaces that all look the same. Ask any coding agent for a landing page, a dashboard, or a settings screen and you get some version of:

- A purple-to-blue gradient in the hero, or a cream background with a big italic serif.
- Everything wrapped in a rounded card, with cards inside cards.
- A tiny uppercase "eyebrow" label above every single heading.
- Colored pill tags on every row, and a pulsing green dot that says "Live".
- An oversized Lucide icon in a pastel square above three identical feature cards.
- "Trusted by" logos at 40% opacity, "10k+ users · 99.9% uptime", and "Supercharge your workflow".

None of it is wrong on its own. Together it is design with no author: the statistical average of ten thousand interfaces, shipped without anyone asking whether it should look like this. Readers now recognize the pattern in under a second, and generic reads as untrustworthy.

When you use AI to fix a UI, it also tends to smooth away the decisions that made the product look like itself.

## How to install No Red Flags

The easiest way to install the skill is to paste this into Claude Code, Codex, or your favorite coding agent:

```text
Install the /no-red-flags skill globally from https://github.com/produtosauvp/no-red-flags
```

You can also install it with `npx`:

```sh
npx skills add produtosauvp/no-red-flags --skill no-red-flags --global --yes
```

Or copy the folder by hand:

```sh
# Project-level
cp -r skills/no-red-flags .claude/skills/no-red-flags

# User-level
cp -r skills/no-red-flags ~/.claude/skills/no-red-flags
```

## How to use No Red Flags

### Fix a UI

```text
/no-red-flags (paste your component, page, or CSS)
```

The skill audits the code, states a design direction, makes the minimum effective edit, keeps your brand and functionality, and lists what it changed.

### Build a UI

```text
/no-red-flags build a pricing page for (product)
```

The skill commits to a direction first (palette, type, structure) and builds so that none of the red flags appear.

### Detect red flags

```text
/no-red-flags is this slop? (paste code or attach a screenshot)
```

The skill names every red flag it found, points to the element, and gives the fix in a few words. It does not guess whether AI made it.

### Generate slop for fun

```text
Draft the most AI-slop landing page possible for (product)
```

Use it to see every red flag in one place, as satire or as a training example.

## The red flags this skill catches

No Red Flags checks 40+ patterns across color, typography, layout, components, motion, and copy, including:

1. **The purple gradient.** Indigo-to-violet on heroes, buttons, and text.
2. **The cream default.** Off-white background, italic serif headline, terracotta accent.
3. **Cardocalypse.** Everything in a rounded card, cards inside cards.
4. **Accent stripe cards.** A thick colored left border on a panel.
5. **Eyebrow on everything.** A tracked-out ALL-CAPS label above every heading.
6. **Icon tiles.** An oversized Lucide or Heroicons glyph in a pastel square above a heading.
7. **Colored pill tags.** A different badge color for every value, a dot in every badge.
8. **The pulsing dot.** `animate-pulse` next to "Live" or "Available".
9. **Fake social proof.** "10k+ users", faded logo rows, avatar stacks, "As seen on".
10. **Glassmorphism and glows.** `backdrop-blur` panels and neon box shadows.
11. **The conveyor belt.** Centered hero, three cards, logos, stats, testimonials, FAQ, CTA.
12. **Zero hierarchy.** Everything present, nothing emphasized.
13. **Modal dumping.** Core actions hidden behind pop-ups.
14. **Fade-and-slide on everything.** Every section animates in, every card lifts on hover.
15. **Portable headlines.** "Build the future of work", "Supercharge", "Seamless".

It also checks the fundamentals: one dominant element per viewport, hierarchy from type rather than decoration, color with a job, honest content, and the accessibility floors (contrast, focus states, touch targets, reduced motion).

## What's inside

- [`SKILL.md`](skills/no-red-flags/SKILL.md) contains the principles, the full red-flag catalog with fixes, the allowed exceptions, the audit grep patterns, and the workflow.
- [`eval.md`](skills/no-red-flags/eval.md) contains the checks the skill runs on its own work.
- [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) contains the Codex plugin metadata.
- [`build_plugin.py`](scripts/build_plugin.py) builds and validates the plugin package.

## Research

The catalog was assembled from designers, engineers, and tooling that measured these patterns in the wild:

- Paul Bakaus, [AI slop design tells](https://www.linkedin.com/posts/paulbakaus_ai-slop-design-tells-design-anti-patterns-activity-7416272383017164800-10DR) and [Impeccable by Design](https://www.paulbakaus.com/impeccable-by-design/). Measured across thousands of generated pages: 74% used the cream default background, 76% reached for extreme letter-spacing, 90%+ failed the contrast floor.
- Adrian Krebs, [Scoring Show HN submissions for AI design patterns](https://www.adriankrebs.ch/blog/design-slop/) and [design-slop-cop](https://github.com/AdrianKrebs/design-slop-cop). 1,590 landing pages scored with deterministic CSS and DOM checks: 22% heavy slop, 32% mild, 46% clean.
- [slop-detect](https://github.com/ravidsrk/slop-detect), a 27-pattern fingerprint with weights (slop fonts, vibe purple, eyebrow pill, cream background, nested cards, crushed tracking).
- Kosta, [Spot the Slop: A UI Designer's Guide to Fixing AI Defaults](https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c). "Slop is design with no author."
- Developers Digest, [AI Design Slop: 16 Patterns That Out Your App as Vibe-Coded](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it).
- Christian Schaffner, [AI slop isn't a content problem, it's a design problem](https://www.linkedin.com/pulse/ai-slop-isnt-content-problem-its-design-christian-schaffner-6qhcc).
- Anthropic, [Prompting for frontend aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics) and the [frontend-design skill](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design), which name the cream-serif-terracotta cluster, tracked-out eyebrow labels, middle-dot meta strings, and single-word headline accents as tells.
- Adam Wathan's [apology](https://x.com/adamwathan/status/1953510802159219096) for making every Tailwind UI button `bg-indigo-500`, the origin of the purple problem.
- [Ferousco-dev/anti-slop-design](https://github.com/Ferousco-dev/anti-slop-design), [wwewtech/anti-slop-design](https://github.com/wwewtech/anti-slop-design), [funboy322/avoid-ai-design](https://github.com/funboy322/avoid-ai-design), and [Vanszs/Anti-AI-UI](https://github.com/Vanszs/Anti-AI-UI), prior skills whose catalogs were cross-checked against this one.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable), whose detector rules for the italic-serif display headline and the hero eyebrow chip informed the thresholds used here.

Modeled on [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), the writing counterpart of this skill.

## License

MIT
