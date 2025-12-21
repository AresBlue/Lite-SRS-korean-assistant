import json
import secrets
import os
import re
from scripts import Message
from config import config

def interim_session(remembered_words, right_words, wrong_words):

    if os.path.exists("interim.json"):
        print("Past session review:\n")

        with open("interim.json", "r", encoding="utf-8") as f:
            last_session = json.load(f)

            quiz_list = []

            while last_session:
                idx = secrets.randbelow(len(last_session))
                quiz_list.append(last_session.pop(idx))

            for remember in quiz_list:
                attempt = re.sub(r'[^a-z\s]', '', input(f"\033[1;32m{remember['korean']}?\033[0m Please enter answer: ").lower()).strip()
                solution = [re.sub(r'[^a-z\s]', '', w.lower()).strip() for w in remember['english'].split(',')]
                attempt_words = attempt.split()
                attempt_words.append(attempt)
                if not any(ans in solution for ans in attempt_words):
                    wrong_words.append(remember)
                    print(f"Wrong! Correct answer{'s' if len(solution) > 1 else ''} for \033[1;31m{remember['korean']}\033[0m {'are' if len(solution) > 1 else 'is'}: \033[1;31m{solution}\033[0m\n")
                    if remember in remembered_words:
                        print("\033[1;31mIt was in remembered words... write it down in your book for active external focus.\033[0m\n")
                else:
                    print(f"Correct :) the solution{'s' if len(solution) > 1 else ''} for \033[1;32m{remember['korean']}\033[0m {'are' if len(solution) > 1 else 'is'}: \033[1;32m{', '.join(solution)}\033[0m\n")
                    if remember in remembered_words:
                        print("repeated word, good job remembering :)\n")
                    else:
                        remembered_words.append(remember)
                        right_words.append(remember)
            Message.spacer()
    else:
        last_session = []
    return remembered_words, right_words, wrong_words

def session(session_size, remembered_words, halfmem, available_words):
    today_session = []
    for _ in range(session_size):
        r = secrets.randbelow(100)
        if r < config["remembered_wordlist_pull"] and remembered_words:
            word = secrets.choice(remembered_words)
            while word in today_session:
                word = secrets.choice(remembered_words)
            today_session.append(word)
        elif r < config["halfmem_wordlist_pull"] and halfmem:
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