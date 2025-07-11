from api_client import RAWGClient
from jogo import JogoOnline
from gerenciador_jogos import GerenciadorJogos

def main():
    gerenciador = GerenciadorJogos()

    nome_busca = input("Digite o nome de um jogo: ")
    dados = RAWGClient.buscar_jogo(nome_busca)

    if dados:
        print("✅ Jogo encontrado:")
        print(dados)

        jogo = JogoOnline(
            nome=dados["nome"],
            genero=dados["genero"],
            nota=dados["nota"],
            servidores=["Brasil", "EUA", "Europa"]
        )

        gerenciador.adicionar_jogo(jogo)
        gerenciador.mostrar_catalogo()
        gerenciador.exportar_csv()

    else:
        print("❌ Jogo não encontrado na API.")

if __name__ == "__main__":
    main()
