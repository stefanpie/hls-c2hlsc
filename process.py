import argparse
import os
import re
import shutil
import sys
import tarfile
import zipfile
from pathlib import Path

from joblib import Parallel, delayed


def get_vitis_hls_clang_pp_path() -> Path:
    vitis_hls_bin_path_str = shutil.which("vitis_hls")
    if vitis_hls_bin_path_str is None:
        raise RuntimeError("vitis_hls not found in PATH")
    vitis_hls_bin_path = Path(vitis_hls_bin_path_str)
    vitis_hls_clang_pp_path = (
        vitis_hls_bin_path.parent.parent
        / "lnx64"
        / "tools"
        / "clang-3.9"
        / "bin"
        / "clang++"
    )
    if not vitis_hls_clang_pp_path.exists():
        raise RuntimeError(
            f"Could not find vitis_hls clang++ bin at {vitis_hls_clang_pp_path}"
        )
    return vitis_hls_clang_pp_path


def get_vitis_hls_include_dir() -> Path:
    vitis_hls_bin_path_str = shutil.which("vitis_hls")
    if vitis_hls_bin_path_str is None:
        raise RuntimeError("vitis_hls not found in PATH")
    vitis_hls_bin_path = Path(vitis_hls_bin_path_str)
    vitis_hls_include_dir = vitis_hls_bin_path.parent.parent / "include"
    return vitis_hls_include_dir


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

    def process_benchmark(design_src_dir: Path):
        design_name = design_src_dir.name
        print(f"Processing {design_name}")
        design_output_dir = output_dir / design_name
        design_output_dir.mkdir(parents=True, exist_ok=True)
        for src_file in design_src_dir.glob("*"):
            shutil.copy(src_file, design_output_dir)

        top_name = None

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
