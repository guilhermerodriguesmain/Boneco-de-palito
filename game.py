from campo import Map
from personagem import Person
import time
import random
import keyboard
debug = True
map = Map(30,90)

name = "deni"#str(input("insira o nome do seu personagem: "))

char ="ê"# input('Muito bem !!\nInsira um caracter para representar seu personagem: ')

# criando personagem do usuario

player = Person(name,char ,3)
x1, y1 = 15 , 5
name_position = 2,3
hp_position = 2,5

# criando personagem controlado pelo jogo
machine = Person('machine', 'ö',5)
x2, y2 = 15 , 45
machine_name_position = 2,86
machine_hp_position = 2,84

def machine_control():
    #necessita de melhoria no equilibrio de movimento
    machine_direction = random.choice(['i','j','k','l'])
    return machine_direction




while True:
    
    map.clear_map()
    
    
    # inserindo personagem de usuario
    map.update_cell(y1, x1, player.person)
    map.update_cell(name_position[0], name_position[0], player.nome) # informação estatica
    #map.update_cell(hp_position[0], hp_position[1], player.hp) # informação estatica
    
    # inserirndo personagem controlado pelo jogo
    map.update_cell(x2, y2, machine.person)
    map.update_cell(machine_name_position[0], machine_name_position[1], machine.nome)# informação estatica
    #map.update_cell(machine_hp_position[0], machine_hp_position[1], machine.hp)# informação estatica
    
    map.show_map()
    
    print(f'{name} para controlar use:\n(w/s/a/d): ')
     
    
    # controle personagem de usuario
    
    
    if keyboard.is_pressed("w") or keyboard.is_pressed("a") or keyboard.is_pressed("s") or keyboard.is_pressed("d"):
        tecla = None
        if keyboard.is_pressed("w"):
            tecla = "w"
        elif keyboard.is_pressed("a"):
            tecla = "a"
        elif keyboard.is_pressed("s"):
            tecla = "s"
        elif keyboard.is_pressed("d"):
            tecla = "d"
        
        if tecla:  # Se uma tecla válida foi pressionada
            x1, y1 = player.set_position(tecla.lower(), x1, y1)
            

    
    
      
    # controle personagem controlado pelo jogo   
    comand = machine_control()
    if comand in ('i', 'j', 'k', 'l'):
        comand_map = {"i": "w", "j": "a", "k": "s", "l": "d"}
        control_machine = comand_map.get(comand, "")
        if debug == True:
            x2, y2 = machine.set_position(control_machine, x2, y2)
        x2, y2 = machine.set_position(control_machine, x2, y2)
        
    
    
    # ataque e defesa
    distancia = abs(x1 - x2) + abs(y1 - y2)
    limite_colisao = 1  # Valor que você pode ajustar dependendo do seu jogo
    if distancia <= limite_colisao:
    
         # Jogador ataca a máquina
        if machine.attack_recive(player.attack(machine)) <= 0:
            map.clear_map()
            print(f"{player.nome} venceu a batalha!\n{'#'*5} VITÓRIA {'#'*5}")
            break

        # Máquina ataca o jogador
        if player.attack_recive(machine.attack(player)) <= 0:
            map.clear_map()
            print(f"{player.nome} foi derrotado!\n{'#'*5} GAME OVER {'#'*5}")
            break
    time.sleep(0.1)
"""
if len(player.hp) <=0 :
    map.clear_map()
    print(f"{player.nome} você perdeu !!\n{'#'*5} GAME OVER {'#'*5}")
    break
elif len(machine.hp) <= 0:
    map.clear_map()
    print(f"{player.nome} você venceu!!\n{'#'*5} VOCE GANHOU {'#'*5}")
    break

if len(machine.hp) <=0 and len(player.hp) > len(machine.hp):
    map.clear_map()
    print(f"{'#'*5} EMPATE {'#'*5}")
    break
"""
   
        
    
    