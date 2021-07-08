from crucible import Entity


class NPC(Entity):

    def __init__(self, name='NPC', size='medium', num_hit_dice=1, skill_prof=None):
        super().__init__(name, size, num_hit_dice, skill_prof)

    def print_block(self):

        # Setup some temporary variables
        str_part = "{} ({:+d})".format(self.strength, self.stat_mod('strength'))
        dex_part = "{} ({:+d})".format(self.dexterity, self.stat_mod('dexterity'))
        con_part = "{} ({:+d})".format(self.constitution, self.stat_mod('constitution'))
        int_part = "{} ({:+d})".format(self.intelligence, self.stat_mod('intelligence'))
        wis_part = "{} ({:+d})".format(self.wisdom, self.stat_mod('wisdom'))
        cha_part = "{} ({:+d})".format(self.charisma, self.stat_mod('charisma'))

        # Stat block header
        stat_block_str =  "______________________________________________________________\n"
        stat_block_str += "|  \033[1m{}\n\033[0m".format(self.name)
        stat_block_str += "|  {} <type>, any alignment\n".format(self.size.capitalize())
        stat_block_str += "|----------\n"
        stat_block_str += "|  \033[1mArmor Class\033[0m {}\n".format(self.ac)
        if self.stat_mod('constitution') != 0:
            stat_block_str += "|  \033[1mHit Points\033[0m {} ({}d{}{:+d})\n".format(self.hp, self.num_hit_dice,
                                                                                self.hit_dice, self.stat_mod('constitution'))
        else:
            stat_block_str += "|  \033[1mHit Points\033[0m {} ({}d{})\n".format(self.hp, self.num_hit_dice,
                                                                                self.hit_dice)
        stat_block_str += "|  \033[1mSpeed\033[0m {} ft.\n".format(self.speed)

        # Statitistics block
        stat_block_str += "|----------\n"
        stat_block_str += "|    \033[1mSTR       DEX       CON       INT       WIS       CHA\033[0m\n"
        stat_block_str += "|  {}  {}  {}  {}  {}  {}\n".format(str_part.center(8), dex_part.center(8),
                                                               con_part.center(8), int_part.center(8),
                                                               wis_part.center(8), cha_part.center(8))
        stat_block_str += "|----------\n"

        # Skills and characteristics
        if self.skill_prof:
            stat_block_str += "|  \033[1mSkills\033[0m "
            for i, skill in enumerate(self.skill_prof):
                stat_block_str += "{} {:+d}".format(skill.capitalize(), self.skill_mod(skill))
                if i < len(self.skill_prof)-1:
                    stat_block_str += ", "
                else:
                    stat_block_str += "\n"

        stat_block_str += "|  \033[1mSenses\033[0m "
        for i, i_sense in enumerate(self.senses):
            stat_block_str += "{}".format(str(i_sense))
            if i < len(self.senses)-1:
                stat_block_str += ", "
            else:
                stat_block_str += "\n"

        stat_block_str += "|  \033[1mLanguages\033[0m \n"
        stat_block_str += "|  \033[1mChallenge\033[0m \n"

        # Add abilities, if any
        ability_str_length = 62
        if len(self.abilities) > 0:
            stat_block_str += "|----------\n"
            for i, i_ability in enumerate(self.abilities):
                ability_str = i_ability.print_ability_string()
                ability_str_split = ability_str.split()
                print_piece = "| "
                for piece in ability_str_split:
                    if len(print_piece) + len(piece) + 1 <= 62:
                        print_piece += " {}".format(piece)
                    else:
                        stat_block_str += "{}\n".format(print_piece)
                        print_piece = "|  {}".format(piece)
                if len(print_piece) > 3:
                    stat_block_str += "{}".format(print_piece)
                if i < len(self.abilities)-1:
                    stat_block_str += "\n|  \n"
                else:
                    stat_block_str += "\n"

        # Add Actions
        stat_block_str += "|----------\n"
        stat_block_str += "|  \033[1mActions\033[0m\n"
        for i, i_action in enumerate(self.actions):
            action_str = i_action.print_action_str()
            action_str_split = action_str.split()
            print_piece = "| "
            for piece in action_str_split:
                if len(print_piece) + len(piece) + 1 <= 62:
                    print_piece += " {}".format(piece)
                else:
                    stat_block_str += "{}\n".format(print_piece)
                    print_piece = "|  {}".format(piece)
            if len(print_piece) > 3:
                stat_block_str += "{}".format(print_piece)
            if i < len(self.actions) - 1:
                stat_block_str += "\n|  \n"
            else:
                stat_block_str += "\n"
        stat_block_str += "|_____________________________________________________________\n"
        return stat_block_str
