import json
from sys import exception

from dice import roll3d6stat, roll_dice, roll3d6, rolld6

from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print

# Set up Rich console
console = Console()

class PlayerCharacter:
    def __init__(self, name,):
        # Store passed in values in the object
        self.name = name
        self.current_hp = 0
        self.str = 8
        self.con = 8
        self.ag = 8
        self.armor = 2
        self.roll_stats()

    def __str__(self):
      return f"{self.name} , HP: {self.current_hp}/{self.get_max_hp()} , STR: {self.str} , CON: {self.con} , AGI: {self.ag} , Armor: {self.armor}."
    
    
    def roll_stats(self):
          self.str = roll3d6stat() 
          self.con = roll3d6stat()
          self.ag = roll3d6stat() 
          self.current_hp = self.get_max_hp()

    def get_max_hp(self):
        return self.con * 2

    def get_damage_max(self):
            return int(self.str / 2)
    
    def take_damage(self, enemy):
            # Someone hit us - we use their damage max to roll.
            rolls, damage = roll_dice(1, enemy.get_damage_max(), count=1)
            self.current_hp = self.current_hp - damage - self.armor
            console.print(f"{self.name} took {damage} damage - armor absorbed {self.armor} hps.")

    def heal(self):
            # Heal
            rolls, heal = roll_dice(5)
            self.current_hp = self.current_hp + heal
            console.print(f"{self.name} healed for {heal} hit points.")
    
    def is_knocked_out(self):
            if self.current_hp < 1:
                return True
            return False

    def load_from_json(self, name, file_path="players.json"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    npcs_list = json.load(f)
    
                for npc in npcs_list:
                    if npc["name"].lower() == name.lower():
                        self.name = npc["name"]
                        self.str = int(npc["strength"])
                        self.ag = int(npc["agility"])
                        self.con = int(npc["constitution"])
                        self.armor = int(npc["armor"])
                        self.current_hp = int(npc["current_hp"])
                        return True
    
                print(f"[!] NPC '{name}' not found in '{file_path}'.")
                return False
            
            except Exception as e:
                    print(f"[!] Failed to load in JSON: {e}")
                    return False
            
    def save_to_json(self, file_path="players.json"):
            our_data = {
                "name": self.name,
                "race": "Unknown",
                # Could be extended to a property
                "strength": str(self.str),
                "agility": str(self.ag),
                "constitution": str(self.con),
                "armor": str(self.armor),
                "current_hp": str(self.current_hp),
            }
            try:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        npcs_list = json.load(f)
                except FileNotFoundError:
                    npcs_list = []

                # Update existing or append new
                updated = False
                for i, npc in enumerate(npcs_list):
                    if npc["name"].lower() == self.name.lower():
                        npcs_list[i] = our_data
                        updated = True
                        break

                if not updated:
                    npcs_list.append(our_data)

                # Save back
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(npcs_list, f, indent=2)

                print(f"[V] {self.name} saved to {file_path}")
            except Exception as e:
                print(f"[!] Failed to save JSON: {e}")

def LoadAllCharacters(file_path="players.json"):
    players = list()


    try:
        with open(file_path, "r", encoding="utf-8") as f:
             npcs_list = json.load(f)

        for npc in npcs_list:
            name = npc["name"]
            pc = PlayerCharacter(name)
            #pc.str = int(npc["str"])
            pc.load_from_json(name)
            players.append(pc)

        return players
    except Exception as e:
        print(f"[!] Failed to load in JSON: {e}")
        return False

if __name__ == "__main__":
    # Running directly
        Derlord = PlayerCharacter("Derlord")
        Derlord.save_to_json("test_players.json")
        #Derlord.load_from_json("Derlord")

        gorak = PlayerCharacter("Gorak")
        print(f"Gorak Rolls: {gorak}")
        gorak.load_from_json("gorak")
        print(f"Gorak Load: {gorak}")
        gorak.current_hp = 10