import time
def word_list_check(SESSION_SIZE, lst_length, halfmem):
    mem_length = len(halfmem)
    if lst_length == 0 and mem_length == 0:
        print("wordlist empty, please delete learning_vocab.json and relaunch from bat/bash.")
        time.sleep(5)
        exit()
    elif lst_length + mem_length < SESSION_SIZE:
        print("Congrats, this is your final session for this word-list!")
        return lst_length + mem_length
    else:
        return SESSION_SIZE