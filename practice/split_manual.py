with open("../docs/sample.txt","r",encoding="utf-8") as f:
    text = f.read()
    print(len(text))


    sents = text.split("。")
    print(len(sents))
    print(type(sents))
    print(sents[0])

    a = 0
    cards = []
    se = set()

    for sent in sents:
        sent = sent.strip()
        if not sent:
            continue
        if len(cards) >= 100:
            se.add(cards)
            cards = []
            a+=1
        cards.append(sent)
    print(cards)
    
    print(a)



