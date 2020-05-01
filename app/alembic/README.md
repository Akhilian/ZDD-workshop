## Alembic - Outil de migration de schéma

**Consulter les migrations de schema**
    
    docker exec -it api alembic history

**Créer une nouvelle migration**

    docker exec -it api alembic revision -m "NOM_DE_LA_REVISION"