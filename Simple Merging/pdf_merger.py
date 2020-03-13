import sys
from PyPDF2 import PdfFileMerger 

merger = PdfFileMerger() # new pdf file merger
files = sys.argv[1:]  # get file path's of pdf files from command prompt

for file_path in files:
    input = open(file_path, "rb")
    merger.append(input)  # append entire input document to the end of the output document

# Write to an output PDF document
output = open("output.pdf", "wb")
merger.write(output)