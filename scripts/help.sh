#!/bin/bash
# if [$1 == HELP_WITH_ERROR_MESSAGE]; then
#     echo -e 'La commande saisie est manquante ou introuvable.'
# fi

if [ $1 == 'HELP_WITH_ERROR_MESSAGE' ]; then
cat << EndOfMessage

La commande saisie est manquante ou introuvable.

EndOfMessage
fi


cat << EndOfMessage
Usage: planecli [--help] <command>

Commands:
    start       Démarre l'application
    stop        Arrête l'application
    alembic     Gestion des migrations de la base de données 

EndOfMessage
