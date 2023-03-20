Django Job Board
Ce projet est une application web qui permet de recenser les annonces et les entreprises qui utilisent la technologie Django. Il s'agit d'un outil pratique pour les personnes cherchant une alternance en lien avec cette technologie.

Installation
Clonez ce repository : git clone https://github.com/AymenK13/Projets.git
Accédez au dossier du projet
Créez un environnement virtuel : python3 -m venv myenv (remplacez myenv par le nom de votre choix)
Activez l'environnement virtuel : source myenv/bin/activate, pour Windows, utilisez myenv\Scripts\activate
Installez les dépendances du projet : pip install -r requirements.txt
Créez la base de données : python manage.py migrate
Lancez le serveur de développement : python manage.py runserver
Fonctionnalités
Ajouter une annonce :
Chaque annonce est reliée à une entreprise
Vous pourrez indiquer la date de candidature
Ajouter l'annonce à vos favoris
Triez les annonces par date d'ajout, ville ou titre du poste.
Afficher uniquement les favoris, les candidatures à laquelle vous avez postulé.
Annuaire :
Vous pouvez enregistrer les entreprises et leur lier leurs annonces.
Ajouter des documents liés à cette entreprise.
Ajouter des notes
Modifier ou supprimer kes infos d'une entreprise.
Index :
Affiche le nombre d'entreprises, et d'annonces enregistrées.
Affiche le nombre de candidature envoyées, ainsi que la dernière annonce et entreprise enregistrée.
À venir :
Envois d'email depuis l'application (tests en cours)
Ajout de l'api Google Maps pour localiser les entreprises
Amélioration de l'interface graphique
En cas de déploiement de l'application, création d'une interface utilisateur et donc utilisation d'un framework frontweb (React ?) afin d'améliorer l'expérience utilisateur (améliorer les performances de l'application, gestion de l'état, séparer la logique de présentation de la logique de l'application)
Contributions
Les contributions sont les bienvenues. Pour toute modification majeure, veuillez d'abord discuter des changements que vous souhaitez apporter en créant une issue.
    
