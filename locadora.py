from datetime import datetime, timedelta

class Veiculo:
    def init(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = True
        
class Carro(Veiculo):
    def init(self, marca, modelo, ano, placa, quilometragem, valor_diaria):
        super().init(marca, modelo, ano)
        self.placa = placa
        self.quilometragem = quilometragem
        self.valor_diaria = valor_diaria
        
class Cliente:
    def init(self, nome, id):
        self.nome = nome
        self.id = id
        self.historico_alugueis = []
        
class Aluguel:
    def init(self, cliente, carro, data_inicio, data_fim):
        self.cliente = cliente
        self.carro = carro
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.valor_aluguel = 0
        
    def calcular_valor(self):
        dias_aluguel = (self.data_fim - self.data_inicio).days + 1
        valor_base = dias_aluguel * self.carro.valor_diaria
        if (self.data_fim - datetime.now()).days < 0:
            atraso = abs((self.data_fim - datetime.now()).days)
            valor_atraso = atraso * self.carro.valor_diaria * 1.2
            self.valor_aluguel = valor_base + valor_atraso
        else:
            self.valor_aluguel = valor_base
            
        self.carro.disponivel = True
        self.cliente.historico_alugueis.append(self)
        
class App:
    def init(self):
        self.clientes = []
        self.carros = []
        self.alugueis = []
        
    def cadastrar_carro(self, carro):
        self.carros.append(carro)
        
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        
    def consultar_disponibilidade(self, carro):
        return carro.disponivel
    
    def listar_carros_por_marca(self, marca):
        return [carro for carro in self.carros if carro.marca == marca]
    
    def listar_carros_por_modelo(self, modelo):
        return [carro for carro in self.carros if carro.modelo == modelo]
    
    def listar_carros_por_ano(self, ano):
        return [carro for carro in self.carros if carro.ano == ano]
    
    def alugar_carro(self, cliente, carro, data_inicio, data_fim):
        if not carro.disponivel:
            return False
        aluguel = Aluguel(cliente, carro, data_inicio, data_fim)
        aluguel.calcular_valor()
        self.alugueis.append(aluguel)
        return True
    
    def devolver_carro(self, aluguel):
        if aluguel in self.alugueis:
            self.alugueis.remove(aluguel)
            return aluguel.valor_aluguel
        return None
