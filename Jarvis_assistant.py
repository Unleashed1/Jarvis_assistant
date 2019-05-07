import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import platform
import sys



#inserire qui sotto i vostri dati da usare durante l'utilizzo dell'assistente vocale
nome ='vostro nome'
mail = 'vostra mail'
rubrica = {}
client = wolframalpha.Client('Your_App_ID')
#le parole non sono scritte correttamente per addolcire il suono

#controllo del so in uso per il motore da usare
if platform.system()== 'Windows':
    engine = pyttsx3.init('sapi5')
if platform.system() == 'Ubuntu' or platform.system() == 'Debian':
    engine = pyttsx3.init('espeak')
#selezione voce
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#funzione di riproduzione suono
def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

#messaggio di benvenuto 
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Buon giorno!')

    if currentH >= 12 and currentH < 18:
        speak('Buon Pomeriggio!')

    if currentH >= 18 and currentH !=0:
        speak('Buona sera!')

greetMe()

speak('Sono la sua assistente, Jarvis')


def myCommand():
    recognizer_instance = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        speak('Come posso aiutarla?')
        recognizer_instance.pause_threshold = 0.8
        print("Listening...")
        audio = recognizer_instance.listen(source)

    try:
        query = recognizer_instance.recognize_google(audio, language='it-IT')
        print(nome + ': ' + query + '\n')
        
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
            webbrowser.open('www.youtube.it')    

        elif 'Jarvis apri google' in query:
            speak('okay')
            webbrowser.open('www.google.it')

        elif 'Jarvis apri g mail' in query:
            speak('okay')
            webbrowser.open('www.gmail.it')

        elif 'Jarvis come va' in query or 'Jarvis come stai?' in query:
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
                    speak("La sua mail è¨ stata inviata con successo!")

                except:
                    speak('Mi dispiace signore i chitauri hanno attaccato i server google, non sono in grado di inviare la mail!')


        elif 'niente' in query or 'Jarvis abortire' in query or 'Fermati' in query or 'Jarvis non ora' in query:
            speak('okay')
            speak('A presto signore, buona giornata.')
            sys.exit()
           
        elif ' ciao jarvis' in query:
            speak('Salve signore!')

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
                    wikipediaapi.Wikipedia('it')
                    results = wikipedia.summary(query, sentences=2)
                    speak('Ci siamo.')
                    speak('WIKIPEDIA dice  - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.it')
        
        speak('Attendo un suo comando...')
