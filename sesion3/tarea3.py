def tarea():
    numeros = [5, 10, 15,20]
    sumaNumers = 0

    for num in numeros:
        sumaNumers += num ** 2

    print("La suma de los cuadrados de estos numeros " + str(numeros) +" es:")    
    print(sumaNumers)
    

if __name__=="__main__":
    tarea()