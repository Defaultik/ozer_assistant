from tts import text_to_speech
from stt import speach_to_text
from api import open_program


def main():
    text = speach_to_text()

    if ("open" in text) and ("program" in text):
        text_to_speech("Okay, which program you want to open?")

        program_name = speach_to_text()
        text_to_speech(f"Okay, I am opening {program_name}")
        open_program(program_name)


if __name__ == "__main__":
    main()