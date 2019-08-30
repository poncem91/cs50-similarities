from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    lines_a = set(a.splitlines())
    lines_b = set(b.splitlines())
    return list(lines_a & lines_b)


def sentences(a, b):
    """Return sentences in both a and b"""
    sent_a = set(sent_tokenize(a))
    sent_b = set(sent_tokenize(b))
    return list(sent_a & sent_b)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # initializes empty list and loops over 'a' to append substrings of nth size into list.
    listA = []
    for index, char in enumerate(a):
        # makes sure loop stops before going over the strings
        if index > len(a) - n:
            break
        listA.append(a[index:(index + n)])

    # initializes empty list and loops over 'b' to append substrings of nth size into list.
    listB = []
    for index, char in enumerate(b):
        # makes sure loop stops before going over the strings
        if index > len(b) - n:
            break
        listB.append(b[index:(index + n)])

    setA = set(listA)
    setB = set(listB)

    return list(setA & setB)