# Reproducibility

## Paper compilation

From the `paper` directory:

```bash
pdflatex ramanujan_landen_nseries_refinement.tex
pdflatex ramanujan_landen_nseries_refinement.tex
```

The second pass settles cross-references and bibliography labels.

## Python environment

Required:

```text
Python 3.10 or later
mpmath
```

Install the dependency with:

```bash
python -m pip install mpmath
```

## Reproduce the numerical diagnostics

From the repository root:

```bash
python scripts/verify_modular_gap_law.py --precision 400 --outdir outputs
```

The default nome is

```text
q = 1e-12
```

and the default modular degrees are

```text
m = 2, 3, 4, 5, 6
```

The script writes:

```text
outputs/modular_gap_law.csv
outputs/agm_linkage_law.csv
outputs/verification_summary.txt
```

## Quantities computed

The modular calculation uses

\[
\lambda(q)=\frac{\vartheta_2(q)^4}{\vartheta_3(q)^4},
\qquad
\delta(q)=\frac{1-\sqrt{1-\lambda(q)}}{1+\sqrt{1-\lambda(q)}}.
\]

For fixed \(m\), it evaluates

\[
R_m(q)=\frac{\delta(q^m)}{\delta(q)^m}
\]

and

\[
C_m(q)=\frac{1}{q^2}\left(\frac{R_m(q)}{4^{1-m}}-1\right).
\]

The paper predicts

\[
R_m(q)\to4^{1-m},
\qquad
C_m(q)\to4m.
\]

The AGM calculation reconstructs the lower Gauss-Legendre sequence and evaluates

\[
\frac{\alpha_n}{\delta_n^2}
\quad\text{and}\quad
\frac{\alpha_{n+1}}{\alpha_n^2},
\]

which approach \(1/8\) and \(1/2\), respectively.

## Interpretation

The numerical outputs illustrate the asymptotic laws and check the implementation. The higher-degree modular gap law is proved analytically in the paper from the small-nome theta-function expansion. The AGM linkage uses the cited classical error asymptotic.
