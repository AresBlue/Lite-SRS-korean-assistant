import json
from scripts import Message, wordlist_state, io_handler, session

def main():
    wrong_words = []
    right_words = []
    SESSION_SIZE = 34 #set to whatever you want, future me :)

    remembered_words, halfmem, lst_total_length, loaded_words = io_handler.import_backup()

    lst_length = len(loaded_words)

    print("\nKorean SRS learning assistant, good luck.")
    print("--------------------"*4)
    Message.message_of_today(lst_length, lst_total_length, len(halfmem))
    print("--------------------"*4)


    remembered_words, right_words, wrong_words = interim_session(remembered_words, right_words, wrong_words)


    with open("remembered_words.json", "w", encoding="utf-8") as f:
        json.dump(remembered_words, f, ensure_ascii=False, indent=2)

    halfmem += wrong_words

    for word in good_words:
    try:
        halfmem.remove(word)
    except ValueError:
        pass

    with open("halfmem.json", "w", encoding="utf-8") as f:
        json.dump(halfmem, f, ensure_ascii=False, indent=2)

    available_words = [w for w in loaded_words if w not in remembered_words and w not in halfmem]


    SESSION_SIZE = wordlist_state.word_list_check(SESSION_SIZE, lst_length, halfmem)

    today_session, available_words = session.session(SESSION_SIZE, remembered_words, halfmem, available_words)

    with open("interim.json", "w", encoding="utf-8") as f:
        json.dump(today_session, f, ensure_ascii=False, indent=2)

    with open("learning_vocab.json", "w", encoding="utf-8") as f:
        json.dump(available_words, f, ensure_ascii=False, indent=2)

    print("Today's session:")
    incrim = 0
    for w in today_session:
        incrim += 1
        print(f"{incrim}: {w['korean']} - {w['english']}")

if __name__ == "__main__":

    main()

