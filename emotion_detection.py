import requests

def emotion_detector(text_to_analyse):
    "Send POST request to Emotion Predict of Watson NLP to get emotion from text_to_analyze"
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=data, headers=headers)
    return response.text