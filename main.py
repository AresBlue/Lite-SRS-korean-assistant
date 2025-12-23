import json
import time
from scripts.Message import *
from scripts import wordlist_state
from scripts import io_handler
from scripts import session
from config import config

def main():
    wrong_words = []
    right_words = []
    session_size = config["session_size"]

    remembered_words, halfmem, lst_total_length, loaded_words = io_handler.import_backup()

    lst_length = len(loaded_words)

    print("\nKorean SRS learning assistant, good luck.")
    spacer()
    message_of_today(lst_length, lst_total_length, len(halfmem))
    spacer()

    remembered_words, right_words, wrong_words = session.interim_session(remembered_words, right_words, wrong_words)

    with open("remembered_words.json", "w", encoding="utf-8") as f:
        json.dump(remembered_words, f, ensure_ascii=False, indent=2)

    halfmem += wrong_words

    for word in right_words:
        try:
            halfmem.remove(word)
        except ValueError:
            pass

    with open("halfmem.json", "w", encoding="utf-8") as f:
        json.dump(halfmem, f, ensure_ascii=False, indent=2)

    available_words = [w for w in loaded_words if w not in remembered_words and w not in halfmem]

    session_size = wordlist_state.word_list_check(session_size, lst_length, halfmem)
    today_session, available_words = session.session(session_size, remembered_words, halfmem, available_words)

    with open("interim.json", "w", encoding="utf-8") as f:
        json.dump(today_session, f, ensure_ascii=False, indent=2)

    if len(available_words) == 0:
        available_words = None # this will make the bat/bash scripts detect the lack of wordlist next run, calling pdf_parser

    with open("learning_vocab.json", "w", encoding="utf-8") as f:
        json.dump(available_words, f, ensure_ascii=False, indent=2)

    print("Today's session:")
    for i, w in enumerate(today_session, start=1):
        print(f"{i}: {w['korean']} - {w['english']}")

    try:
        spacer()
        print("To quit session, please Ctrl+C...\n")
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting SRS learning assistant, please review today's words...")
        time.sleep(1)

if __name__ == "__main__":

    main()