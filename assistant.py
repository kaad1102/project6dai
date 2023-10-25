import speech_recognition
import pyttsx3
import requests
import json
import os
def play_voice_assistant_speech(text_to_speech):

    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()

def weather(city):
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?&q=" + city + "&lang=ru&units=metric&appid=db9b6f4ba87ed79cfc1c54f5cb8438eb")
        data = response.json()
        temperature = round(data['main']['temp'])
        print(temperature)
        mes = ('Сейчас в городе', city, str(temperature), '°')
        return mes
    except:
        mes = 'Проверьте название города!'
        return mes



def record_and_recognize_audio(*args: tuple):

    with microphone:
        recognized_data = ""


        recognizer.adjust_for_ambient_noise(microphone, duration=3)

        try:
            print('запись')
            audio = recognizer.listen(microphone, 0, 2)


        except speech_recognition.WaitTimeoutError:
            return


        try:
            print("чел")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass


        except speech_recognition.RequestError:
            print("ошибка")

        return recognized_data


def record():

        voice_input = record_and_recognize_audio()
        print(voice_input)
        return voice_input



if __name__ == "__main__":


    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    ttsEngine = pyttsx3.init()
    while True:
        words = record()
        word = words.split()
        i=len(word)
        for words_count in range (i):
            command = word[words_count]
            if command == "погода":
                play_voice_assistant_speech("город")
                city = record()
                result = weather(city)
                print (result)
                play_voice_assistant_speech(result)


