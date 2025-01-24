"""
Nom: tornaElMesGranOMesPetit
Descripció: Funció que retorna el valor més gran
    o el més petit dels nombres rebuts dins un vector,
    que torni el valor més gran o el més petit
    dependrà del contingut de la variable tipus.
    Els valors del vector estaran entre -100 i 100.
===========================
    NOTA IMPORTANT:
        Que els valors del vector estiguin
        entre -100 i 100 NO HO CONTROLARÀ la funció!
===========================
===== Dades d'entrada =====
@param: vectorRebut de tipus vector d'enters amb
    els nombres dels quals es vol conèixer
    el nombre més gran o el més petit,
    depenent del contingut de la variable tipus.
@param: tipus de tipus cadena
    Si el contingut de tipus és "g",
    caldrà tornar el nombre més gran, però
    si el contingut de tipus és "p",
    caldrà tornar el nombre el més petit.
    En qualsevol altre cas, la funció retornarà
    el nombre 101, com a codi d'error.
===== Dades a tornar =====
@return: nombreATornar
    el nombre més gran del vector rebut.
"""
def tornaElMesGranOMesPetit(vectorRebut, tipus):
    posicio=0
    numGran=0
    numPetit=100
    while(posicio<len(vectorRebut)):
        if(tipus=='G' or tipus=='g'):

           if(vectorRebut[posicio]>numGran):
               numGran=vectorRebut[posicio]
           else:
               posicio+=1
               nombreATornar = numGran

        if (tipus == 'P' or tipus == 'p'):
            if (vectorRebut[posicio] < numPetit):
                numPetit=vectorRebut[posicio]
            else:
                posicio += 1
                nombreATornar = numPetit
    return nombreATornar

# Programa principal
if __name__ == '__main__':
    # Declaració de variables
    vector = list()
    mida = int()
    index = int()
    opcioEscollida = str()
    elNombreTornat = int()
    valorLlegit = int()
    valorLlegitNoEsCorrecte = bool()
    # Inicialització de variables
    mida = 5
    opcioEscollida = "cap"
    # Bucle per inicialitzar el vector
    index = 0
    while(index<mida):
        vector.append("")
        index += 1

    # Bucle per omplir el vector amb nombres
    # controlant que els nombres no estiguin fora dels
    # limits -100 i 100
    index = 0
    while(index<mida):
        valorLlegitNoEsCorrecte = True
        while(valorLlegitNoEsCorrecte):
            print(f"Entra el valor {index+1} de {mida}: ", end="")
            valorLlegit = int(input())
            if(valorLlegit < -100 or valorLlegit > 100):
                print("\tERROR! Cal que el valor estigui entre -100 i 100!",
                      "\n\tSi us plau, torna a intentar-ho!")
            else:
                valorLlegitNoEsCorrecte = False
                vector[index] = valorLlegit
        index += 1

    # Bucle per escollir el tipus
    while(opcioEscollida == "cap"):
        print(f"Entra si vols escollir el valor més petit (P o p) o el més gran (G o g): ", end="")
        opcioEscollida = input().lower()
        if(opcioEscollida != "p" and opcioEscollida != "g" ):
            print("\tERROR! Cal que el valor sigui P o p o G o g!",
                      "\n\tSi us plau, torna a intentar-ho!")
            opcioEscollida = "cap"

    # Fem una crida a la funció tornaElMesGranOMesPetit que heu creat per provar-la!
    elNombreTornat = tornaElMesGranOMesPetit(vector,opcioEscollida)

    print(f"El vector té els següents nombres {vector}")

    if (opcioEscollida == "g"):
        print(f"El nombre més gran és {elNombreTornat}")
    elif (opcioEscollida == "p"):
        print(f"El nombre més petit és {elNombreTornat}")
    else:
        print(f"\t\tCodi {elNombreTornat} rebut!\n\t\tHi hagut algun error!")