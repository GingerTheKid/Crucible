from abc import ABC, abstractmethod
from math import floor


class Action(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def print_action_str(self):
        raise NotImplementedError


class MeleeAttack(Action):
    """
    Basic melee attack with single type of damage (i.e. most melee weapons)
    """

    def __init__(self, name, stat_mod=0, prof_mod=0, reach=5, hit=(1, 6), dmg_type='piercing'):
        self.name = name
        self.mod = stat_mod
        self.prof = prof_mod
        self.reach = reach
        self.hit = hit
        self.avg_dmg = floor(self.hit[0] * sum(range(1, self.hit[1] + 1)) / self.hit[1]) + self.mod
        self.type = dmg_type

    def print_action_str(self):
        act_str = "{}. ".format(self.name)
        act_str += "Melee Weapon Attack: "
        act_str += "{:+d} to hit, ".format(self.mod + self.prof)
        act_str += "reach {:d} ft., one target.".format(self.reach)
        act_str += " Hit: {:d} ({:d}d{:d}{:+d}) {} damage.".format(self.avg_dmg, self.hit[0], self.hit[1], self.mod,
                                                                   self.type)
        return act_str


class MeleeAttackBonusDamage(Action):
    """
    Melee attack that inflicts multiple types of damage on a single hit (e.g. poisoned weapons)
    """

    def __init__(self, name, stat_mod=0, prof_mod=0, reach=5, hit=[(1, 6)], dmg_type=['piercing']):
        self.name = name
        self.mod = stat_mod
        self.prof = prof_mod
        self.reach = reach
        self.hit = hit
        self.avg_dmg = [floor(x[0] * sum(range(1, x[1] + 1)) / x[1]) for x in self.hit]
        self.avg_dmg[0] += self.mod
        self.type = dmg_type

    def print_action_str(self):
        act_str = "{}. ".format(self.name)
        act_str += "Melee Weapon Attack: "
        act_str += "{:+d} to hit, ".format(self.mod + self.prof)
        act_str += "reach {:d} ft., one target.".format(self.reach)
        for i, i_hit in enumerate(self.hit):
            if i == 0:
                act_str += " Hit: {:d} ({:d}d{:d}{:+d}) {} damage".format(self.avg_dmg[i], i_hit[0], i_hit[1], self.mod,
                                                                          self.type[i])
            else:
                act_str += " plus {:d} ({:d}d{:d}) {} damage.".format(self.avg_dmg[i], i_hit[0], i_hit[1], self.type[i])
        return act_str


class MeleeAttackTwoModes(Action):
    pass


class RangedAttack(Action):
    """
    Basic ranged attack with single type of damage (i.e. most ranged weapons)
    """

    def __init__(self, name, stat_mod=0, prof_mod=0, reach=(50, 100), hit=(1, 6), dmg_type='piercing'):
        self.name = name
        self.mod = stat_mod
        self.prof = prof_mod
        self.reach = reach
        self.hit = hit
        self.avg_dmg = floor(self.hit[0] * sum(range(1, self.hit[1] + 1)) / self.hit[1]) + self.mod
        self.type = dmg_type

    def print_action_str(self):
        act_str = "{}. ".format(self.name)
        act_str += "Ranged Weapon Attack: "
        act_str += "{:+d} to hit, ".format(self.mod + self.prof)
        act_str += "range {:d}/{:d} ft., one target.".format(self.reach[0], self.reach[1])
        act_str += " Hit: {:d} ({:d}d{:d}{:+d}) {} damage.".format(self.avg_dmg, self.hit[0], self.hit[1], self.mod,
                                                                   self.type)
        return act_str

class RangedAttackBonusDamage(Action):
    """
    Ranged attack that inflicts multiple types of damage on a single hit (e.g. poisoned weapons)
    """

    def __init__(self, name, stat_mod=0, prof_mod=0, reach=(50, 100), hit=[(1, 6)], dmg_type=['piercing']):
        self.name = name
        self.mod = stat_mod
        self.prof = prof_mod
        self.reach = reach
        self.hit = hit
        self.avg_dmg = [floor(x[0] * sum(range(1, x[1] + 1)) / x[1]) for x in self.hit]
        self.avg_dmg[0] += self.mod
        self.type = dmg_type

    def print_action_str(self):
        act_str = "{}. ".format(self.name)
        act_str += "Melee Weapon Attack: "
        act_str += "{:+d} to hit, ".format(self.mod + self.prof)
        act_str += "range {:d}/{:d} ft., one target.".format(self.reach[0], self.reach[1])
        for i, i_hit in enumerate(self.hit):
            if i == 0:
                act_str += " Hit: {:d} ({:d}d{:d}{:+d}) {} damage".format(self.avg_dmg[i], i_hit[0], i_hit[1], self.mod,
                                                                          self.type[i])
            else:
                act_str += " plus {:d} ({:d}d{:d}) {} damage.".format(self.avg_dmg[i], i_hit[0], i_hit[1], self.type[i])
        return act_str