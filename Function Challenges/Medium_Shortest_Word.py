def shortest_word(sentence):
    a = sentence.split()
    b = min(a, key=len)
    return b


def shortest_word(sentence):
    a=sentence.split()
    short_word=a[0]
    for i in a:
        if len(i)<len(short_word):
            short_word =i
    return short_word
