import time
import pyotp
import qrcode

#Chave para funcionamento da autenticação
chave_mestre = "RBJE6YE7O2N5HMTWXLI75NHG4Y6RWILE"
codigo = pyotp.TOTP(chave_mestre)

link = pyotp.TOTP(chave_mestre).provisioning_uri(name="Usuário", issuer_name="BanCO²")

qrcodeacesso = qrcode.make(link)
qrcodeacesso.save("autenticacao.png")

# Dicionário para armazenar os dados de login
bancodelogins = {
    'usuario': '123'
}

def login():
    while True:
        username = input("\nDigite o seu nome de usuário: ")
        password = input("Digite a sua senha: ")

        codigo_usuario = (input("Código: "))
        testecodigo = (codigo.verify(codigo_usuario))

        if username in bancodelogins and bancodelogins[username] == password and testecodigo == True:
            print("Login bem-sucedido!")
            return True
        else:
            print("Nome de usuário/senha incorreta ou código invalido. Tente novamente.")

# Teste do sistema de login
while not login():
#Menu de opções do banco    
    voltar = True
def menu():
    #Dicionário para os créditos de carbono
    creditos = {
    'Energia Eólica': 0,
    'Painéis Solares': 0,
    'Combustíveis Renováveis': 0,
    'Reflorestamento': 0,
    'Redução de Emissões': 0
}
    
    while True:
        print("\n\nSelecione uma opção:")
        print("1. Depositar créditos de carbono na sua conta")
        print("2. Retirar créditos de carbono de sua conta")
        print("3. Calcular o valor de seus créditos de carbono")
        print("4. Verificar seus créditos")
        print("5. Calcular quanto carbono gera com seus dispositivos por mês")
        print("6. Sair")
        choice = (input("Escolha uma opção: "))

        if choice == "1":
            print("\n\nVocê selecionou a opção 1: Depositar créditos de carbono a sua conta")
            voltar = False
            def menudeposita():

                while True:
                    print("\nFontes de crédito de carbono:")
                    print("1. Energia Eólica")
                    print("2. Painéis Solares")
                    print("3. Combustíveis Renováveis")
                    print("4. Reflorestamento")
                    print("5. Redução de Emissões")
                    print("6. Sair")
                    choice = (input("\n\nEscolha em qual tipo de fonte deseja depositar esse crédito: "))
                    
                    if choice == "1":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser depositada para Energia Eólica: "))
                        if (creditos['Energia Eólica'] + quantidade) <0:
                            print("Não é possível depositar essa quantidade")
                        else:    
                            creditos['Energia Eólica'] += quantidade
                            print(f"{quantidade} créditos de carbono adicionados para Energia Eólica.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")
                            
                    elif choice == "2":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser depositada para Painéis Solares: "))
                        if (creditos['Painéis Solares'] + quantidade) <0:
                            print("Não é possível depositar essa quantidade")
                        else:
                            creditos['Painéis Solares'] += quantidade
                            print(f"{quantidade} créditos de carbono adicionados para Painéis Solares.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")

                    elif choice == "3":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser depositada para Combustíveis Renováveis: "))
                        if (creditos['Combustíveis Renováveis'] + quantidade) <0:
                            print("Não é possível depositar essa quantidade")
                        else:
                            creditos['Combustíveis Renováveis'] += quantidade
                            print(f"{quantidade} créditos de carbono adicionados para Combustíveis Renováveis.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")

                    elif choice == "4":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser depositada para Reflorestamento: "))
                        if (creditos['Reflorestamento'] + quantidade) <0:
                            print("Não é possível depositar essa quantidade")
                        else:
                            creditos['Reflorestamento'] += quantidade
                            print(f"{quantidade} créditos de carbono adicionados para Reflorestamento.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")    
                    
                    elif choice == "5":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser depositada para Redução de Emissões: "))
                        if (creditos['Redução de Emissões'] + quantidade) <0:
                            print("Não é possível depositar essa quantidade")
                        else:
                            creditos['Redução de Emissões'] += quantidade
                            print(f"{quantidade} créditos de carbono adicionados para Redução de Emissões.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")
                    
                    elif choice == "6":
                        return voltar
                        

                    else:
                        print("Opção inválida. Tente novamente.")                               

            if __name__ == "__main__":
                menudeposita()
                

        elif choice == "2":
            print("\n\nVocê selecionou a opção 2: Retirar créditos de carbono da sua conta")
            voltar = False
            def menuretira():

                while True:
                    print("\nFontes de crédito de carbono:")
                    print("1. Energia Eólica")
                    print("2. Painéis Solares")
                    print("3. Combustíveis Renováveis")
                    print("4. Reflorestamento")
                    print("5. Redução de emissões")
                    print("6. Sair")
                    choice = input("Escolha de qual tipo de fonte deseja retirar esse crédito:")

                    if choice == "1":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser retirada de Energia Eólica: "))
                        if (creditos['Energia Eólica'] - quantidade) <0:
                            print("Não é possível retirar essa quantidade")
                        else:          
                            creditos['Energia Eólica'] -= quantidade
                            print(f"{quantidade} créditos de carbono retirados de Energia Eólica.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")

                    elif choice == "2":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser retirada de Painéis Solares: "))
                        if (creditos['Painéis Solares'] - quantidade) <0:
                            print("Não é possível retirar essa quantidade")
                        else:    
                            creditos['Painéis Solares'] -= quantidade
                            print(f"{quantidade} créditos de carbono retirados de Painéis Solares.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")

                    elif choice == "3":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser retirada de Combustíveis Renováveis: "))
                        if (creditos['Combustíveis Renováveis'] - quantidade) <0:
                            print("Não é possível retirar essa quantidade")
                        else:
                            creditos['Combustíveis Renováveis'] -= quantidade
                            print(f"{quantidade} créditos de carbono retirados de Combustíveis Renováveis.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")

                    elif choice == "4":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser retirada de Reflorestamento: "))
                        if (creditos['Reflorestamento'] - quantidade) <0:
                            print("Não é possível retirar essa quantidade")
                        else:    
                            creditos['Reflorestamento'] -= quantidade
                            print(f"{quantidade} créditos de carbono retirados de Reflorestamento.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")   
                    
                    elif choice == "5":
                        quantidade = int(input("\nDigite a quantidade de créditos de carbono a ser retirada de Redução de Emissões: "))
                        if (creditos['Redução de Emissões'] - quantidade) <0:
                            print("Não é possível retirar essa quantidade")
                        else:
                            creditos['Redução de Emissões'] -= quantidade
                            print(f"{quantidade} créditos de carbono retirados de Redução de Emissões.")
                            for forma, qtd in creditos.items():
                                print(f"{forma}: {qtd}")
                    
                    elif choice == "6":
                        return voltar
                    
                    else:
                        print("\nOpção inválida. Tente novamente.")

            if __name__ == "__main__":
                menuretira()

        elif choice == "3":
            print("\nVocê selecionou a opção 3. Calcular o valor de seus créditos de carbono")
            for forma, qtd in creditos.items():
                a = (creditos['Energia Eólica'] * 25)
                b = (creditos['Painéis Solares'] * 25)
                c = (creditos['Combustíveis Renováveis'] * 25)
                d = (creditos['Reflorestamento'] * 25)
                e = (creditos['Redução de Emissões'] * 25)
                print('Energia Eólica:', a , "Reais")
                print('Painéis Solares:', a , "Reais")
                print('Combustíveis Renováveis:', a , "Reais")
                print('Reflorestamento:', a , "Reais")
                print('Redução de Emissões:', a , "Reais")
                break
                
        
        elif choice == "4":
            print("\nVocê selecionou a opção 4. Verificar seus créditos")
            for forma, qtd in creditos.items():
                print(f"{forma}: {qtd}")

        elif choice == "5":
            print("\nPara calcularmos o quanto gastou de carbono, necessitamos que passe as seguintes informações:")
            tel = int(input("Insira o número de telefones que usa nosso autenticador:"))
            cargatel = int(input("Quantas vezes recarrega o celular no dia?:"))
            mesestel = cargatel * 31
            gastotel = mesestel * 0.015
            pc = int(input("Insira em quantos computadores utiliza nosso sistema:"))
            horaspc = int(input("Insira quantas horas por dia utiliza o computador (Caso seja mais de um, adicione o valor somado dos dois)"))
            diaspc = int(input("Insira quantos dias por mês utiliza o computador (Caso seja mais de um, adicione o valor somado dos dois)"))
            gastopc = (400 * horaspc * diaspc) / 1000
            gastoCO = ((gastopc + gastotel) * 81.7 ) /1000
            print(f"Você utiliza nossos serviços em {tel + pc} dispositivos.\nCalculamos o gasto de carbono utilizando a energia utilizada por seus dispositivos mensalmente, e após isso convertemos para quilos de carbono jogados na atmosfera, os cálculos utilizados estão na documentação do sistema:" )            
            print(f"O gasto do(s) computadores é de {gastopc}kWh por mês")
            print(f"O gasto total de carbono dos seus dispositivos é de {gastoCO:.2f}kg por mês")
        elif choice == "6":
            print("\nSaindo do programa, obrigado por utilizar nossos serviços")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

