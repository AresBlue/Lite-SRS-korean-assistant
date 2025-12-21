import json, os, datetime

def import_backup():

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

    with open(f"backups/halfmem_backup-{iso_date}.json", "w", encoding="utf-8") as f:
        json.dump(halfmem, f, ensure_ascii=False, indent=2)

    with open("learning_vocab-static.json", "r", encoding="utf-8") as f:
        lst_total_length = len(json.load(f))

    return remembered_words, halfmem, lst_total_length, loaded_words