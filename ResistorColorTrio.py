def label(colors):
    code=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    if len(colors)>3:colors=colors[:-1]
    val1=code.index(colors[0]);val2=code.index(colors[1]);val3=code.index(colors[2])
    ResistorVal=str(val1)+str(val2);TotalResistor=int(ResistorVal)*pow(10,val3)
    if str(TotalResistor).count('0')<12 and str(TotalResistor).count('0')>=9:
        return str(int(TotalResistor/pow(10,9)))+' gigaohms'
    if str(TotalResistor).count('0')<9 and str(TotalResistor).count('0')>=6:
        return str(int(TotalResistor/pow(10,6)))+' megaohms'
    if str(TotalResistor).count('0')<6 and str(TotalResistor).count('0')>=3:
        return str(int(TotalResistor/pow(10,3)))+' kiloohms'
    
    return str(TotalResistor)+' ohms'

print(label(["blue", "green", "yellow", "orange"]))
