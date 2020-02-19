def to_camel_case(text):
    cameltings = ""
    if text != "":
        splitext = text.split("-")
        print(splitext)
        for i in range(len(splitext)):
            splitext[i] = splitext[i].split("_")
        print(splitext)
        if splitext[0][0].isupper() == True:
            for i, word in enumerate(splitext):
                splitext[i]=word.capitalize()
        else:
            for i, word in enumerate(splitext):
                if i==0:
                    continue
                splitext[i]=word.capitalize()  
        for i in splitext:
            cameltings += i
        return cameltings
    else:
        return text

print(to_camel_case("the_stealth_warrior"))