import requests


def language_detect(text):
    url = "https://api.textgain.com/1/language"
    data = {"top": "3", "q": text}
    return requests.get(url, data).json()


def gender_detect(text):
    url = "https://api.textgain.com/1/gender"
    data = {"top": "3", "q": text}
    return requests.get(url, data).json()


def age_detect(text):
    url = "https://api.textgain.com/1/age"
    data = {"top": "3", "q": text}
    return requests.get(url, data).json()


def NER(text):
    url = "https://api.textgain.com/1/concepts"
    data = {"top": "3", "q": text}
    return requests.get(url, data).json()


def sentiment(text):
    url = "https://api.textgain.com/1/sentiment"
    data = {"top": "3", "q": text}
    return requests.get(url, data).json()

t = "I love this phone's physical buttons and flashy colors -- teal, orange, and OK, a more buttoned-up gray. I'd take it over the flagship phone design any day. I just wish they'd added a physical camera shutter button along the spine to match all those navigation keys."
print(age_detect(t))
print(gender_detect(t))