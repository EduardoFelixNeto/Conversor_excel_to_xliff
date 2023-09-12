import openpyxl

# Carregar o arquivo
workbook = openpyxl.load_workbook('<FILE_NAME>.xlsx')

# Selecionar a planilha ativa
sheet = workbook.active

headers = []
for cell in sheet[2]:
    headers.append(cell.value)

# Iterar sobre as linhas a partir da terceira linha
data = []
for row in sheet.iter_rows(min_row=3, values_only=True):
    row_data = dict(zip(headers, row))
    data.append(row_data)

with open('<FILE_NAME>.xliff','w') as file:
    file.write(f'<xliff version="{data[0]["/@version"]}.0">\n')
    file.write(f'<file original="{data[0]["/file/@original"]}.0" source-language="{data[0]["/file/@source-language"]}" target-language="en" datatype="{data[0]["/file/@datatype"]}">\n')
    file.write(f'<header></header>\n')
    file.write(f'<body>\n')
    for item in data:
        file.write(f'<trans-unit id="{item["/file/body/trans-unit/@id"]}">\n')
        file.write(f'<source>{item["/file/body/trans-unit/target"]}</source>\n')
        file.write(f'<target>{item["/file/body/trans-unit/source"]}</target>\n')
        file.write(f'</trans-unit>\n')
    file.write('</body>\n')
    file.write('</file>\n')
    file.write('</xliff>\n')
        