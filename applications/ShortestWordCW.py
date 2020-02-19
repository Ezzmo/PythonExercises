def find_short(s):
    splits = s.split(" ")
    lengths = []
    for word in splits:
        lengths.append(len(word))
    l = min(lengths)
    return l # l: shortest word length

print(find_short("Hello my name is mo"))