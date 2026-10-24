# Ramanujan, Landen, and Baker N-Series Refinement

**Subtitle:** Higher-Degree Modular Gap Laws and a Two-Axis Comparison  
**Author:** Wayne Baker  
**Date:** Original June 2026; revised October 21, 2026  
**Status:** Preprint / source and reproducibility archive

This repository contains the paper, LaTeX source, and numerical verification script for:

> **Ramanujan, Landen, and Baker N-Series Refinement: Higher-Degree Modular Gap Laws and a Two-Axis Comparison**

## Read the paper

- [`paper/ramanujan_landen_nseries_refinement.pdf`](paper/ramanujan_landen_nseries_refinement.pdf)
- [`paper/ramanujan_landen_nseries_refinement.tex`](paper/ramanujan_landen_nseries_refinement.tex)

## Main result

Let

\[
\delta(q)=\frac{1-k'(q)}{1+k'(q)},
\qquad
k'(q)=\sqrt{1-\lambda(q)},
\qquad
\lambda(q)=\frac{\vartheta_2(q)^4}{\vartheta_3(q)^4}.
\]

For every fixed integer \(m\ge 2\), the paper proves

\[
\frac{\delta(q^m)}{\delta(q)^m}
=
4^{1-m}\left(1+4m q^2+O(q^4)\right),
\qquad q\to0.
\]

Thus the classical leading limit

\[
\frac{\delta(q^m)}{\delta(q)^m}\longrightarrow 4^{1-m}
\]

has a first-correction coefficient governed by the linear degree law \(4m\).

## AGM linkage

For the normalized Gauss-Legendre AGM gap

\[
\delta_n=\frac{a_n-b_n}{a_n+b_n},
\]

and the fitted dynamic correction coefficient

\[
\alpha_n=-\frac{\pi_{n+1}-\pi}{\pi_{n+1}-\pi_n},
\]

the paper rewrites the classical AGM error law in the gap variable and obtains

\[
\frac{\alpha_n}{\delta_n^2}\longrightarrow\frac18.
\]

This is consistent with the companion coefficient law

\[
\frac{\alpha_{n+1}}{\alpha_n^2}\longrightarrow\frac12.
\]

## Scope

The comparison is structural, not identificational:

- Ramanujan's ellipse approximation acts along an eccentricity axis.
- Fixed N-series refinement cancels an even-power hierarchy in the resolution variable \(N^{-2}\).
- The Landen transformation contracts the normalized modular gap quadratically.
- The companion Baker \(4{:}3\) trisection cascade contracts a normalized signed angular error cubically.

The paper does **not** claim that fixed N-series extrapolation or the trisection cascade is a modular transformation.

## Publication and scope

This is a **verified revised preprint currently held in a private repository**. The fixed-degree first-correction
coefficient follows from the classical theta expansion; its use here is a careful
comparison with different resolution and geometric trisection error mechanisms.
No common operator, conjugacy or new modular transformation is claimed.

The current TeX and the rebuilt nine-page PDF are paired in the `paper/` folder.
The exact committed verification script passed GitHub Actions at 400-digit
precision, with downloadable CSV artifacts:
[successful verification run](https://github.com/CWBaker360/ramanujan-landen-nseries-refinement/actions/runs/39671843702).
The paper remains a preprint and has not been independently peer-reviewed.

## Numerical verification

The script

```text
scripts/verify_modular_gap_law.py
```

reproduces the modular-gap values reported in the paper and independently checks the finite AGM linkage diagnostics.

Run from the repository root:

```bash
python scripts/verify_modular_gap_law.py --precision 400 --outdir outputs
```

The script writes:

```text
outputs/modular_gap_law.csv
outputs/agm_linkage_law.csv
outputs/verification_summary.txt
outputs/modular_gap_sweep.csv
```

## Related repositories

- [`nseries-pi-acceleration`](https://github.com/CWBaker360/nseries-pi-acceleration)
- [`agm-prefactor-coefficient-law`](https://github.com/CWBaker360/agm-prefactor-coefficient-law)
- [`constructible-cubic-trisection`](https://github.com/CWBaker360/constructible-cubic-trisection)
- [`proportional-subtended-cubic-refinement`](https://github.com/CWBaker360/proportional-subtended-cubic-refinement)

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── REPRODUCIBILITY.md
├── LICENSE_NOTICE.md
├── CHANGELOG.md
├── SHA256SUMS.txt
├── .github/workflows/verify-numerics.yml
├── paper/
│   ├── ramanujan_landen_nseries_refinement.tex
│   ├── ramanujan_landen_nseries_refinement.pdf
│   └── README.md
├── scripts/
│   ├── verify_modular_gap_law.py
│   └── README.md
└── docs/
    ├── abstract.md
    ├── repository_description.md
    ├── github_upload_checklist.md
    └── release_verification_2026-10-21.md
```

## Rights

Copyright © 2026 Wayne Baker. All rights reserved unless otherwise stated.

## Manuscript review status (October 24, 2026)

The PDF and LaTeX files currently in `paper/` are the repository's existing published/preprint versions. A subsequent editorial and mathematical review has identified proposed clarifications for a future revision. Those revisions have **not** been merged into this repository, and the current PDF must not be described as incorporating them. Existing numerical verification scripts and results are unchanged. A revised source/PDF pair will be considered separately after a source-to-PDF consistency check and further mathematical review. This status notice makes no new scientific or priority claim.
