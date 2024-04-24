# Mesmo código do csv_test mas aplicando o conceito de classes

import pandas as pd # type: ignore


class CsvProcessor:
    def __init__(self,file_path: str): #  toda classe precisa de uma método construtor que é o método de inicialização
        self.file_path = file_path # Aqui registramos na propriedade da classe que é o file_path que recebemos
        self.df = None # Aqui criamos uma segunda instância para inicializar um parâmetro df pois quero que o dataframe fique salvo na minha classe porque sei que vou transformar o csv
        self.df_filtrado = None


    def carregar_csv(self): # O nosso primeiro método está recebendo self que são todos os parâmetros que já estão dentro desta classe (file_path e df)
        self.df = pd.read_csv(self.file_path) # Essa função não vai ter retorno pois a razão dele é associar os atributos.


    # def filtrar_por(self, coluna, atributo):
    #     self.df_filtrado = self.df[self.df[coluna] == atributo]
    #     return self.df_filtrado

    ## Vamos receber um vetor de strings
    def filtrar_por2(self, colunas, atributos): # Esse é um exemplo onde abordamos recursividade. A recursividade é quando a minha função chama novamente a minha função se for necessário. Imagina que vamos receber várias colunas
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")

        if len(colunas) == 0:
            return self.df

        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas == 1):
            return df_filtrado
        else:
            return self.filtrar_por2(colunas[1:], atributos[1:])



    # def sub_filtro(self, coluna, atributo):
    #     return self.df_filtrado[self.df_filtrado[coluna] == atributo]


# Agora vamos fazer uma implementação dessa função




