import json
import os
from scripts import io_handler

def word_adder():

    def word_finder(wordlist, user_word):
        for word in wordlist:
            if user_word == word["english"]:
                return word
        return None

    def interim_save(interim_data):
        with open("interim.json", "w", encoding="utf-8") as f:
            json.dump(interim_data, f, ensure_ascii=False, indent=2)

    remembered_words, halfmem, _, loaded_words = io_handler.import_backup()
    sources = [loaded_words, halfmem, remembered_words]

    if os.path.exists("interim.json"):

        print("Word_adder starting...")

        with open("interim.json", "r", encoding="utf-8") as f:
            interim_data = json.load(f)

            user_word = input("Enter your word: ").strip().lower()

            if word_finder(interim_data, user_word):
                print("Word already in interim_data.")
                return

            for source in sources:
                found_word = word_finder(source, user_word)

                if found_word:
                    interim_data.append(found_word)

                    print(f"Word found! word is: {found_word} and has been added to interim_data.")

                    if source is loaded_words:
                        source.remove(found_word)

                        with open("learning_vocab.json", "w", encoding="utf-8") as f:
                            json.dump(loaded_words, f, ensure_ascii=False, indent=2)

                    break

            else:
                translation = input("Word not present anywhere... please give translation: ").strip()
                interim_data.append({"english": user_word, "translation": translation})

            interim_save(interim_data)

    else:
        print("Interim.json not found, ending.")

    return

word_adder()