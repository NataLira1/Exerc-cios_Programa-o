num = input("Digite um número: ")


if num.isnumeric():
    num = int(num)
    resto = num % 2
    if resto == 0:
        print('O número é par')
    else:
        print('O número é impar')
else:
    print('O número não é inteiro')