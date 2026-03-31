print(f"Bem vindo ao Banco Senac.")

idade = input("Informe sua idade ")
salario = input("Informe seu salário ")
tempo_de_trabalho = input("Informe tempo de trabalho (em anos) ")

if idade > "18" and salario >= "2000" and tempo_de_trabalho >= "2":
    print (f"Empréstimo aprovado")
else:
    print (f"Empréstimo negado")

valor_emprestimo = input("Qual o valor do empréstimo desejado?")
