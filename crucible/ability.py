class Ability:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def print_ability_string(self, short=False):
        # ability_str = "\033[1m{}\033[0m".format(self.title)
        ability_str = "{}.".format(self.title)
        if not short:
            ability_str += " {}".format(self.description)
        return ability_str


# Library of Abilities - will move to something else one day
fey_ancestry = Ability("Fey Ancestry", "The creature has advantage on saving throws against being charmed, "
                                       "and magic can't put the creature to sleep.")
sunlight_sensitivity = Ability("Sunlight Sensitivity", "While in sunlight, the creature has disadvantage on attack "
                                                       "rolls, as well as on Wisdom (Perception) checks that rely on"
                                                       " sight.")