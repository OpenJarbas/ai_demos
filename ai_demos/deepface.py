import requests

# TODO test if token expires
TOKEN = "0113b67e-213b-4167-a95c-0689b73288be"


def face_analysis(face_picture):
    url = "https://api.deepface.ir/analysis"
    with open(face_picture, 'rb') as f:
        files = {'file': (face_picture, f.read(), 'image/jpeg')}
    r = requests.post(url, files=files, data={"token": TOKEN})
    return r.json()["data"]


def face_emotion(face_picture):
    url = "https://api.deepface.ir/emotion"
    with open(face_picture, 'rb') as f:
        files = {'file': (face_picture, f.read(), 'image/jpeg')}
    r = requests.post(url, files=files, data={"token": TOKEN})
    return r.json()["data"]
