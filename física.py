def Graus_Celsius(): 
    Celsius= float(input("Digite um número: "))
    Fahrenheit= Celsius*(9.0/5.0)+32.0
    print("A temperatura em Fahrenheit é", Fahrenheit)

def Graus_Fahrenheit():
    Fahrenheit=float(input("Digite um número: "))
    Celsius= 5.0*(Fahrenheit-32.0)/9.0
    print("A temperatura em Celsius é", Celsius)
    
def Graus_Kelvin():
    Kelvin=float(input("Digite um número: "))
    Celsius= Kelvin-273.15
    print("A temperatura em Celsius é", Celsius)
    
def Celsius_Kelvin():
    Celsius=float(input("Digite um número: "))
    Kelvin= Celsius+273.15
    print("A temperatura em Kelvin é", Kelvin)
    
def intro():
    print("Pressione 1 para converter Kelvin para Ceulsius")
    print()
    print("Pressione 2 para converter Ceulsius para Kelvin")
    print()
    print("Pressione 3 para converter Celsius em Fahreinheit")
    tipo_de_conversao= int(input("Pressione 4 para converter Fahreinheit em Celsius:  "))
    if tipo_de_conversao == 4:
        print()
        print("Vamos converter Fahreinheit para Celsius")
        print()
        Graus_Fahrenheit()
    
    if tipo_de_conversao ==3:
        print()
        print("Vamos converter Ceulsius para Fahreinheit")
        print()
        Graus_Celsius()
    
    if tipo_de_conversao ==2:
        print()
        print("Vamos converter Ceulsius para Kelvin")
        print()
        Celsius_Kelvin()
    
    if tipo_de_conversao ==1:
        print()
        print("Vamos converter Kelvin para Ceulsius")
        print()
        Graus_Kelvin()

intro()   

opcao =0
while True:        
    print()
    print ("1 - Voltar ao inicio")
    print ("0 - Sair")
    opcao = int(input("> "))
    if (opcao == 1):
        intro()
    if opcao == 0:
        break
    
    