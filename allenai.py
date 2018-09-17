import requests

ALLENNLP_URL = "http://demo.allennlp.org/predict/"


def textual_entailment(premise, hypothesis):
    # use the source: https://github.com/allenai/scitail
    """
    Textual Entailment (TE) takes a pair of sentences and predicts whether the facts in the first necessarily imply the facts in the second one.
    The AllenNLP toolkit provides the following TE visualization, which can be run for any TE model you develop.
    This page demonstrates a reimplementation of the decomposable attention model (Parikh et al, 2017) ,
    which was state of the art for the SNLI benchmark (short sentences about visual scenes) in 2016.
    Rather than pre-trained Glove vectors, this model uses ELMo embeddings,
    which are completely character based and improve performance by 2%

    :param premise:
    :param hypotheses:
    :return:
    """
    url = ALLENNLP_URL + "textual-entailment"
    data = {"premise": premise,
            "hypothesis": hypothesis}
    r = requests.post(url, json=data).json()
    probs = r["label_probs"]
    return {"entailment": probs[0], "contradiction": probs[1], "neutral": probs[2]}


def machine_comprehension(question, passage):
    # DO NOT ABUSE, dev purposes only
    """
    Machine Comprehension (MC) answers natural language questions by selecting an answer span within an evidence text.
    The AllenNLP toolkit provides the following MC visualization, which can be used for any MC model in AllenNLP.
    This page demonstrates a reimplementation of BiDAF (Seo et al, 2017), or Bi-Directional Attention Flow,
    a widely used MC baseline that achieved state-of-the-art accuracies on the SQuAD dataset (Wikipedia sentences) in early 2017.

    :param question:
    :param passage:
    :return:
    """
    url = ALLENNLP_URL + "machine-comprehension"
    data = {"passage": passage, "question": question}
    r = requests.post(url, json=data).json()
    return r["best_span_str"]


def semantic_role_labeling(sentence):
    # DO NOT ABUSE, dev purposes only
    """
    Semantic Role Labeling (SRL) recovers the latent predicate argument structure of a sentence,
    providing representations that answer basic questions about sentence meaning,
    including “who” did “what” to “whom,” etc.
    The AllenNLP toolkit provides the following SRL visualization, which can be used for any SRL model in AllenNLP.
    This page demonstrates a reimplementation of a deep BiLSTM model (He et al, 2017),
    which is currently state of the art for PropBank SRL (Newswire sentences).
    :param sentence:
    :return:
    """
    url = ALLENNLP_URL + "semantic-role-labeling"
    data = {"sentence": sentence}
    r = requests.post(url, json=data).json()
    roles = {}
    words = r["words"]
    verbs = r["verbs"]
    for v in verbs:
        arg0 = []
        arg1 = []
        verb = v["verb"]
        tags = v["tags"]
        for idx, t in enumerate(tags):
            if "I-ARGM" in t:
                arg0.append(words[idx])
            elif "I-ARG1" in t:
                arg1.append(words[idx])
        if not len(arg0):
            continue
        arg0 = " ".join(arg0)
        arg1 = " ".join(arg1)
        roles[verb] = [arg0, arg1]
    return roles


def constituency_parse(sentence):
    # DO NOT ABUSE, dev purposes only
    """
    A constituency parse tree breaks a text into sub-phrases, or constituents. Non-terminals in the tree are types of phrases, the terminals are the words in the sentence. This demo is an implementation of a minimal neural model for constituency parsing based on an independent scoring of labels and spans described in Extending a Parser to Distant Domains Using a Few Dozen Partially Annotated Examples (Joshi et al, 2018). This model uses ELMo embeddings, which are completely character based and improves single model performance from 92.6 F1 to 94.11 F1 on the Penn Treebank, a 20% relative error reduction.
    :param sentence:
    :return:
    """
    url = ALLENNLP_URL + "constituency-parsing"
    data = {"sentence": sentence}
    r = requests.post(url, json=data).json()
    return r


def NER(text):
    url = ALLENNLP_URL + "named-entity-recognition"
    data = {"sentence": text}
    return requests.post(url, json=data).json()


# DO NOT ABUSE
def euclid(text):
    url = "http://euclid.allenai.org/api/solve?query=" + text
    return requests.get(url).text


# DO NOT ABUSE
# use the source https://github.com/allenai/aristo-mini
def aristo(text):
    url = "http://aristo-demo.allenai.org/api/ask?text=" + text
    data = requests.get(url).json()
    return data
