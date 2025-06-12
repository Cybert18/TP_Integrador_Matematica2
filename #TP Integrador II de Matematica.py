#TP Integrador II de Matematica
#Conjuntos DNI
# Parte 1 – Desarrollo Matemático (Conjuntos y Lógica)

# 1.      Cada integrante debe anotar su número de DNI.

# 2.      A partir de los DNIs, se deben formar tantos conjuntos de dígitos únicos como integrantes tenga el grupo.

# 3.      Realizar entre esos conjuntos las siguientes operaciones: unión, intersección, diferencia (entre pares) y diferencia simétrica.

# 4.      Para cada una de estas operaciones, se debe realizar un diagrama de Venn (a mano o digital), que debe incluirse en la entrega.

# 5.      Redactar al menos dos expresiones lógicas en lenguaje natural, que puedan luego implementarse en Python y escribir en la documentación que van a presentar cual seria el resultado con los conjuntos que tienen.

# Ejemplos de expresiones lógicas:

# Si todos los conjuntos tienen al menos 5 elementos, entonces se considera que hay una alta diversidad numérica.·         
# Si el conjunto A tiene más elementos que el conjunto B y el conjunto C contiene al menos un número impar, entonces se cumple la condición de combinación amplia.·         
# Si ningún conjunto tiene el número 0, entonces se considera un grupo sin ceros.·         
# Si algún dígito aparece en todos los conjuntos, se marca como dígito común.·         
# Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces se etiqueta como "grupo par".·         
# Si la intersección entre todos los conjuntos tiene exactamente un elemento, se considera un dígito representativo del grupo.
# Estas expresiones deben incluirse en el archivo PDF de la parte teórica y se espera que al menos una de ellas se implemente directamente como lógica en el programa Python.


# Parte 2 – Desarrollo del Programa en Python



# El programa debe implementar varias de las ideas trabajadas en papel. Debe incluir:



# A. Operaciones con DNIs

# ·         Ingreso de los DNIs (reales o ficticios).

# ·         Generación automática de los conjuntos de dígitos únicos.

# ·         Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.

# ·         Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.

# ·         Suma total de los dígitos de cada DNI.

# ·         Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.

# Ejemplos:

# ·         Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".

# ·         Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta
def Genera_Conjuntos(Aux):
    str_DNI = str(Aux)
    Conjunto_DNI = {int(digito) for digito in str_DNI}
    return Conjunto_DNI

def Union_Conjuntos(A,B):
    C = A.union(B)
    return C

def Union_total(A, B, C):
    U_total = A | B | C
    return U_total


def Inter_Conjuntos(A,B):
    C = A.intersection(B)
    return C

def Inter_Total(A,B,C):
    I_total = A & B & C
    return I_total

def Diferencia_Conjuntos(A,B):
    C = A - B
    return C

def Diferencia_simetrica(A,B):
    C = A.symmetric_difference(B)
    return C

def DSimetrica_total(A, B, C):
    Ds_total= A ^ B ^ C 
    return Ds_total


#DNI de los Integrantes de Grupo
#Generacion de Conjuntos apartirde los DNI con los que se va a operar

DNI_1 = 34711991
conjunto_DNI1 = Genera_Conjuntos(DNI_1)

DNI_2 = 31230293
conjunto_DNI2 = Genera_Conjuntos(DNI_2)

DNI_3 = 39717139
conjunto_DNI3 = Genera_Conjuntos(DNI_3)

#Aqui mostramos los conjunto con los que se va a operar
print(f"Conjunto 1: {conjunto_DNI1}")
print(f"Conjunto 2: {conjunto_DNI2}")
print(f"Conjunto 3: {conjunto_DNI3}")

#Visualización de Operaciones de conjuntos unión, intersección, diferencias y diferencia simétrica
print("-----------------------Union de Conjuntos---------------------")

print(f"{conjunto_DNI1} Union {conjunto_DNI2} = {Union_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Union {conjunto_DNI3} = {Union_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Union {conjunto_DNI3} = {Union_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")

print(f"Union Total de los Conjuntos = {Union_total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")

print("--------------------Interseccion de Conjuntos------------------")

print(f"{conjunto_DNI1} Interseccion {conjunto_DNI2} = {Inter_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Interseccion {conjunto_DNI3} = {Inter_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Interseccion {conjunto_DNI3} = {Inter_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")


print(f"Interseccion Total de los Conjuntos = {Inter_Total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")

print("-------------------Diferencia de Conjuntos por Pares-----------------")
print(f"{conjunto_DNI1} Diferencia {conjunto_DNI2} = {Diferencia_Conjuntos(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI2} Diferencia {conjunto_DNI1} = {Diferencia_Conjuntos(conjunto_DNI2,conjunto_DNI1)}")

print(f"{conjunto_DNI1} Diferencia {conjunto_DNI3} = {Diferencia_Conjuntos(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI3} Diferencia {conjunto_DNI1} = {Diferencia_Conjuntos(conjunto_DNI3,conjunto_DNI1)}")

print(f"{conjunto_DNI2} Diferencia {conjunto_DNI3} = {Diferencia_Conjuntos(conjunto_DNI2,conjunto_DNI3)}")
print(f"{conjunto_DNI3} Diferencia {conjunto_DNI2} = {Diferencia_Conjuntos(conjunto_DNI3,conjunto_DNI2)}")


print("----------------Diferencia Simetrica de Conjuntos------------")

print(f"{conjunto_DNI1} Diferencia Simetrica {conjunto_DNI2} = {Diferencia_simetrica(conjunto_DNI1,conjunto_DNI2)}")
print(f"{conjunto_DNI1} Diferencia Simetrica {conjunto_DNI3} = {Diferencia_simetrica(conjunto_DNI1,conjunto_DNI3)}")
print(f"{conjunto_DNI2} Diferencia Simetrica {conjunto_DNI3} = {Diferencia_simetrica(conjunto_DNI2,conjunto_DNI3)}")

print(f"Diferencia Simetrica Total = {DSimetrica_total(conjunto_DNI1,conjunto_DNI2,conjunto_DNI3)}")

