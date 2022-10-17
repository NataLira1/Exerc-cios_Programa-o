horario = input("Que horas são: ")

if horario.isnumeric():
    horario = int(horario)
    if horario > 0 and horario < 11:
        print("Bom dia!")
    elif horario > 12 and horario < 17:
        print("Boa Tarde!")
    else:
        print("Boa noite!")

else:
    print ("Horário inválido!")
