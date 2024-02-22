# Simulation Service :chart_with_upwards_trend:

Projet dans le cadre de notre module de Python avancé.

Réalisé par Clément Gambier et Tristan Fumière en AP4 (Promo 2022-2025) :man_technologist: :man_technologist:

Le projet vise à développer un service de simulation de données basé sur Python pour faciliter la gestion d'énergies renouvelables.

L'objectif principal est de créer une API REST qui offre des fonctionnalités avancées de simulation, intégrant une blockchain pour la traçabilité des transactions énergétiques. :electric_plug: :gear:

## Démarches pour lancer le projet :hammer_and_wrench:

1. Activer l'environnement
    ```sh
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install "pymongo[srv]"
    ```

2. Lancer un conteneur Docker pour sauvegarder les données (la blockchain étant centralisée afin de faciliter la simulation) avec une base de données MongoDB.
    ```sh
    docker-compose up -d
    ```

3. Pour lancer le programme
    ```sh
    cd src
    python3 main.py
    ```

## Endpoints disponibles :rocket:

- Route GET : pour récupérer les données de la blockchain
    - http://localhost:5000/chain

- Route POST : pour ajouter un nouveau bloc à la blockchain
    - http://localhost:5000/block
