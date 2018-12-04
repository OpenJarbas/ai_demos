import requests


def NER(text):
    # DO NOT ABUSE THIS, dev purposes only
    data = {"text": text.replace(" ", "+"),
            "langs": "en",
            "tokenization": "tokenization",
            "min_O": 0.00
            }
    url = "https://entityextractor.appspot.com/ner"
    r = requests.post(url, data=data)

    t = r.text.replace("<br>", "")
    NER = []
    # parse colors
    candidates = [c for c in t.split("</font>") if not c.startswith('<font color="black">')]
    for c in candidates:
        if not c:
            continue
        color, name = c.split(">")
        color = color.replace('<font color="', "").replace('"', "")
        name = name.strip()
        if color == "red":
            NER.append((name, "person"))
        elif color == "green":
            NER.append((name, "organization"))
        elif color == "blue":
            NER.append((name, "location"))
    return NER
