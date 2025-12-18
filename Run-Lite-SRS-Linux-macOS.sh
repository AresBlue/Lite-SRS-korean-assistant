#!/bin/bash

[ ! -d ".venv" ] && python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f "learning_vocab.json" ]; then
    echo "learning_vocab.json missing, running PDF_parser please have vocab list PDF in main directory..."
    python scripts/PDF_parser.py
fi

python main.py
