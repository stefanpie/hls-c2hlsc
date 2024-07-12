import argparse
import os
import re
import shutil
import sys
import tarfile
import zipfile
from pathlib import Path

from joblib import Parallel, delayed


def gather_kernel_description() -> dict[str, str]:
    kernel_descriptions: dict[str, str] = {}
    kernel_description_md = (
        Path(__file__).parent / "kernel_descriptions" / "kernel_descriptions.md"
    )
    kernel_description_md_text = kernel_description_md.read_text()
    kernel_description_md_text = kernel_description_md_text.replace(
        "# Kernel Descriptions", ""
    )

    kernel_header_matches = list(re.finditer("## (.+)", kernel_description_md_text))
    kernel_header_match_text = [match.group(1) for match in kernel_header_matches]
    kernel_header_locs_start = [match.span()[0] for match in kernel_header_matches]
    for i in range(len(kernel_header_locs_start)):
        if i < len(kernel_header_locs_start) - 1:
            kernel_descriptions[kernel_header_match_text[i]] = (
                kernel_description_md_text[
                    kernel_header_locs_start[i] : kernel_header_locs_start[i + 1]
                ]
            )
        else:
            kernel_descriptions[kernel_header_match_text[i]] = (
                kernel_description_md_text[kernel_header_locs_start[i] :]
            )

    kernel_descriptions = {k: v.strip() for k, v in kernel_descriptions.items()}

    return kernel_descriptions


def main(args: argparse.Namespace):
    n_jobs: int = args.jobs

    benchmark_src_dir: Path = args.benchmark_src_dir
    output_dir: Path = args.output_directory
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file: Path = args.output_file

    if not benchmark_src_dir.exists():
        raise FileNotFoundError(
            "Benchmark source directory not found at {}".format(benchmark_src_dir)
        )

    design_src_dirs = sorted(benchmark_src_dir.glob("*"))

    kernel_descriptions = gather_kernel_description()

    def process_benchmark(design_src_dir: Path):
        design_name = design_src_dir.name
        print(f"Processing {design_name}")
        design_output_dir = output_dir / design_name
        design_output_dir.mkdir(parents=True, exist_ok=True)
        for src_file in design_src_dir.glob("*"):
            shutil.copy(src_file, design_output_dir)

        # make a kernel_description.md
        kernel_description = kernel_descriptions[design_name]
        kernel_description_fp = design_output_dir / "kernel_description.md"
        kernel_description_fp.write_text(kernel_description)

    Parallel(n_jobs=n_jobs)(
        delayed(process_benchmark)(benchmark) for benchmark in design_src_dirs
    )

    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(output_dir, arcname=output_dir.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "benchmark_src_dir",
        type=Path,
        nargs="?",
        default=Path("./hls-c2hlsc-src/"),
        help="Path to the input benchmark source directory",
    )
    parser.add_argument(
        "output_directory",
        type=Path,
        nargs="?",
        default=Path("./hls-c2hlsc/"),
        help="Generated output directory with processed benchmarks",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        nargs="?",
        default=Path("./hls-c2hlsc.tar.gz"),
        help="Generated output tar.gz file with processed benchmarks",
    )
    parser.add_argument(
        "-j",
        "--jobs",
        type=int,
        nargs="?",
        default=1,
        help="Number of jobs to run in parallel",
    )

    args = parser.parse_args()
    main(args)
