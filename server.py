'''Emotion detector application on Flask
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''Request to emotion detection api
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)
    anger = res['anger']
    disgust = res['disgust']
    fear = res['fear']
    joy = res['joy']
    sadness = res['sadness']
    dominant_emotion = res['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid Text! Please try again!"

    return (
        f"For the given statement, the system response is:\n"
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},\n"
        f"'joy': {joy}, and 'sadness': {sadness}.\n"
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    '''Render homepage
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
