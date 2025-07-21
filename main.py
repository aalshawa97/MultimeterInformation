#Multimeter facts

def switch(menu):
    if menu == "1":
        return "Multimeters measure electrical properties such as voltage, current, and resistance. Current is a measure of the rate at which electric charge flows past a specific point in a circuit. Resistance is measure of how much the flow of electrons is slowed down by resistance, measured in ohms. Voltage is the measure of electrical potential difference that pushes electrons through a circuit.V = I(current)*R(resistance)"
    else:
        return "Goodbye!"

print("Hi, what would you like to know about multimeters?")
print (switch(input("Press 1 if you would like to know what multimeters do.")))
