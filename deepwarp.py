import requests
from os.path import abspath
import base64


def animate_eyes(face_picture, mode=None, engine="deepwarp_demo"):
    # https://github.com/ddtm/deep-smile-warp
    face_picture = abspath(face_picture)
    modes = ["roll", "scroll", "cross", "shift"]
    if mode is None:
        res = []
        for m in modes:
            res += animate_eyes(face_picture, m, engine)
        return res
    mode = mode.lower()
    assert mode in modes
    url = "http://163.172.78.19/process"
    with open(face_picture, 'rb') as f:
        files = {'file': (face_picture, f.read(), 'image/jpeg')}
    r = requests.post(url, data={"action": mode}, files=files)
    url = r.headers["location"]
    done = False
    # check if ready
    while not done:
        r = requests.get(url)
        if r.json()["state"] != "PROGRESS":
            done = True
            data = base64.decodebytes(bytes(r.json()["result"].split("base64,")[1], encoding="utf-8"))
            with open(face_picture+"_"+mode+".mp4", "wb") as f:
                f.write(data)
    return [face_picture+"_"+mode+".mp4"]


def roll_eyes(face_picture):
    return animate_eyes(face_picture, "roll")


def scroll_eyes(face_picture):
    return animate_eyes(face_picture, "scroll")


def cross_eyes(face_picture):
    return animate_eyes(face_picture, "cross")


def shift_eyes(face_picture):
    return animate_eyes(face_picture, "shift")

