#Nomes: Matheus e Rodrigo

import csv

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.lista_favoritos = []
        self.lista_ultimos_assistidos = []

    def adicionar_favorito(self, midia):
        if midia not in self.lista_favoritos:
            if len(self.lista_favoritos) >= 10:
                self.lista_favoritos.pop(0)
            self.lista_favoritos.append(midia)
            print("Midia adicionada aos favoritos.")
        else:
            print("Midia já está nos favoritos.")

    def remover_favorito(self, midia):
        if midia in self.lista_favoritos:
            self.lista_favoritos.remove(midia)
            print("Midia removida dos favoritos.")
        else:
            print("Midia não encontrada nos favoritos.")

    def adicionar_ultimo_assistido(self, midia):
        if midia in self.lista_ultimos_assistidos:
            self.lista_ultimos_assistidos.remove(midia)
        elif len(self.lista_ultimos_assistidos) >= 10:
            self.lista_ultimos_assistidos.pop(0)
        self.lista_ultimos_assistidos.append(midia)
        print("Midia adicionada aos últimos assistidos.")

    def listar_midias_apropriadas(self, tipo, catalogo):
        midias_apropriadas = []
        lista_midias = catalogo.obter_lista(tipo)
        for midia in lista_midias:
            if midia.classificacao != "18 anos" or self.idade >= 18:
                midias_apropriadas.append(midia)
        return midias_apropriadas

    def assistir_midia(self, midia):
        print(f"A midia {midia.titulo} foi exibida.")
        self.adicionar_ultimo_assistido(midia)

    def favoritar_midia(self, midia, favoritar):
        if favoritar:
            self.adicionar_favorito(midia)
        else:
            self.remover_favorito(midia)

    def buscar_por_titulo(self, titulo, catalogo):
        tipos_midia = ["Serie", "Filme", "Documentario", "Animacao", "Programa de TV"]
        for tipo in tipos_midia:
            lista_midias = catalogo.obter_lista(tipo)
            for midia in lista_midias:
                if midia.titulo == titulo:
                    return midia
        return None

class Catalogo:
    def __init__(self):
        self.lista_series = []
        self.lista_filmes = []
        self.lista_documentarios = []
        self.lista_animacoes = []
        self.lista_programas_tv = []

    def adicionar_midia(self, midia, tipo):
        if tipo == "Serie":
            self.lista_series.append(midia)
        elif tipo == "Filme":
            self.lista_filmes.append(midia)
        elif tipo == "Documentario":
            self.lista_documentarios.append(midia)
        elif tipo == "Animacao":
            self.lista_animacoes.append(midia)
        elif tipo == "Programa de TV":
            self.lista_programas_tv.append(midia)
        print("Midia adicionada com sucesso!")

    def obter_lista(self, tipo):
        if tipo == "Serie":
            return self.lista_series
        elif tipo == "Filme":
            return self.lista_filmes
        elif tipo == "Documentario":
            return self.lista_documentarios
        elif tipo == "Animacao":
            return self.lista_animacoes
        elif tipo == "Programa de TV":
            return self.lista_programas_tv

