def two_fer(name=""):
    if not name:
        return "One for you, one for me."
    return f"One for {name}, one for me."

#V2
def two_fer(name="you"):
    return f"One for {name}, one for me"