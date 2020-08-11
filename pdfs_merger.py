import os,sys
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pdfrw import PdfReader, PdfWriter

input_paths = '/Users/Su/Desktop/dummy_pdfs' # this is a relative path and need to change its directory
os.chdir(input_paths) 

x = [a for a in os.listdir(input_paths) if a.endswith(".pdf")]

# after changing the directory to the current path, then needs to loop through all pdf files 

pdf_merger = PdfFileMerger()
pdf_writer = PdfFileWriter()

for pdf in x:
    pdfFileObj = open(pdf, 'rb')
    pdf_reader = PdfFileReader(pdfFileObj)

    for pageNum in range(0, pdf_reader.numPages):
        pageObj = pdf_reader.getPage(pageNum)
        pdf_writer.addPage(pageObj)

with open('/Users/Su/Desktop/dummy_pdfs/test.pdf', 'wb') as output:
    pdf_writer.write(output)    

output.close()

