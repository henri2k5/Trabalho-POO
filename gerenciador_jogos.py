import pandas as pd
from jogo import Jogo, JogoOnline

class GerenciadorJogos:
    def __init__(self):
        self.catalogo = []

    def adicionar_jogo(self, jogo):
        self.catalogo.append(jogo)

    def adicionar_jogo_por_info(self, nome, genero, nota):
        jogo = Jogo(nome, genero, nota)
        self.adicionar_jogo(jogo)

    def mostrar_catalogo(self):
        for jogo in self.catalogo:
            jogo.exibir_info()

    def exportar_csv(self, nome_arquivo="catalogo.csv"):
        df = pd.DataFrame([vars(j) for j in self.catalogo])
        df.to_csv(nome_arquivo, index=False)
        print(f"📄 Catálogo exportado para {nome_arquivo}")
