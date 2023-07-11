class Jogador:
    def __init__(self, nome, numero_camisa):
        self.nome = nome
        self.numero_camisa = numero_camisa
        self.__posicao = None

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao


class NoLista:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.jogadores = None

    def adicionar_jogador(self, jogador):
        numeroCamisa = NoLista(jogador)

        if self.jogadores is None:
            self.jogadores = numeroCamisa
        else:
            if jogador.numero_camisa < self.jogadores.jogador.numero_camisa:
                numeroCamisa.proximo = self.jogadores
                self.jogadores = numeroCamisa
            else:
                atual = self.jogadores
                anterior = None

                while atual is not None and jogador.numero_camisa > atual.jogador.numero_camisa:
                    anterior = atual
                    atual = atual.proximo

                numeroCamisa.proximo = atual
                anterior.proximo = numeroCamisa

    def imprimir_lista(self):
        atual = self.jogadores

        while atual is not None:
            jogador = atual.jogador
            print(f"Nome: {jogador.nome}, Número da camisa: {jogador.numero_camisa}, Posição: {jogador.get_posicao()}")
            atual = atual.proximo


lista = ListaEncadeada()

while True:
    print("----- Menu -----")
    print("1. Adicionar jogador")
    print("2. Imprimir lista de jogadores")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do jogador: ")
        numero_camisa = int(input("Digite o número da camisa do jogador: "))
        posicao = input("Digite a posição do jogador: ")
        jogador = Jogador(nome, numero_camisa)
        jogador.set_posicao(posicao)
        lista.adicionar_jogador(jogador)
        print("Jogador adicionado com sucesso!")
    elif escolha == "2":
        print("Lista de jogadores:")
        lista.imprimir_lista()
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Digite novamente.")
