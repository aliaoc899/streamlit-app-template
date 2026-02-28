#!/usr/bin/env python3
"""Set up dependencies (if needed) and launch the Streamlit app."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import setup_student_env


def main() -> int:
    setup_code = setup_student_env.main()
    if setup_code != 0:
        return setup_code

    venv_python = setup_student_env.get_venv_python_path()
    app_file = Path(__file__).resolve().parent / "app.py"

    print("\nStarting Streamlit app...")
    print("Press Ctrl+C to stop.")
    subprocess.run([str(venv_python), "-m", "streamlit", "run", str(app_file)], check=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"\nFailed to start Streamlit (exit code {exc.returncode}).")
        raise SystemExit(exc.returncode)
    except KeyboardInterrupt:
        print("\nStopped.")
        raise SystemExit(0)
