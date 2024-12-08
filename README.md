# Site Python-Flask - Exercices de Python

Bienvenue sur le site Python-Flask, un projet conçu pour regrouper divers exercices réalisés dans le cadre de cours de Python. Ce site inclut plusieurs fonctionnalités allant de la gestion des scores et des personnes, à des jeux interactifs comme le Morpion, ainsi qu'une implémentation de l'algorithme de Dijkstra.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone <URL de votre dépôt>
    ```

2. Naviguez vers le répertoire du projet :
    ```bash
    cd <nom_du_répertoire>
    ```

3. Créez un environnement virtuel :
    ```bash
    python -m venv venv
    ```

4. Activez l'environnement virtuel :
    ```bash
    # Sur Windows
    venv\Scripts\activate
    # Sur macOS/Linux
    source venv/bin/activate
    ```

5. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Lancement du Serveur

Lancez le serveur Flask en exécutant le fichier `app.py` :
```bash
python app.py
```
## Fonctionnalités

### Gestion des Personnes
Ajoutez, modifiez, supprimez et affichez des personnes dans une base de données. Cette section comprend un formulaire pour entrer des informations personnelles.

### Gestion des Scores
Ajoutez, modifiez, supprimez et affichez des scores associés aux personnes dans une base de données. Cette section permet de gérer les performances et les résultats de manière interactive.

### Jeu de Morpion (Tic-Tac-Toe)
Un jeu de Morpion où vous jouez contre l'ordinateur :
- Vous jouez avec la croix (X).
- L'ordinateur joue avec le rond (O).
- Le jeu alterne les coups et détermine le gagnant ou si la partie est nulle.

### Calculateur de Date
Entrez un nombre de jours pour obtenir la date correspondant à "aujourd'hui moins le nombre de jours indiqué".

### Affichage des Graphiques de Stock
Récupère les données boursières d'un ticker spécifique (par exemple, TSLA pour Tesla) et affiche un graphique de l'évolution des prix de clôture.

### Algorithme de Dijkstra
- Implémente et visualise l'algorithme de Dijkstra pour trouver le chemin le plus court dans un graphe :
- Définir les Sommets : Entrez le nombre de sommets à inclure dans le graphe.
- Définir les Arêtes : Entrez les arêtes et leurs poids entre les sommets sélectionnés. Assurez-vous que chaque sommet a au moins une arête.
- Générer le Graphe : Le graphe est généré et visualisé. Vous pouvez également sélectionner deux sommets pour calculer le chemin le plus court entre eux.

### Étapes de l'Algorithme de Dijkstra
- Initialisation : Chaque sommet est initialisé avec une distance infinie, sauf le sommet de départ qui est initialisé à 0.
- Traitement des Sommets : Utilisation d'une file de priorité pour traiter le sommet avec la plus petite distance courante.
- Mise à Jour des Distances : Pour chaque voisin du sommet courant, la distance est mise à jour si un chemin plus court est trouvé.
- Finalisation : Lorsque tous les sommets ont été traités, les distances minimales et les chemins sont déterminés.

L'algorithme continue jusqu'à ce que tous les sommets aient été traités, garantissant ainsi le chemin le plus court depuis le sommet de départ à chaque autre sommet dans le graphe.

#### Ce projet a été réalisé dans le cadre d'un cours de Python. par Thomas Clerc.
