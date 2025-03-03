import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    dict0bj = { "raw_document": { "text": text_to_analyse } }

    res = requests.post(url, json = dict0bj, headers = headers)

    formatted_res = json.loads(res.text)

    anger = formatted_res["emotionPredictions"][0]["emotion"]["anger"]
    disgust = formatted_res["emotionPredictions"][0]["emotion"]["disgust"]
    fear = formatted_res["emotionPredictions"][0]["emotion"]["fear"]
    joy = formatted_res["emotionPredictions"][0]["emotion"]["joy"]
    sadness = formatted_res["emotionPredictions"][0]["emotion"]["sadness"]
    highest_index = 0
    dominant_emotion = ""
    # if anger > highest_index:
    #     highest_index = anger
    #     dominant_emotion = "anger"
    # if disgust > highest_index:
    #     highest_index = disgust
    #     dominant_emotion = "disgust"
    # if fear > highest_index:
    #     highest_index = fear
    #     dominant_emotion = "fear"
    # if joy > highest_index:
    #     highest_index = joy
    #     dominant_emotion = "joy"
    # if sadness > highest_index:
    #     highest_index = sadness
    #     dominant_emotion = "sadness"

    return {'anger': anger, "disgust" : disgust, "fear" : fear, "joy" : joy, "sadness" : sadness, "dominant_emotion" : None}