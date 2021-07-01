from math import floor

from crucible.npc import NPC
from crucible.senses import Sense

if __name__ == '__main__':
    drow = NPC('Drow', size='medium', num_hit_dice=3,
               skill_prof=['perception', 'stealth'])
    drow.dexterity = 14
    drow.intelligence = 11
    drow.wisdom = 11
    drow.charisma = 12
    drow.add_sense(Sense('darkvision', '120 ft.'))

    hit_dice = int(6)
    num_hit_dice = 2
    hp = floor(num_hit_dice * sum(range(1, hit_dice+1)) / hit_dice)
    print(drow.hp)
    print(drow.skill_mod('stealth'))
    stat_block = drow.print_block()
    print(stat_block)
