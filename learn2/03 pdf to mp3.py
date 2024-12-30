import pyttsx3
from PyPDF2 import PdfReader

reader = PdfReader("book.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)


speaker = pyttsx3.init()

speaker.save_to_file(text, 'story.mp3')
speaker.runAndWait()

speaker.stop()