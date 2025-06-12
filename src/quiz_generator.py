from transformers import pipeline

def generate_quiz(text):
    qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
    return qg_pipeline(text)[0]['generated_text']
