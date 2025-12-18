@echo off
IF NOT EXIST ".venv" python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

FOR /F %%i IN ('python -c "import json,os; print(len(json.load(open('learning_vocab.json')))) if os.path.exists('learning_vocab.json') else 0"') DO SET LEN=%%i
IF %LEN%==0 (
    echo learning_vocab.json missing or empty, running initialization...
    python scripts\PDF_parser.py
)

python main.py %*