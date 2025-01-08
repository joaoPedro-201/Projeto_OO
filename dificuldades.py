import random
from jogador import JogadorMaquina
from collections import Counter


class MaquinaFacil(JogadorMaquina):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_jogada(self, *_):
        return random.choice(["pedra", "papel", "tesoura"])


class MaquinaMedia(JogadorMaquina):
    def __init__(self, nome):
        super().__init__(nome)
        self.jogadas_passadas = []

    def fazer_jogada(self, jogada_anterior):
        if jogada_anterior:
            self.jogadas_passadas.append(jogada_anterior)
        if self.jogadas_passadas:
            contador = Counter(self.jogadas_passadas)
            mais_comum = contador.most_common(1)[0][0]
            if mais_comum == "pedra":
                return "papel"
            elif mais_comum == "papel":
                return "tesoura"
            else:
                return "pedra"

        return random.choice(["pedra", "papel", "tesoura"])


class MaquinaDificil(JogadorMaquina):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_jogada(self, jogada_anterior):
        if jogada_anterior == "pedra":
            return "papel"
        elif jogada_anterior == "papel":
            return "tesoura"
        else:
            return "pedra"
