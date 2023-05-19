def value(colors):
    colorsdef={"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5","blue":"6","violet":"7","grey":"8","white":"9"}
    string=""
    if len(colors)>2:
        colors=colors[:-1]
    for c in colors:
        if c in colorsdef:string+=colorsdef.get(c)
    return int(string)