import PyPDF2
import re
import json
import random
import time
import Message
import os

def pdf_parser():
    Message.spacer()

    target_dir = os.path.join(os.path.dirname(__file__), "..")

    local_pdf = []

    for f in os.listdir(target_dir):
        if f.endswith(".pdf"):
            local_pdf.append(f)

    if len(local_pdf) == 0:
        print("No PDF files found, please place PDF files in main directory...")

        while len(local_pdf) == 0:
            time.sleep(10)
            print('...')
            for f in os.listdir(target_dir):
                if f.endswith(".pdf"):
                    local_pdf.append(f)

    for num, pdf in enumerate(local_pdf):
        print(f"{num+1}: {pdf}")

    learning_words = []
    text = ''

    Message.spacer()

    pdf_pointer = int(input("Enter the PDF file's number from above: "))

    while len(text) == 0:
        try:
            with open(f"{local_pdf[pdf_pointer-1]}", "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
        except FileNotFoundError:
            pdf_pointer = int(input("File not found... Please re-enter number: "))

    for line in text.split("\n"):
        if not re.match(r'^\d+', line):
            continue

        entries = re.findall(r'(\d+)([^\d]+?)\s([^\d]+?)(?=\d|$)', line)
        for entry in entries:
            learning_words.append({"korean": entry[1].strip(), "english": entry[2].strip()})
    Message.spacer()
    sample = str(random.choice(learning_words))
    user_input = input(f"If the following is similar to this: 'korean': '경기장', 'english': 'stadium, arena' \nThen enter Y, else, PDF not compatible with parser.\n{sample}\nY/n:")

    if user_input.lower() != "y":
        print("Warning: The import may have formatting issues, please use a different PDF.")
        time.sleep(5)
        exit()
    else:
        print("Import looks good!")
    with open("learning_vocab.json", "w", encoding="utf-8") as f:
        json.dump(learning_words, f, ensure_ascii=False, indent=2)


    if os.path.exists("learning_vocab-static.json"):
        with open("learning_vocab-static.json", "r", encoding="utf-8") as f:
            old_static = json.load(f)

        for word_dict in old_static:
            learning_words.append(word_dict)

    with open("learning_vocab-static.json", "w", encoding="utf-8") as f:
        json.dump(learning_words, f, ensure_ascii=False, indent=2)

    Message.spacer()
    time.sleep(0.1)
    print("Exiting PDF_parser. goodluck...")
    time.sleep(1)

pdf_parser()