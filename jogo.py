class Jogo:
    def __init__(self, nome, genero, nota):
        self.nome = nome
        self.genero = genero
        self.nota = nota

    def exibir_info(self):
        print(f"🎮 {self.nome} | Gênero: {self.genero} | Nota: {self.nota}")


class JogoOnline(Jogo):
    def __init__(self, nome, genero, nota, servidores):
        super().__init__(nome, genero, nota)
        self.servidores = servidores

    def exibir_info(self):  
        super().exibir_info()
        print(f"🌐 Servidores disponíveis: {', '.join(self.servidores)}")