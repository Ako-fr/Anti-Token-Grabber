# Dev - Ako
# Discord : https://discord.gg/gFkwb4F673

from os import system
system("title Installation des modules")

try: import colorama
except: system("pip install colorama")
from colorama import Fore, init
init()

try: import requests
except: system("pip install requests")
from requests import delete, get

yes = ['yes', 'oui', 'Yes', 'Oui', 'y', 'o', 'Y', 'O']
no = ['no', 'non', 'No', 'Non', 'N', 'n']
webhook = "https://discord.com/api/webhooks/"
pastbin = "https://pastbin/"

wait = f"[{Fore.BLUE}*{Fore.RESET}]"
system("title Anti Token Grabber - Ako")
print(f"""
  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$        /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$ | $$|__  $$__/|_  $$_/       /$$__  $$| $$__  $$ /$$__  $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$$$| $$   | $$     | $$        | $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$$$$$$$| $$ $$ $$   | $$     | $$        | $$ /$$$$| $$$$$$$/| $$$$$$$$| $$$$$$$ | $$$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$| $$  $$$$   | $$     | $$        | $$|_  $$| $$__  $$| $$__  $$| $$__  $$| $$__  $$| $$__/   | $$__  $$ 
| $$  | $$| $$\  $$$   | $$     | $$        | $$  \ $$| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$  | $$| $$ \  $$   | $$    /$$$$$$      |  $$$$$$/| $$  | $$| $$  | $$| $$$$$$$/| $$$$$$$/| $$$$$$$$| $$  | $$
|__/  |__/|__/  \__/   |__/   |______/       \______/ |__/  |__/|__/  |__/|_______/ |_______/ |________/|__/  |__/
                                                                                                                        
                            {wait} Recherche de Token Grabber
                            {wait} Suppresion de Grabber
                            {wait} Discord : https://discord.gg/gFkwb4F673
                            {wait} Devloppeur : >Ako’#7882
                            
      """)

fiche = input("[*] Indiquez le fichier a vérifier : ")
fichier = open(fiche,"r").read().splitlines()
def decompilation(fichier):
    print(f"[*] Je décompile {fichier}")
    # Le décompilateur n'est pas dev par moi (il est dispo sur github !)
    system(f"python decompilateur.py {fichier}")

print("[*] Je vérifie si je trouve un webhook")
for ligne in fichier:
    if webhook in ligne:
        print("[*] webhook trouvé")
        print(ligne)
        whb = input("[*] Indique l'url du webhook : ")
        while 5:
            if whb == '':
                print("[*] Merci d'indinquer l'url du webhook !")
                whb = input("[*] Indique l'url du webhook : ")
        if whb == '':
            print("[*] Vous n'avez toujours pas indiquer de webhook")
            input("[*] Appuyez pour quittez...")
        while 5:
            if "https://discord.com/api/webhooks/" not in whb:
                print("[*] Webhook Invalide")
                whb = input("[*] Indique l'url du webhook : ")
        if "https://discord.com/api/webhooks/" not in whb:
            print("[*] Vous n'avez toujours pas indiquer de webhook valide")
            input("[*] Appuyez pour quittez...")
        elif "https://discord.com/api/webhooks/" in whb:
            print("[*] Webhook Valide")
            check = input("[*] Voulez-vous que je le check : ")
            if check == yes:
                checking = get(whb)
                if checking.status_code == 200:
                    print("[*] Webhook Valide !")
                    deleting = input("[*] Est-ce que je delete le webhook : ")
                    if deleting == yes:
                        delete(whb)
                        print("[*] Webhook Delete")
                        input("[*] Appuyez pour quittez...")
                    elif deleting == no:
                        print("[*] Je ne delete pas le webhook")
                        input("[*] Appuyez pour quittez...")
                    else: 
                        print("[*] Veuillez rentrez une commande valide")
                        input("[*] Appuyez pour quittez...")
                elif checking.status_code == 401:
                    print("[*] Webhook invalide")
                    input("[*] Appuyez pour quittez...")
            elif checking == no:
                print("[*] Je ne check pas le webhook")
                deleting_2 = input("[*] Est-ce que je delete le webhook : ")
                if deleting_2 == yes:
                    print("[*] Je delete le webhook")
                    delete(whb)
                    print("[*] Webhook delete")
                    input("[*] Appuyez pour quittez...")
                elif deleting_2 == no:
                    print("[*] Je ne delete pas le webhook")
                    input("[*] Appuyez pour quittez...")
                else:
                    print("[*] Veuillez entrez une commande valide")
                    input("[*] Appuyez pour quittez...")
            else:
                print("[*] Veuillez rentrez une commande valide")
                input("[*] Appuyez pour quittez...")
        else:
            print("[*] Une erreur est surevenue ")
            input("[*] Appuyez pour quittez...")
                
    elif not webhook in fichier:
        print("[*] Aucun webhook trouvé")
        print("[*] Je cherche l'importe d'un potentiel webhook")
        web = "webhook"
        if web in fichier:
            print("[*] J'ai trouvé le mot webhook")
            print(ligne)
            other = input("[*] Voulez-vous une recherche de plus de mot : ")
            if other == yes:
                system(f'findstr webhook "{fichier}')
                input("[*] Appuyez pour quittez...")
            elif other == no:
                print("[*] Ok, je passe")
                past = input("[*] Voulez-vous que je cherche un pastbin : ")
                if past == yes:
                    if pastbin in fichier:
                        print("[*] Pastbin trouvé")
                        print(ligne)
                        input("[*] Appuyez pour quittez...")
                    else:
                        print("[*] Je n'est rien trouvé")
                        dec = input("[*] Voulez-vous décompilez le fichier : ")
                        if dec == yes:
                            print("[*] Je décompile le fichier")
                            decompilation()
                        elif dec == no:
                            print("[*] Je ne décompile pas le fichier")
                            input("[*] Appuyez pour quittez...")
                        else: 
                            print("[*] Veuillez entrez une commande valide")
                elif past == no:
                    print("[*] Je ne cherche pas de pastbin")
                    deco = input("[*] Voulez-vous décompilez le fichier : ")
                    if deco == yes:
                        print("[*] Je décompile le fichier")
                        decompilation()
                    elif deco == no:
                        print("[*] Je ne décompile pas le fichier")
                        input("[*] Appuyez pour quittez...")
                    else: 
                        print("[*] Veuillez entrez une commande valide")
                else:
                    print("[*] Veuillez entrez une commande valide")
                    input("[*] Appuyez pour quittez...")
            else:
                print("[*] Veuillez entrez une commande valide")
                input("[*] Appuyez pour quittez...")
        elif not web in fichier:
            print("[*] Je n'est rien trouvé")
            decop = input("[*] Voulez-vous décompilez le fichier : ")
            decompilation(fichier)

# Anti Token Grabber by >Ako’#7882
