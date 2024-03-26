import pyautogui
import pyttsx3
import pyperclip
import time

def read_selected_text():
    pyautogui.hotkey('ctrl', 'c')   # Ctrl+C to copy the selected text
    time.sleep(0.5)  # Wait for the copying to finish
    selected_text = pyperclip.paste()

    if selected_text.strip():
        engine = pyttsx3.init()         # Initialize text-to-speech engine
        engine.setProperty('rate', 150)  # Adjust speech rate (words per minute)

        engine.say(selected_text)  #speaks here
        engine.runAndWait()
    else:
        print("No text selected.")

if __name__ == "__main__":
    read_selected_text()
