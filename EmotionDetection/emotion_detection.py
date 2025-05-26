import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = {"raw_document": {"text": text_to_analyze}}

    res = requests.post(url, headers=headers, json=json_input)

    if res.status_code == 200:
        res_obj = res.json()

        emotions = res_obj['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key=emotions.get)

        return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
        }
    else:
        return None
