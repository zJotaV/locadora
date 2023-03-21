from datetime import timedelta, date
import random

lista_dos_carros = []
lista_dos_clientes = []

class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado_de_aluguel = False

class Carro(Veiculo):
    def __init__(self,marca, modelo, ano, placa, quilometragem, valor):
        super().__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor

    def alugar_carro(self, tempo_a_ser_alugado):
        self.estado_de_aluguel = True
        self.tempo_a_ser_alugado = int(tempo_a_ser_alugado)
        self.valor_a_ser_pago = self.tempo_a_ser_alugado*self.valor_diaria
        
        dia_alugado = date.today()
        dia_final = timedelta(days= self.tempo_a_ser_alugado) + timedelta(-1)
        dia_da_entrega = dia_alugado + dia_final
    
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
        print(f"o valor total a ser pago é de: R${self.valor_a_ser_pago}")

    def __str__(self):
        return f"marca: {self.marca}\n modelo: {self.modelo}\nano: {self.ano}\nvalor da diaria: {self.valor_diaria}\nplaca: {self.placa}\nquilometragem: {self.quilometragem}"
    
class Cliente():
    def __init__(self, nome, id_usuario) -> None:
        self.nome = nome
        self.id_usuario = id_usuario
        self.historico_do_usuario = []

    def consulta_de_historico(self):
        if len(self.historico_do_usuario) > 0:
            for carro in self.historico_do_usuario:
                print("="*10)
                print(f" {carro.marca}\n {carro.modelo}\n {carro.ano}\n {carro.placa} ")
                print("="*10)
        else:
            print("o cliente não possui carros cadastrados")

    def adicionar_ao_historico(self, carro_alugado):
        lista_dos_carros.append(carro_alugado)

    def __str__(self):
        return f"Cliente: {self.nome} -- id: {self.id_usuario}"

class App(Carro):
    def cadastrar_carro():
        marca = str(input("marca:"))
        modelo = str(input("modelo: "))
        ano = int(input("ano: "))
        quilometragem = int(input("quilometros rodados: "))
        placa = str(input("placa do carro: "))
        diaria_do_carro = int(input("valor da diaria: "))
        carro_cadastrado = Carro(marca, modelo, ano, placa, quilometragem, diaria_do_carro)
        lista_dos_carros.append(carro_cadastrado)

    def cadastro_do_cliente():
        novo_usuario = str(input("nome do cliente: "))
        id_usuario = random.randint(100,999)
        cliente_novo = Cliente(novo_usuario, id_usuario)
        lista_dos_clientes.append(cliente_novo)

    def alugar_um_carro():
        lista_de_carros_disponiveis = []
        
        #seleçao de clientes
        App.mostrar_cliente()
        cliente = int(input("Qual cliente irá alugar o carro: "))
        cliente_selecionado = lista_dos_clientes[cliente]

        #cria uma lista de carros disponiveis
        for carros in lista_dos_carros:
            if(carros.estado_de_aluguel == False):
                lista_de_carros_disponiveis.append(carros)
        
        #mostra carros disponiveis
        if(len(lista_de_carros_disponiveis) > 0):
            i = 0
            for carros in lista_de_carros_disponiveis:
                if(carros.estado_de_aluguel == False):
                    print(i,"---------")
                    print(carros)
                i+=1
            #escolhe carro
            carro_escolhido = int(input("id do carro selecionado: "))
            
            carro_alugado = lista_dos_carros[carro_escolhido]

            tempo_que_devolvel = int(input("por quantos dias sera alugado: "))

            carro_alugado.alugar_carro(tempo_que_devolvel)

            cliente_selecionado.adicionar_ao_historico(carro_alugado)

            print("carro alugado com sucesso")

        else:
            print("não possui carros disponiveis")

    def devolver_o_carro():
        lista_de_carros_alugados = []

        for carros in lista_dos_carros:
            if(carros.estado_de_aluguel == True):
                lista_de_carros_alugados.append(carros)

        if(len(lista_de_carros_alugados) > 0):
            i =0
            for carros in lista_dos_carros:
                print(i,"---------")
                print(carros)
            i+=1

            carro_selecionado = int(input("qual carro deseja devolver: "))  
            carro_selecionado = lista_dos_carros[carro_selecionado]

            dias_entregue = int(input("em quantos dias foi entregue"))
            
            carro_selecionado.devolver_carro(dias_entregue)
            
        else:
            print("não possui carros disponiveis")

    def mostrar_cliente():
        i= 0
        for clientes in lista_dos_clientes:
            print("*"*10)
            print(i,"-",clientes)

    def mostrar_carros():
        i = 0
        for carros in lista_dos_carros:
            print(i,"*"*10) 
            print(carros)  

    def ver_historico():
        App.mostrar_cliente()
        cliente_verificado = int(input("qual historico deseja ver"))
        cliente_selecionado = lista_dos_clientes[cliente_verificado]
        cliente_selecionado.consulta_de_historico()

    def lista_marca():
        lista_das_marcas = []

        for i in range(len(lista_dos_carros)):
            lista_das_marcas.append(lista_dos_carros[i].marca)
        
        marca_dos_carros = list(set(lista_das_marcas))

        for marcas in lista_das_marcas:
            print(marcas)

        marca = str(input("de qual marca deseja ver os carros"))

        for carros in lista_dos_carros:
            if(carros.marca == marca):
                print(carros)

    def lista_modelo():
        lista_dos_modelos = []

        for i in range(len(lista_dos_carros)):
            lista_dos_modelos.append(lista_dos_carros[i].modelo)

        modelos_dos_carros = list(set(lista_dos_modelos))
        
        for modelos in modelos_dos_carros:
            print(modelos)

        modelo = str(input("de qual modelo deseja ver os carros"))

        for carros in lista_dos_carros:
            if(carros.modelo == modelo):
                print(carros)

    def lista_ano():
        lista_dos_anos = []

        for i in range(len(lista_dos_carros)):
            lista_dos_anos.append(lista_dos_carros[i].ano)

        anos_dos_carros = list(set(lista_dos_anos))

        for anos in anos_dos_carros:
            print(anos)

        ano = int(input("de qual ano deseja ver os carros"))
        
        for carros in lista_dos_carros:
            if(carros.ano == ano):
                print(carros)
