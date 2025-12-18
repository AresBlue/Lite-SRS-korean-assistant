@echo off
IF NOT EXIST ".venv" python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

IF NOT EXIST "learning_vocab.json" (
    echo learning_vocab.json missing, running PDF_parser...
    python scripts\PDF_parser.py
)

python main.py %*
