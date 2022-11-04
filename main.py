import PyPDF2

name = input("enter the pdf file name without the extension(.pdf)\n")
name = name + '.pdf'
pdffileobj = open(name, 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)
file1 = open("result.txt", "a", encoding='windows-1252')
x = pdfreader.numPages
for i in range(x):
    pageobj = pdfreader.getPage(i)
    text = pageobj.extractText()
    file1.writelines(text)

# if __name__ == '__main__':
