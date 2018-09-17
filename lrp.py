import requests


def vqa(picture, question):
    # http://sequel-demo.lille.inria.fr/
    url = "https://lrpserver.hhi.fraunhofer.de/visual-question-answering/api/upload_image"

    with open(picture, 'rb') as f:
        files = {'file': (picture, f.read(), 'image/jpeg')}
    r = requests.post(url, files=files).json()
    img_id = r["img_id"]

    url = "https://lrpserver.hhi.fraunhofer.de/visual-question-answering/api/upload_question"
    data = {"img_id": img_id, "question": question}
    r = requests.post(url, data=data).json()
    r["viz0"][0] = "https://lrpserver.hhi.fraunhofer.de/visual-question-answering" + r["viz0"][0][1:]
    r["viz1"][0] = "https://lrpserver.hhi.fraunhofer.de/visual-question-answering" + r["viz1"][0][1:]
    return r
