import PyPDF2
import re, json, random, time
import Message

def pdf_parser():
    Message.spacer()
    pdf_pointer = input("Please enter pdf file name without file extension('example', not 'example.pdf'): ")
    text = ""
    while len(text) == 0:
        try:
            with open(f"{pdf_pointer}.pdf", "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
        except FileNotFoundError:
            pdf_pointer = input("File not found... please check PDF name and try again('example', not 'example.pdf'): ")

    learning_words = []

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
    with open("learning_vocab-static.json", "w", encoding="utf-8") as f:
        json.dump(learning_words, f, ensure_ascii=False, indent=2)

    Message.spacer()
    time.sleep(0.1)
    print("Exiting PDF_parser. goodluck...")
    time.sleep(1)

pdf_parser()