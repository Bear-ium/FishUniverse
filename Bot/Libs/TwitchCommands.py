#(args: list[str], user: str) -> tuple[str, bool]:

def Shutdown(args: list[str], user: str) -> tuple[str, bool]:
    if user == "majojobears" or user == "theactualevie" or user == "danmanplayz":
        return (f"Goodbye {user} & chat!",True)
    else:
        return ("",False)
    pass

def Hello(args: list[str], user: str) -> tuple[str, bool]:
    firstWord  = args[0] if len(args) > 0 else ""
    secondWord = args[1] if len(args) > 1 else ""
    thirdWord  = args[2] if len(args) > 2 else ""
    
    return (f"Hello @{user}, your 3 words were: {firstWord}, {secondWord}, {thirdWord}", False)