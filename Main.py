from Banco import Banco

nomeBanco = input("Insira o nome de seu banco: ")
IDBanco = int(input("Insira o ID de seu Banco: "))
B = Banco(nomeBanco,IDBanco)
print("Bem-vindo(a) ao Banco " + nomeBanco)
while True:
    print("\n")
    print("----- Menu do Banco " + nomeBanco + " -----")
    print("1.Adicionar Conta;\n"
         +"2.Selecionar Conta;\n"
         +"3.Remover Conta;\n"
         +"4.Listar Contas;\n"
         +"5.Dados do Banco;\n"
         +"6.Sair do Programa;")
    print("--------------------")
    
    op = int(input("Insira um operação: "))
    match op:
        case 1:
            B.limparTela()
            op = int(input("Escolha o tipo de conta:\n1.Conta Corrente;\t2.Conta Poupança;\n"))
            if op == 1:
                titular = input("Digite um titular válido: ")
                ID = int(input("Insira um ID de Conta válido: "))
                op = int(input("Há depósito inicial nessa conta?\n1.Sim;\t2.Não;\n"))
                if op == 1:
                    valor = float(input("Insira o valor do depósito inicial: "))
                    op = int(input("Há limite de saldo específico?\n1.Sim;\t2.Não;\n"))
                    if op == 1:
                        limite = float(input("Insira o valor do limite: "))
                        B.adicionarContaCorrente(titular,ID,valor,limite)
                        B.limparTela()

                    else:
                        B.adicionarContaCorrente(titular,ID,valor,1000.00)
                        B.limparTela()

                else:
                    op = int(input("Há limite de saldo específico?\n1.Sim;\t2.Não;\n"))
                    if op == 1:
                        limite = float(input("Insira o valor do limite: "))
                        B.adicionarContaCorrente(titular,ID,0.00,limite)
                        B.limparTela()
                    else:
                        B.adicionarContaCorrente(titular,ID,0.00,1000.00)
                        B.limparTela
            else:
                titular = input("Digite um titular válido: ")
                ID = int(input("Insira um ID de Conta válido: "))
                op = int(input("Há depósito inicial nessa conta?\n1.Sim;\t2.Não;\n"))
                if op == 1:
                    valor = float(input("Insira o valor do depósito inicial: "))
                    taxaRendimento = float(input("Insira o valor da Taxa de Rendimento: "))
                    B.adicionarContaPoupanca(titular,ID,valor,taxaRendimento)
                    B.limparTela()
                else:
                    taxaRendimento = float(input("Insira o valor da Taxa de Rendimento: "))
                    B.adicionarContaPoupanca(titular,ID,0.0,taxaRendimento)
                    B.limparTela()



        case 2:
             B.limparTela()
             op = int(input("Escolha o tipo de Conta a ser selecionada:\n"
                       +"1.Conta Corrente;\t2.Conta Poupança;\n"))
             if op == 1:
                  ID = int(input("Insira o ID da Conta Corrente:"))
                  B.limparTela()
                  while(True):
                      if(B.procurarContaCorrente(ID)):
                            print("Menu da Conta " + str(ID) + "\n"
                                + "1.Depósito;\t2.Saque;\t3.Transferência;\t4.Sair do Menu Conta;\n")
                            op = int(input("Insira uma operação: "))
                            match op:
                                case 1:
                                    valor = float(input("Insira o valor de depósito:"))
                                    for i in B.contasCorrente:
                                        if i.conta == ID:
                                            i.depositar(valor)
                                case 2:
                                    valor = float(input("Insira o valor de saque:"))
                                    for i in B.contasCorrente:
                                        if i.conta == ID:
                                            i.sacar(valor)
                                case 3:
                                    op = int(input("Escolha o tipo da conta destinatário:\n1.Conta Corrente;\t2.Conta Poupança;\n"))
                                    if op == 1:
                                        IDreceptor = int(input("Insira o ID da conta receptora:"))
                                        IDdoador = int(input("Insira o ID de sua conta: "))
                                        valor = float(input("Insira o valor de transferência: "))
                                        for i in B.contasCorrente:
                                           for j in B.contasCorrente:
                                               if i.conta == IDdoador and j.conta == IDreceptor:
                                                    if i.sacar(valor):
                                                        j.depositar(valor)
                                                        print("Transferência realizada com sucesso!")
                                                    else:
                                                       print("Credenciais Inválidas!")
                                    else:
                                        IDreceptor = int(input("Insira o ID da conta receptora:"))
                                        IDdoador = int(input("Insira o ID de sua conta: "))
                                        valor = float(input("Insira o valor de transferência: "))
                                        for i in B.contasCorrente:
                                           for j in B.contasPoupanca:
                                               if i.conta == IDdoador and j.conta == IDreceptor:
                                                    if i.sacar(valor):
                                                        j.depositar(valor)
                                                        print("Transferência realizada com sucesso!")
                                                    else:
                                                      print("Credenciais Inválidas!")               
                                case 4:
                                    B.limparTela()
                                    break
                      else:
                        print("ID não encontrado!")
                        break

             elif op == 2:
                ID = int(input("Insira o ID da Conta Poupança:"))
                B.limparTela()
                while(True):
                      if(B.procurarContaPoupanca(ID)):
                            print("Menu da Conta " + str(ID) + "\n"
                                + "1.Depósito;\t2.Saque;\t3.Transferência;\t4.Sair do Menu Conta;\n")
                            op = int(input("Insira uma operação: "))
                            match op:
                                case 1:
                                    valor = float(input("Insira o valor de depósito:"))
                                    for i in B.contasPoupanca:
                                        if i.conta == ID:
                                            i.depositar(valor)
                                case 2:
                                    valor = float(input("Insira o valor de saque:"))
                                    for i in B.contasPoupanca:
                                        if i.conta == ID:
                                            i.sacar(valor)
                                        else:
                                            print("Saldo insuficiente!")
                                case 3:
                                    op = int(input("Escolha o tipo da conta destinatário:\n1.Conta Corrente;\t2.Conta Poupança;\n"))
                                    if op == 1:
                                        IDreceptor = int(input("Insira o ID da conta receptora:"))
                                        IDdoador = int(input("Insira o ID de sua conta: "))
                                        valor = float(input("Insira o valor de transferência: "))
                                        for i in B.contasPoupanca:
                                           for j in B.contasCorrente:
                                               if i.conta == IDdoador and j.conta == IDreceptor:
                                                    if i.sacar(valor):
                                                        j.depositar(valor)
                                                        print("Transferência realizada com sucesso!")
                                                    else:
                                                       print("Credenciais inválidas!")
                                    else:
                                        IDreceptor = int(input("Insira o ID da conta receptora:"))
                                        IDdoador = int(input("Insira o ID de sua conta: "))
                                        valor = float(input("Insira o valor de transferência: "))
                                        for i in B.contasPoupanca:
                                           for j in B.contasPoupanca:
                                               if i.conta == IDdoador and j.conta == IDreceptor:
                                                    if i.sacar(valor):
                                                        j.depositar(valor)
                                                        print("Transferência realizada com sucesso!")
                                                    else:
                                                        print("Credenciais inválidas!")    
                                   
                                case 4:
                                    B.limparTela()
                                    break
                      else:
                            print("ID não encontrado!")
                            break

        case 3:
            B.limparTela()
            op  = int(input("Escolha o tipo de conta a ser removida:\n"
                       +"1.Conta Corrente;\t2.Conta Poupança;\n"))
            if op == 1:
                ID = int(input("Insira o ID da Conta Corrente a ser deletada: "))
                B.limparTela()
                if(B.procurarContaCorrente(ID)):
                    op = int(input("Tem certeza que deseja remover esta conta?\n"
                               +"1.Sim;\t2.Não;\n"))
                    if op == 1:
                        B.excluirContaCorrente(ID)
                        B.excluirConta(ID)
                    elif op == 2:

                            pass
                    else:
                        print("Operação Inválida!")
                else:
                    print("ID não registrado!")

            elif op == 2:
                ID = int(input("Insira o ID da Conta Poupança a ser deletada: "))
                B.limparTela()
                if(B.procurarContaPoupanca(ID)):
                    op = int(input("Tem certeza que deseja remover esta conta?\n"
                               +"1.Sim;\t2.Não;\n"))
                    if op == 1:
                         B.excluirContaPoupanca(ID)
                         B.excluirConta(ID)
                    elif op == 2:
                          pass
                    else:
                        print("Operação Inválida!")   
                else:
                    print("ID não registrado!") 

        case 4:
            B.limparTela()
            while(True):
                print("1.Lista de Contas Corrente;\t"
                     +"2.Lista de Contas Poupança\t"
                     +"3.Lista de todas as Contas;\t"
                     +"4.Sair\n")
                op = int(input("Insira uma operação:"))
                if op == 1:
                    B.limparTela()
                    B.mostrarContasCorrente()
                elif op == 2:
                    B.limparTela()
                    B.mostrarContasPoupanca()
                elif op == 3:
                    B.limparTela()
                    B.mostrarContas()
                elif op == 4:
                    break
                else:
                    print("Operação Inexistente!")

        case 5:
            while(True):
                B.limparTela()
                B.mostrarDados()
                op = int(input("Pressione 1 para retornar ao Menu do Banco:\n"))
                if op == 1:
                    break
                    
        case 6:
            print("Encerrando o programa. Até mais!")
            break
        
        case _:
            B.limparTela()
            print("Operação Inexistente!")
