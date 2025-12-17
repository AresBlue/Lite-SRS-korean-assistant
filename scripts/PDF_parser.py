import PyPDF2
import re, json, random

def pdf_parser():
    with open("TOPIK1vocab.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    learning_words = []

    for line in text.split("\n"):
        if not re.match(r'^\d+', line):
            continue

        entries = re.findall(r'(\d+)([^\d]+?)\s([^\d]+?)(?=\d|$)', line)
        for entry in entries:
            learning_words.append({"korean": entry[1].strip(), "english": entry[2].strip()})

    sample = learning_words[random.randint(0, len(learning_words) - 1)]
    user_input = input(f"If the following is similar to this: 'korean': '경기장', 'english': 'stadium, arena' \nThen enter Y, else, PDF not compatable with parser.\n{sample}\nY/n:")

    if user_input.lower() != "y":
        print("Warning: The import may have formatting issues.")
    else:
        print("Import looks good!")
    with open("learning_vocab.json", "w", encoding="utf-8") as f:

        json.dump(learning_words, f, ensure_ascii=False, indent=2)

pdf_parser()
