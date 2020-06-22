# Le ZDD pour les opérations périlleuses

## Cas d'usages

Pour tout projet ventant sa haute disponibilité, la migration de schéma de base de données peut s'avérer douloureuse. 
Si elle faite en une seule fois (schéma base v1 vers schéma base v2), il est impossible de garantir la disponibilité de l'application :
- Le changement de schéma peut poser des LOCK sur la table
- La migration de données peut s'avérer longue
- Le code applicatif doit changer pour gérer ce nouveau modèle de données
    
Des cas d'usages fréquents amènent ces problématiques : 
- changement du modèle relationnel métier
- demande de conservation de données d'historique
    
Malgré tout le continuous deployment nous garantit une amélioration du time-to-market et la qualité des developpements.      
Comment faire pour que ces livraisons fréquentes n'impactent pas la disponibilité du site ?

## Comment modifier notre base de données sans interruption de service ?  

Pour qu'une migration se passe bien, 3 choses doivent être respecter : 
- Le code deployé doit fonctioner pour la version initiale et cible du schéma de base de données (exemple : si j'ajoute l'âge de quelqu'un le code doit fonctionner même si l'infos n'est pas disponible)
- Les modifications de la base ne doivent pas poser de lock qui empêcherait le fonctionnement de l'application actuelle (lecture comme écriture)
- En cas d'erreur, le retour au modèle de données différents doit être possible (ROLLBACK) 

Automatiser ces migrations via des outils (alembic, liquibase, flyway) est un bon moyen d'éviter les erreurs manuelles et de rollback facilement.

Dans les étapes présentes ci-dessous, v1 le schéma initial de bases de données et v2 représente le schéma cible.  
Les étapes à suivre sont les suivantes :

- **Étape 0** : Application qui marche avec v1.

- **Étape 1** : Faire évoluer le schéma initiale de BDD pour permettre de stocker des données dans la version v2. 
Ce script porte le nom de **script d'expansion**.
Il est accompagné du **script de rollback** qui permettra de retourner au schéma initial sans perdre de données en cas de problème.

- **Étape 2** : Deployer une version du code de l'application qui manipule les données dans le schéma v1 **et** v2.  
**Attention**, en lecture, cela peut soulever des questions du type "quelles données restent références pendant cette phase de transition ?".   
Même questions sur l'écriture et la ré-écriture, si la donnée est dupliquée, elle devra être modifiée à deux endroits (ou pas ...).

- **Étape 3** : Migrer les données v1 nécessaires vers v2.  
Si la migration concerne un grand volume de données, un traitement par batch peut être nécessaire pour ne pas mettre de lock sur la table.
Chaque batch de migration pourra avoir ce déroulé :
    1. Il démarre une transaction.
    2. Il sélectionne les lignes de la table à modifier, et les verrouille (pour éviter les modifications conccurentes).
    3. Il adapte les données au schéma cible.
    4. Il valide la transaction, relâchant ainsi les données.

- **Étape 4** : Déployer une version du code de l'application qui expose les données basés sur le schéma de données v2.

- **Étape 5** : Nettoyer le schéma de BDD v1 et le code associé. Le script de migration de schéma se nomme le **script de contraction**. 
Il va permettre au schéma de base de données d'arriver au schéma cible.

Les éléments qui facilitent le ZDD sont les suivants :
- Connaitre les mécanismes de verrous et transaction de la base de données. Cela peut être facilité par l'utilisation d'un ORM.

Sources : 
https://www.braintreepayments.com/blog/safe-operations-for-high-volume-postgresql/  
https://blog.octo.com/zero-downtime-deployment/  
https://blog.octo.com/versionning-dapi-zero-downtime-deployment-et-migration-sql-theorie-et-cas-pratique/
