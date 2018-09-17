import requests


def vqa(picture, question):
    # http://sequel-demo.lille.inria.fr/
    url = "http://sequel-demo.lille.inria.fr/api/upload_image"

    with open(picture, 'rb') as f:
        files = {'file': (picture, f.read(), 'image/jpeg')}
    r = requests.post(url, files=files).json()
    img_id = r["img_id"]

    url = "http://sequel-demo.lille.inria.fr/api/upload_question"
    data = {"img_id": img_id, "question": question}
    r = requests.post(url, data=data).json()
    return r
