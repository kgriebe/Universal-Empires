#!/usr/bin/python

# Basic Ship Class

class ship:
    def __init__(self):
        # What is the name of the ship
        self.name = ""
        # How much Exp does this ship have
        self.exp = ""
        # What level is the ship
        self.level = ""
        # Max Level
        self.max_level = ""
        # What id number is the ship
        self.ident = ""
        # Rarity
        self.rarity = ""
        # How Many HP the ship has
        self.shield_points = ""
        # How much HP is recovered when heal gems are matched
        self.repair_rate = ""
        # Percentage of incoming damage reduced
        self.damage_reduction = ""
        # Type of damage that gets reduced
        self.damage_reduction_type = ""
        # How much damage the ship does when damage gems are matched
        self.attack_value = ""
        # How many turns between skill deployment
        self.speed = ""
        # Skill ability the ship possesses
        self.skill = ""
        # How much damage is increased or decreased via modifications
        self.weapon_mod = ""
        # How much armor is increased or decreased via modifications
        self.armor_mod = ""
        # How much shield is increased or decreased via modifications
        self.shield_mod = ""
        # How much skills speed is increased or decreased via modifications
        self.engine_mod = ""
        # What type of damage does this ship do
        self.damage_type = ""
        # How many weapon hardpoints does this ship have
        self.weapon_hardpoint = ""
        # How many armor hardpoints does this ship have
        self.armor_hardpoint = ""
        # How many shield hardpoints does this ship have
        self.shield_hardpoint = ""
        # How many engine hardpoints does this have
        self.engine_hardpoint = ""
        # What skill does this ship confer when assigned as wing leader
        self.wing_leader_skill = ""