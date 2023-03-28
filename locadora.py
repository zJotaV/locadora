#Importação da função datetime e random, para calcular tempo e gerar id randomicamente, nessa sequência
from datetime import timedelta, date
import random

#Criação das listas para receber os carros e os clientes
lista_dos_carros = []
lista_dos_clientes = []

#Classe Veiculo que recebe os parâmetros marca, modelo e ano
class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado_de_aluguel = False

#Classe Carro que é herda os parâmetros de Veiculo que recebe os parâmetros marca, modelo, ano, placa, quilometragem e valor
class Carro(Veiculo):
    def __init__(self,marca, modelo, ano, placa, quilometragem, valor):
        super().__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor

    #Função de alugar carro que recebe o tempo que o carro vai ser alugado e calcula o valor a ser pago
    def alugar_carro(self, tempo_a_ser_alugado):
        self.estado_de_aluguel = True
        self.tempo_a_ser_alugado = int(tempo_a_ser_alugado)
        self.valor_a_ser_pago = self.tempo_a_ser_alugado*self.valor_diaria
        
        dia_alugado = date.today()
        dia_final = timedelta(days= self.tempo_a_ser_alugado) + timedelta(-1)
        dia_da_entrega = dia_alugado + dia_final

    #Função para devolver carro, recebe os dias que o cliente utilizou o carro e calcula o valor que o cliente deve pagar,
    #se tiver multa, ela também calcula
    def devolver_carro(self, dia_apos_aluguel):
        self.dias_do_aluguel = dia_apos_aluguel
        self.estado_de_aluguel = False

        if(self.dias_do_aluguel > self.tempo_a_ser_alugado):
            tempo_atrasado = self.dias_do_aluguel - self.tempo_a_ser_alugado
            self.valor_a_ser_pago = (self.valor_diaria*self.tempo_a_ser_alugado) + ((self.valor_diaria+(self.valor_diaria*0.20))*tempo_atrasado)

        else:
            if(self.tempo_a_ser_alugado > self.dias_do_aluguel):
                self.valor_a_ser_pago = self.valor_diaria*self.dias_do_aluguel

            else:
                self.valor_a_ser_pago = self.valor_diaria*self.tempo_a_ser_alugado
        print(f"\nO valor total a ser pago é de: R${self.valor_a_ser_pago}")

    def __str__(self):
        if(self.estado_de_aluguel == False):
            alugado = "\nDisponível\n"
        else:
            alugado = "\nIndisponível\n"

        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nValor da diária: {self.valor_diaria}\nPlaca: {self.placa}\nQuilometragem: {self.quilometragem}\n {alugado}"

#Classe Cliente que recebe os parâmetros nome e id do usuário e inicializa a lista de histórico do cliente 
class Cliente():
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.historico_do_usuario = []

    #Passa por todos os carros adicionados e printa o histórico do cliente selecionado
    def consulta_de_historico(self):
        if len(self.historico_do_usuario) > 0:
            printf("\n\n")
            for carro in self.historico_do_usuario:
                print("="*10)
                print(f" Marca: {carro.marca}\nModelo: {carro.modelo}\nAno: {carro.ano}\nPlaca: {carro.placa} ")
                print("="*10)
            print("\n\n")
        else:
            print("\nO cliente não possui carros cadastrados\n")

    def adicionar_ao_historico(self, carro_alugado):
        self.historico_do_usuario.append(carro_alugado)

    def __str__(self):
        return f"Cliente: {self.nome} -- id: {self.id_usuario}"
    
