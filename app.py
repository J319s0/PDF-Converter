from pdf2image import convert_from_path
import os
from ctypes import windll

#Fix scaling issues with windows
windll.shcore.SetProcessDpiAwareness(1)

#Get current path
absolutepath = os.path.abspath(__file__)
parentDirectory = os.path.dirname(absolutepath)
#Get path PDFs will be located in
path = os.path.join(parentDirectory, 'PDF')
#Get path JPGs will be saved into
outputPath = os.path.join(parentDirectory, 'Output') 

print("Checking if necessary folders exist..")
if os.path.isdir(path):
    print("Folders exist. Continuing..")
    i=0
    for pdfFiles in os.listdir(path):
    #Get PDF file
        if pdfFiles.endswith(".pdf"):
            i = i + 1
            print("File Found.")
            #Move into PDF files directory
            os.chdir(path)
            #Read PDF file
            pages = convert_from_path(pdfFiles)
            #ignore '.pdf'
            pdfFiles = pdfFiles[:-4]
            #Move out of PDF files directory
            os.chdir(parentDirectory)

            #Get each page in PDF file
            for page in pages:
                #Save as JPG
               page.save("Output\page%d.jpg" % pages.index(page), "JPEG")
            print("Pages saved.")
    #No pdf files
    if i==0:
        print("No PDF files found. Please place PDFs into 'PDF' Folder and run this again.")
#No folders to contain files
else:
    #Create required folders
    os.mkdir(path)
    os.mkdir(outputPath)
    print("Folders created. Please place PDFs into 'PDF' Folder and run this again.")