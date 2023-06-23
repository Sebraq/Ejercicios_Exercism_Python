from itertools import zip_longest

def transpose(lines):
    lines = lines.splitlines()
    lines=(l for l in zip_longest(*lines,fillvalue='_'))
    lines = ("".join(l).rstrip("_").replace("_", " ") for l in lines)
    return "\n".join(lines).rstrip()

