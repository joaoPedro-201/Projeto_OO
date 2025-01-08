from jogo import Jogo
from sistema_pontuacao import SistemaPontuacao


def main():
    sistema_pontuacao = SistemaPontuacao()
    jogo = Jogo(sistema_pontuacao)
    jogo.executar()


if __name__ == "__main__":
    main()
