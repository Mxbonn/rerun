#!/usr/bin/env python3

"""Run various rust checks for CI."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
from glob import glob


class Timing:
    def __init__(self, command: str, duration: float) -> None:
        self.command = command
        self.duration = duration


def run_cargo(cargo_cmd, cargo_args: str) -> Timing:
    args = ["cargo", cargo_cmd, "--quiet"] + cargo_args.split(" ")
    cmd_str = subprocess.list2cmdline(args)
    print(f"> {cmd_str}")
    start_time = time.time()

    env = os.environ.copy()
    env["RUSTFLAGS"] = "--deny warnings"
    env["RUSTDOCFLAGS"] = "--deny warnings --deny rustdoc::missing_crate_level_docs"

    result = subprocess.run(args, env=env, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"'{cmd_str}' failed with exit-code {result.returncode}. Output:\n{result.stdout}\n{result.stderr}")
        sys.exit(result.returncode)

    return Timing(cmd_str, time.time() - start_time)


def package_name_from_cargo_toml(cargo_toml_path: str) -> str:
    with open(cargo_toml_path) as file:
        cargo_toml_contents = file.read()
    package_name_result = re.search(r'name\s+=\s"([\w\-_]+)"', cargo_toml_contents)
    if package_name_result is None:
        raise Exception(f"Failed to find package name in '{cargo_toml_path}'")

    return package_name_result.group(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Rust checks and tests")
    parser.add_argument(
        "--skip-check-individual-crates",
        help="If true, don't check individual crates in /crates/.",
        action="store_true",
    )
    parser.add_argument(
        "--skip-check-individual-examples",
        help="If true, don't check individual examples in /examples/rust/.",
        action="store_true",
    )
    parser.add_argument("--skip-docs", help="If true, don't run doc generation.", action="store_true")
    parser.add_argument("--skip-tests", help="If true, don't run tests.", action="store_true")
    args = parser.parse_args()

    # ----------------------

    # NOTE: a lot of these jobs use very little CPU, but we csannot parallelize them because they all take a lock on the `target` directory.

    timings = []

    # First check with --locked to make sure Cargo.lock is up to date.
    timings.append(run_cargo("check", "--locked --all-features"))

    timings.append(run_cargo("fmt", "--all -- --check"))
    timings.append(run_cargo("cranky", "--all-targets --all-features -- --deny warnings"))

    # Check a few important permutations of the feature flags for our `rerun` library:
    timings.append(run_cargo("check", "-p rerun --no-default-features"))
    timings.append(run_cargo("check", "-p rerun --no-default-features --features sdk"))

    # Since features are additive, check crates individually.
    if args.skip_check_individual_examples is not True:
        for cargo_toml_path in glob("./examples/rust/**/Cargo.toml", recursive=True):
            package_name = package_name_from_cargo_toml(cargo_toml_path)
            timings.append(run_cargo("check", f"--no-default-features -p {package_name}"))
            timings.append(run_cargo("check", f"--all-features -p {package_name}"))

    if args.skip_check_individual_crates is not True:
        for cargo_toml_path in glob("./crates/**/Cargo.toml", recursive=True):
            package_name = package_name_from_cargo_toml(cargo_toml_path)
            timings.append(run_cargo("check", f"--no-default-features -p {package_name}"))
            timings.append(run_cargo("check", f"--all-features -p {package_name}"))

    # Doc tests
    if args.skip_docs is not True:
        # Full doc build takes prohibitively long (over 17min as of writing), so we skip it:
        # timings.append(run_cargo("doc", "--all-features"))

        # These take around 3m40s each on CI, but very useful for catching broken doclinks:
        timings.append(run_cargo("doc", "--no-deps --all-features --workspace"))
        timings.append(run_cargo("doc", "--document-private-items --no-deps --all-features --workspace"))

    if args.skip_tests is not True:
        # We first use `--no-run` to measure the time of compiling vs actually running

        # Just a normal `cargo test` should always work:
        timings.append(run_cargo("test", "--all-targets --no-run"))
        timings.append(run_cargo("test", "--all-targets"))

        # Full test of everything:
        timings.append(run_cargo("test", "--all-targets --all-features --no-run"))
        timings.append(run_cargo("test", "--all-targets --all-features"))

    # Print timings overview
    print("-----------------")
    print("Timings:")
    timings.sort(key=lambda timing: timing.duration, reverse=True)
    for timing in timings:
        print(f"{timing.duration:.2f}s \t {timing.command}")


if __name__ == "__main__":
    main()
