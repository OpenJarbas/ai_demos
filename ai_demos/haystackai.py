import requests


# self hosted https://github.com/itoolset/nsfw
def open_nsfw(picture_path, engine="haystackai_demo"):
    url = "https://api.haystack.ai/api/image/custom?output=json&limit=10000&model=yahoonsfw&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def analyze(picture_path, engine="haystackai_demo"):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def hotness(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=attractiveness&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def emotion(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=emotion&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def nudity(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=nudity&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def flower_demo(picture_path):
    url = "https://api.haystack.ai/api/image/custom?output=json&limit=10000&model=oxfordflower&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def yearbook_demo(picture_path):
    url = "https://api.haystack.ai/api/image/custom?output=json&limit=10000&model=yearbook&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def ethnicity(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=ethnicity&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def gender(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=gender&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def age(picture_path):
    url = "https://api.haystack.ai/api/image/analyze?output=json&limit=10000&model=age&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def inception(picture_path):
    url = "https://api.haystack.ai/api/image/custom?output=json&limit=10000&model=inception&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def places(picture_path):
    url = "https://api.haystack.ai/api/image/custom?output=json&limit=10000&model=places205alexnet&apikey=c1ee6e8f5a8a2a26935e38d211a0e327"
    with open(picture_path, 'rb') as f:
        files = {'image': (picture_path, f.read(), 'image/jpeg')}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Host": "api.haystack.ai",
        "Origin": "https://www.haystack.ai",
        "Referer": "https://www.haystack.ai/demos/Yahoo-NSFW-Demo"}
    r = requests.post(url, files=files, headers=headers)
    return r.json()

