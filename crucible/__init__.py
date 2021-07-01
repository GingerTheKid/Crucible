from math import floor
from abc import ABC, abstractmethod
from crucible.senses import Sense

class Entity(ABC):
    def __init__(self, name='Entity', size='medium', num_hit_dice=1, skill_prof=None):
        self.name = name

        self.size = size
        self.num_hit_dice = num_hit_dice

        self._speed = 30

        self._stats = [10, 10, 10, 10, 10, 10]
        self.skills = dict()
        self.add_skills()

        self.prof_bonus = int(2)

        self.skill_prof = skill_prof
        if self.skill_prof is not None:
            for skill in self.skill_prof:
                base_skill = self.skills[skill]
                self.skills[skill] = (base_skill[0], True)

        self.passive_perception = 10 + self.skill_mod('perception')
        self.senses = [Sense("passive Perception", "{:d}".format(self.passive_perception))]
        self._actions = []

    @property
    def strength(self):
        return self._stats[0]

    @strength.setter
    def strength(self, new_val):
        self._stats[0] = new_val

    @property
    def dexterity(self):
        return self._stats[1]

    @dexterity.setter
    def dexterity(self, new_val):
        self._stats[1] = new_val

    @property
    def constitution(self):
        return self._stats[2]

    @constitution.setter
    def constitution(self, new_val):
        self._stats[2] = new_val

    @property
    def intelligence(self):
        return self._stats[3]

    @intelligence.setter
    def intelligence(self, new_val):
        self._stats[3] = new_val

    @property
    def wisdom(self):
        return self._stats[4]

    @wisdom.setter
    def wisdom(self, new_val):
        self._stats[4] = new_val

    @property
    def charisma(self):
        return self._stats[5]

    @charisma.setter
    def charisma(self, new_val):
        self._stats[5] = new_val

    @property
    def hit_dice(self):
        if self.size == 'tiny':
            return int(4)
        elif self.size == 'small':
            return int(6)
        elif self.size == 'medium':
            return int(8)
        elif self.size == 'large':
            return int(10)
        elif self.size == 'huge':
            return int(12)
        elif self.size == 'gargantuan':
            return int(20)
        else:
            return int(8)

    @property
    def hp(self):
        return floor(self.num_hit_dice * sum(range(1, self.hit_dice + 1)) / self.hit_dice) \
               + self.num_hit_dice * self.stat_mod('constitution')

    @property
    def ac(self):
        return self.stat_mod('dexterity') + 10

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_val):
        self._speed = new_val

    def add_skills(self):
        self.skills['acrobatics'] = ('dexterity', False)
        self.skills['animal_handling'] = ('wisdom', False)
        self.skills['arcana'] = ('intelligence', False)
        self.skills['athletics'] = ('strength', False)
        self.skills['deception'] = ('charisma', False)
        self.skills['history'] = ('intelligence', False)
        self.skills['insight'] = ('wisdom', False)
        self.skills['investigation'] = ('intelligence', False)
        self.skills['medicine'] = ('wisdom', False)
        self.skills['nature'] = ('intelligence', False)
        self.skills['perception'] = ('wisdom', False)
        self.skills['performance'] = ('charisma', False)
        self.skills['persuasion'] = ('charisma', False)
        self.skills['religon'] = ('intelligence', False)
        self.skills['sleight_of_hand'] = ('dexterity', False)
        self.skills['stealth'] = ('dexterity', False)
        self.skills['survival'] = ('wisdom', False)

    def stat_mod(self, stat_name):
        stat_val = self.__getattribute__(stat_name)
        return floor((stat_val - 10) / 2)

    def skill_mod(self, skill_name):
        this_skill = self.skills[skill_name]
        return self.stat_mod(this_skill[0]) + this_skill[1] * self.prof_bonus

    def add_sense(self, new_sense):
        self.senses.insert(-1, new_sense)

    @abstractmethod
    def print_block(self):
        raise NotImplementedError
