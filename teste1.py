class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        return (self.marca, self.modelo, self.ano)

class Carro(Veiculo):
    def __init__(self,placa,quilometragem,marca,modelo,ano):
        super(Carro,self).__init__(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.diaria = 2.5
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def ler_carro(self):
        print("\nplaca:",self.placa,"KM:",self.quilometragem,"diaria:",self.diaria,"marca:",self.marca,"modelo:",self.modelo,"ano:",self.modelo)
        return self.placa, self.quilometragem, self.diaria, self.marca, self.modelo, self.ano

marca = input("Cadastre a Marca do Veiculo: ")
modelo = input('Cadastre o Modelo do veiculo: ')
ano = int(input("Cadastre o Ano do Veiculo"))
placa = input("Cadastre a placa: ")
quilometragem = int(input("Cadastre a KM: "))

g1 = Veiculo(marca,modelo,ano)
g1 = Carro(placa,quilometragem)
g1.ler_carro()
