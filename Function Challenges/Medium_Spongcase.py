def to_spongecase(text):
    result = ""
    uppercase = False
    for i in text:
        if uppercase:
            result += i.upper()
        else:
            result += i.lower()
        if i.isalpha():
            uppercase = not(uppercase)
    return result
