import requests  # Import the requests library to handle HTTP requests
import json # Import JSON library for formatting
def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Converting teh response to a Python dictionary
    response_data = response.json()

    # Create a new output dictionary
    output_data = []

    # Process each prediction
    for prediction in response_data['emotionPredictions']:
        # Process main emotion scores
        emotions = prediction['emotion']
        dominant_emotion = get_dominant_emotion(emotions)
        main_emotion_data = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        # Append the main emotion data
        output_data.append(main_emotion_data)
    
    # Convert to JSON dictionary
    output_json = json.dumps(output_data, indent=4)
    return output_json  # Return the response text from the API in JSON format

# Function to calculate the dominant emotion
def get_dominant_emotion(emotions):
    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion