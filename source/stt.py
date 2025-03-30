import speech_recognition as sr


def speach_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  # Без таймаутов и лимитов по времени

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
    except sr.UnknownValueError:
        return "nonsense"
    except sr.RequestError:
        return "badrequest"

    return text
