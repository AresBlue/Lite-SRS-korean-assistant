from config import english_garbage_words, korean_garbage_words

def garbage_parser(loaded_words):

    cleaned_words = []

    for word in loaded_words:

        for garbage in english_garbage_words:
            word['english'] = word['english'].replace(garbage, '').strip()
        for garbage in korean_garbage_words:
            word['korean'] = word['korean'].replace(garbage, '').strip()

        if word['english'] and word['korean']:
            cleaned_words.append(word)

    return cleaned_words
