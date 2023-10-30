import time
import pyotp
import qrcode
#Chave para funcionamento da autenticação
chave_mestre = "RBJE6YE7O2N5HMTWXLI75NHG4Y6RWILE"
codigo = pyotp.TOTP(chave_mestre)

# Dicionário para armazenar os dados de login
bancodelogins = {
    'usuario': '123'
}

def login():
    username = input("Digite o seu nome de usuário: ")
    password = input("Digite a sua senha: ")

    if username in bancodelogins and bancodelogins[username] == password:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorreta. Tente novamente.")

# Teste do sistema de login
login()


#Autenticação
codigo_usuario = input("Código: ")
print(codigo.verify(codigo_usuario))

#Menu de opções do banco    
def menu():
    #Dicionário para os créditos de carbono
    creditos = {
    'Energia Eólica': 0,
    'Painéis Solares': 0,
    'Combustíveis Renováveis': 0,
    'Reflorestamento': 0,
    'Redução de Emissões': 0
}
    print("Selecione uma opção:")
    print("1. Depositar créditos de carbono na sua conta")
    print("2. Retirar créditos de carbono de sua conta")
    print("3. Calcular o valor de seus créditos de carbono")
    print("4. Verificar seus créditos")
    print("5. Sair")

    while True:
        choice = (input("Escolha uma opção: "))

        if choice == "1":
            print("Você selecionou a opção 1: Depositar créditos de carbono a sua conta")
            voltar = False
            def menudeposita():
                print("Fontes de crédito de carbono:")
                print("1. Energia Eólica")
                print("2. Painéis Solares")
                print("3. Combustíveis Renováveis")
                print("4. Reflorestamento")
                print("5. Redução de Emissões")
                print("6. Sair")

                while True:
                    choice = (input("Escolha em qual tipo de fonte deseja depositar esse crédito: "))
                    
                    if choice == "1":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser depositada para Energia Eólica: "))
                        creditos['Energia Eólica'] += quantidade
                        print(f"{quantidade} créditos de carbono adicionados para Energia Eólica.")
                        print(creditos)

                    elif choice == "2":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser depositada para Painéis Solares: "))
                        creditos['Painéis Solares'] += quantidade
                        print(f"{quantidade} créditos de carbono adicionados para Painéis Solares.")
                        print(creditos)

                    elif choice == "3":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser depositada para Combustíveis Renováveis: "))
                        creditos['Combustíveis Renováveis'] += quantidade
                        print(f"{quantidade} créditos de carbono adicionados para Combustíveis Renováveis.")
                        print(creditos)

                    elif choice == "4":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser depositada para Reflorestamento: "))
                        creditos['Reflorestamento'] += quantidade
                        print(f"{quantidade} créditos de carbono adicionados para Reflorestamento.")
                        print(creditos)    
                    
                    elif choice == "5":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser depositada para Redução de Emissões: "))
                        creditos['Redução de Emissões'] += quantidade
                        print(f"{quantidade} créditos de carbono adicionados para Redução de Emissões.")
                        print(creditos)
                    
                    elif choice == "6":
                        return voltar

                    else:
                        print("Opção inválida. Tente novamente.")                               

            if __name__ == "__main__":
                menudeposita()
            print(menudeposita)
                

        elif choice == "2":
            print("Você selecionou a opção 2: Retirar créditos de carbono da sua conta")
            voltar = False
            def menuretira():
                print("Fontes de crédito de carbono:")
                print("1. Energia Eólica")
                print("2. Painéis Solares")
                print("3. Combustíveis Renováveis")
                print("4. Reflorestamento")
                print("5. Redução de emissões")
                print("6. Sair")

                while True:
                    choice = input("Escolha de qual tipo de fonte deseja retirar esse crédito:")

                    if choice == "1":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser retirada de Energia Eólica: "))
                        creditos['Energia Eólica'] -= quantidade
                        print(f"{quantidade} créditos de carbono retirados de Energia Eólica.")
                        print(creditos)

                    elif choice == "2":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser retirada de Painéis Solares: "))
                        creditos['Painéis Solares'] -= quantidade
                        print(f"{quantidade} créditos de carbono retirados de Painéis Solares.")
                        print(creditos)

                    elif choice == "3":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser retirada de Combustíveis Renováveis: "))
                        creditos['Combustíveis Renováveis'] -= quantidade
                        print(f"{quantidade} créditos de carbono retirados de Combustíveis Renováveis.")
                        print(creditos)

                    elif choice == "4":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser retirada de Reflorestamento: "))
                        creditos['Reflorestamento'] -= quantidade
                        print(f"{quantidade} créditos de carbono retirados de Reflorestamento.")
                        print(creditos)    
                    
                    elif choice == "5":
                        quantidade = int(input("Digite a quantidade de créditos de carbono a ser retirada de Redução de Emissões: "))
                        creditos['Redução de Emissões'] -= quantidade
                        print(f"{quantidade} créditos de carbono retirados de Redução de Emissões.")
                        print(creditos)
                    
                    elif choice == "6":
                        return voltar
                    
                    else:
                        print("Opção inválida. Tente novamente.")

            if __name__ == "__main__":
                menuretira()
            print(menuretira)

        elif choice == "3":
            print("Você selecionou a opção 3. Calcular o valor de seus créditos de carbono")
            for forma, qtd in creditos.items():
                print(forma, qtd * 25, "Reais")
                total = sum(25 * valor for valor in creditos.values())
                print(f"O valor total dos seus créditos de carbono é {total} Reais.")
        
        elif choice == "4":
            print("Você selecionou a opção 4. Verificar seus créditos")
            print(creditos)

        elif choice == "5":
            print("Saindo do aplicativo, obrigado por utilizar nossos serviços")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

print(menu)