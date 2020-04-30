# Atelier ZDD

[![Build Status](https://travis-ci.org/Akhilian/ZDD-workshop.svg?branch=master)](https://travis-ci.org/Akhilian/ZDD-workshop)

## Contexte

Depuis quelques mois, vous êtes responsable de maintenir et d'enrichir une API public qui permet de consulter **"DEFINIR LR THEME"**.

- Avion
    - En vol
    - Au sol
    - En maintenance
- Aeroport
  - Pistes
  - Hangar
- Position
  - GPS
  - Altitude

Grâce à vos efforts, et l'appui de quelques sponsors, cette API connait un succès grandissant et le nombre de vos utilisateurs - et donc le nombre de requêtes - ne cesse de grandir. Ce qui était un petit projet aux ambitions modestes doit maintenant continuer à évoluer tout en assurant une disponibilité maximale.

## Requirements
* Docker (version 19.0)
* Un éditeur de texte

## Architecture applicative

L'application a été construite en s'inspirant du pattern d'architecture connu sous le nom d'architecture hexagonale, popularisé par Alistair Cockburn.

L'application expose une API disponible sur l'adresse http://localhost, qui ne suit pas de formalisme particulier, mais est inspiré du principe de ressource au centre du concept d'API Rest. Le format d'échange est le JSON.

Pour le développement, un pgadmin est disponible sur l'addresse http://localhost:5050 mais cette application n'est pas disponible en production. Il est possible de s'y connecter : identifiant : `pgadmin4@pgadmin.org` et mot de passe : `admin` .

L'accès à la base de données est protégé par un mot de passe : `postgres`

### Description technique

Une API
  - Python / Flask

Une BDD postgres
  - Postgres 10.12

Images (pour le dev local)
  - Docker (v19.03.8)
    

### Outils et commandes
Il est possible (et recommandé) de lancer l'application en local pour prendre connaissance du contexte, et d'effectuer des modifications sur son poste avant d'envoyer le code en production.

Une description des endpoints et de comment les utiliser est disponible pour le logiciel [Insomnia](https://insomnia.rest/) via le fichier `.json` éponyme.


**Lancer l'application en local**

    docker-compose up

**Se connecter au conteneur de l'API**

    docker exec -it api bash

**Consulter les migrations de schema**
    
    docker exec -it api alembic history

**Créer une nouvelle migration**

    docker exec -it api alembic revision -m "NOM_DE_LA_REVISION"

**Lancer les tests en local**

Dans le répertoire `app/`

    PYTHONPATH=. py.test --durations=0
