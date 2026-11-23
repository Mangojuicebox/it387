from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print

from players import PlayerCharacter, LoadAllCharacters
from rooms import RoomObject

from config import e, p

print("[bold green]Welcome to the game![/bold green]")
p("Game started.")

player_list = LoadAllCharacters()

print(f"Character List: \n{player_list}")