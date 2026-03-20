# Estrutura de repetição
# if (se) -> Verifica se uma condição é (verdadeira). Se for, ele executa o código.
#elif (senão se) -> É usado para testar várias condições. Ele só executada se todas as condições anteriores forem falsas.
# else (senão) -> Executa o código se a condição if for false (falsa).

# idade_usuario = 16
# #se o usuário for maior de 18 anos, eu vou passar a informação: Você é maior de idade;
# if idade_usuario >= 18:
#     print("Você é maior de idade.")
# else:
#      print("Vaza daqui mermão.")

idade = 73
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 0 and idade < 18:
    print("Vaza daqui mermão.")
elif idade >=70:
    print("Vai dormir vovô.")
else:
    print("Vaza daqui mermão.")