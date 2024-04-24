# Esse código era receber um csv

import pandas as pd # type: ignore

df = pd.read_csv('/home/faust/Projetos/EngDados/aula12_bootcamp/exemplo.csv')

df_filtrado = df[df['estado'] == 'SP']

print(df_filtrado)