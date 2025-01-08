from jogador import JogadorHumano
from dificuldades import MaquinaFacil, MaquinaMedia, MaquinaDificil
from mensagens import mostrar_resultado, mostrar_menu


class Jogo:
    def __init__(self, sistema_pontuacao):
        self.sistema_pontuacao = sistema_pontuacao
        self.jogador1 = JogadorHumano("Jogador Humano")
        self.maquina = None

    def configurar_maquina(self, dificuldade):
        if dificuldade == "Fácil":
            self.maquina = MaquinaFacil("Máquina")
        elif dificuldade == "Médio":
            self.maquina = MaquinaMedia("Máquina")
        else:
            self.maquina = MaquinaDificil("Máquina")

    def executar(self):
        while True:
            self.sistema_pontuacao.zerar_pontuacao()
            dificuldade = mostrar_menu()
            self.configurar_maquina(dificuldade)

            jogada_anterior = None

            while True:
                jogada1 = self.jogador1.fazer_jogada()
                jogada2 = self.maquina.fazer_jogada(jogada_anterior)

                jogada_anterior = jogada1

                vencedor = self.determinar_vencedor(jogada1, jogada2)
                mostrar_resultado(
                    self.jogador1.nome, jogada1,
                    self.maquina.nome, jogada2, vencedor
                )
                if vencedor == "jogador":
                    self.sistema_pontuacao.registrar_vitoria("jogador")
                elif vencedor == "maquina":
                    self.sistema_pontuacao.registrar_vitoria("maquina")
                self.sistema_pontuacao.mostrar_pontuacao()

                continuar = input(
                    "Você quer jogar novamente? (sim/não): "
                                  ).lower()
                if continuar not in ["sim", "s"]:
                    break

            jogar_novamente = input(
                "Você deseja jogar novamente? (sim/não): "
                ).lower()
            if jogar_novamente not in ["sim", "s"]:
                print("Obrigado por jogar! Até a próxima!")
                break

    def determinar_vencedor(self, jogada1, jogada2):
        regras = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}
        if jogada1 == jogada2:
            return "empate"
        elif regras[jogada1] == jogada2:
            return "jogador"
        else:
            return "maquina"
