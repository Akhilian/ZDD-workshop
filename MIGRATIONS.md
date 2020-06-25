# Les différentes migrations

## Les migrations "sans risque"

Les opérations suivantes n'ont normalement pas d'impact sur les applications et peuvent être jouées sans précaution particulière.
**Néanmoins**, il est important de faire en sorte que le code soit toujours compatible avec la version de la base de données déployée.

- Ajouter une nouvelle colonne **sans valeur par défaut**

- Supprimer une colonne

- Ajouter un index **CONCURRENTLY**

- Supprimer une contrainte (exemple: non-nullable)

- Ajouter une valeur par défaut à une colonne (ce ne sera effectif que sur les prochaines insertions)

## Les migrations "périlleuses"

Les migrations suivantes sont plus sensibles car nécessite l'ajout de LOCK *qui peuvent durer longtemps* et provoquer des indisponibilités.
La plupart du temps, la solution consiste à remplacer une opération complexe qui nécessite un lock par plusieurs mises en production qui utilisent des migrations sans risque.

Pour les faire sans interruption de service, il faudra plusieurs MEP. On utilisera le processus ZDD.

- Changer le type d'une colonne
    1. Ajouter la nouvelle colonne
    2. changer le code pour remplir les deux colonnes
    3. migrer les données vers la nouvelle colonne
    4. Supprimer l'ancienne colonne

- Ajouter une colonne avec une valeur par défaut
    1. Ajouter la nouvelle colonne
    2. Ajouter la contrainte *valeur par défaut* dans la nouvelle colonne 
    3. Remplir la colonne avec la valeur par défaut

- Ajouter une colonne non-nullable
    1. Ajouter la colonne sans la contrainte NOT NULL
    2. Compléter les données de la table si certaines sont NULL 
    3. Ajouter la contrainte avec au choix :
        1. au niveau de la table (option la moins risquée)
        2. au niveau de la colonne *en s'assurant qu'il y a un index sur la colonne qu'on modifie* (option la plus risquée)

- Ajouter une colonne avec une contrainte UNIQUE
    1. Ajouter la colonne
    2. Ajout de l'index CONCCURENTLY sur la colonne
    3. Ajouter la contrainte à la table en utilisant l'index (USING INDEX nom_de_l_index)

- Ajouter un index   
L'ajout d'un index est une opération en écriture coûteuse. 
L'option "safe" consiste à poser l'index CONCURRENTLY ([voir la doc ici](https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY)).

**Attention:** Poser un index avec l'option **CONCURRENTLY** demande plus de temps et de travail avant que l'index existe.
Si l'index est nécessaire immédiatement, il faudra trouver d'autres solutions.

