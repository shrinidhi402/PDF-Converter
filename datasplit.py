import pandas as pd
import xlsxwriter
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i",'--image',required=True, help="pdf path")
args = vars(ap.parse_args())
file_name = args['image']
doc_file = 'pdfcopy/' + file_name
df = pd.read_excel(doc_file)
# print(df)

split_values = df['Marks'].unique()
# print(df['Marks'][2])
# print(split_values)
# print(split_values[3])

dfinal_40_50 = pd.DataFrame(columns = [ 'Marks'])
dfinal_50_60 = pd.DataFrame(columns = ['Marks'])
dfinal_60_70 = pd.DataFrame(columns = ['Marks'])
dfinal_70_80 = pd.DataFrame(columns = ['Marks'])
dfinal_80_90 = pd.DataFrame(columns = ['Marks'])
dfinal_90_100 = pd.DataFrame(columns = ['Marks'])

for value in split_values:
  df1 = df[df['Marks'] == value]
  if value in range(40,50):
    dfinal_40_50 = dfinal_40_50.append(df1, ignore_index=True)
  elif value in range(50,60):
    dfinal_50_60 = dfinal_50_60.append(df1, ignore_index=True)
  elif value in range(60,70):
    dfinal_60_70 = dfinal_60_70.append(df1, ignore_index=True)
  elif value in range(70,80):
    dfinal_70_80 = dfinal_70_80.append(df1, ignore_index=True)
  elif value in range(80,90):
    dfinal_80_90 = dfinal_80_90.append(df1, ignore_index=True)
  elif value in range(90,100):
    dfinal_90_100 = dfinal_90_100.append(df1, ignore_index=True)


writer = pd.ExcelWriter('marksheet_2.xlsx', engine='xlsxwriter')

dfinal_40_50.to_excel(writer, sheet_name='40-50',index=False)
dfinal_50_60.to_excel(writer, sheet_name='50-60',index=False)
dfinal_60_70.to_excel(writer, sheet_name='60-70',index=False)
dfinal_70_80.to_excel(writer, sheet_name='70-80',index=False)
dfinal_80_90.to_excel(writer, sheet_name='80-90',index=False)
dfinal_90_100.to_excel(writer, sheet_name='90-100',index=False)
writer.save()
   

