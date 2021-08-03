#/!/bin/python3

# l'idée de ce script est calculer 

print("""
          __                 __   _________        .__          
  _______/  |_  ____   ____ |  | _\_   ___ \_____  |  |   ____  
 /  ___/\   __\/  _ \_/ ___\|  |/ /    \  \/\__  \ |  | _/ ___\ 
 \___ \  |  | (  <_> )  \___|    <\     \____/ __ \|  |_\  \___ 
/____  > |__|  \____/ \___  >__|_ \\______  (____  /____/\___  >
     \/                   \/     \/       \/     \/          \/ 
""")
print("V1 Calcul  seulement le ratio")

# Les ETF a repartir, avec prix au 02/08/2020
# 45% S&P 500           (PE500)     29,42 
# 10% Russel 2000       (RS2K)      271
# 20% MSCI EM Asia      (PAASI)     24,81
# 20% Stoxx Europe 600  (ETZ)       13,34
# 5%  Topix             (PTPXE)     23,65

# Declaration variable pour chaque ETF

ETF1 = "PE500"
ETF2 = "RS2K"
ETF3 = "PAASI"
ETF4 = "ETZ"
ETF5 = "PTPXE"

# Declaration des ratio de chaque ETF

rETF1 = 45
rETF2 = 10
rETF3 = 20
rETF4 = 20
rETF5 = 5

# Déclaration des prix  de chaque ETF

pETF1 = 29.42
pETF2 = 271
pETF3 = 24.81
pETF4 = 13.34
pETF5 = 23.65

# Utilisateur entre le montant a repartir

portfolio = input("Montant a repartir :")

# fonction de calcul

def calculN (ratio,prix,total):
    x = ((int(ratio) * int(total)) / 100)
    nombre = float(x) / float(prix)
    return nombre

print(f"Repartition des ETF pour un total de {portfolio}")

nETF1 = calculN(rETF1,pETF1,portfolio)
nETF2 = calculN(rETF2,pETF2,portfolio)
nETF3 = calculN(rETF3,pETF3,portfolio)
nETF4 = calculN(rETF4,pETF4,portfolio)
nETF5 = calculN(rETF5,pETF5,portfolio)

print(f"Nombre de {ETF1} : {nETF1}")
print(f"Nombre de {ETF2} : {nETF2}")
print(f"Nombre de {ETF3} : {nETF3}")
print(f"Nombre de {ETF4} : {nETF4}")
print(f"Nombre de {ETF5} : {nETF5}")