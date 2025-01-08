class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def fazer_jogada(self):
        raise NotImplementedError(
            "Este método deve ser implementado pelas subclasses."
            )


class JogadorHumano(Jogador):
    def fazer_jogada(self):
        jogada = input(
            f"{self.nome}, escolha Pedra, Papel ou Tesoura: "
            ).lower()
        while jogada not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida, tente novamente!")
            jogada = input(
                f"{self.nome}, escolha Pedra, Papel ou Tesoura: "
                ).lower()
        return jogada


class JogadorMaquina(Jogador):
    def fazer_jogada(self, jogada_oponente=None):
        raise NotImplementedError(
            "Deve ser implementado nas subclasses específicas de dificuldade."
                                  )
