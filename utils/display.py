from rich.console import Console
from rich.progress import track

console = Console()

def fancy_print(msg, style="bold green"):
    console.print(f"[ {msg} ]", style=style)

def progress_bar(data, description):
    return track(data, description=description)