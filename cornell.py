import requests


def politeness(text):
    # http://www.cs.cornell.edu/~cristian//Politeness.html
    data = {"text": text}
    r = requests.post("http://politeness.cornell.edu/score-politeness", data=data)
    return r.json()