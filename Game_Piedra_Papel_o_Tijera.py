import random

""" Realiza un programa que simule el juego de piedra, papel o tijera. Una partida de 2 de 3 rondas. """

def Elegir_Validar_Opciones():
    options = ("piedra", "papel", "tijera")
    while True:
        user_option = input("Elije: Piedra, Papel o Tijera: ").lower()
        if not user_option in options:
            continue
        else:
            pc_option = random.choice(options)
            break
    return user_option, pc_option

def Eligir_Ganador_De_Ronda(user_option, pc_option):
    if user_option == pc_option:
        print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> EMPATE  ")
        return 0, 0
    elif user_option == "piedra":
        if pc_option == "papel":
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> PC GANA")
            return 0, 1
        else:
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> GANASTE")
            return 1, 0
    elif user_option == "papel":
        if pc_option == "piedra":
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> GANASTE")
            return 1, 0
        else:
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> PC GANA")
            return 0, 1
    elif user_option == "tijera":
        if pc_option == "piedra":
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> PC GANA")
            return 0, 1
        else:
            print(f"Elegiste: {user_option.capitalize()}, PC eligio: {pc_option.capitalize()} -> GANASTE")
            return 1, 0

def Elegir_Ganador_Juego(primero_que_gane_n = 2):
    número_de_ronda = 1
    your_number_wins = 0
    pc_number_wins = 0

    while your_number_wins < primero_que_gane_n and pc_number_wins < primero_que_gane_n:
        print()
        print("RONDA", número_de_ronda)
        user_option, pc_option = Elegir_Validar_Opciones()
        your_number_wins_aux, pc_number_wins_aux = Eligir_Ganador_De_Ronda(user_option, pc_option)
        your_number_wins += your_number_wins_aux
        pc_number_wins += pc_number_wins_aux
        número_de_ronda += 1
    
    return your_number_wins, pc_number_wins
    

def Juego_Piedra_Papel_Tijera():
    print("-" * 26)
    print("| PIEDRA, PAPEL o TIJERA |")
    print("-" * 26)

    user_number_wins, pc_number_wins = Elegir_Ganador_Juego()

    print()
    if user_number_wins > pc_number_wins:
        print('*' * 22)
        print('* EL GANADOR ES USER *')
        print('*' * 22)
    else:
        print('*' * 32)
        print('* EL GANADOR ES PC MASTER RACE *')
        print('*' * 32)

if __name__ == "__main__":
    Juego_Piedra_Papel_Tijera()