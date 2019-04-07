import requests


def coreference(text):
    url = "https://cogcomp.org/demo_files/Coref.php"
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    return r.json()


def ner_extended(text):
    url = "http://cogcomp.org/demo_files/NERextended.php"
    return _ugly_parse(text, url)


def ner(text, extended=False):
    if extended:
        return ner_extended(text)
    url = "http://cogcomp.org/demo_files/NER.php"
    return _ugly_parse(text, url)


def _ugly_parse(text, url):
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    data = r.json()
    ents = []
    # ugly but easy, TODO use bs4 and do it properly
    bucket = data["content"].split('<span class="token ')[1:]
    for e in bucket:
        ent = e.split('">')[0]
        label = e.split('">')[1].split("</span>")[0]
        ents += [(ent, label)]
    return ents


def number_quantization(text):
    url = "https://cogcomp.org/demo_files/Quantities.php"
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    # TODO parse
    return r.json()["content"]


def wikifier(text):
    url = "https://cogcomp.org/demo_files/Wikifier.php"
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    return r.json()["data"]["array"]


def pos_tag(text):
    url = "https://cogcomp.org/demo_files/POS.php"
    return _ugly_parse(text, url)


def shallow_parse(text):
    url = "https://cogcomp.org/demo_files/ShallowParse.php"
    return _ugly_parse(text, url)


def lexical_level_matching(text1, text2):
    url = "https://cogcomp.org/demo_files/LLM.php"
    data = {"lang": "en", "val1": text1, "val2": text2}
    r = requests.post(url, json=data)
    return r.json()["content"]["output"]


def algebra(text):
    url = "https://cogcomp.org/demo_files/Math.php"
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    return r.json()



if __name__ == "__main__":
    from pprint import pprint

    text = "My sister loves dogs. She has lots of animals"

    # pprint(coreference(text))

    text = "Helicopters will patrol the temporary no-fly zone around New " \
           "Jersey's MetLife Stadium Sunday, with F-16s based in Atlantic " \
           "City ready to be scrambled if an unauthorized aircraft does " \
           "enter the restricted airspace."
    pprint(ner_extended(text))
    pprint(ner(text))
    pprint(number_quantization(text))
    pprint(wikifier(text))
    pprint(pos_tag(text))
    pprint(shallow_parse(text))
    pprint(lexical_level_matching("i think", "i exist"))
    text = "Sandy has 10.0 books, Benny has 24.0 books, and Tim has 33.0 books. How many books do they have together?"
    pprint(algebra(text))
