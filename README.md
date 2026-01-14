Un projet simple d’application web en Python utilisant le framework Flask, dans le cadre de ma formation de Concepteur Développeur d'Applications.
Cette application sert de base pour apprendre à utiliser Flask et créer une application web locale.

-> Fonctionnalités:

- Serveur web léger avec Flask
- Routes définies dans app.py
- Templates HTML dans le dossier templates


-> Prérequis :

- Python 3.7 ou uultérieur
- pip 
- venv


-> Installation

1) Cloner le dépôt :
git clone https://github.com/minafnd/projet_flask_python.git
cd projet_flask_python


2) Crée un environnement virtuel :
python3 -m venv venv
source ./.venv/bin/activate  # Sur Windows : .\.venv\Scripts\activate
deactivate # pour désactiver l'environnement virtuel


3) Installer les dépendances :
pip install -r requirements.txt #pour avoir la liste des requirements dans un fichier txt, pour pouvoir reproduire le setup de la venv facilement
pip install flask


-> Pour lancer l’application

À la racine du projet :

python app.py # ou python3 app.py

Par défaut, l’application tourne sur :

http://127.0.0.1:5000


📁 Structure du projet
projet_flask_python/
├── app.py               ← fichier principal de l’application Flask
├── requirements.txt     ← dépendances Python
├── templates/           ← modèles HTML
│   └── *.html
├── .gitignore
└── README.md

