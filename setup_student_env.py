#!/usr/bin/env python3
"""Set up a local virtual environment and install dependencies."""

from __future__ import annotations

import json
import os
import subprocess
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS_FILE = ROOT / "requirements.txt"
VSCODE_SETTINGS_FILE = ROOT / ".vscode" / "settings.json"


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


def get_vscode_interpreter_path() -> str:
    if os.name == "nt":
        return r"${workspaceFolder}\.venv\Scripts\python.exe"
    return "${workspaceFolder}/.venv/bin/python"


def configure_vscode_interpreter() -> None:
    # If we are in a subdirectory of the workspace (likely), we should try to
    # update the workspace settings if possible, or just use absolute paths.
    # But for simplicity in this template, let's just make sure the local
    # settings file uses an absolute path so it works regardless of how
    # the project is opened (if the user opens this specific folder).
    
    VSCODE_SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    settings: dict[str, object] = {}
    if VSCODE_SETTINGS_FILE.exists():
        try:
            settings = json.loads(VSCODE_SETTINGS_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass  # Start fresh if invalid

    # Use absolute path to ensure it works even if workspace root is different
    # or if it's a nested folder.
    settings["python.defaultInterpreterPath"] = str(get_venv_python_path())
    settings["python.terminal.activateEnvironment"] = True
    
    VSCODE_SETTINGS_FILE.write_text(
        json.dumps(settings, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("Updated local VS Code settings for .venv interpreter.")


def main() -> int:
    # Ensure consistent working directory (script folder)
    os.chdir(ROOT)

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
    configure_vscode_interpreter()

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
