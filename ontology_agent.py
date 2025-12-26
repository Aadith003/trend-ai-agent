
from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-mpnet-base-v2")
def normalize(topic, ontology):
    for t in ontology:
        if model.similarity([topic],[t])[0][0]>0.82:
            return t
    ontology.append(topic)
    return topic
