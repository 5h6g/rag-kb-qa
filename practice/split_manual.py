with open("../docs/sample.txt","r",encoding="utf-8") as f:
    text = f.read()
    print(len(text))


    sents = text.split("。")
    print(len(sents))
    print(type(sents))
    print(sents[0])


    count = 0
    for sent in sents:
        if 




