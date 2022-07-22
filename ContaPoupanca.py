from Conta import Conta

class ContaPoupanca(Conta):

    def __init__(self, titular, conta, saldo,taxaRendimento):
        super().__init__(titular, conta, saldo)
        self.taxaRendimento = taxaRendimento
        self.saldo += self.saldo*0.01*self.taxaRendimento
