
class Person:
    
    def __init__(self, nome, forma, poder = 3, defesa = 2):
        self.nome = nome
        self.position = None
        self.person = self.Character(forma)
        self.hp = 10 #['#','#','#','#','#','#','#','#','#','#']
        self.poder = poder
        self.defesa_activate=False
        self.defesa = defesa
        
    
    def Character(self, head):
        self.head =str(head)
        self.character =[
            f" {self.head} ", # Cabeça
            "/|\\", # tronco + braços
            "/ \\" # pernas
        ]
        
        personagem_escudo = [
            "  o ",
            "(/|\\_",
            " / \\"
        ]
        return self.character
    def set_position(self, sense, x, y):
        
        if sense == "w":
            y -= 1
        elif sense == "s":
            y += 1
        elif sense == "a":
            x -= 1
        elif sense == "d":
            x += 1
        return x, y
    
    def attack(self, adversary):
        dano = max(0, self.poder - adversary.defesa)
        return  dano
    def attack_recive(self, dano):
        self.hp -= dano

        # Garante que o HP não seja menor que zero
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.nome} foi derrotado!")

        # Retorna o valor atualizado do HP
        return self.hp
        