# nlp_module.py
import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_response(response):
    doc = nlp(response)
    return {"num_tokens": len(doc), "sentiment": "positive"}
