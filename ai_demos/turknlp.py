import requests

# WIP


def similar(text, n=10, model="Finnish 4B wordforms skipgram"):
    models = ["Suomi24 wordforms skipgram",
              "Finnish 4B wordforms skipgram",
              "Suomi24 lemmas skipgram",
              "English GoogleNews Negative300"]
    assert model in models
    model = model.replace(" ", "+")
    text = text.replace(" ", "+")
    url = "http://bionlp-www.utu.fi/wv_demo/nearest"
    data = {
        "form[0][name]": "word",
        "form[0][value]": text,
        "form[1][name]": "topn",
        "form[1][value]": n,
        "model_name": model
    }
    headers = {"Host": "bionlp-www.utu.fi",
        "Connection": "keep-alive",
        "Content-Length": "148",
        "Origin": "http://bionlp-www.utu.fi",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "DNT": "1",
        "Referer": "http://bionlp-www.utu.fi/wv_demo/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"}
    r = requests.post(url, data=data)
    print(r.text)