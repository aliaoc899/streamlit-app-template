# Streamlit App Template

Template for students to clone and run quickly.
Open this repository folder itself in VS Code (not a parent directory that contains other `.venv` folders).
For full student instructions and troubleshooting, see `STEPS.md`.
If commands say `file does not exist`, run `cd ..` and then `cd streamlit-app-template` before retrying.

## Quick Start (Recommended)
1. From this folder, run one command:
- macOS/Linux:
```bash
python3 setup_starter.py
```
- Windows:
```powershell
python setup_starter.py
```
This will:
- create/reuse `.venv`
- install dependencies (`requirements.txt` if present, otherwise script defaults)
- start `streamlit run app.py`
- set VS Code to use this folder's `.venv` interpreter

If `import streamlit` is still underlined in VS Code:
1. Open Command Palette (`Cmd+Shift+P` on macOS / `Ctrl+Shift+P` on Windows)
2. Run `Python: Select Interpreter`
3. Choose this project interpreter:
- macOS/Linux: `.venv/bin/python`
- Windows: `.venv\\Scripts\\python.exe`

## Setup Then Run Manually
1. Run setup:
- macOS/Linux:
```bash
python3 setup_script.py
```
- Windows:
```powershell
python setup_script.py
```
2. Activate the virtual environment:
- macOS/Linux:
```bash
source .venv/bin/activate
```
- Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
3. Start the app:
```bash
streamlit run app.py
```
Or run without activating:
- macOS/Linux: `./.venv/bin/streamlit run app.py`
- Windows: `.\.venv\Scripts\streamlit.exe run app.py`

## Manual Setup (Alternative)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
