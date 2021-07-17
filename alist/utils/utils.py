import webbrowser


def modif_text(modification, text):
    if modification.get("lower", False) is True:
        text = text.lower()
    if modification.get("upper", False) is True:
        text = text.upper()
    for k, v in modification.items():
        if k != "lower" and k != "upper":
            text = text.replace(k, v)
    return text


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
