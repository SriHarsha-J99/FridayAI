import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import os
from twilio.rest import Client


account_id = os.environ.get('acc id')
auth_token = os.environ.get('acc auth_token')

client1 = Client(account_id,auth_token)
auth_token = os.environ.get('58982c7b527192cb039c37340e1df49a'),
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('your_App_id')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Friday!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
       
        
        if 'browser' in query:
            s=query.split()
            h=s[1]
            st=''
            st=st.join(h)
            speak('Okay')
            webbrowser.open_new_tab('www.'+st+'.com')

        elif 'sms' in query:
            speak("What is the message sir?")
            body=myCommand()
            client1.messages.create(from_=os.environ.get('+12052878563'),
                       to=os.environ.get('+918688888933'),
                       body='body')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif "'Who\'s the boss" in query:
            speak('It\'s you Harsha /;D')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("your_username", 'your_password')
                    server.sendmail('usrname', "recipient_email", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'thats it friday' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it!')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it!')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')