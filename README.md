# FlashbotMongoDB

Notre projet FlashbotMongoDB est un projet Scrapy qui se compose de plusieurs fichiers en Python:
- flashbot.py qui est le fichier principal nous a permis d'extraire les textes des offres d'emploi du site web Monster
- Les fichiers items.py, pipelines.py et settings.py qui permettent de faire la connection entre le module Scrapy et MongoDB et permettent donc d'alimenter notre base MongoDB avec les données extraites par Scrapy.
Ces 3 fichiers cités se trouvent dans le dossier jobboard tandis que flashbot.py se trouve dans le dossier jobboard/spiders
Pour effectuer à la fois l'extraction du site web Monster et le remplissage de MongoDB avec les données extraites on utilise la commande suivante:

```sh
scrapy crawl flashbot
```

Le dossier FlaskDataJobs, lui affiche la liste des jobs obtenue avec MongoDB sur un navigateur. Pour effectuer cet affichage, on lance la commande suivante:

```sh
python3 flask_flashbot.py
```
Cette commande nous donnera la location des données dans le navigateur.
