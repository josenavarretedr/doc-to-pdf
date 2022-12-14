import os
from os import listdir
from os.path import isfile, join


mypath = './archivos/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

mylist = [1,2,3,4,5,6,7]
files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f)]
print(files_no_ext)


# from PyPDF2 import PdfFileReader, PdfFileWriter


# pdf_file_path = 'prueba.pdf'
# file_base_name = pdf_file_path.replace('.pdf', '')
# output_folder_path = os.path.join(os.getcwd(), 'output')

# pdf = PdfFileReader(pdf_file_path)

# for page_number in range(pdf.getNumPages()):
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(pdf.getPage(page_number))

#     with open(os.path.join(output_folder_path, repr(onlyfiles[page_number])+'.pdf'.format(file_base_name, page_number+1)), 'wb') as output_file:
#         pdf_writer.write(output_file)
#         print('Created:'+repr(onlyfiles[page_number])+'.pdf'.format(file_base_name, page_number))
#         output_file.close()