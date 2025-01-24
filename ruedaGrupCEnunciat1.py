from xml.sax.saxutils import escape

if __name__ == '__main__':
    nomServei1 = "B - Bàsic: Menú senzill i sala"
    nomServei2 = "P - Prèmium: Menú gurmet i sala gran"
    nomServei3 = "V - VIP: Menú exclusiu, sala gran i decoració especial"
    nomServei4 = "T - Total VIP: Inclou tots els serveis VIP més assistència especialitzada"
    numEmpreses=int()
    esCorrecte=bool()
    esCorrecte=True
    nomEmpresa=str()
    servei=str()
    numPersones=int()
    preuInicial=int()
    preuDescomptat=int()
    descompte1=0
    descompte2=0

    comptador=1
    preuDelServei1 = 30
    preuDelServei2 = 50
    preuDelServei3 = 80
    preuDelServei4 = 120


    while(comptador<10):
        print(f"Quin és el nom de la empresa número {comptador}?")
        nomEmpresa=input()
        if(nomEmpresa=='*'):
            break
        else:
            print(f"Quin servei vol fer servir: {nomServei1}, {nomServei2}, {nomServei3}, {nomServei4}.Insereixi només la lletra del servei que vulgui fer servir")
            servei = input()
            if (servei == 'B' or servei == 'b' or servei == 'P' or servei == 'p' or servei == 'V' or servei == 'v' or servei == 'T' or servei == 't'):
                print("Quantes persones hi ha a la empresa?")
                numPersones = int(input())
                if (servei == 'B' or servei == 'b'):
                    preuInicial = numPersones * preuDelServei1
                    if (numPersones > 50):
                        descompte = preuInicial - (preuInicial * 0.05)
                        preuDescomptat = preuInicial - descompte
                    if(preuDescomptat>5000):
                        descompte2=(preuDescomptat - 5000)  - ((preuDescomptat - 5000) * 0.1)
                        preuDescomptat= preuDescomptat -descompte2
                if (servei == 'P' or servei == 'p'):
                    preuInicial = numPersones * preuDelServei2
                    if (numPersones > 50):
                        descompte1 = preuInicial - (preuInicial * 0.05)
                        preuDescomptat = preuInicial - descompte1
                    if (preuDescomptat > 5000):
                        descompte2 = (preuDescomptat - 5000) - ((preuDescomptat - 5000) * 0.1)
                        preuDescomptat = preuDescomptat - descompte2
                if (servei == 'V' or servei == 'v'):
                    preuInicial = numPersones * preuDelServei3
                    if (numPersones > 50):
                        descompte1 = preuInicial - (preuInicial * 0.05)
                        preuDescomptat = preuInicial - descompte1
                    if (preuDescomptat > 5000):
                        descompte2 = (preuDescomptat - 5000) - ((preuDescomptat - 5000) * 0.1)
                        preuDescomptat = preuDescomptat - descompte2
                if (servei == 'T' or servei == 't'):
                    preuInicial = numPersones * preuDelServei4
                    if (numPersones > 50):
                        descompte1 = preuInicial - (preuInicial * 0.05)
                        preuDescomptat = preuInicial - descompte1
                    if (preuDescomptat > 5000):
                        descompte2 = (preuDescomptat - 5000) - ((preuDescomptat - 5000) * 0.1)
                        preuDescomptat = preuDescomptat - descompte2
            else:
                print("Error!!!Insereix una lletra d'un servei existent!")
            print(f"Detalls de la factura:"
                  f"\n\t Empresa:{nomEmpresa}"
                  f"\n\t Tipus de servei:{servei}"
                  f"\n\t Nombre de persones:{numPersones}"
                  f"\n\t Cost inicial:{preuInicial}"
                  f"\n\t Descompte 1 (5% per més de 50 persones):{descompte}"
                  f"\n\t Descompte 2 (si el preu supera els 5000€):{descompte2}"
                  f"\n\t Total a pagar:{preuDescomptat}")

            comptador +=1