#Classe App que herda os parâmetros de Carro e inicializa todas as funções do código
class App(Carro):
    def cadastrar_carro():
        marca = str(input("\nMarca:"))
        modelo = str(input("Modelo: "))
        ano = int(input("Ano: "))
        quilometragem = int(input("Quilometros rodados: "))
        placa = str(input("Placa do carro: "))
        diaria_do_carro = int(input("Valor da diaria: "))
        carro_cadastrado = Carro(marca, modelo, ano, placa, quilometragem, diaria_do_carro)
        lista_dos_carros.append(carro_cadastrado)
        print("\n")
        print("Carro cadastrado com sucesso!!!\n\n")

    #Função que recebe o nome do cliente e adiciona a lista de clientes
    def cadastro_do_cliente():
        novo_usuario = str(input("\nNome do cliente: "))
        id_usuario = random.randint(100,999)
        cliente_novo = Cliente(novo_usuario, id_usuario)
        lista_dos_clientes.append(cliente_novo)
        print("\nCliente cadastrado com sucesso!!!\n")

    #Cria a lista de carros disponíveis, seleciona o cliente desejado e mostra se o carro foi alugado ou não.
    def alugar_um_carro():
        lista_de_carros_disponiveis = []
        
        #seleçao de clientes
        App.mostrar_cliente()
        cliente = int(input("\nSelecione o número do cliente desejado: "))
        cliente_selecionado = lista_dos_clientes[cliente]
        print("\n")

        #Cria uma lista de carros disponiveis
        for carros in lista_dos_carros:
            if(carros.estado_de_aluguel == False):
                lista_de_carros_disponiveis.append(carros)
        
        #Mostra carros disponíveis
        if(len(lista_de_carros_disponiveis) > 0):
            i = 0
            print("\n")
            for carros in lista_de_carros_disponiveis:
                if(carros.estado_de_aluguel == False):
                    print(i,"---------")
                    print(carros)
                i+=1
            #Escolhe carro
            print("\n")
            carro_escolhido = int(input("id do carro selecionado: "))
            
            carro_alugado = lista_dos_carros[carro_escolhido]

            tempo_que_devolvel = int(input("\nPor quantos dias será alugado: "))

            carro_alugado.alugar_carro(tempo_que_devolvel)

            cliente_selecionado.adicionar_ao_historico(carro_alugado)

            print("\nCarro alugado com sucesso!!!\n")

        else:
            print("\nNão possui carros disponíveis\n")

    #Função para devolver um carro alugado, cria uma lista de carros que estão alugados e seleciona o que deseja devolver.
    def devolver_o_carro():
        lista_de_carros_alugados = []

        #Lista de carros alugados para devolver
        for carros in lista_dos_carros:
            if(carros.estado_de_aluguel == True):
                lista_de_carros_alugados.append(carros)

        #Verifica se ta vazio e mostra
        if(len(lista_de_carros_alugados) > 0):
            i =0
            for carros in lista_dos_carros:
                print(i,"---------")
                print(carros)
            i+=1

            carro_selecionado = int(input("\nSelecione o carro que deseja devolver: "))  
            carro_selecionado = lista_dos_carros[carro_selecionado]

            dias_entregue = int(input("\nDias utilizados: "))
            
            carro_selecionado.devolver_carro(dias_entregue)
            
        else:
            print("\nNão possui carros disponíveis\n")

    #Função para mostrar os clientes cadastrados
    def mostrar_cliente():
        i= 0
        print("\n")
        for clientes in lista_dos_clientes:
            print("*"*10)
            print(i,"-",clientes)
            i=i+1
        print("\n")

    #Função para mostrar os carros cadastrados
    def mostrar_carros():
        i = 0
        for carros in lista_dos_carros:
            print("\n\n")
            print(i,"*"*10) 
            print(carros)
            print("\n\n")
            i=i+1

    #Função para mostrar o histórico de aluguéis do cliente selecionado
    def ver_historico():
        App.mostrar_cliente()
        cliente_verificado = int(input("\nSelecione o número do cliente: "))
        cliente_selecionado = lista_dos_clientes[cliente_verificado]
        cliente_selecionado.consulta_de_historico()

    #Função para listar o carro por marca
    def lista_marca():
        lista_das_marcas = []

        #Geração de lista com todas as marcas repetidas
        for i in range(len(lista_dos_carros)):
            lista_das_marcas.append(lista_dos_carros[i].marca)

        #Remove marcas repetidas
        #Set limpa valores iguais
        marca_dos_carros = list(set(lista_das_marcas))

        #Mostra todas as marcas
        print("\n")
        for marcas in marca_dos_carros:
            print(marcas)

        marca = str(input("\nSelecione a marca desejada: "))

        #Mostra carros da marca escolhida
        print("\n")
        for carros in lista_dos_carros:
            if(carros.marca == marca):
                print(carros)
        print("\n")

    #Função para mostrar os carros por modelo
    def lista_modelo():
        lista_dos_modelos = []

        for i in range(len(lista_dos_carros)):
            lista_dos_modelos.append(lista_dos_carros[i].modelo)

        modelos_dos_carros = list(set(lista_dos_modelos))
        
        print("\n")
        for modelos in modelos_dos_carros:
            print(modelos)

        modelo = str(input("\nSelecione o modelo desejado: "))

        print("\n")
        for carros in lista_dos_carros:
            if(carros.modelo == modelo):
                print(carros)
        print("\n")

    #Função para mostrar os carros por ano
    def lista_ano():
        lista_dos_anos = []

        for i in range(len(lista_dos_carros)):
            lista_dos_anos.append(lista_dos_carros[i].ano)

        anos_dos_carros = list(set(lista_dos_anos))

        print("\n")
        for anos in anos_dos_carros:
            print(anos)

        ano = int(input("\nSelecione o ano desejado: "))
        
        print("\n")
        for carros in lista_dos_carros:
            if(carros.ano == ano):
                print(carros)
        print("\n")

    #Menu de interação e seleção de opções
    def menu():
        while(True):
            print("1-Mostrar carros")
            print("2-Cadastrar carro")
            print("3-Alugar carro")
            print("4-Devolver carro")
            print("5-Cadastrar cliente")
            print("6-Verificar historico")
            print("7-Listar por ano")
            print("8-Listar por marca")
            print("9-Listar por modelo")
            print("10-Ver clientes")
            print("0-Encerrar\n")

            opc = int(input("Selecione uma opção: "))

            if(opc == 0):
                print("\nPrograma finalizado!!!\n")
                break
            elif(opc == 1):
                App.mostrar_carros()
            elif(opc == 2):
                App.cadastrar_carro()
            elif(opc == 3):
                App.alugar_um_carro()
            elif(opc == 4):
                App.devolver_o_carro()
            elif(opc == 5):
                App.cadastro_do_cliente()
            elif(opc == 6):
                App.ver_historico()
            elif(opc == 7):
                App.lista_ano()
            elif(opc == 8):
                App.lista_marca()
            elif(opc == 9):
                App.lista_modelo()
            elif(opc == 10):
                App.mostrar_cliente()
            else:
                print("\nOpção inválida\n")

#Inicializa o programa chamando a função do menu
App.menu()
