class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano 

class Carro(Veiculo):
    def __init__(self,marca, modelo, ano, placa, quilometragem, valor_diaria):
        super().__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria

class Cliente:
    def __init__(self, nome, id, historico_aluguel):
        self.nome = nome
        self.id = id
        self.historico_aluguel = historico_aluguel

class ListaCarros:
    def __init__(self):
        self.carros = []

class App(Carro): 
    def cadastrar_carro(self):
        marca = str(input("Digite a marca: "))
        modelo = str(input("Digite o modelo: "))
        ano = int(input("Digite o ano: "))
        placa = str(input("Digite a placa: "))
        km = int(input("Digite a quilometragem: "))
        valor_diaria = int(input("Digite o valor da diária: "))
        carro = Carro(marca, modelo, ano, placa, km, valor_diaria)
        self.carros.append(carro)

app = App()
