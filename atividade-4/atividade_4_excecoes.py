# Atividade 4 - Tratamento de Exceções
# Linguagens de Programação I

def divisao_segura():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 / numero2

    except ValueError:
        print("Erro: digite apenas números.")

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")

    else:
        print("Resultado:", resultado)

    finally:
        print("Operação finalizada.")


def saque_bancario():
    try:
        saldo = float(input("Informe o saldo da conta: "))
        saque = float(input("Informe o valor do saque: "))

        if saque <= 0:
            raise Exception("O valor do saque deve ser maior que zero.")

        if saque > saldo:
            raise Exception("Saldo insuficiente.")

    except ValueError:
        print("Erro: digite valores válidos.")

    except Exception as erro:
        print("Erro:", erro)

    else:
        saldo = saldo - saque
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: R$ {saldo:.2f}")

    finally:
        print("Operação bancária finalizada.")


print("1 - Divisão segura")
print("2 - Sistema de saque bancário")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    divisao_segura()
elif opcao == "2":
    saque_bancario()
else:
    print("Opção inválida.")
