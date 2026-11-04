with open("../docs/sample.txt","r",encoding="utf-8") as f:
    text = f.read()
    print(len(text))


    sents = text.split("。")
    print(len(sents))
    print(type(sents))
    print(sents[0])

    print("-----------")


    count = 0
    cards = set()
    st = ""
    for sent in sents:
        num = len(sent) + len(st)
        if num <= 100:
            st += sent
        else:
            count = count + 1
            cards.add(st)
            st = ""
            st += sent

count+=1
cards.add(st)
print("-----------")
print(st)
print(count)
print(len(cards))
print(sum(len(s) for s in cards))



