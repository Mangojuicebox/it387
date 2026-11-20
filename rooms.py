import json
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print


class RoomObject:
    def __init__(self, title, description, enemies=list()):
        self.name = title
        self.description = description
        self.enemies = enemies

    def print_room(self):
        s_width = 60
        print(f"[bold yellow]{self.name.upper().center(s_width, '-')}[/bold yellow]")
        print(f"| {self.description.ljust(s_width - 4)} |")
        print("|" + "-" * (s_width - 2) + "|")
        #console.print(f"| You see {you_see.ljust(s_width - 12)} |")
        for enemy in self.enemies:
            print(f" - {enemy.name}")
            print("|" + "-" * (s_width - 2) + "|")
            print("| " + "What do you do?".ljust(s_width - 4) + " |")
        #console.print(f"| {"1. Attack".ljust(s_width - 4)} |")
        #console.print(f"| {"2. Heal".ljust(s_width - 4)} |")
        #console.print(f"| {option3.ljust(s_width - 4)} |")
            print("|" + "-" * (s_width - 2) + "|")
        #console.print(f"| Log: {log.ljust(s_width - 9)} |")
            print("|" + "-" * (s_width - 2) + "|")

        choice = Prompt.ask( f"[magenta]What action?[/magenta]" )

        return choice
    
    def __str__(self):
        return f"Room: {self.name}"
    
if __name__ == "__main__":
    entryway = RoomObject("Entryway", "You see big doors")
    print(f"{entryway}")