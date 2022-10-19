palavra_chave = 'goiaba'
digitados = []
repeticao = []
chances = len(palavra_chave) - 1
print('Bem Vindo! ao jogo de advinhação\n',
      'Você terá que advinhar uma palavra\n')
print('DICA: A palavra-chave possui {} letras'.format(len(palavra_chave)))
print('DICA: fruta')
print()

while True:

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print('\nIsso não vale, digite apenas uma letra!\n')
        continue
    elif letra.isalpha() == False:
        print('\nDigite APENAS letra, sem números, símbolos e espaços\n')
        continue

    digitados.append(letra)
    repeticao.append(letra)

    if letra == repeticao:
        print('Você já digitou esse valor, TENTE NOVAMENTE!')
        continue

    if letra in palavra_chave:
        print('Parabéns, você encontrou uma letra! ')
        chances -= 1
    else:
        print('Letra {} não existe na palavra'.format(letra))
        digitados.pop()
        chances -= 1

    palavraformada = ''
    palavra2 = palavra_chave.upper()

    for id in palavra_chave:
        if id in digitados:
            palavraformada = palavraformada + id
        else:
            palavraformada = palavraformada + '*'

    if palavraformada == palavra_chave:
        print('Você conseguiu concluir a palavra!')
        print('A palavra-chave era {}'.format(palavra2))
        break
    else:
        print('Sua palavra por enquanto está assim : {}'.format(palavraformada))
        print('E você ainda possui {} chances'.format(chances))
        print()


    if chances == 0:
        print('Suas chances acabaram, agora tente advinhar a palavra')
        print('Palavra: {}'.format(palavraformada))
        tentativa = input("Digite a sua tentativa: ")
        if tentativa == palavra_chave:
            print()
            print('Meus parabéns, você conseguiu concluir o jogo!')
            print('A palavra chave era {}'.format(palavra2))
            break
        else:
            print()
            print('Que pena, essa não era a palavra')
            print('A palavra chave era {}'.format(palavra2))
            break
