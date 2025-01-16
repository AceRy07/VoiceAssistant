from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser
from pathlib import Path
import urllib.parse 

r = sr.Recognizer()

class VoiceAssistant():

    def record(ask=False):
        with sr.Microphone() as source:
            if ask:
                print(ask)
            
            audio = r.listen(source)
            voice = ""

            try:
                voice = r.recognize_google(audio,language="tr-TR")

            except sr.UnknownValueError:
                print("Assistant: I don't understand")
            
            except sr.RequestError:
                print("Assistant: Error in the system")
            
            return voice
        
    def speak(self, string):
        tts=gTTS(text=string, lang="tr", slow=False)
        file = "answer"+str(random.randint(0,124312412312))+".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)


    def response(self, voice):
        if "merhaba" in voice:
            self.speak("Sana da merhaba gençler")

        if "selam" in voice:
            self.speak("Sana da selamlar olsun.")

        if "teşekkür ederim" in voice or "teşekkürler" in voice:
            self.speak("rica ederim.")

        if "görüşürüz" in voice:
            self.speak("Görüşürüz birtanem")
            exit()

        if "hangi gündeyiz" in voice:
            today = time.strftime("%A")
            today.capitalize()
            if today == "Monday":
                today="Pazartesi"
            elif today == "Thuesday":
                today="Salı"
            elif today == "Wendesday":
                today="Çarşamba"
            elif today == "Thursday":
                today="Perşembe"
            elif today == "Friday":
                today="Cuma"
            elif today == "Saturday":
                today="Cumartesi"
            elif today == "Sunday":
                today="Pazar"
            self.speak(today)

        if "saat kaç" in voice:
            selection = ["Saat şu an: ", "Hemen bakıyorum: "]
            clock = datetime.now().strftime("%H:%M")
            selection = random.choice(selection)
            self.speak(selection+clock)

        if "google'da ara" in voice:
            self.speak("Ne aramak istersin")
            search = self.record()
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            self.speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))

        if "youtube'da ara" in voice:
            self.speak("Aramak istediğin video adı?")
            video_adi = self.record()
            video_adi = urllib.parse.quote(video_adi)
            youtube_url = f"https://www.youtube.com/results?search_query={video_adi}"
            webbrowser.open(youtube_url)
            print(f"'{video_adi}' için YouTube'da arama yapılıyor...")

        if "uygulama aç" in voice:
            self.speak("Hangi uygulamayı açmamı istiyorsun?")
            runApp = self.record()
            runApp = runApp.lower()

            if "valo" in runApp:
                os.startfile("D:\\Valorant\\Riot Games\\Riot Client\\RiotClientServices.exe")
                self.speak("İstediğin uygulamayı açıyorum")

            if "steam" in runApp:
                os.startfile("D:\\Steam\\steam.exe")
                self.speak("İstediğin uygulama açılıyor.")


            # if "dc" in voice:
            #     os.startfile(r"C:\\Users\\DELL\\AppData\\Local\\Discord\\app-1.0.9178\\Discord.exe") # r ile ham string olarak belirtildi.
            #     self.speak("İstediğin uygulamayı açıyorum")


        if "not et" in voice:
            self.speak("Dosya ismi ne olsun?")
            txtFile = self.record() + ".txt"
            self.speak("Ne kaydetmek istiyorsun?")
            theText = self.record()
            f = open(txtFile, "w", encoding="utf-8")
            f.writelines(theText)
            f.close()

        if "sil" in voice:
            self.speak("Silmek istediğin dosyanın adını söyle.")
            dosya_adi = self.record() + ".txt" # Burada record'dan dosya adını alıyoruz string olarak

            # Dosya adını Path objesine dönüştür
            dosya_yolu = Path(dosya_adi) #string'den pathlib.Path nesnesine dönüştürülüyor.

            if dosya_yolu.exists():
                try:
                    dosya_yolu.unlink()
                    self.speak(f"{dosya_adi} adlı dosya başarıyla silindi.")
                except PermissionError:
                    self.speak(f"{dosya_adi} adlı dosyayı silmek için yetkiniz yok.")
                except OSError as e:
                    self.speak(f"Dosya silinirken bir hata oluştu: {e}")
                    print(e)
            else:
                self.speak(f"{dosya_adi} adlı dosya bulunamadı.")




    def wakeUp(self, wake):
        if "uyan" in wake:
            while True:
                playsound("DING.mp3")
                print("Listening")
                wake=self.record()

                if wake!="":
                    voice = wake.lower()
                    print(wake.capitalize())
                    self.response(voice)

assistant=VoiceAssistant()
playsound("DING.mp3")


wake = assistant.record()

if wake!='':
    wake = wake.lower()
    print(wake.capitalize())
    assistant.wakeUp(wake)