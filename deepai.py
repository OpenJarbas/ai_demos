import requests


def demographic_recognition(face_picture):
    url = "https://api.deepai.org/api/demographic-recognition"
    with open(face_picture, 'rb') as f:
        files = {'image': (face_picture, f.read(), 'image/jpeg')}
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    r = requests.get("https://api.deepai.org" + job)
    return r.json()


def nudity_detection(picture):
    url = "https://api.deepai.org/api/nsfw-detector"
    with open(picture, 'rb') as f:
        files = {'image': (picture, f.read(), 'image/jpeg')}
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    r = requests.get("https://api.deepai.org" + job)
    return r.json()


def deepmask(picture, save_path=None):
    save_path = save_path or picture + "_mask.jpg"
    url = "https://api.deepai.org/api/deepmask"
    with open(picture, 'rb') as f:
        files = {'content': (picture, f.read(), 'image/jpeg')}
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    r = requests.get("https://api.deepai.org" + job).content
    with open(save_path, "wb") as f:
        f.write(r)
    return save_path


def densecap(picture):
    url = "https://api.deepai.org/api/densecap"
    with open(picture, 'rb') as f:
        files = {'image': (picture, f.read(), 'image/jpeg')}
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    return requests.get("https://api.deepai.org" + job).json()


def image_similarity(picture1, picture2):
    url = "https://api.deepai.org/api/image-similarity"
    with open(picture1, 'rb') as f:
        files = {'image1': (picture1, f.read(), 'image/jpeg')}
    with open(picture2, 'rb') as f:
        files['image2'] = (picture2, f.read(), 'image/jpeg')
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    return requests.get("https://api.deepai.org" + job).json()


def neuraltalk(picture):
    url = "https://api.deepai.org/api/neuraltalk"
    with open(picture, 'rb') as f:
        files = {'image': (picture, f.read(), 'image/jpeg')}
    headers = {"origin": "https://deepai.org",
                "referer": "https://deepai.org/ai-image-processing",
                "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
    r = requests.post(url, files=files, data={"new_try_it": "1"}, headers=headers)
    job = r.json()["result_data"]["output_url"]
    return requests.get("https://api.deepai.org" + job).text
