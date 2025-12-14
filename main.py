import secrets, json, os, datetime
import Message

wrong_words = []
SESSION_SIZE = 34 #set to whatever you want, future me :)

if os.path.exists("remembered_words.json"):
    with open("remembered_words.json", "r", encoding="utf-8") as f:
        remembered_words = json.load(f)
else:
    remembered_words = []

if os.path.exists("halfmem.json"):
    with open("halfmem.json", "r", encoding="utf-8") as f:
        halfmem = json.load(f)
else:
    halfmem = []

dt_object = datetime.datetime.now()
iso_date = dt_object.strftime('%Y-%m-%d')

with open(f"backups/remembered_words-backup-{iso_date}.json", "w", encoding="utf-8") as f:
    json.dump(remembered_words, f, ensure_ascii=False, indent=2)

with open("learning_vocab.json", "r", encoding="utf-8") as f:
    loaded_words = json.load(f)

with open(f"backups/learning_vocab-backup-{iso_date}.json", "w", encoding="utf-8") as f:
    json.dump(loaded_words, f, ensure_ascii=False, indent=2)


with open("learning_vocab-static.json", "r", encoding="utf-8") as f:
    lst_total_length = len(json.load(f))

lst_length = len(loaded_words)

print("\nKorean SRS learning assistant, good luck.")
print("--------------------"*4)
Message.message_of_today(lst_length, lst_total_length, len(halfmem))
print("--------------------"*4)

if os.path.exists("interim.json"):
    print("Past session review:\n")

    with open("interim.json", "r", encoding="utf-8") as f:
        last_session = json.load(f)

        for remember in last_session:
            attempt = input(f"{remember['korean']}?").strip().lower()
            solution = [w.strip().lower() for w in remember['english'].split(',')]
            if attempt not in solution:
                wrong_words.append(remember)
                print(f"Wrong! Correct answer(s) for {remember['korean']}: {remember['english']}\n")
                if remember in remembered_words:
                    print("It was in remembered words... write it down in your book for active external focus.\n")
            else:
                print(f"Correct :) the solution for {remember['korean']} is/are {remember['english']}\n")
                if remember in remembered_words:
                    print("repeated word, good job remembering :)\n")
                else:
                    remembered_words.append(remember)
        print("--------------------"*4)
else:
    last_session = []

with open("remembered_words.json", "w", encoding="utf-8") as f:
    json.dump(remembered_words, f, ensure_ascii=False, indent=2)

halfmem += wrong_words

with open("halfmem.json", "w", encoding="utf-8") as f:
    json.dump(halfmem, f, ensure_ascii=False, indent=2)

available_words = [w for w in loaded_words if w not in remembered_words and w not in halfmem]

def word_list_check(SESSION_SIZE, lst_length, halfmem):
    mem_length = len(halfmem)
    if lst_length + mem_length < SESSION_SIZE:
        print("Congrats, this is your final session for this word-list!")
        return lst_length + mem_length
    elif lst_length + mem_length == 0:
        print("No words in wordlist, would you like ") #going to add in the pdf parser hook here.
    else:
        return SESSION_SIZE

SESSION_SIZE = word_list_check(SESSION_SIZE, lst_length, halfmem)


today_session = []
for _ in range(SESSION_SIZE):
    r = secrets.randbelow(100)
    if r < 5 and remembered_words:
        word = secrets.choice(remembered_words)
        while word in today_session:
            word = secrets.choice(remembered_words)
        today_session.append(word)
    elif r < 35 and halfmem:
        word = secrets.choice(halfmem)
        while word in today_session:
            word = secrets.choice(halfmem)
        today_session.append(word)
    else:
        if available_words:
            retry = 0
            word = secrets.choice(available_words)
            while word in today_session and retry < len(available_words):
                retry += 1
                word = secrets.choice(available_words)
            today_session.append(word)
            available_words.remove(word)


with open("interim.json", "w", encoding="utf-8") as f:
    json.dump(today_session, f, ensure_ascii=False, indent=2)

with open("learning_vocab.json", "w", encoding="utf-8") as f:
    json.dump(available_words, f, ensure_ascii=False, indent=2)

print("Today's session:")
incrim = 0
for w in today_session:
    incrim += 1
    print(f"{incrim}: {w['korean']} - {w['english']}")