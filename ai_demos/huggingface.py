import requests


def neuralconvo(text):
    """
    This is a demo of chatting with a Deep learning chatbot trained through Neuralconvo, a Torch library that implements Sequence to Sequence Learning with Neural Networks (seq2seq), reproducing the results in the Neural Conversational Model paper (aka the Google chatbot).

    source: http://neuralconvo.huggingface.co/

    :param text: (str) utterance to send to bot
    :return:     (str) text response from bot
    """
    url = "http://neuralconvo-ec2.huggingface.co/hey"
    data = {"q": text, "uuid": "3666b7f8-b80c-f5a9-476a-05d42b2ec024"}
    r = requests.get(url, data)
    return r.text


def neuralcoref(text):
    """
    State-of-the-art neural coreference resolution system based on neural nets and spaCy,

    Coreference is the fact that two or more expressions in a text – like pronouns or nouns – link to the same person or thing. It is a classical Natural language processing task, that has seen a revival of interest in the past two years as several research groups applied cutting-edge deep-learning and reinforcement-learning techniques to it. It is also one of the key building blocks to building conversational Artificial intelligences. I

    source: https://huggingface.co/coref/

    :param text: (str)  your sentence
    :return:     (dict) json response
    """
    params = {"text": text.replace(".", ",").replace("\n", ", ")}
    r = requests.get("https://coref.huggingface.co/coref", params=params).json()
    return r