from operator import truediv
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class Banco:
    def __init__(self,nome,ID):
        self.nome = nome 
        self.ID = ID
        self.contas = []
        self.contasCorrente = []
        self.contasPoupanca = []
    
    def adicionarContaCorrente(self,titular,conta,saldo,limite):
        self.contasCorrente.append(ContaCorrente(titular,conta,saldo,limite))
        self.contas.append(ContaCorrente(titular,conta,saldo,limite))

    def adicionarContaPoupanca(self,titular,conta,saldo,taxaRendimento):
        self.contasPoupanca.append(ContaPoupanca(titular,conta,saldo,taxaRendimento))
        self.contas.append(ContaPoupanca(titular,conta,saldo,taxaRendimento))

    
    def mostrarContasCorrente(self):
        for i in self.contasCorrente:
           print("---------- ID " + str(i.conta) +" ----------\n"
                +"Titular: " + i.titular + "\n"
                +"ID da Conta:" + str(i.conta) + "\n"
                +"Saldo: R$" + str(format("%.2f"%i.saldo))+"\n"
                +"Limite da Conta: R$-" + str(format("%.2f"%i.limite)) +"\n"
                +"----------------------------------------------")

    def mostrarContasPoupanca(self):
        for i in self.contasPoupanca:
          print("---------- ID " + str(i.conta) +" ----------\n"
                +"Titular: " + i.titular + "\n"
                +"ID da Conta:" + str(i.conta) + "\n"
                +"Saldo (Aplicada a Taxa de Rendimento): R$" + str(format("%.2f"%i.saldo))+"\n"
                +"Taxa de Rendimento: " + str(format("%.2f"%i.taxaRendimento)) + "%" + "\n"
                +"--------------------------------------------")

    def mostrarContas(self):
        for i in self.contas:
             print("---------- ID " + str(i.conta) +" ----------\n"
                +"Titular: " + i.titular + "\n"
                +"ID da Conta:" + str(i.conta))
             print("--------------------------------------------\n" )


    def procurarConta(self,ID):
        for i in self.contas:
            if i.conta == ID:
                print("----- Conta Encontrada -----")
                print("Titular: " + i.titular)
                print("ID de Conta: " + str(i.conta))
                print("----------------------------")
                return True
            else:
                return False


    def procurarContaCorrente(self,ID):
        for i in self.contasCorrente:
            if ID == i.conta:
                print("----- Conta Corrente Selecionada ----- ")
                print("Titular: " + i.titular)
                print("ID de Conta: " + str(i.conta))
                print("Saldo: R$" + str(format("%.2f"%i.saldo)))
                print("Limite da Conta: R$-" + str(format("%.2f"%i.limite)))
                print("---------------------------------------")
                return True


    def procurarContaPoupanca(self,ID):
        for i in self.contasPoupanca:
            if i.conta == ID:
                print("----- Conta Poupança Selecionada ----- ")
                print("Titular: " + i.titular)
                print("ID de Conta: " + str(i.conta))
                print("Saldo: R$" + str(format("%.2f"%i.saldo)))
                print("Taxa de Rendimento: " + str(format("%.2f"%i.taxaRendimento)) + "%")
                print("---------------------------------------")
                return True
    
    def excluirContaCorrente(self,ID):
        for i in self.contasCorrente:
            if(i.conta == ID):
                self.contasCorrente.remove(i)
                print("Conta Corrente removida!")
                return True
            else:
                return False

    def excluirConta(self,ID):
        for i in self.contas:
            if(i.conta == ID):
                self.contas.remove(i)
                return True
            else:
                return False
    
    def excluirContaPoupanca(self,ID):
        for i in self.contasPoupanca:
            if(i.conta == ID):
                self.contasPoupanca.remove(i)
                print("Conta Poupança removida!")
                return True
            else:
                return False

    def depositar(self,valor,ID):
        for i in self.contas:
            if(i.conta == ID):
                i.saldo+=valor
                return True

    def sacar(self,valor,ID):
        for i in self.contas:
            if(i.conta == ID and i.saldo >=valor):
                 i.saldo-=valor
                 return True


    def limparTela(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def mostrarDados(self):
        print("---------- Dados do Banco ----------")
        print("Nome do Banco: " + self.nome)
        print("ID do Banco: " + str(self.ID))
        print("Contas cadastradas: " + str(len(self.contasPoupanca) + len(self.contasCorrente)))
        print("Contas Corrente cadastradas: " + str(len(self.contasCorrente)))
        print("Contas Poupança cadastradas: " + str(len(self.contasPoupanca)))
        print("------------------------------------")
