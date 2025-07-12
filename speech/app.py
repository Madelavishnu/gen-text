import speech_recognition as sr



recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 You said:", text)
except sr.UnknownValueError:
    print("❌ Couldn’t understand your speech.")
    text = ""
except sr.RequestError as e:
    print("⚠️ API error; check your internet connection.", e)
    text = ""
