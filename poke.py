"""
Pokemon Game Project using Python with a focus on classes and OOP
"""

class Pokemon:
  def __init__(self, name, level, race ):
    self.name = name
    self.level = level
    #determine pokemon type
    self.race = race        
    self.max_hp = level*5
    self.cur_hp = level*5
    #check for alive or fiented
    self.is_feinted = False


  def lose_health(self, dmg_received):
      print(self.name + " lost " + str(dmg_received) + " health")

  def reg_health(self):
      print(self.name + " now has " + self.cur_hp + " health")

  def knockout(self):
      print(self.name + " has feinted")

  def revive(self):
      print(self.name + " has been revived")

  def attack(self, opponent):
    if (self.race == "water" and opponent.race == "fire") or (self.race == "fire" and opponent.race == "grass") or (self.race == "grass" and opponent.race == "water"):
      print(self.name + " is super effective!")
      #print attack message
      opponent.lose_health(opponent.level*2)
      #update health
      opponent.cur_hp -= opponent.level*2
      #Check if opponent health is less than 0
      if opponent.cur_hp <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_hp = 0
      
    elif (self.race == "water" and opponent.race == "grass") or (self.race == "fire" and opponent.race == "water") or (self.race == "grass" and opponent.race == "fire"):
      print(self.name + " is not effective!")
      #print attack message
      opponent.lose_health(opponent.level/2)
      #update health
      opponent.cur_hp -= opponent.level/2
      #Check if opponent health is less than 0
      if opponent.cur_hp <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_hp = 0
    else:
      #print attack message
      opponent.lose_health(opponent.level)
      #update health
      opponent.cur_hp -= opponent.level
      #Check if opponent health is less than 0
      if opponent.cur_hp <= 0:
        print(opponent.name + " has feinted!")
        opponent.is_feinted = True
        opponent.cur_hp = 0


class Trainer:
  def __init__(self, name):
    self.poke_lst = []
    self.name = name
    self.potions = 0
    self.cur_act_poke = 0

  def heal_active_poke(self):
    #check if pokemon is feinted
    if self.poke_lst[self.cur_act_poke].is_feinted == True:
      #update cur_hp value to full hp
      self.poke_lst[self.cur_act_poke].cur_hp = self.poke_lst[self.cur_act_poke].max_hp
      #let user know pokemon is no longer feinted
      self.poke_lst[self.cur_act_poke].revive()
      return
    #update cur_hp value to full hp
    self.poke_lst[self.cur_act_poke].cur_hp = self.poke_lst[self.cur_act_poke].max_hp
    print(self.poke_lst[self.cur_act_poke].name + " has been healed.")

  def fight(self, trainer_2):
    print(self.poke_lst[self.cur_act_poke].name + " has been challenged by " + trainer_2.poke_lst[trainer_2.cur_act_poke].name)
    #check if pokemon is feinted
    if (self.poke_lst[self.cur_act_poke].is_feinted == True) or (trainer_2.poke_lst[trainer_2.cur_act_poke].is_feinted == True):
      #prompt to switch pokemon
      if self.poke_lst[self.cur_act_poke].is_feinted == True:
        self.switch_poke()
      else:
        trainer_2.switch_poke()
    self.poke_lst[self.cur_act_poke].attack(trainer_2.poke_lst[trainer_2.cur_act_poke])

  def switch_poke(self):
    print("Please choose a new pokemon:")
    i = 0
    #print pokemon names that are not feinted
    while i < len(self.poke_lst):
      if self.poke_lst[i].is_feinted == False:
        print(str(i+1) + " --> " + self.poke_lst[i].name)
      i += 1
    choice = int(input())
    print(self.poke_lst[self.cur_act_poke].name + " has been swapped for " + self.poke_lst[choice-1].name)
    self.cur_act_poke = choice-1

    

###############################
        # Methods #
###############################

def choose_pokemon(trainer, poke_1, poke_2, poke_3):
  print("Hello " + trainer.name + " please choose your pokemon by entering the pokemon name: ")
  print("1. " + poke_1.name + "\n" + "2. " + poke_2.name + "\n" + "3. " + poke_3.name + "\n")
  starter_choice = input()
  print("\n\n")
  if starter_choice == poke_1.name:
    trainer.poke_lst.append(poke_1)
    return poke_3
  elif starter_choice == poke_2.name:
    trainer.poke_lst.append(poke_2)
    return poke_1
  elif starter_choice == poke_3.name:
    trainer.poke_lst.append(poke_3)
    return poke_2
  else:
    print("Invalid starter choice")
    choose_pokemon(trainer, poke_1, poke_2, poke_3)