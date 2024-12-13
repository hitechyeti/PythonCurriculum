def convert_to_titlecase(str):
    words=str.split()
    m=[word.capitalize() for word in words]
    return ' '.join(m)

def convert_to_titlecase(s):
    return s.title()
