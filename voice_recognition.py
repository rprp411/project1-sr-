import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
r = sr.Recognizer()
def start_recognition():
    try:
        with sr.Microphone() as source:
            print("Speak...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()
            print("Recognized text:", text)
            result_label.config(text=f"Recognized Text: {text}")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except KeyboardInterrupt:
        print("Exiting...")
        window.destroy()

window = tk.Tk()
window.title("Speech Recognition")
window.geometry("400x200")
window.configure(bg="lightblue")

start_button = tk.Button(window,bg='green', text="Start Recognition", command=start_recognition)
start_button.pack(pady=20)

result_label = tk.Label(window, bg='yellow',text="Recognized Text: ")
result_label.pack(pady=20)

window.mainloop()



