import speech_recognition as sr # Imports the speech to text module
import pyttsx # Import the text to speech module
engine = pyttsx.init()


engine.say('Greetings! Welcome to this primitive calculator. With your input we will simulate simple mathematical calculations')
engine.runAndWait()

def taleInput():
    taleInput == ""
    return taleInput # Creates the variable that holds the reply from the user's voice

engine.say("Please say the option that corresponds to your choice, one to five")
engine.runAndWait()

#print what options the user have aviable
print "Your options are:"
print " "
print "1) Addition"
print "2) Subtraction"

print "3) Multiplication"

print "4) Division"
print "5) Quit"
print " "
    
# Starts recoring from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)


WIT_AI_KEY = "MNC6LBRKJ5JH2X5T532ZDBELUKSNVD52" # Wit.ai client key
try:
    taleInput = r.recognize_wit(audio, key=WIT_AI_KEY) # saves the user's voice input into this variable    
except sr.UnknownValueError:
    print("Could not understand that, sorry")
except sr.RequestError as e:
    print("Something whent wrong with the client / server, sorry; {0}".format(e))
    
if taleInput == "one":
    print "You choosed addition"
    print ""
    engine.say("You have choosen addition, please follow the instructions on the screen")
    engine.runAndWait()
    add1 = input("Add this: ") # The numbers to add togheter
    add2 = input("to this: ")
    engine.say("By addings these two numbers, we got the following number") # The computer tells the user this message and prints result
    engine.runAndWait()
    print add1, "+", add2, "=", add1 + add2
    print "" # To add a extra space for convinience saks
        
elif taleInput == "two": # The rest of the methods below follows the addition patern with simple mathematical calculations
    print "You choosed subtraction"
    print ""
    engine.say("You have choosen subtraction, please follow the instructions on the screen")
    engine.runAndWait()    
    sub2 = input("Subtract this: ")
    sub1 = input("from this: ")
    engine.say("By subtracting these two numbers, we got the following number")
    engine.runAndWait()
    print sub1, "-", sub2, "=", sub1 - sub2
    print ""
        
elif taleInput == "three":
    print "You choosed multiplying"
    print ""
    engine.say("You have choosen multiplying, please follow the instructions on the screen")
    engine.runAndWait()    
    mul1 = input("Multiply this: ")
    mul2 = input("with this: ")
    engine.say("By multiplying these two numbers, we got the following number")
    engine.runAndWait()
    print mul1, "*", mul2, "=", mul1 * mul2
    print ""
        
elif taleInput == "four":
    print "You choosed dividing"
    print ""
    engine.say("You have choosen dividing, please follow the instructions on the screen")
    engine.runAndWait()    
    div1 = input("Divide this: ")
    div2 = input("by this: ")
    engine.say("By dividing these two numbers we got the following number")
    engine.runAndWait()
    print div1, "/", div2, "=", div1 / div2
    print ""
        
elif taleInput == "five":
    print "You choosed to quit"
    engine.say("Thank you for using this simple calculator Which is shamelessly borrowed from sthurlow.com.")
    engine.say("If I were Janis I would be mighty impressed by such an intelligent program")
    engine.runAndWait()
        
else: # If the computer cannot determine what word was said, return this message and close the program. 
    print "Could not understand that word, sorry *sadbot*"
    engine.say("We could not understand what was said, sorry. The program will therfore close")
    engine.runAndWait()  
    

engine.say("Thank you for using this simple calculator")
engine.say("Please close this program and start over again if you wish to do a new calculation")
engine.say("Doing a loop is so yesterday, wink wink")
engine.runAndWait()
print "Press enter to close the program"
raw_input()
    