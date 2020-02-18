def find_short(s):
    splits = s.split(" ")
    lengths = []
    for i,word in enumerate(splits):
        lengths.append(len(word))
    print(lengths)
    l = min(lengths)
    return l # l: shortest word length

find_short("Hello my name is mo")