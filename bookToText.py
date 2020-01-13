# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 02:38:12 2020

@author: VicFabrice
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import re

output = PdfFileWriter()
pdfBook = PdfFileReader(open("ess.pdf", "rb"))


pageObj = pdfBook.getPage(1)         
text = str(pageObj.extractText())

print(re.split('[.]', text))
                 
#quotes = re.findall(r'"[^"]*"',text)
#for quote in quotes:
#    print(quote)

    
    
numPages = pdfBook.getNumPages() 

print(numPages)
# print how many pages input1 has:
print("El segundo sexo tiene " + str(numPages) + " paginas.")

