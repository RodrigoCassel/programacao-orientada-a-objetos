# 1. Você faz parte da equipe de desenvolvimento de uma plataforma de streaming e sua tarefa é
# implementar a funcionalidade de persistência de dados. A plataforma permite que os usuários se
# cadastrem, façam assinaturas e acessem conteúdos exclusivos.
# Você precisa criar as classes Usuário e Assinatura para representar os dados dos usuários e suas
# assinaturas, além de implementar a leitura desses dados a partir de arquivos CSV.
# Classe Usuário
# Atributos: nome, sobrenome, data de nascimento (no formato dd/mm/aaaa), CPF, nome de
# usuário, senha, assinaturas (uma lista de objetos da classe Assinatura).
# Métodos da classe Usuário:
# • Construtor: recebe os atributos do usuário (exceto as assinaturas) e inicializa os respectivos
# atributos. Deve-se, no seu cabeçalho, inicializar todos os valores com ‘None’, pois estes
# valores podem vir mais tarde com a desserialização.
# • adicionar_assinatura(assinatura): recebe um objeto da classe Assinatura e adiciona à lista
# de assinaturas do usuário.
# • cancelar_assinatura(id_assinatura): recebe o ID de uma assinatura e remove-a da lista de
# assinaturas do usuário. Esse ID corresponde ao índice da assinatura do usuário na lista, que
# o usuário visualizará no menu e o selecionará.
# • exibir_dados(): exibe os dados do usuário, incluindo nome, sobrenome, data de nascimento,
# CPF, nome de usuário e senha.
# • serializar(): retorna uma string contendo os atributos do usuário no formato CSV (separados
# por vírgula) para posterior persistência em arquivo.
# • desserializar(dados): método estático que recebe uma lista com os dados de uma assinatura
# no formato CSV e altera os atributos de um objeto da classe Usuários com os valores lidos.
# Classe Assinatura
# Atributos: tipo, preço, ID do usuário, status.
# Métodos da classe Assinatura:
# • Construtor: recebe os atributos da assinatura e inicializa os respectivos atributos. Deve-se,
# no seu cabeçalho, inicializar todos os valores com ‘None’, pois estes valores podem vir mais
# tarde com a desserialização.
# • exibir_dados(): exibe os dados da assinatura, incluindo tipo, preço, ID do usuário e status.
# • serializar(): retorna uma string contendo os atributos da assinatura no formato CSV
# (separados por vírgula) para posterior persistência em arquivo.
# • desserializar(dados): método estático que recebe uma lista com os dados de uma assinatura
# no formato CSV e altera os atributos de um objeto da classe Assinatura com os valores lidos.
# Inicialmente, você precisa implementar as classes Usuário e Assinatura com seus respectivos
# métodos de acordo com as especificações acima. Em seguida, você deve implementar o código que
# realiza a leitura dos arquivos CSV contendo os dados dos usuários e assinaturas. O arquivo
# "usuarios.csv" contém as informações dos usuários, já o arquivo "assinaturas.csv" contém os dados
# das assinaturas, de maneira que podemos atribuí-las aos usuários.
# Após a leitura dos arquivos, você deve adicionar as assinaturas aos usuários correspondentes. Cada
# assinatura deve ser associada ao usuário com base no ID do usuário (CPF) presente no arquivo de
# assinaturas.
# Para testar, inicialmente comece com a leitura dos arquivos de exemplo fornecidos em aula.
# Permita adicionar usuários e adicionar/cancelar assinaturas no sistema. Permita salvar as
# alterações, alterando (reescrevendo) os arquivos CSV.

import csv

class Usuario:
    def __init__(self, nome, sobrenome, data_nascimento, cpf, nome_usuario, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.assinaturas = []

    def adicionar_assinatura(self, assinatura):
        self.assinaturas.append(assinatura)

    def cancelar_assinatura(self, id_assinatura):
        if id_assinatura < len(self.assinaturas):
            del self.assinaturas[id_assinatura]

    def exibir_dados(self):
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Nome de Usuário: {self.nome_usuario}")
        print(f"Senha: {self.senha}")

    def serializar(self):
        return f"{self.nome},{self.sobrenome},{self.data_nascimento},{self.cpf},{self.nome_usuario},{self.senha}"

    @staticmethod
    def desserializar(dados):
        nome, sobrenome, data_nascimento, cpf, nome_usuario, senha = dados
        return Usuario(nome, sobrenome, data_nascimento, cpf, nome_usuario, senha)


class Assinatura:
    def __init__(self, tipo, preco, id_usuario, status):
        self.tipo = tipo
        self.preco = preco
        self.id_usuario = id_usuario
        self.status = status

    def exibir_dados(self):
        print(f"Tipo: {self.tipo}")
        print(f"Preço: {self.preco}")
        print(f"ID do Usuário: {self.id_usuario}")
        print(f"Status: {self.status}")

    def serializar(self):
        return f"{self.tipo},{self.preco},{self.id_usuario},{self.status}"

    @staticmethod
    def desserializar(dados):
        tipo, preco, id_usuario, status = dados
        return Assinatura(tipo, preco, id_usuario, status)


def ler_usuarios():
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            usuario = Usuario.desserializar(linha)
            usuarios.append(usuario)
    return usuarios


def gravar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for usuario in usuarios:
            escritor_csv.writerow(usuario.serializar().split(','))


def ler_assinaturas():
    assinaturas = []
    with open('assinaturas.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            assinatura = Assinatura.desserializar(linha)
            assinaturas.append(assinatura)
    return assinaturas


def gravar_assinaturas(assinaturas):
    with open('assinaturas.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for assinatura in assinaturas:
            escritor_csv.writerow(assinatura.serializar().split(','))


def adicionar_usuario(usuario):
    usuarios = ler_usuarios()
    usuarios.append(usuario)
    gravar_usuarios(usuarios)


def adicionar_assinatura(assinatura):
    assinaturas = ler_assinaturas()
    assinaturas.append(assinatura)
    gravar_assinaturas(assinaturas)


def cancelar_assinatura(id_assinatura):
    assinaturas = ler_assinaturas()
    if id_assinatura < len(assinaturas):
        del assinaturas[id_assinatura]
        gravar_assinaturas(assinaturas)


# Exemplo de uso

# Lendo usuários e assinaturas existentes nos arquivos CSV
usuarios = ler_usuarios()
assinaturas = ler_assinaturas()

# Criando um novo usuário e adicionando uma assinatura
novo_usuario = Usuario("João", "Silva", "01/01/1990", "123456789", "joaosilva", "senha123")
nova_assinatura = Assinatura("Premium", 9.99, "123456789", "Ativa")
novo_usuario.adicionar_assinatura(nova_assinatura)

# Adicionando o novo usuário e assinatura ao sistema
adicionar_usuario(novo_usuario)

# Cancelando a segunda assinatura do primeiro usuário
cancelar_assinatura(1)

# Exibindo os dados do primeiro usuário
usuarios = ler_usuarios()
usuarios[0].exibir_dados()
