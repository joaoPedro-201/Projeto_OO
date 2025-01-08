import json


class SistemaPontuacao:
    def __init__(self, arquivo="placar.json"):
        self.arquivo = arquivo
        self.pontuacao = {"jogador": 0, "maquina": 0}
        self.carregar_pontuacao()

    def carregar_pontuacao(self):
        try:
            with open(self.arquivo, "r") as file:
                self.pontuacao = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.salvar_pontuacao()

    def salvar_pontuacao(self):
        with open(self.arquivo, "w") as file:
            json.dump(self.pontuacao, file)

    def registrar_vitoria(self, vencedor):
        if vencedor in self.pontuacao:
            self.pontuacao[vencedor] += 1
        self.salvar_pontuacao()

    def zerar_pontuacao(self):
        self.pontuacao = {"jogador": 0, "maquina": 0}
        self.salvar_pontuacao()

    def mostrar_pontuacao(self):
        print("🏆 Placar Atual:")
        print(f"Jogador: {self.pontuacao['jogador']}")
        print(f"Máquina: {self.pontuacao['maquina']}")
