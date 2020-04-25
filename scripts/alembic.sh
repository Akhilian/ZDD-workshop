#!/bin/bash
function migration_alembic
{
cat << EndOfMessage
Usage: planecli alembic [--help] <command>

Commands:
    current                 Migration actuelle de l'api
    history                 Liste des migrations
    upgrade <target>        Appliquer une nouvelle migration
        • head              Applique l'ensemble des migrations disponibles
        • +1                Applique une migration supplémentaire

    downgrade <target>      Appliquer toutes les migrations depuis la dernière déjà jouée
        • -1                

    help                    Afficher la document d'Alembic

EndOfMessage
}

if [ -z $2 ]
then
    migration_alembic
else
    case $2 in
        '--help') migration_alembic;;
        'help') docker exec -t api alembic $2;;
        *) docker exec -t api alembic $2;;
    esac
fi
