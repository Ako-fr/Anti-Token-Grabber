<h1 align="center">Anti Discord Token Grabber</h1>
<h3 align="center">Un programme simple qui vérifie si un discord grabber ce trouve dans votre fichier .exe, en utilisant plusieurs commande simple et un décomplilateur open souce trouvable sur github</h3><br>
<p align="center"><img src="https://camo.githubusercontent.com/23b938114b74aebf335eda497b1e53030976a0255c6fadb319622c135c54c2c1/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f6a544e47335246364577626b7044344c5a782f67697068792e676966"></p><br>
<h1 align="center">Modules & Installation</h1>

```python
import colorama, requests
```

```python
try: import colorama, requests
except: system("pip install -r requirements.txt")
```

<br>
<h1 align="center">Utilisation</h1>
<h3 align="center">Le programme est très simple d'utilisation, il vous suffit de deplacer le fichier .exe dans le même fichier que l'anti grabber. Ensuite ouvrez le fichier "main.py" et suivez les indications.</h3><br>
<p align="center"><img src="https://cdn.discordapp.com/attachments/881202945444679691/890715662421475338/unknown.png"></p><br>
<h3 align="center">Voila un exemple du code, celui va inspecter chaque ligne du fichier pour vérifier s'il contient quel que chose qui pourrait resemble a un webhook discord</h3><br>

```python
yes = ['yes', 'oui', 'Yes', 'Oui', 'y', 'o', 'Y', 'O']
no = ['no', 'non', 'No', 'Non', 'N', 'n']
webhook = "https://discord.com/api/webhooks/"
pastbin = "https://pastbin/"

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
```
