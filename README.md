# Ramanujan, Landen, and Baker N-Series Refinement

**Subtitle:** Higher-Degree Modular Gap Laws and a Two-Axis Comparison  
**Author:** Wayne Baker  
**Date:** June 2026  
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
├── .gitignore
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
    └── github_upload_checklist.md
```

## Rights

Copyright © 2026 Wayne Baker. All rights reserved unless otherwise stated.
