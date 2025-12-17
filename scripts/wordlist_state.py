def word_list_check(SESSION_SIZE, lst_length, halfmem):
    mem_length = len(halfmem)
    if lst_length + mem_length < SESSION_SIZE:
        print("Congrats, this is your final session for this word-list!")
        return lst_length + mem_length
    elif lst_length + mem_length == 0:
        print("No words in wordlist, would you like ") #going to add in the pdf parser hook here.
    else:
        return SESSION_SIZE