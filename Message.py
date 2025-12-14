def message_of_today(lst_length, lst_total_length, halfmem_length):
    print(f"{100-(((lst_length+halfmem_length)/lst_total_length)*100):.1f}% left including half remembered words!")
    percentage = (lst_length / lst_total_length) * 100
    if halfmem_length > 100:
        print("You might need to remediate off of half remembered list in 'halfmem.json'")
    if lst_length < (lst_total_length * 0.1):
        print(f"Congrats, you are so close! {100-percentage:.1f}% left!")
    elif lst_length < (lst_total_length * 0.25):
        print(f"Congrats, less than one-quarter left! {percentage:.1f}% done so far!")
    elif lst_length < (lst_total_length * 0.5):
        print(f"Congrats, over half way there! {percentage:.1f}% left so far!")
    elif lst_length < (lst_total_length * 0.70):
        print(f"Congrats, already pretty far there! {percentage:.1f}% left so far!")
    elif lst_length < (lst_total_length * 0.80):
        print(f"Just starting out, but you can do it! {percentage:.1f}% left so far!")
    else:
        print(f"You can do it! {percentage:.1f}% to do so far!")

