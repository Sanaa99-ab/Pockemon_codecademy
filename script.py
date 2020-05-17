class Pokemon:

  def __init__(self, name, p_type, max_health, health, expr, is_knocked_out=False, level=0):
    self.name = name #pockemon name 
    self.level = level #game level 
    self.p_type = p_type #fire or water
    self.max_health = max_health # 100%
    self.health = health #current health
    self.is_knocked_out = is_knocked_out #pk out
    self.expr = expr # experience

  def __repr__(self):
    return "infos: name: {}, type: {}, max_health: {}, current_health: {}, level: {}, experience: {}".format(self.name, self.p_type, self.max_health, self.health, self.level, self.expr)

  def lose_health(self, amount):
    self.health = self.health - amount
    return "{a} now has {b} health".format(a = self.name, b = self.health )

  def gain_health(self, gain):
    self.health == self.health + gain
    print(self.name, "has gain", gain)
    return self.health

  def knock_out(self):
    if self.health == 0:
      self.is_knocked_out = True
      print(self.name, "is knock out")
    return self.is_knocked_out

  def revive(self):
    if self.is_knocked_out == False:
      self.health = self.max_health
      print(self.name, "has been revived.")
    return self.health, self.is_knocked_out

   #my pokemon is attacking other pokemon what damage happen to the other ?
  def attack(self, other_pokemon):
    damage = 1
    if other_pokemon.is_knocked_out == True:#pokemon is knock out
      print(other_pokemon.name, "has alraedy knocked out")
      return
    #pokemon is not knock out   
    else:
# my pokemen is type water
      if self.p_type == "water":
        if other_pokemon.p_type == "fire":
          damage *= 2
        elif (other_pokemon.p_type == "grass") or ( other_pokemon.p_type == "water"):
          damage *= (1/2)
        return damage
#my pokemon is type fire 
      elif self.p_type == "fire":
        if other_pokemon.p_type == "grass":
          damage *= 2
        elif (other_pokemon.p_type == "water") or (other_pokemon.p_type == "fire"):
          damage *= (1/2)
        return damage
#my pokemon is type grass
      elif self.p_type == "grass":
        if other_pokemon.p_type == "water":
          damage *= 2
        elif (other_pokemon.p_type == "grass") or (other_pokemon.p_type == "fire"):
          damage *= (1/2)
        return damage
#how much the other pokemon is damaged    
    dmg = other_pokemon.lose_health(damage)    
    print(self.name, " attacked ", other_pokemon.name)
    print(other_pokemon.name, " has lost health now it has ", dmg)
  
  def experience(self, exp):
    self.expr += exp
    print(self.name, " has gained ", self.expr,"experience.")
    if self.expr >= 10:
      self.level_up()
  
  def level_up(self):
    self.expr = 0
    self.level += 1
    self.health = self.max_health
    print("Congrats!", self.name, "is now level up to level", self.level, "!!")

# a trainer class
class Trainer:
  def __init__(self, pokemons, potions, current_pokemon, name):
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon
    self.name = name

  def __repr__(self):
    return "infos: name :{a} ,his pokemons: {b}, with {c} potions. his current pokemon is {d}.".format(a = self.name, b = self.pokemons, c = self.potions, d = self.current_pokemon) 

  def use_potion(self):

    if self.potions > 0:
      if self.current_pokemon.health < self.current_pokemon.max_health:
        self.current_pokemon.gain_health(1)
        self.potions -= 1 
        print("your pokemon is now ", self.current_pokemon.health, " as health!")
      elif self.current_pokemon.health >= self.current_pokemon.max_health:
        print("your pokemon has already the maximum health!")
      return self.potions

    else:
     print("no potions left!!")

  def attack(self, other_trainer):
    their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
    self.current_pokemon.attack(their_pokemon)

  def switch(self, choosen_pk):
    #pokemon is in list of pokemons
    if choosen_pk in self.pokemons:
      if choosen_pk.is_knocked_out == True:
        print("this pokemon is already knock out")
      else:
        self.current_pokemon = choosen_pk
        print("you already switch pokemon into ",self.current_pokemon)

    #pokemon in not in list of pokemons    
    else:
      print("pokemon is not in your lists of pokemons")

class Chamander(Pokemon):
  def __init__(self, name, p_type, max_health, health, expr, is_knocked_out, level):
    super().__init(name, p_type, health, is_knocked_out, level)





#Test
pokemon_one = Pokemon("a", "fire", 100, 60, False, 0)
pokemon_two = Pokemon("b", "water", 100, 80, False, 1)
trainer_one = Trainer([pokemon_one,pokemon_two], 3, pokemon_one, "alex")   
