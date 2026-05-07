class Livro:
    def __init__(self, titulo, autor):
        # Privar os dados
        self.__titulo = titulo
        self.__autor = autor

        def exibir_info(self):
            print("Título: ", self.__titulo)
            print("Autor: ", self.__autor)

    # getter-> permite acessar o titulo

    @property
    def titulo(self):
        return self.__titulo
    # setter -> permite modificar o titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) > 2:
            print("Titulo muito curto")
        else:
            self.__titulo = novo_titulo

    # getter -> permite acessar o autor

    def autor(self):
        return self.__autor
    # setter -> permite modificar o autor

    def autor(self, novo_autor):
        if len(novo_autor) > 2:
            print("Autor muito curto")
        else:
            self.__autor = novo_autor


livros = []


while True:
    print("\n ====Sistema de Biblioteca====")
    print("1- Cadastrar Livro")
    print("2- Listar Livros")
    print("3- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor: ")
        ano = input("Digite o ano de publicação:")

        livro = Livro(titulo, autor)
        # livros.append(livro)

        arquivo = open("livros.txt", "a")
        arquivo.write(livro.titulo + " - " + livro.autor +
                    " - " + livro.ano + "\n")
        arquivo.close()

        print(livros)

    elif opcao == "2":
        arquivo = open("livros.txt", "r")
        livros = arquivo.readlines()
        print("\n ==== Livros Cadastrados ====")

        for livro in livros:
            print(livro.strip())
            # livro.exibir()

        arquivo.close()

    # Sair

    elif opcao == "3":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")
