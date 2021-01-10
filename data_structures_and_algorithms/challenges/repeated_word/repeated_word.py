import re

def repeated_word(txt):
    x = re.findall(r"[A-z]*\w", txt)
    temp = []
    for i in x:
        if i.lower() in temp:
            return i
        else:
            temp.append(i.lower())


# if __name__ == "__main__":
#     f = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
#     print(repeated_word(f))