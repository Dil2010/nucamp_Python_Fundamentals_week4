class Player:
    max_hp=4000

player1=Player()
print(player1.max_hp)

player2=Player()
print(player2.max_hp)

Player.max_hp=5000

print(player1.max_hp)
print(player2.max_hp)

class Player:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        self.score=0
        pass

player1=Player("Aron",1200)
player2=Player("Dason",1300)

print("Player1 Name:",player1.name,"Player1 hitpoints:",player1.hp,"Player score:",player1.score)
print("Player1 Name:",player2.name,"Player1 hitpoints:",player2.hp,"Player score:",player2.score)

player1.hp=player1.hp+500
player1.score=player1.score+10

print("Player1 Name:",player1.name,"Player1 hitpoints:",player1.hp,"Player score:",player1.score)
print("Player1 Name:",player2.name,"Player1 hitpoints:",player2.hp,"Player score:",player2.score)
