import requests


def relation_extraction(text):
    # DO NOT ABUSE, dev purposes only
    url = "http://semanticparsing.ukp.informatik.tu-darmstadt.de:5000/relation-extraction/parse/"
    return requests.post(url, json={"inputtext": text}).json()
