# No red flags eval

Use this after a Build or Fix. Answer each check with pass or fail. If any check fails, fix the work before returning it.

For Detect requests, make sure the response names each red flag with its location and a short fix, without rewriting the UI, scoring it, or claiming AI authorship.

## Direction and principles

1. Is there a stated three-line direction (dominant color plus accent plus neutrals; display face plus body face; structural device), and does every visual choice follow from it?
2. Does the direction come from the product, its audience, and its subject, rather than from what looks modern?
3. Were existing brand tokens, fonts, components, and design-system rules preserved?
4. Does each viewport have one dominant element and at most three secondary ones?
5. Is every card, grid, badge, and numbered marker justified by the content it holds?
6. Does hierarchy come from type scale, weight, and spacing rather than from labels, icons, glows, or gradients?
7. Are saturated colors limited to actions, states, and one brand accent, with at most five meaningful colors on the page?
8. Does every animation answer a user action, with at most one orchestrated entrance per page?
9. Is every number, logo, quote, and status real and sourced, or removed?
10. In Fix mode, was the edit the minimum needed, with markup, state, handlers, and component APIs intact?
11. Does every section pass the portability test, or was it replaced with something only this product could show?
12. Are the floors met: 4.5:1 body contrast, 3:1 for large text and UI, visible focus states, 44px touch targets, keyboard reachability, `prefers-reduced-motion` respected?

## Color

1. No purple, indigo, or violet accents, and no purple-to-blue or violet-to-cyan gradients?
2. No gradient text, aurora blobs, orbs, mesh gradients, or particle backgrounds?
3. No neon glows, colored shadows, or glowing borders?
4. Dark mode, if used, chosen for the context with body text passing contrast and no neon accents?
5. No cream-plus-italic-serif-plus-terracotta default, unless the brand defines it?
6. Neutrals tinted toward the brand, no grey text on colored surfaces, no untinted pure black?
7. Tags and categories neutral by default, with color reserved for at most five semantic states that always carry a word?

## Typography

1. No Inter, Roboto, Arial, Open Sans, Lato, or system-ui as the only face, and no reflex reach for Space Grotesk, Geist, Instrument Serif, Fraunces, Syne, or Playfair?
2. At most one eyebrow label on the page, and only where it separates content without a heading?
3. No single-word italic, serif, or colored accents in headlines, and no oversized italic serif hero?
4. Tracking near zero, with no crushed display or spaced-out body text?
5. A clear modular scale with at least a 3x jump between body and the top level, and no 72px+ headline holding a long sentence?
6. Monospace only on code, terminal output, and tabular figures?
7. No middle-dot meta strings, no `WORD — fragment` labels, no `→` glued to buttons, no `01 / 02 / 03` on non-sequences?
8. No eyebrow, headline, and subheadline that repeat the same claim, and no descriptive paragraph under every heading?

## Layout and structure

1. Cards only around bounded, interactive, or repeated units, with no nesting beyond one level and no cards around plain text?
2. No colored left or top accent stripes outside genuine alerts?
3. A radius scale with meaning rather than one radius everywhere?
4. Section order driven by the argument, with anatomy broken at least every two or three sections and container widths and rhythm varied?
5. No three identical icon cards in a row and no bento grid used as a default?
6. One primary action per screen, one page-level filter bar, no metric repeated across tiles?
7. No tilted or fake dashboard mockups, placeholder avatars, or perfect fake charts?
8. Spacing that tightens inside groups and loosens between sections, rather than one gap on everything?

## Components and icons

1. No icon tiles (oversized default-set icon in a rounded pastel square) above headings?
2. Icons only where they replace a word or mark a function, one set, one stroke width, no Sparkles, no emoji icons?
3. No pill above the H1?
4. No colored pill tags on every card or row, no dot inside every badge, "New" badges with an expiry?
5. No pulsing green dot?
6. No unsourced stat banner, faded logo grid, avatar stack, gradient letter avatars, "As seen on", or auto-scrolling marquee?
7. No glassmorphism outside a true overlay with a solid scrim?
8. No full-width gradient pill buttons and no hover scaling?
9. No three-tier pricing with a random "Most popular" ribbon?
10. No auto-forwarding carousels?
11. No core action, form, or detail view hidden in a modal, no nested modals, no modal on load?
12. Feedback only where the outcome is not otherwise visible, nothing under 200ms, errors never auto-dismissed?
13. Empty and error states that explain what happened and what to do next?
14. No floating action button, auto-opening chat bubble, fake-urgency announcement bar, scroll progress bar, or back-to-top button on short pages?
15. Focus-visible, active, disabled, loading, and error states present on interactive elements?

## Motion

1. No fade-and-slide entrance on every section and no lift on every card hover?
2. No bounce, spring, or elastic easing, no `transition: all`, no animated gradient backgrounds?
3. Hover and state changes at 100 to 200ms with ease-out, entrances at 200 to 300ms, exits faster?

## Copy inside the UI

1. No portable headline ("Build the future of…", "Supercharge…", "All-in-one…", "Seamless", "Effortless", "Elevate", "Unlock")?
2. Buttons that say what happens next rather than "Get Started" and "Learn more"?
3. Each claim made once, in the place with the most weight?

## Final read

1. Would a designer who knows the product recognize this as made for it, not for any product?
2. Are fewer than three instant tells present, and ideally none?
3. Does the output include the direction, the full revised or new code, and a short **What changed** section mapping each red flag to its fix?
4. For Detect requests, does the response name each red flag with a location and a short fix, without rewriting, scoring, or claiming AI authorship?
