#Program to read the Word Document



#This is a third party module install it by typing 'pip install python-docx'

#import the 'python-docx'
import docx

def getText(filename):

    #create a document object
    doc = docx.Document(filename)
    
    fullText = []

    #loop through all the paragraphs in the document
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('file_Location/file_Name.docx'))
