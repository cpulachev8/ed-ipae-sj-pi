# def posiciones_de(a: str, b: str, index: int):    
#     print(index)
#     try:
#         if index == len(a):
#             return a.index(b)
#         else:
#             index = a.index(b, index)
#             posiciones.append(index)
#             return posiciones_de(a, b, index + 1)
#     except:
#         print("Fin")

def posiciones_de_beta(a: str, b: str):
    print(a)
    try:
        if len(a) == 0:
            return
        else:
            index = a.index(b)
            if len(posiciones)==0:
                posiciones.append(index)
            else:
                posiciones.append(posiciones[len(posiciones) - 1]+index+1)
            return posiciones_de_beta(a[index+1:], b)
    except:
        print("Fin Programa")

index = 0
posiciones = []    
cadena=  input("INGRESE TEXTO : ")
busca=input("INGRESE LETRA A BUSCAR: ")
# posiciones_de(cadena, busca, index)
posiciones_de_beta(cadena, busca)
print(posiciones)

# Wilmots Ortiz
# def buscar_pal(palabra,letra):     
#     lista=[]     
#     for posicion,caracter in enumerate(palabra):      
#         if(caracter==letra):          
#             lista.append(posicion)     
#     print(lista) 

# palabra=input("Ingrese la frase: ") 
# letra=input("busque la letra: ")  
# buscar_pal(palabra,letra)

# Edgar Espinoza
# def busqueda_palabra(a,b):
#     lista = []
#     numero = 0
#     for i in range (len(a)):
#         if a[i]==b:
#             lista.append(i)
#     print (lista)

# a= str(input("Ingrese el texto : "))
# b= str(input("Ingrese la palabra : "))
# busqueda_palabra(a,b)

# Diana Moran
# def posiciones_de(cadena, silaba, idx):
#     y = len(silaba)
#     x = cadena.find(silaba)
#     idx.append(x)
#     nueva_cadena = cadena.replace(silaba, y*'-', 1)
#     # print(nueva_cadena)
#     if x == -1:
#         print(idx[:-1])
#         return(idx[:-1])
#     else:
#         posiciones_de(nueva_cadena, silaba, idx)

# idx = []
# palabra=input("Ingrese la frase: ") 
# letra=input("busque la letra: ")  
# posiciones_de(palabra, letra, idx)

# Elías Tagle
# lista = []

# def posiciones_de(a,b):
#     for i in range(len(a)):
#         if a[i] == b[0] and a[i+1] == b[1]:
#             lista.append(i)
#     return lista

# palabra=input("Ingrese la frase: ") 
# letra=input("busque la letra: ")  
# print(posiciones_de(palabra, letra))

# Brad Solorzano
# palabra = input("Ingrese Frase: ")
# palabra2 = input("Ingrese palabra a buscar: ")
# lst = []

# def pala():
#     for pos,char in enumerate(palabra):
#         if(char == palabra2):
#             lst.append(pos)
#     print(lst)

# pala()

# Madeleine Sanchez
# cadena=  input("INGRESE TEXTO : ")
# busca=input("INGRESE LETRA A BUSCAR: ")
# # devolvemos con len la longitud del texto que hemos escrito
# # Método 2, con índice
# for indice in range(len(cadena)):
#     caracter = cadena[indice]
#     if caracter ==busca:
#         print("En el índice",indice," tenemos a '",caracter,"'")