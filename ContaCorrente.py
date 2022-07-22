from Conta import Conta

class ContaCorrente(Conta):
    
    def __init__(self, titular, conta, saldo, limite):
        super().__init__(titular, conta, saldo)
        self.limite = limite

    def verificarSaque(self,valor):
        if self.saldo + self.limite >= valor:
            return True
        else:
            return False

