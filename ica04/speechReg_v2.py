"""
OPTIMUS J49S
A wit.ai chat bot

Thanks to:
- http://stackoverflow.com/questions/7771011/parse-json-in-python
- https://docs.python.org/2/library/json.html
- http://docs.python-guide.org/en/latest/scenarios/json/
"""

# Import dependencies
import speech_recognition as sr
import pyttsx
import json

# pyttsx speech preferences
engine = pyttsx.init()
engine.setProperty("rate", 100)
engine.setProperty("voice", 16)

# Initiate variables
WIT_AI_KEY = "XWEMS7AMLRWMZRUEIIVZPBGACSVDVP4I"
r = sr.Recognizer()
m = sr.Microphone()

# Adjust microphone sensitivity
with m as source: r.adjust_for_ambient_noise(source)

def parseReplyData(replyData):
    replyData = json.dumps(replyData) # Parse JSON object to JSON String
    parsed_json = json.loads(replyData) # Parse JSON string to Python dict
    
    if parsed_json["_text"] == "hello":
        print("hello to you as well")

        
def main():
    while True:
        print("Listening")
        with m as source: audio = r.listen(source)
        print("Recognizing")
        try:
            
            # Utilising wit.ai as speech recognizer 
            # Because we define shoow_all as true, it returns a raw JSON object
            replyData = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
            parseReplyData(replyData)
                    
        except sr.UnknownValueError:
            print("I didn't understand that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from wit.ai web services; {0}".format(e))

main()