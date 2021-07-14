import webbrowser


def open_url(url):
    webbrowser.open(url)


def pretty_number(nb):
    nb = str(nb)
    return " ".join((nb[::-1][i: i + 3] for i in range(0, len(nb), 3)))[::-1]
