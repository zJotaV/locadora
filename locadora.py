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
