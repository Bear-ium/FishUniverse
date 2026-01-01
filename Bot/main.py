print("[DEBUG] Running main.py\n\n\n\n\n\n\n\n\n\n")

# ----------------------------

# Library Imports
from TwitchBotPlus import Bot as TwitchBot
from typing import Callable
from pathlib import Path

# Custom Library Imports
from Libs import Emojis
from Libs.TwitchCommands import Shutdown, Hello


envPath = Path(__file__).parent.parent / ".env"
CommandFn = Callable[
    # args, user
    [list[str], str],
    #reply, shutdown request
    tuple[str, bool]
]
CommandHandle = "-"

COMMANDS: dict[str, CommandFn] = {
    "shutdown": Shutdown,
    "hello": Hello
}

TwitchBot(
    COMMANDS=COMMANDS,
    ENV_Path=envPath,
    HANDLE=CommandHandle
).start()