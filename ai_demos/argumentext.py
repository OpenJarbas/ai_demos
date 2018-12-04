import requests


def get_arguments(text):
    s = requests.Session()
    url = "http://www.argumentsearch.com/index"
    data = {"query": text, "language": "en"}
    r = s.get(url, data=data)
    #print(r.text)
    print(r.__dict__)
    #r = s.get("http://www.argumentsearch.com/static/scripts.js")
    #print(r.text)

get_arguments("nuclear energy")