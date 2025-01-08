# Jogo de Pedra, Papel e Tesoura

Este é um jogo de **Pedra, Papel e Tesoura** implementado em Python. O jogo permite que o jogador humano jogue contra uma máquina com diferentes níveis de dificuldade. O placar é salvo entre sessões de jogo.

## Funcionalidades

- **Sistema de Pontuação**: O jogo mantém um placar acumulado entre as partidas. O placar é salvo em um arquivo JSON e exibido ao final de cada rodada.
- **Níveis de Dificuldade**: Existem três níveis de dificuldade para a máquina:
  - **Fácil**: A máquina escolhe aleatoriamente.
  - **Médio**: A máquina prevê a jogada do jogador com base em jogadas anteriores.
  - **Difícil**: A máquina escolhe sempre a jogada que derrota a do jogador.
- **Interface de Texto Interativa**: O jogo interage com o jogador através de texto, com mensagens divertidas e coloridas que indicam o vencedor de cada rodada.

## Requisitos

- Python 3.x
- Bibliotecas adicionais:
  - `colorama`: Para colorir o texto no terminal.
  - `json`: Para salvar o placar em um arquivo JSON.

Você pode instalar as dependências necessárias com:

```bash
pip install colorama

Como jogar:

- Clone o repositório ou baixe os arquivos.
- Execute o arquivo main.py para iniciar o jogo.
- Escolha o nível de dificuldade desejado.
- Faça sua jogada escolhendo entre "Pedra", "Papel" ou "Tesoura".
- O jogo continuará até que você decida sair.
- Estrutura do Projeto

O projeto é composto pelas seguintes classes principais:

- Jogador: Classe abstrata que define a interface para jogadores.
- JogadorHumano: Implementação da classe Jogador para o jogador humano.
- JogadorMaquina: Classe abstrata para máquinas de diferentes dificuldades.
- MaquinaFacil, MaquinaMedia, MaquinaDificil: Implementações de máquinas com diferentes níveis de dificuldade.
- Jogo: Controlador do fluxo do jogo, onde o jogador interage com a máquina.
- SistemaPontuacao: Responsável por salvar e carregar o placar do jogo.

Exemplo de execução do código:

Escolha o nível de dificuldade (Fácil/Médio/Difícil): Fácil
Jogador Humano, escolha Pedra, Papel ou Tesoura: pedra
Jogador Humano escolheu: pedra
Máquina escolheu: tesoura
🎉 Você venceu!
🏆 Placar Atual:
Jogador: 1
Máquina: 0
Você quer jogar novamente? (sim/não): sim

Diagrama UML:
O diagrama UML do projeto pode ser visualizado [aqui](uml/uml_diagrama.png).
