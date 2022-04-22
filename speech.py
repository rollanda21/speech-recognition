#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
liste = []

max = 20

j = 0
sum = 0

for j in range(0,300):

	liste.append(sum)
	sum = sum + 5

print('****************** dernière valeur de sum:***************** \n')
print(sum)


i = 0
for i in liste:


	with sr.AudioFile("{0}_Clip0030.wav".format(i)) as source:
	    
	    audio_text = r.listen(source)
	    
	# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
	    try:
	        
	        # using google speech recognition
	        text = r.recognize_google(audio_text, language = "fr-CA")
	        #print('Converting audio transcripts into text ...')
	        print(text)
	     
	    except:
	         print('Inaudible...')

    