def carregar_catalogo(nome_arquivo):
    catalogo = Catalogo()
    with open(nome_arquivo, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # Pula o cabeçalho
        for row in reader:
            tipo = row[1]
            titulo = row[2]
            genero = row[3]
            ano_lancamento = row[4]
            classificacao = row[5]

            # Verifica se o valor de ano_lancamento é um número inteiro
            try:
                ano_lancamento = int(ano_lancamento)
            except ValueError:
                print(f"Valor invalido para Ano de Lançamento: {ano_lancamento}")
                continue

            if tipo == "Serie":
                num_temporadas = int(row[6])
                lista_episodios = eval(row[7])  # Converter string para lista
                midia = Serie(titulo, genero, ano_lancamento, classificacao, num_temporadas, lista_episodios)
            elif tipo == "Filme":
                diretor = row[6]
                produtor = row[7]
                midia = Filme(titulo, genero, ano_lancamento, classificacao, diretor, produtor)
            elif tipo == "Documentario":
                tema = row[6]
                midia = Documentario(titulo, genero, ano_lancamento, classificacao, tema)
            elif tipo == "Animacao":
                estudio = row[6]
                midia = Animacao(titulo, genero, ano_lancamento, classificacao, estudio)
            elif tipo == "Programa de TV":
                num_episodios = int(row[6])
                lista_episodios = row[7].split(",")   # Converter string para lista
                midia = ProgramaTV(titulo, genero, ano_lancamento, classificacao, num_episodios, lista_episodios)
            else:
                print(f"Tipo de midia invalido: {tipo}")
                continue

            catalogo.adicionar_midia(midia, tipo)

    return catalogo

class Usuario:
    def __init__(self, nome_usuario, senha, tipo_assinatura):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.lista_perfis = []

    def adicionar_perfil(self, nome, idade):
        if len(self.lista_perfis) < self.obter_limite_perfis():
            perfil = Perfil(nome, idade)
            self.lista_perfis.append(perfil)
            print("Perfil adicionado com sucesso!")
        else:
            print("Limite maximo de perfis atingido para o tipo de assinatura.")

    def remover_perfil(self, nome):
        for perfil in self.lista_perfis:
            if perfil.nome == nome:
                self.lista_perfis.remove(perfil)
                print("Perfil removido com sucesso!")
                return
        print("Perfil não encontrado.")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso!")

    def alterar_plano(self, novo_tipo_assinatura):
        self.tipo_assinatura = novo_tipo_assinatura
        print("Plano alterado com sucesso!")

    def obter_limite_perfis(self):
        if self.tipo_assinatura == "Simples":
            return 3
        elif self.tipo_assinatura == "Premium":
            return 5


class Midia:
    contador_id = 1,

    def __init__(self, tipo, titulo, genero, ano_lancamento, classificacao):
        self.id = Midia.contador_id
        Midia.contador_id += 1
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.classificacao = classificacao

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Tipo:", self.tipo)
        print("Titulo:", self.titulo)
        print("Genero:", self.genero)
        print("Ano de Lancamento:", self.ano_lancamento)
        print("Classificacao:", self.classificacao)

class Serie(Midia):
    def __init__(self, titulo, genero, ano_lancamento, classificacao, num_temporadas, lista_episodios):
        super().__init__("Serie", titulo, genero, ano_lancamento, classificacao)
        self.num_temporadas = num_temporadas
        self.lista_episodios = lista_episodios

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Numero de Temporadas:", self.num_temporadas)

    def listar_episodios(self, num_temporada):
        if num_temporada > 0 and num_temporada <= self.num_temporadas:
            print(f"Episodios da Temporada {num_temporada}:")
            if num_temporada <= len(self.lista_episodios):
                for episodio in self.lista_episodios[num_temporada-1]:
                    print(episodio)
            else:
                print("Temporada nao encontrada.")
        else:
            print("Numero de temporada invalido.")


class Filme(Midia):
    def __init__(self, titulo, genero, ano_lancamento, classificacao, diretor, produtor):

        super().__init__("Filme", titulo, genero, ano_lancamento, classificacao)
        self.diretor = diretor
        self.produtor = produtor

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Diretor(a):", self.diretor)
        print("Produtor(a):", self.produtor)


class Documentario(Midia):
    def __init__(self, titulo, genero, ano_lancamento, classificacao, tema):
        super().__init__("Documentario", titulo, genero, ano_lancamento, classificacao)
        self.tema = tema

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Tema:", self.tema)


class Animacao(Midia):
    def __init__(self, titulo, genero, ano_lancamento, classificacao, estudio):
        super().__init__("Animacao", titulo, genero, ano_lancamento, classificacao)
        self.estudio = estudio

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Estudio:", self.estudio)


class ProgramaTV(Midia):
    def __init__(self, titulo, genero, ano_lancamento, classificacao, num_episodios, lista_episodios):
        super().__init__("Programa de TV", titulo, genero, ano_lancamento, classificacao)
        self.num_episodios = num_episodios
        self.lista_episodios = lista_episodios

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Numero de Episodios:", self.num_episodios)

    def listar_episodios(self):
        print("Episodios:")
        for episodio in self.lista_episodios:
            print(episodio)


# Exemplo de uso

# Carrega o catálogo a partir do arquivo "catalogoGeral.csv"
catalogo_geral = carregar_catalogo("catalogoGeral.csv")

# Cria um usuário
usuario = Usuario("joao123", "senha123", "Premium")

# Adiciona um perfil ao usuário
usuario.adicionar_perfil("João", 25)

# Lista as mídias apropriadas para o perfil "João" do usuário
perfil_joao = usuario.lista_perfis[0]
midias_apropriadas = perfil_joao.listar_midias_apropriadas("Serie", catalogo_geral)
for midia in midias_apropriadas:
    midia.exibir_informacoes()

# Exibe informações de uma série específica
serie = catalogo_geral.obter_lista("Serie")[0]
serie.exibir_informacoes()

# Lista os episódios da temporada 2 da série
serie.listar_episodios(2)

# Adiciona a série aos favoritos do perfil "João"
perfil_joao.adicionar_favorito(serie)

# Remove a série dos favoritos do perfil "João"
perfil_joao.remover_favorito(serie)

# Altera a senha do usuário
usuario.alterar_senha("nova_senha")

# Altera o plano de assinatura do usuário
usuario.alterar_plano("Simples")
