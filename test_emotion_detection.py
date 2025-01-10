from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
	def test_emotion_analyzer(self):
		# Test case for emotion: joy
		result_1 = emotion_detector("I am glad this happened")
		print(result_1)
		# Test case for emotion: anger
		result_2 = emotion_detector("I am really mad about this")
		print(result_2)
		# Test case for emotion: disgust
		result_3 = emotion_detector("I feel disgusted just hearing about this")
		print(result_3)
		# Test case for emotion: sadness
		result_4 = emotion_detector("I am so sad about this")
		print(result_4)
		# Test case for emotion: fear
		result_5 = emotion_detector("I am really afraid that this will happen")
		print(result_5)
		
unittest.main()