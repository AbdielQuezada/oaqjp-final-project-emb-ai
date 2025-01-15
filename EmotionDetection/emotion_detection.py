import requests  # Import the requests library to handle HTTP requests
import json # Import JSON library for formatting

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)

    # Task 7 error handling: managing blank entries from users.
    if not text_to_analyse:
        return "Error: 'text_to_analyse' is empty."

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    try:
        response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

        # Task 7 error handling: status_code = 400
        if response.status_code == 400:
            output_data = [{
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }]
            return json.dumps(output_data, indent=4)  # Convert to JSON dictionary and return the response text from the API in JSON format

        # If no errors are found proceed as normal and converting the response to a Python dictionary
        response_data = response.json()
        output_data = [] # Initialize the output data list

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

        return json.dumps(output_data, indent=4)  # Convert to JSON dictionary and return the response text from the API in JSON format
    
    except requests.exceptions.RequestException as e:
        return f"Error: An exception occurred - {str(e)}"

# Function to calculate the dominant emotion
def get_dominant_emotion(emotions):
    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    return dominant_emotion