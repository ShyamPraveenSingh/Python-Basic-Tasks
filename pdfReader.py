#Copy the text contents of the pdf file.

#the module used is PyPDF2 (it is a third party module, install it with using pip)
import PyPDF2


#opening the pdf file in 'rb' mode
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)


#get the total number of pages present in the pdf file
print('The total number of pages is:', reader.numPages)


#Confirmation
print ('Do you want to print all the text of the pdf file? ', end='')
ans = input()


#extract all the text from the pdf
if str(ans) == 'y' or 'Y':
    for pageNum in range (reader.numPages):
        print(reader.getPage(pageNum).extractText())


