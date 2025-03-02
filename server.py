from flask import Flask, request, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text_to_analyse)    
    if result['dominant_emotion'] == None:
        return "<b>Invalid text! Please try again!</b>"
    return (
        "For the given statement, the system response is"
        f" 'anger': {result['anger']}, 'disgust': {result['disgust']},"
        f" 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}."
        f" The dominant emotion is <b>{result['dominant_emotion']}</b>."
        )

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)    