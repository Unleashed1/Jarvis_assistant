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

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Buon giorno!')

    if currentH >= 12 and currentH < 18:
        speak('Buon Pomeriggio!')

    if currentH >= 18 and currentH !=0:
        speak('Buona sera!')

greetMe()

speak('Sono il suo assistente, Jarvis')
speak('Come posso aiutarla?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  2
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='it-IT')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Mi scusi non ho capito, potrebbe ripetere?')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'apri youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')    

        elif 'Jarvis apri google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'Jarvis apri g mail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "Jarvis come va?" in query or 'Jarvis come stai?' in query:
            stMsgs = ['Hail idra!, ops questo non avrei dovuto dirlo!', 'Sto bene grazie signore', 'Bene!', 'Tutto ok e pronto ad eseguire i suoi ordini signore']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('A chi devo spedire questa mail?')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('Cosa vuole che scriva?')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("mail", 'pass')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email inviata con successo!')

                except:
                    speak('Mi dispiace signore i chitauri hanno attaccato i server google, non sono in grado di inviare mail!')


        elif 'niente' in query or 'Jarvis abortire' in query or 'Fermati' in query or 'Jarvis non ora' in query:
            speak('okay')
            speak('A presto signore, buona giornata.')
            sys.exit()
           
        elif 'Ciao Jarvis' in query:
            speak('Buongiorno signore!')

        elif 'Grazie jarvis' in query or 'Grazie' in query or '':
            speak('Arrivederci signore, le auguro una buona giornata.')
            sys.exit()
                        
            

        else:
            query = query
            speak('Faccio una ricerca...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA dice - ')
                    speak('Ci siamo.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Attendo un suo comando...')
