import webbrowser


def open_url(url):
    webbrowser.open(url)


def pretty_number(nb):
    nb = str(nb)
    return " ".join((nb[::-1][i: i + 3] for i in range(0, len(nb), 3)))[::-1]


def wrap_text(text, length=150, lines=10):
    liste = []
    mots = text.split(" ")
    nb = length
    lignes = 0
    for i in mots:
        if nb - len(i) <= 0:
            nb = length - len(i)
            lignes += 1
            if lignes == lines:
                liste.append("...")
                break
            else:
                liste.extend(("\n", i, " "))
        else:
            liste.extend((i, " "))
            nb -= len(i)
    return "".join(liste)
