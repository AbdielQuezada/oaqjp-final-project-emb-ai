# Import the Flask class from the flask module
from flask import Flask, render_template, request, make_response
# Import the emotion_detector
from EmotionDetection.emotion_detection import emotion_detector
import json

# Create an instance of the Flask class, passing in the name of the current module
# app = Flask(__name__)
app = Flask("Emotion Detector")

# Define a route for the root URL ("/")
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    # return "Hello, World!"
    return render_template('index.html')

@app.route("/emotionDetector")
def RunSentimentAnalysis():
    result = emotion_detector(request.args.get('textToAnalyze'))
    
    # Debugging: Print out the result to see its structure
    # print(f"Result from emotion_detector: {result}")
    
    # In case the result is a string, I need to parse it.
    if isinstance(result, str):
        try:
            result = json.loads(result)  # Converting the string to a dictionary or list of dictionaries
        except json.JSONDecodeError:
            return f"Error: Could not parse the result string as JSON. Result: {result}"

    # I will assume the result is a list of dictionaries
    if isinstance(result, list):
        response = result[0]  # I'm getting the first dictionary in the list
    else:
        return f"Error: The result is not a list. Result: {result}"

    # Format my response
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominand emotion is {response['dominant_emotion']}."
    )

    return formatted_output