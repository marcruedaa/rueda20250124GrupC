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

    comptador=1
    preuDelServei1 = 30
    preuDelServei2 = 50
    preuDelServei3 = 80
    preuDelServei4 = 120


    while(comptador<10):
        print(f"Quin és el nom de la empresa número {comptador}?")
        nomEmpresa=input()
        if(nomEmpresa=='*'):
            print(f"Quin servei vol fer servir: {nomServei1}, {nomServei2}, {nomServei3}, {nomServei4}.Insereixi només la lletra del servei que vulgui fer servir")
            servei=input()
            if(servei=='B' or servei=='b' or servei=='P' or servei=='p' or servei=='V' or servei=='v' or servei=='T' or servei=='t')