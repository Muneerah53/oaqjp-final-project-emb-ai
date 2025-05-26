from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector  


app = Flask(__name__)

@app.route('/')
def render_homepage():
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
  text_to_analyze = request.args.get('textToAnalyze')
  analyazed_emotions = emotion_detector(text_to_analyze)

  emotions = {key: value for key, value in analyazed_emotions.items() if key != 'dominant_emotion'}

  response = f"For the given statement, the system response is {emotions}. The dominant emotion is {analyazed_emotions['dominant_emotion']}."

  return response

if __name__ == '__main__':
    app.run(debug=True)
    
