#!/usr/bin/env python3
"""Numerical checks for the Ramanujan-Landen-N-series refinement paper.

The script verifies:
  1. R_m(q) = delta(q^m) / delta(q)^m -> 4^(1-m),
  2. C_m(q) = q^(-2) * (R_m(q)/4^(1-m) - 1) -> 4m,
  3. alpha_n / delta_n^2 -> 1/8 for the Gauss-Legendre AGM sequence,
  4. alpha_(n+1) / alpha_n^2 -> 1/2.

It writes CSV files and a plain-text summary into the requested output directory.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

import mpmath as mp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify the modular gap and AGM linkage laws."
    )
    parser.add_argument(
        "--precision",
        type=int,
        default=400,
        help="Decimal working precision (default: 400).",
    )
    parser.add_argument(
        "--q",
        default="1e-12",
        help="Positive nome used for the displayed modular-gap check (default: 1e-12).",
    )
    parser.add_argument(
        "--m-min",
        type=int,
        default=2,
        help="Smallest modular degree (default: 2).",
    )
    parser.add_argument(
        "--m-max",
        type=int,
        default=6,
        help="Largest modular degree (default: 6).",
    )
    parser.add_argument(
        "--agm-rows",
        type=int,
        default=6,
        help="Number of AGM linkage rows, starting at n=0 (default: 6).",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("outputs"),
        help="Output directory (default: outputs).",
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Write outputs without enforcing the built-in numerical checks.",
    )
    return parser.parse_args()


def fmt(value: mp.mpf, digits: int = 70) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def modular_delta(q: mp.mpf) -> mp.mpf:
    """Return delta(q) = (1-k')/(1+k') from theta functions."""
    theta2 = mp.jtheta(2, 0, q)
    theta3 = mp.jtheta(3, 0, q)
    lam = (theta2 / theta3) ** 4
    k_prime = mp.sqrt(1 - lam)
    return (1 - k_prime) / (1 + k_prime)


def modular_rows(q: mp.mpf, degrees: Iterable[int]) -> list[dict[str, object]]:
    delta_q = modular_delta(q)
    rows: list[dict[str, object]] = []
    for m in degrees:
        limit = mp.power(4, 1 - m)
        ratio = modular_delta(q**m) / (delta_q**m)
        correction = (ratio / limit - 1) / (q**2)
        rows.append(
            {
                "m": m,
                "q": q,
                "ratio": ratio,
                "predicted_limit": limit,
                "ratio_error": ratio - limit,
                "correction": correction,
                "predicted_correction": mp.mpf(4 * m),
                "correction_error": correction - 4 * m,
            }
        )
    return rows


def agm_rows(count: int) -> list[dict[str, object]]:
    """Compute lower Gauss-Legendre approximants and linkage diagnostics."""
    # Need count+2 approximants to form alpha_(n+1)/alpha_n^2 through count-2.
    a = mp.mpf(1)
    b = 1 / mp.sqrt(2)
    t = mp.mpf(1) / 4
    p = mp.mpf(1)

    approximants: list[tuple[mp.mpf, mp.mpf]] = []
    for _ in range(count + 2):
        pi_n = (a + b) ** 2 / (4 * t)
        delta_n = (a - b) / (a + b)
        approximants.append((pi_n, delta_n))

        a_next = (a + b) / 2
        b_next = mp.sqrt(a * b)
        t_next = t - p * (a - a_next) ** 2
        p_next = 2 * p
        a, b, t, p = a_next, b_next, t_next, p_next

    alphas: list[mp.mpf] = []
    for n in range(count + 1):
        eps_n = approximants[n][0] - mp.pi
        eps_next = approximants[n + 1][0] - mp.pi
        alphas.append(-eps_next / (eps_next - eps_n))

    rows: list[dict[str, object]] = []
    for n in range(count):
        delta_n = approximants[n][1]
        alpha_n = alphas[n]
        coeff_ratio = alphas[n + 1] / alpha_n**2 if n + 1 < len(alphas) else mp.nan
        rows.append(
            {
                "n": n,
                "delta_n": delta_n,
                "alpha_n": alpha_n,
                "alpha_over_delta_squared": alpha_n / delta_n**2,
                "alpha_next_over_alpha_squared": coeff_ratio,
            }
        )
    return rows


def write_modular_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = [
        "m",
        "q",
        "ratio",
        "predicted_limit",
        "ratio_error",
        "correction",
        "predicted_correction",
        "correction_error",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] if k == "m" else fmt(row[k]) for k in fields})


def write_agm_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = [
        "n",
        "delta_n",
        "alpha_n",
        "alpha_over_delta_squared",
        "alpha_next_over_alpha_squared",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] if k == "n" else fmt(row[k]) for k in fields})


def run_checks(
    q: mp.mpf,
    modular: list[dict[str, object]],
    agm: list[dict[str, object]],
) -> None:
    if not (0 < q < 1):
        raise ValueError("q must satisfy 0 < q < 1")

    # At q=1e-12, the ratio error is O(q^2) and the correction error is O(q^2).
    ratio_tol = 100 * q**2
    correction_tol = 1000 * q**2
    for row in modular:
        if abs(row["ratio_error"]) > ratio_tol:
            raise AssertionError(f"modular ratio check failed for m={row['m']}")
        if abs(row["correction_error"]) > correction_tol:
            raise AssertionError(f"first-correction check failed for m={row['m']}")

    # The finite AGM rows should move monotonically toward the limiting constants.
    linkage_errors = [abs(row["alpha_over_delta_squared"] - mp.mpf(1) / 8) for row in agm]
    coeff_errors = [abs(row["alpha_next_over_alpha_squared"] - mp.mpf(1) / 2) for row in agm]
    if any(b >= a for a, b in zip(linkage_errors, linkage_errors[1:])):
        raise AssertionError("AGM one-eighth linkage errors are not decreasing")
    if any(b >= a for a, b in zip(coeff_errors, coeff_errors[1:])):
        raise AssertionError("AGM coefficient-ratio errors are not decreasing")


def write_summary(
    path: Path,
    precision: int,
    q: mp.mpf,
    modular: list[dict[str, object]],
    agm: list[dict[str, object]],
    checks_run: bool,
) -> None:
    lines = [
        "Ramanujan-Landen-N-series numerical verification",
        "=" * 51,
        f"working_precision_dps: {precision}",
        f"nome_q: {fmt(q, 30)}",
        f"checks_run: {checks_run}",
        "",
        "Modular gap diagnostics",
        "-----------------------",
    ]
    for row in modular:
        lines.append(
            f"m={row['m']}: R_m={fmt(row['ratio'], 35)}, "
            f"C_m={fmt(row['correction'], 35)}"
        )

    lines.extend(["", "AGM linkage diagnostics", "-----------------------"])
    for row in agm:
        lines.append(
            f"n={row['n']}: alpha/delta^2={fmt(row['alpha_over_delta_squared'], 35)}, "
            f"alpha_next/alpha^2={fmt(row['alpha_next_over_alpha_squared'], 35)}"
        )

    lines.extend(
        [
            "",
            "Interpretation",
            "--------------",
            "The finite computations illustrate the limits 4^(1-m), 4m, 1/8, and 1/2.",
            "The analytic proofs and scope qualifications are given in the paper.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    if args.precision < 100:
        raise ValueError("Use at least 100 decimal digits; 400 is recommended.")
    if args.m_min < 2 or args.m_max < args.m_min:
        raise ValueError("Require 2 <= m-min <= m-max.")
    if args.agm_rows < 2:
        raise ValueError("agm-rows must be at least 2.")

    mp.mp.dps = args.precision
    q = mp.mpf(args.q)
    degrees = range(args.m_min, args.m_max + 1)

    modular = modular_rows(q, degrees)
    agm = agm_rows(args.agm_rows)

    if not args.skip_checks:
        run_checks(q, modular, agm)

    args.outdir.mkdir(parents=True, exist_ok=True)
    write_modular_csv(args.outdir / "modular_gap_law.csv", modular)
    write_agm_csv(args.outdir / "agm_linkage_law.csv", agm)
    write_summary(
        args.outdir / "verification_summary.txt",
        args.precision,
        q,
        modular,
        agm,
        not args.skip_checks,
    )

    print(f"Verification complete: {args.outdir}")
    print(f"m range: {args.m_min}..{args.m_max}")
    print(f"q: {args.q}")
    print(f"precision: {args.precision} dps")


if __name__ == "__main__":
    main()
