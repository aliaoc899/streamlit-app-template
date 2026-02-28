# Student Steps

## Step 1 (One-Time Setup)
1. Open this folder (`streamlit-app-template`) in VS Code.
2. In Terminal, move into the project directory:
- `cd streamlit-app-template`
3. Run setup:
- macOS/Linux: `python3 setup_script.py`
- Windows: `python setup_script.py`
4. Wait for `Setup complete.` (do not press `Ctrl+C` during setup).

## What setup_script.py does
- creates/reuses `.venv`
- installs dependencies (`requirements.txt` if present, otherwise built-in defaults)
- sets VS Code to this folder's interpreter

## Step 2 (Run App)
1. Run starter:
- macOS/Linux: `python3 setup_starter.py`
- Windows: `python setup_starter.py`
2. Keep terminal open while app is running.
3. Stop app with `Ctrl+C`.

## Optional: Run Without Starter Script
- macOS/Linux: `./.venv/bin/streamlit run app.py`
- Windows: `.\.venv\Scripts\streamlit.exe run app.py`

## Common Fixes
1. `import streamlit` is underlined in VS Code:
- `Cmd/Ctrl + Shift + P` -> `Python: Select Interpreter`
- choose `.venv/bin/python` (macOS/Linux) or `.venv\Scripts\python.exe` (Windows)

2. `python` not found:
- macOS/Linux: use `python3 ...`
- Windows: use `python ...`

3. `file does not exist` / `No such file or directory`:
- you are likely in the wrong folder
- run `cd ..` once, then `cd streamlit-app-template`
- rerun setup: `python3 setup_script.py` (or `python setup_script.py` on Windows)

4. Wrong environment picked:
- close VS Code
- reopen only this project folder (not its parent folder)
- run `python3 setup_script.py` (or `python` on Windows) again

5. You pressed `Ctrl+C` during setup and `.venv` is broken:
- rerun `python3 setup_script.py` (or `python setup_script.py` on Windows)
- the script now auto-rebuilds incomplete `.venv` folders
