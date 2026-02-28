#!/usr/bin/env python3
"""Set up a local virtual environment and install dependencies."""

from __future__ import annotations

import os
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS_FILE = ROOT / "requirements.txt"


def run_command(cmd: list[str], description: str) -> None:
    print(f"\n==> {description}")
    subprocess.run(cmd, check=True)


def get_venv_python_path() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def get_activation_hint() -> str:
    if os.name == "nt":
        return r".\.venv\Scripts\Activate.ps1"
    return "source .venv/bin/activate"


def get_direct_streamlit_command() -> str:
    if os.name == "nt":
        return r".\.venv\Scripts\streamlit.exe run app.py"
    return "./.venv/bin/streamlit run app.py"


def main() -> int:
    if not REQUIREMENTS_FILE.exists():
        print(f"Could not find requirements file: {REQUIREMENTS_FILE}")
        return 1

    if VENV_DIR.exists():
        print("Virtual environment already exists at .venv. Reusing it.")
    else:
        print("Creating virtual environment at .venv ...")
        venv.EnvBuilder(with_pip=True).create(VENV_DIR)

    venv_python = get_venv_python_path()
    if not venv_python.exists():
        print(f"Could not find virtual environment Python at: {venv_python}")
        return 1

    run_command(
        [str(venv_python), "-m", "pip", "install", "--upgrade", "pip"],
        "Upgrading pip",
    )
    run_command(
        [str(venv_python), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)],
        "Installing dependencies",
    )

    print("\nSetup complete.")
    print(f"Activate environment: {get_activation_hint()}")
    print("Then run: streamlit run app.py")
    print(f"Or run directly: {get_direct_streamlit_command()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"\nA setup command failed (exit code {exc.returncode}).")
        raise SystemExit(exc.returncode)
