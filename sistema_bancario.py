import datetime

usuarios = []
contas = []

def criar_usuario():
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    if any(u['cpf'] == cpf for u in usuarios):
        print("CPF já cadastrado.")
        return
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    usuarios.append({"nome": nome, "cpf": cpf, "nascimento": nascimento})
    print(f"Usuário {nome} criado com sucesso.")

def criar_conta():
    cpf = input("CPF do titular: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("Usuário não encontrado.")
        return
    numero_conta = len(contas) + 1
    contas.append({
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": []
    })
    print(f"Conta nº {numero_conta} criada com sucesso.")

def acessar_conta():
    cpf = input("CPF: ")
    conta = next((c for c in contas if c['usuario']['cpf'] == cpf), None)
    if conta:
        menu_conta(conta)
    else:
        print("Conta não encontrada.")

def menu_conta(conta):
    while True:
        print("\nMenu da Conta")
        print("[1] Ver saldo")
        print("[2] Depositar")
        print("[3] Sacar")
        print("[4] Extrato")
        print("[5] Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        elif opcao == "2":
            valor = float(input("Valor para depósito: R$ "))
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"].append((datetime.datetime.now(), f"Depósito: +R$ {valor:.2f}"))
                print("Depósito realizado.")
            else:
                print("Valor inválido.")
        elif opcao == "3":
            valor = float(input("Valor para saque: R$ "))
            if valor > 0 and valor <= conta["saldo"]:
                conta["saldo"] -= valor
                conta["extrato"].append((datetime.datetime.now(), f"Saque: -R$ {valor:.2f}"))
                print("Saque realizado.")
            else:
                print("Saldo insuficiente ou valor inválido.")
        elif opcao == "4":
            print("\nExtrato:")
            for data, transacao in conta["extrato"]:
                print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {transacao}")
            print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        print("\nBem-vindo ao BancoPy")
        print("[1] Criar usuário")
        print("[2] Criar conta")
        print("[3] Acessar conta")
        print("[4] Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            criar_usuario()
        elif escolha == "2":
            criar_conta()
        elif escolha == "3":
            acessar_conta()
        elif escolha == "4":
            print("Encerrando sessão.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
