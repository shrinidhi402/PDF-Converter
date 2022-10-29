import tabula
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i",'--image',required=True, help="pdf path")
args = vars(ap.parse_args())
file_name = args['image']

doc_pdf = 'pdfcopy/'+ file_name
table = tabula.read_pdf(doc_pdf,pages="all")
var = table[0]
tabula.convert_into(doc_pdf,"demo7.csv",pages="all")



# import json
# import os

# from win32com.client import Dispatch
    
# file_name = loader['name'] 

# word = win32com.client.Dispatch("Word.Application")
# word.visible = 0

# doc_pdf ="D:/xampp/htdocs/Workspace/DemoFiles/"+ file_name
# input_file = os.path.abspath(doc_pdf)
# wb = word.Documents.Open(input_file)
# output_file = os.path.abspath(doc_pdf[0:-4]+ "docx".format())
# wb.SaveAs2(output_file,FileFormat=16)
# print("Conversion Completed...")
# wb.Close()
# word.Quit()
# os.startfile(output_file+".docx")