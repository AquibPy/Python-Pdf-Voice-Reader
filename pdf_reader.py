import PyPDF2
import pyttsx3

def extract_text(filename):
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    mytext = ""

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        mytext += pageObj.extractText()
    pdfFileObj.close()
    return mytext

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 2000)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

if __name__== '__main__':
    text = extract_text('sample.pdf')
    speak(text)
    sample = open('sample.txt','w')
    sample.write(text)
    sample.close()