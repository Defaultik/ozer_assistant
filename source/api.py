import os

def open_program(program_name):
    programs = {
        "google chrome": "chrome.exe",
        "firefox": "firefox.exe",
        "microsoft edge": "msedge.exe",
        "vlc media player": "vlc.exe",
        "notepad": "notepad.exe"
    }

    program = programs.get(program_name.lower())
    
    if program:
        os.system(f"start {program}")