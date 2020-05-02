## Alembic - Outil de migration de schéma

**Consulter les migrations de schema**
    
    docker exec -it api alembic history

**Consulter l'ID de la migration actuelle**
    
    docker exec -it api alembic current

**Créer une nouvelle migration**

    docker exec -it api alembic revision -m "NOM_DE_LA_REVISION"

**Executer les migrations jusqu'à la dernière**
    
    docker exec -it api alembic upgrade head

où `head` est la révision cible (la plus récente dans la majorité des cas).

**Revenir d'une migration en arrière**

    docker exec -it api alembic downgrade -1