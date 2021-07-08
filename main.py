from math import floor

from crucible.npc import NPC
from crucible.senses import Sense
from crucible.ability import fey_ancestry, sunlight_sensitivity
from crucible.action import MeleeAttack, MeleeAttackBonusDamage, RangedAttack, RangedAttackBonusDamage

if __name__ == '__main__':
    drow = NPC('Drow', size='medium', num_hit_dice=3,
               skill_prof=['perception', 'stealth'])
    drow.dexterity = 14
    drow.intelligence = 11
    drow.wisdom = 11
    drow.charisma = 12
    drow.add_sense(Sense('darkvision', '120 ft.'))
    drow.add_ability(fey_ancestry, sunlight_sensitivity)
    shortsword = MeleeAttack('Shortsword', drow.stat_mod('dexterity'), drow.prof_bonus, 5, (1,6))
    poisoned_sword = MeleeAttackBonusDamage('Poisoned Shortsword', drow.stat_mod('dexterity'), drow.prof_bonus, 5,
                                            [(1, 6), (1, 8)], ['piercing', 'poison'])
    hand_crossbow = RangedAttack('Hand Crossbow', drow.stat_mod('dexterity'), drow.prof_bonus, (30, 120), (1, 6), 'piercing')
    hand_crossbow_poisoned = RangedAttackBonusDamage('Poisoned Hand Crossbow', drow.stat_mod('dexterity'),
                                                     drow.prof_bonus, (30, 120), [(1, 6), (1, 8)],
                                                     ['piercing', 'poison'])
    drow.add_action(shortsword, poisoned_sword, hand_crossbow, hand_crossbow_poisoned)


    hit_dice = int(6)
    num_hit_dice = 2
    hp = floor(num_hit_dice * sum(range(1, hit_dice+1)) / hit_dice)
    print(drow.hp)
    print(drow.skill_mod('stealth'))
    stat_block = drow.print_block()
    print(stat_block)
