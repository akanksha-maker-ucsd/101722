# importing required modules 
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('paper-1.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 


#get number of pages 
totalpages = pdfReader.numPages

for i in range(totalpages):
    # creating a page object 
    pageObj = pdfReader.getPage(i)
        
    # extracting text from page 
    print(pageObj.extractText()) 
    
# closing the pdf file object 
pdfFileObj.close() 


