# pip install SpeechRecognition << need this package
# Need to run the following commands to download the vader nltk:
# python3
# import nltk
# nltk.download('vader_lexicon')
# python -m nltk.downloader vader_lexicon << this also works

from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

with AudioFile('chile.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)

if scores['compound'] > 0:
    print("This is a positive speech.")
else:
    print("This is a negative speech.")