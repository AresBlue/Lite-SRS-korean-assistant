import PyPDF2
import re, json
def pdf_parser():
    with open("TOPIK1vocab.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    learning_words = []


    for line in text.split("\n"):
        # Skip non-entry lines
        if not re.match(r'^\d+', line):
            continue

        # Split multiple entries in the line (detect number + Korean + English pattern)
        entries = re.findall(r'(\d+)([^\d]+?)\s([^\d]+?)(?=\d|$)', line)
        for entry in entries:
            learning_words.append({"korean": entry[1].strip(), "english": entry[2].strip()})

    with open("learning_vocab.json", "w", encoding="utf-8") as f:
        json.dump(learning_words, f, ensure_ascii=False, indent=2)