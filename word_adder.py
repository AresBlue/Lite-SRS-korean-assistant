import json
import os
from scripts import io_handler

def word_adder():

    def word_finder(wordlist, user_word):
        for word in wordlist:
            if user_word in word["english"]:
                return word
        return None

    remembered_words, halfmem, _, loaded_words = io_handler.import_backup()
    sources = [loaded_words, halfmem, remembered_words]

    if os.path.exists("interim.json"):

        print("Word_adder starting...")

        with open("interim.json", "r", encoding="utf-8") as f:
            interim_data = json.load(f)

            user_word = input("Enter your word: ").strip().lower()

            found_words = []

            for i, source in enumerate(sources):
                found_word = word_finder(source, user_word)

                if found_word:
                    print(f"Word found! it is: {found_word}")

                    found_words.append((found_word, source))


            if found_words == []:
                print("No words found...")
                translation = input("Please give translation: ").strip()
                interim_data.append({"english": user_word, "translation": translation})

            else:
                print("Found word(s):")
                for i, (w, _) in enumerate(found_words, start=1):
                    print(f"{i}: {w['korean']} - {w['english']}")

                choice = input("Please choose which word you'd like to add by it's number: ")
                try: choice = int(choice)
                except ValueError:
                    choice = input("Please enter a number: ")

                if choice < 1 or choice > len(found_words):
                    choice = int(input("Stay within bounds of the possible word choices please: "))

                word, source = found_words[choice - 1]

                if word in interim_data:
                    print("Word already in interim_data.")
                    return

                if source is loaded_words:
                    loaded_words.remove(word)

                    with open("learning_vocab.json", "w", encoding="utf-8") as f:
                        json.dump(loaded_words, f, ensure_ascii=False, indent=2)

                else:
                    pass

                interim_data.append(word)

            with open("interim.json", "w", encoding="utf-8") as f:
                json.dump(interim_data, f, ensure_ascii=False, indent=2)

    else:
        print("Interim.json not found, ending.")

    return

word_adder()