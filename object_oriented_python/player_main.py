class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
        
=========================================================================================================

from player import Player

tim = Player("Tim")

from enemy import Enemy, Troll, Vampire
#
# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(10)
# print(random_monster)

beautiful_troll = Troll("Pug")
print("Beautfiful Troll - {}".format(beautiful_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

beautiful_troll.grunt()
another_troll.grunt()
brother.grunt()

dracula = Vampire("Dracula")
# print(dracula)
# dracula.take_damage(5)
# print(dracula)
# dracula.take_damage(6)
# print(dracula)
# dracula.reincarnate()

while dracula.alive:
    dracula.take_damage(1)
    print(dracula)

dracula.reincarnate()

==========================================================================================================================


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False


    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=10)

    def reincarnate(self):
        one_death = False
        while one_death == False:
            if self.lives == 0:
                self.lives = 1
                self.hit_points = 10
                print("I, {0.name} am a vampire and have come back to life! Lives: {0.lives}, HP: {0.hit_points}".format(self))
                one_death = True

    def take_damage(self, damage):
        if not self.reincarnate():
            super().take_damage(damage=damage)
            
class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 140

    def take_damage(self, damage):
        remaining_points = self.hit_points - (damage / 4.0)
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("You dealt {} points damage but I took {} points of damage and have {} left".format(damage, (damage / 4.0), self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False
