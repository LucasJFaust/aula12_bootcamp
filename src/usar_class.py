from interface.classes.csv_class import CsvProcessor
import pandas as pd  # type: ignore

arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(arquivo_csv)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por2(['estado', 'preço'],['SP', '10,50']))
# print(arquivo_csv.df)
print('####################################')

# arquivo_csv2 = './exemplo2.csv'
# filtro2 = 'estado'
# limite2 = 'DF'

# arquivo_csv2 = CsvProcessor(arquivo_csv2)
# arquivo_csv2.carregar_csv()
# print(arquivo_csv2.filtrar_por(filtro2,limite2))
# print(arquivo_csv2.sub_filtro('preço', '10,50'))