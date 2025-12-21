@echo off
IF NOT EXIST ".venv" python -m venv .venv
call .venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

IF EXIST "learning_vocab.json" (
    for %%F in (learning_vocab.json) do (
        if %%~zF==0 (
            echo learning_vocab.json exists but is empty, removing file...
            del "learning_vocab.json"
        )
    )
)

IF NOT EXIST "learning_vocab.json" (
    echo learning_vocab.json missing, running PDF_parser...
    python scripts\PDF_parser.py
)

python main.py


