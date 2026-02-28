# Streamlit App Template

Template for students to clone and run quickly.
Open this repository folder itself in VS Code (not a parent directory that contains other `.venv` folders).

## Quick Start (Recommended)
1. From this folder, run one command:
- macOS/Linux:
```bash
python3 start_student_app.py
```
- Windows:
```powershell
python start_student_app.py
```
This will:
- create/reuse `.venv`
- install dependencies
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
python3 setup_student_env.py
```
- Windows:
```powershell
python setup_student_env.py
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
