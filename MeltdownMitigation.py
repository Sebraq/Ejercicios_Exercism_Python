#Check for critically

def is_criticality_balanced(temperature,neutrons):
    if temperature<800 and neutrons>500 and temperature*neutrons<500000:
        status=True
    else:
        status=False

    return bool(status)

#Determine the Power output range
def reactor_efficiency(voltage,current,maxPowa):
    genePowa=voltage*current
    percentage=(genePowa/maxPowa)*100

    if percentage>=80 :
        message="green"
    elif percentage<80 and percentage>=60:
        message="orange"
    elif percentage<60 and percentage>=30:
        message="red"
    elif percentage<30 :
        message="black"

    return str(message)

#Fail Safe Mechanism
def fail_safe(temperature,neutrons,threshold):
    if (temperature*neutrons)<(threshold*0.9):
        message="LOW"
    elif (threshold*0.9)<=(temperature*neutrons)<=(threshold*1.1):
        message="NORMAL"
    else:
        message="DANGER"
        
    return str(message)


    
