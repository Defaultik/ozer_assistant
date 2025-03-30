from gtts import gTTS
import pygame
import io


def text_to_speech(text):
    tts = gTTS(text=text, lang="en", slow=False)
    
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file, "mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)