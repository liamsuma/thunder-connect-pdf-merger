import os,sys
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pdfrw import PdfReader, PdfWriter

input_paths = '/Users/Su/Desktop/Backlog_Data/Zaro Inc'

x = [a for a in os.listdir(input_paths) if a.endswith(".pdf")]

writer = PdfWriter()
for inpfn in x:
    writer.addpages(PdfReader(inpfn).pages)
writer.write('test.pdf')


