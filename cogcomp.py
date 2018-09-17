import requests


def coreference(text):
    url = "https://cogcomp.org/demo_files/Coref.php"
    data = {"lang": "en", "text": text}
    r = requests.post(url, json=data)
    return r.json()
