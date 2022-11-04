import PyPDF2
import pyperclip


name = input("enter the pdf file name without the extension(.pdf)\n")
name = name + '.pdf'
pdffileobj = open(name, 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)
x = pdfreader.numPages
output = ''
for i in range(x):
    pageobj = pdfreader.getPage(i)
    text = pageobj.extractText()
    output += text
pyperclip.copy(output)
# if __name__ == '__main__':
