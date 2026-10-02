import pyttsx3
import PyPDF2 as pdf
from tkinter.filedialog import askopenfilename

file = askopenfilename()

reader = pdf.PdfReader(file)
pages = len(reader.pages)

player = pyttsx3.init()

for num in range(pages):
    page = reader.pages[num]
    text = page.extract_text()

    if text:
        player.say(text)

player.runAndWait()