# Paper and revision status

This directory currently contains:

```text
ramanujan_landen_nseries_refinement.tex
ramanujan_landen_nseries_refinement.pdf
```

**Important:** The October 21, 2026 changelog records a working source revision after the packaged `preprint-v1` PDF. The TeX and PDF have **not** been certified as a matching build. Do not treat the PDF as representing all current TeX edits. The repository's `CITATION.cff` continues to describe the earlier `preprint-v1` citation until a revised paper is approved and released.

From the `paper` directory, a local rebuild can be attempted with:

```bash
pdflatex -halt-on-error ramanujan_landen_nseries_refinement.tex
pdflatex -halt-on-error ramanujan_landen_nseries_refinement.tex
```

Rebuilding does not, by itself, verify the mathematics or certify identity with the previously checked-in PDF. Regenerate version metadata and checksums only as part of a controlled release after review.
