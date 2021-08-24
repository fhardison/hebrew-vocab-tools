def load_lex():
    data = {}
    with open('heb_lex.txt', 'r', encoding="UTF-8") as f:
        for line in f:
            strong, index, bdb, form, gloss = line.replace('\n', '').split("\t", maxsplit=4)
            data[form] = gloss
    return data


