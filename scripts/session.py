import json, secrets, os, re
from scripts import Message

def interim_session(remembered_words, right_words, wrong_words):
    if os.path.exists("interim.json"):
        print("Past session review:\n")

        with open("interim.json", "r", encoding="utf-8") as f:
            last_session = json.load(f)

            for remember in last_session:
                attempt = input(f"{remember['korean']}? Please enter answer: ").strip().lower()
                solution = [re.sub(r'[^a-z\s]', '', w).lower().strip() for w in remember['english'].split(',')]
                attempt_words = attempt.split()
                attempt_words.append(attempt)
                if not any(ans in solution for ans in attempt_words):
                    wrong_words.append(remember)
                    print(f"Wrong! Correct answer(s) for {remember['korean']}: {solution}\n")
                    if remember in remembered_words:
                        print("It was in remembered words... write it down in your book for active external focus.\n")
                else:
                    print(f"Correct :) the solution for {remember['korean']} is/are: {solution}\n")
                    if remember in remembered_words:
                        print("repeated word, good job remembering :)\n")
                    else:
                        remembered_words.append(remember)
                        right_words.append(remember)
            Message.spacer()
    else:
        last_session = []
    return remembered_words, right_words, wrong_words

def session(SESSION_SIZE, remembered_words, halfmem, available_words):
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

    return today_session, available_words



