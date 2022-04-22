
#import library
import speech_recognition as sr
import pydub
from pydub import AudioSegment
import math

audio = AudioSegment.from_file('16.wav')
total_duration = math.ceil(audio.duration_seconds)
print(total_duration)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable


with sr.AudioFile('16.wav') as source:
    
    audio_text = r.record(source, duration=4)
    #audio_text1 = r.record(source, duration=4)
    
	# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text, language = "fr-FR")
        #text1 = r.recognize_google(audio_text1, language = "fr-FR")
        #print('Converting audio transcripts into text ...')
        print(text)
        #print(text1)
     
    except:
         print('Sorry.. run again...')