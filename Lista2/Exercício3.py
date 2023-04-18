#3)Crie uma classe CadastroCliente com os atributos nome, sobrenome, data de nascimento, email,
#CPF e senha. Faça um pequeno programa que permita o cliente se cadastrar e depois consultar
#seus dados. Para consultar seus dados, é necessário que ele faça o login com seu email e senha.
#Se o cliente errar a senha 3x, o cadastro é bloqueado e ele não pode mais acessar.


class Data:
    # def __init__(self, dia, mes, ano):
    #     self.dia = dia
    #     self.mes = mes
    #     self.ano = ano

    def __init__(self):
        self.dia = 0 
        self.mes = 0 
        self.ano = 0  

    def alterarDia(self, dia): #Método de setar o valor do atributo dia
        self.dia = dia

    def alterarMes(self, mes): #Método de setar o valor do atributo mes
        self.mes = mes

    def alterarAno(self, ano): #Método de setar o valor do atributo ano
        self.ano = ano

    def retornarDia(self): #Método para retornar o valo do atributo dia
        return self.dia
    def retornarMes(self): #Método para retornar o valo do atributo mes
        return self.mes
    def retornarAno(self): #Método para retornar o valo do atributo ano
        return self.ano
    
    def exibirData(self):
        return self.dia,self.mes,self.ano

    def retornarStrMes(self): 
        if self.mes == 1:
            return 'janeiro'
        elif self.mes == 2:
            return 'fevereiro'
        elif self.mes == 3:
            return 'março'
        elif self.mes == 4:
            return 'abril'
        elif self.mes == 5:
            return 'maio'
        elif self.mes == 6:
            return 'junho'
        elif self.mes == 7:
            return 'julho'
        elif self.mes == 8:
            return 'agosto'
        elif self.mes == 9:
            return 'setembro'
        elif self.mes == 10:
            return 'outubro'
        elif self.mes == 11:
            return 'novembro'
        elif self.mes == 12:
            return 'dezembro'
        else:
            print ('Mês inválido!')
    
    # def exibirDataPorExtenso(self):
    #     dataINT = self.retornarStrMes() #método chamado de dentro da própria classe
    #     print(cidade, ', ', self.dia, ' de ' , self.mes, ' de ', self.ano)


class CadastroCliente:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.dataNascimento = ''
        self.email = ''
        self.cpf = ''
        self.__senha = ''
        self.cidade = ''
        self.__bloqueado = False

    # Métodos de set (setters)
    def alterarNome(self, nome):
        self.nome = nome

    def alterarSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def alterarDataNascimento(self, dia, mes, ano):
        self.dataNascimento = Data()
        self.dataNascimento.alterarDia(dia)
        self.dataNascimento.alterarMes(mes)
        self.dataNascimento.alterarAno(ano)

    def alterarEmail(self,email):
        self.email = email
        #recomendável fazer uma validação do email (@,.)
    
    def alterarCPF(self, cpf):
        #recomendável fazer validação: nro de caracteres e 
        #verificar se caracteres são numéricos
        #asciiCode = ord(cpf[i]) //recupera o valor em ascii
        #if (asciiCode >= 48 and asciiCode <=57): //é um caracter numerico
        self.cpf = cpf

    def alterarCidade(self, cidade):
        self.cidade = cidade

    def alterarSenha(self, senha):
        # recomendável validar senha (caracter numérico, maiúscula...)
        self.__senha = senha
    
    def validarSenha(self, senhaDigitada):
        if self.__senha == senhaDigitada:
            return True
        else:
            return False
        
    def bloquear(self):
        self.__bloqueado = True

    # Métodos de get (getters): retornam valores dos atributos
    def retornaNome(self):
        return self.nome
    def retornaSobrenome(self):
        return sobrenome
    def retornaCPF(self):
        return cpf
    def retornaEmail(self):
        return email
    def retornaCidade(self):
        return cidade
    def retonaDataNascimento(self):
        return data


cliente = CadastroCliente()

nome = input('Digite nome: ')
cliente.alterarNome(nome)

sobrenome = input('Digite sobrenome: ')
cliente.alterarSobrenome(sobrenome)

#.. fazer a leitura do restante e alterar no objeto do cadastro
senhaCriada = input('Digite a nova senha: ')
cliente.alterarSenha(senhaCriada)

cpf = input('Digite seu CPF:')
cliente.alterarCPF(cpf)

email = input('Digite seu email:')
cliente.alterarEmail(email)

cidade = input('Digite o nome da cidade de nascimento: ')
cliente.alterarCidade(cidade)

data = Data()
dia = input('Digite o dia de nascimento: ') 
data.alterarDia(dia)
mes = input('Digite o mês de nascimento: ') 
data.alterarMes(mes)
ano = input('Digite o ano de nascimento: ') 
data.alterarAno(ano)

contTentativas = 0
acertouSenha = False

while contTentativas < 3 and not acertouSenha:
    senhaDigitada = input('Digite sua senha cadastrada: ')
    validacao = cliente.validarSenha(senhaDigitada)
    if validacao == True:
        acertouSenha = True
    else:
        print('Senha incorreta!')
    contTentativas = contTentativas + 1

if (acertouSenha == False):
    #bloqueia a conta
    cliente.bloquear()
    print('Conta bloqueada!')
else:
    print('Dados do cliente: ')
    print(cliente.retornaNome(),(cliente.retornaSobrenome()))
    print(cliente.retornaEmail())
    print(cliente.retornaCPF())
    print(cliente.retornaCidade(),(data.exibirData()))