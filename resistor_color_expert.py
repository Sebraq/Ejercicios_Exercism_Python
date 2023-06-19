def resistor_label(colors):
    resist=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    tolerance={'grey':0.05,'violet':0.1,'blue':0.25,'green':0.5,'brown':1,'red':2,'gold':5,'silver':10}
    if len(colors)==1:
        return str(resist.index(colors[0]))+" ohms"
    if len(colors)==4:
        val1=resist.index(colors[0])
        val2=resist.index(colors[1])
        multi=resist.index(colors[2])
        tol=tolerance.get(colors[3])
        resistance=str(val1)+str(val2)
        totalresist=int(resistance)*pow(10,multi)
    if len(colors)==5:
        val1=resist.index(colors[0])
        val2=resist.index(colors[1])
        val3=resist.index(colors[2])
        multi=resist.index(colors[3])
        tol=tolerance.get(colors[4])
        resistance=str(val1)+str(val2)+str(val3)
        totalresist=int(resistance)*pow(10,multi)

    return str(ourvalue(totalresist))+" ±"+str(tol)+"%"


def ourvalue(res):
    res=str(res)
    if len(res)>=7:
        num=int(res)/pow(10,6)
        if num.is_integer():num=int(num)
        return str(num)+' megaohms'
    if len(res)<=6 and len(res)>=4:
        num=int(res)/pow(10,3)
        if num.is_integer():num=int(num)
        return str(num)+' kiloohms'
    if len(res)<=3:
        return str(res)+' ohms'

print(resistor_label(["red", "green", "yellow", "yellow", "brown"]))