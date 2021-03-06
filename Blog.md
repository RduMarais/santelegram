# SanTelegram Bot

Cet hiver 2020, il est plus important que jamais de garder le contact avec ceux qui nous sont proches. Contact à distance évidemment, vu que l'hiver est marqué par : 1) le froid (logique) et 2) une pandémie mortelle. Pas facile donc de se préparer avec ses proches et sa famille à fêter Noël sereinement. Et pour éviter de réduire Noël à un simple envoi de cadeaux achetés en ligne à des entreprises payant plus ou moins leurs impôts, en discutant avec un ami (bien que collègue), on a eu cette idée de faire un **Bot Telegram "calendrier de l'Avent"**. 

> Ce post de blog a pour but de vous aider à faire votre en bot rapidement. Je m'adresse à des gens qui ont peu ou pas codé du tout. 
>
> Si ce n'est pas votre cas, ou si vous êtes pressés, vous pouvez copier-coller les fichiers qui sont à la fin du post ou [sur mon GitHub](https://github.com/RduMarais/santelegram) et rentrer dans les 10 minutes promises par le titre.

#### Telegram, c'est quoi ? 

Pour ceux qui ne connaissent pas [Telegram](https://telegram.org/), il s'agit d'une messagerie chiffrée, exactement comme WhatsApp. Les quelques différences avec WhatsApp sont : 

 * la possibilité de créer des canaux de conversation chiffrés de bout-en-bout ;
 * le fait que l'application soit développée en source ouverte ; 
 * la possibilité de créer des Bots ; 

Concrètement, c'est comme WhatsApp, mais avec quelques options en plus pour préserver sa vie privée des [companies comme WhatsApp](https://fr.wikipedia.org/wiki/Facebook_(entreprise)). Je ne dis pas que c'est le [Graal de la vie privée](https://www.signal.org/fr/) mais c'est déjà pas mal.

#### Le Bot

Donc l'idée du bot est simple : dans un chat de groupe, tous les jours, quelqu'un ouvre la "case" du jour. Pour réunir les gens autour du bot, tout le monde peut essayer de l'ouvrir, mais une seule personne, déterminée aléatoirement, peut réussir.
Une fois la "case" ouverte, le bot envoie une image, une citation, un lien, qui vient d'une liste prédéterminée.

Si le projet vous plaît, voilà comment faire !


# Ingrédients

Pour faire un Bot Telegram, il vous faut : 

 * un compte Telegram ;
 * un groupe sur lequel faire votre Bot ; 
 * Un ordinateur ;
 * avoir quelques bases en Python (un _hello world_ suffit)
 * Un serveur.

**Par serveur, j'entends** un ordinateur qui pourra rester allumé tant que vous voulez faire fonctionner votre bot, et qui peut faire des requêtes web. Donc il faut avoir suffisamment confiance en la connexion pour pas qu'elle flanche en pleine conversation avec le Bot. Pour les plus _esthètes_, il s'agira donc d'un vrai serveur, éventuellement dans le _cloud_ pour faire chic. Mais pour ce projet, **un vieux PC pentium 4 qui traîne dans un grenier fera très bien l'affaire**.

# Créer le Bot

Pour créer le bot, d'innombrables tutoriels existent. J'ai utilisé [celui-là](https://blog.usejournal.com/part-1-how-to-create-a-telegram-bot-in-python-under-10-minutes-145e7f4e6e40?gi=322a274e6e6c), que je reprends ci-dessous dans les grandes lignes.

 * Il faut se connecter sur Telegram. 
 * Chercher dans la barre de recherche un compte qui s'appelle BotFather ou @botfather de son username.

![Ledit BotFather, petit pères des bots.](https://miro.medium.com/max/1400/1*fV8qxeAoRT8xhVW9-l6g3Q.png)

 * Pour lancer la conversation, cliquez sur le gros bouton `START`.
 * BotFather va vous proposer une série d'options pour gérer votre bot. 
 * Dans le cas présent, nous allons en créer un avec la commande `/newbot`.
 	 * vous allez vite le voir : dans Telegram, les intercations avec les bots se font par "commandes" prédéfinies. Pour indiquer au bot qu'on lui envoie une commande, il faut utiliser ce caractère `/`
 * Donc l'échange avec BotFather devrait se dérouler comme ça : 
 	 * `/newbot`
 	 * `<le nom affiché que vous voulez donner à votre bot>`
 	 * `<l'identifiant de votre bot>`
 * La contrainte sur l'identifiant de votre bot est simple :
 	 * ne pas être déjà pris
 	 * finir avec 'bot'.
 * Si c'est bon, votre bot est créé ! 
 * Vous recevez alors un message contenant alors une chaine de caractères aléatoire. C'est votre clé API, gardez-là bien précieusement !
 * BotFather reste disponible pour vous aider à customiser votre bot avec différentes commandes pour changer sa description, sa photo, etc.

![Récupération de la clé API d'un nouveau bot](https://miro.medium.com/max/1400/1*5Ws-d5E_W_QMu4qQsLrGHA.jpeg)

# Configurer son bot

> Cette partie vise à expliquer comment créer le programme qui va interagir avec notre bot. Si vous êtes pressés, vous pouvez très bien sauter toute cette partie et récupérer uniquement le programme complet à la fin.

## Prérequis

Le programme que je vous propose pour interagir avec notre bot est écrit en Python. C'est un langage qui se comprend assez facilement, qui est courant et qui n'a pas besoin de compiler. Tout ça fait qu'il est très pratique pour des petits scripts comme notre bot.

Si vous ne l'avez pas déjà, il faut donc [installer Python](https://www.python.org/downloads/). Faites attention en installant : les versions Python2 et Python3 ne sont pas compatibles entre elles ! Ici, nous allons utiliser Python3 et pas Python2, parce qu'on est bientôt en 2021 et qu'on est pas des barbares quand même.

Pour que le programme soit court et simple à comprendre, il utilise des **bibliothèques**, c'est à dire des bouts de code que beaucoup de gens utilisent, et qu'on a mis en commun pour pas avoir tout à réécrire. Il faut donc installer les bibliothèques susnommées.

Pour gérer facilement ces bibliothèques de code, nous avons besoin de pip, que l'on peut [télécharger ici](https://pip.pypa.io/en/stable/installing/). Si vous venez de télécharger Python3, pip est inclus dedans par défaut. Pip est un gestionnaire de bibliothèques, c'est grâce à cet outil que ajouter, mettre à jour ou supprimer des bibliothèques se gère aussi simplement que des applications que l'on télécharge sur l'App Store ou le Play Store.

Enfin, il faut savoir que si vous utilisez Linux, certains composants sont écrits en Python. Donc modifier les bibliothèques installées peut mettre un peu le bazar si on sait pas faire. Pour éviter cela, nous allons utiliser un **environnement virtuel**. Cela permet de choisir la version exacte de Python, les bibliothèques installées etc. sans modifier directement ce qui est sur votre ordinateur. Pour cela, plusieurs solutions, je vous propose ici d'utiliser `python -m venv` mais vous faites comme vous voulez.

Une fois pip et virtualenv installés, nous pouvons revenir à notre bot !

## Préparer le code

Commençons par créer un dossier pour le bot et se rendre dedans avec la commande suivante si vous êtes sur Linux/MacOS : 

```bash
mkdir santabot/
cd santabot
```

Si vous êtes sur Windows, le plus simple c'est encore de créer un nouveau dossier et de l'ouvrir. Mais on va utiliser la ligne de commande à un moment ou un autre dans le tutoriel, donc vous pouvez déjà l'ouvrir en faisant `Windows`+`cmd` et `Entrée`. Là, vous pouvez naviguer dans vos dossiers en écrivant `cd <nom du dossier>` pour aller dans un dossier, `cd ..` pour revenir en arrière, et `dir` pour afficher ce qu'il y a dans un dossier. Comme vous pouvez le déduire des lignes précédentes, c'est sensiblement la même chose que sur Linux. La seule différence, c'est que sur Linux on liste les éléments d'un dossier avec `ls`, alors que sur Windows on le fait avec `dir`.

Maintenant, on va créer l'environnement virtuel comme prévu avec la commande suivante : 

```bash
python -m venv .
```

Puis on l'active avec pour Linux/MacOS :

```bash
source bin/activate
```

Puis, on va télécharger les bibliothèques dont je vous parlais avec Pip : 

```bash
pip install python-telegram-bot telethon configparser logging
```

Ensuite, on va créer un fichier **santabot.py** pour notre code. Là encore, vous pouvez utiliser la méthode de votre choix : si vous êtes à l'aise avec la ligne de commande c'est bien, mais un simple clic droit dans l'explorateur de fichiers -> nouveau fichier marche très bien.

Pour éditer le fichier, les adeptes de Linux seront déjà équipés de leur éditeur de texte préféré (vim/emacs/nano/gedit/atom/changer directement les bits sur le disque dur), mais sur Windows le Bloc-note (Notepad) marche très bien.

## Let's code ! 

> Disclaimer : Le but de ce tutoriel est d'arriver assez rapidement à un script qui marche, tout en comprenant ce que l'on a fait. Cela relève plus du script "quick & dirty" que du cours de code ! 

### Squelette du script

Ouvrez donc le fichier **santabot.py** créé et copiez-collez les lignes suivantes : 


<script src="https://gist.github.com/RduMarais/2c8a8f6179be3d65b5c53b5a807e31d9.js"></script>


Le début du fichier sert à indiquer à votre ordinateur comment lire ce fichier. Les quelques commentaires indiquent qu'il s'agit d'un logiciel libre et à quoi il sert. La fin du fichier contient la fonction `main()` que nous allons compléter, et une petite fonction qui indique à python qu'il faut exécuter la fonction main lorsqu'on exécute le script.

### Interagir avec le bot

Copiez le code suivant dans la fonction `main()`: 

<script src="https://gist.github.com/RduMarais/cf56b8d12a80fbcf2412cba074dc0ecb.js"></script>

Cette fonction crée un objet `updater`, qui est l'objet de la bibliothèque **telegram.ext** qui interagit avec le bot.

Les lignes `dp.add_handler()` ajoutent des fonctions au Bot. la syntaxe est assez simple : `dp.add_handler(CommandHandler("start", start))` indique que si le bot reçoit la commande `/start`, il faut lancer la fonction `start`. Charge à nous de la créer.

on va donc ajouter une section **FONCTIONS** à notre script avec les fonctions suivantes, juste au dessus de la section **MAIN**

<script src="https://gist.github.com/RduMarais/26e28c5aa449baf2770266a12c0599c5.js"></script>

Ces fonctions vont simplement envoyer le texte pré-enregistré lorsqu'on utilise ces commandes avec le bot.

A ce niveau-là, on peut tester d'échanger avec le bot pour le faire marcher. 

### Premier test

Avant de lancer le script, il nous faut deux choses : 

 * avoir un moyen d'obtenir des informations sur le fonctionnement du bot ;
 * s'identifier dans Telegram ; 

Pour ça, ajoutez début du script les lignes suivantes : 

<script src="https://gist.github.com/RduMarais/8752f0c7b70f58bc278089273c1219f3.js"></script>

Remplacez `""` dans la ligne API_KEY par votre propre clé, que vous avez obtenue de BotFather. 

Les premières lignes vont créer un objet `logger`, qui nous transmettras des informations sur l'état du bot. Vous pouvez ajouter pour plus de visibilité les lignes `logger.info("fonction help")` et `# logger.info("fonction start")`, cela vous indiquera si les fonctions ont bien été exécutées par le bot. 

>C'est une bonne habitude en général de gagner de la visibilité sur ce qui se passe dans le code quand on est en train de développer.

Le bot est prêt à être lancé une première fois ! Pour cela, revenez dans votre ligne de commande, et lancez la commande suivante : 
`python santabot.py`. Dans mon cas, j'ai un résultat comme ceci : 

<script src="https://gist.github.com/RduMarais/1aa29f0c6fa6a518cf8a11a91b7d8990.js"></script>

 * Le logger nous indique que le bot a bien démarré.
 * Telegram nous demande de nous authentifier avec notre numéro de téléphone et un code envoyé dans l'application.
 * Logiquement, Telegram nous envoie un message quelques secondes plus tard pour nous prévenir que quelqu'un s'est loggé sur notre compte.

**Pour l'arrêter :** Il faut appuyer dans la ligne de commande sur `Ctrl`+`C`. C'est un peu brutal en règle générale, mais là pas de soucis, c'est fait pour.

### J'ai une erreur, help !

Il se peut qu'il y ait des erreurs à résoudre, en particulier : `TabError: inconsistent use of tabs and spaces in indentation`. Cette erreur est courante lorsqu'on copie-colle du code depuis Internet. En fait, Python est un langage qui utilise l'indentation, c'est à dire la mise en forme des paragraphes, pour comprendre l'organisation du code. Pour qu'il puisse s'y retrouver, il faut utiliser soit des espaces, soit des tabulations pour la mise en forme. On peut corriger ça avec un simple `Ctrl`+`H` dans l'éditeur de texte (sauf raccourcis pathologiques\*). 

Si vous avez une autre erreur, les erreurs de Python sont généralement assez simples à corriger car elles vous indiquent la ligne où l'erreur a lieu et le type d'erreur (`SyntaxError`, `AttributError`, etc.). Une recherche sur Google résoud assez rapidement le problème. 

> **Avoir une erreur et chercher sur Google comment la résoudre, ce n'est pas un vrai problème, c'est le cycle naturel de l'écriture de code.** Tout le monde le fait, même des développeurs expérimentés ! Personne ne connait tout un langage et toutes les librairies par coeur. Donc pas de panique, c'est normal.

### Tester le Bot dans Telegram

On peut maintenant accéder au bot dans Telegram, et lui envoyer les commandes `/start`et `help`.

Vous constatez que le bot vous répond comme prévu.


### Améliorer le code

Avant de passer à la partie "ouverture d'une case d'un calendrier de l'avant", nous allons améliorer un peu le code. En particulier, nous allons : 

 1. ajouter un message d'erreur qui récupère toutes les commandes que le bot n'a pas compris.
 2. utiliser un fichier de configuration ;

Pour ajouter un message d'erreur, il suffit de décommenter, c'est à dire enlever le caractère `#` de la ligne :

<script src="https://gist.github.com/RduMarais/a36b4fc25a87dc8dc777801240a248cc.js"></script>

de la fonction `main()`. Ce que fait cette ligne, c'est qu'elle appelle une fonction `erreur()` si le Bot ne comprend pas le texte qu'on lui envoie.

Il faut donc ajouter la fonction `erreur()` suivante à vos fonctions : 

<script src="https://gist.github.com/RduMarais/88f61efa129225fc9d3d2c65bb1be84d.js"></script>

Maintenant, vous avez peut-être envie de changer certains textes renvoyés par le bot. Pour cela, il suffit de le changer directement dans le code. En règle générale, devoir modifier le code pour pouvoir changer quelque chose d'accessoire, comme du texte, ce n'est pas une bonne idée (on dit que ce texte est _hard codé_). Donc nous allons mettre tout le texte dans un fichier à part, et notre code ira lire ce fichier. De cette manière, si vous décidez de changer la langue du bot, il suffira de modifier le fichier de texte.

Un autre avantage est que la clé API du bot ne se retrouve pas dans le texte du code. Si vous voulez partager ce code, comme je l'ai fait sur [GitHub](https://github.com/RduMarais/santelegram) il ne faut pas que vous donniez au monde entier accès à votre bot.

Donc nous allons pour cela créer un fichier **config.ini**, qui devrait ressembler à : 

<script src="https://gist.github.com/RduMarais/c899505bd4c1af2254bd0026cb7bf149.js"></script>

Nous allons utiliser le module `configparser` pour lire les données qui sont dedans. Ajoutez la fonction suivante à la section "VARIABLES GLOBALES".

<script src="https://gist.github.com/RduMarais/231abe4295a41b9826963e15a713f6ae.js"></script>

Ce que fait cette fonction, c'est qu'elle lit la partie _API_ dans le fichier de configuration. Les deux variables `API_KEY` et `CONVS` sont maintenant définies pour tout le script. On reviendra sur les variables `START_TIME` et `STOP_TIME` dans un instant

On va ajouter cette fonction en haut de la section "FONCTIONS" : 

<script src="https://gist.github.com/RduMarais/69c1c2301c944be954c6bd3d81847d85.js"></script>

> Vous noterez que j'ai ajouté un appel à `logger`. C'est un bon endroit pour le faire, parce que savoir quelles sont les valeurs lues va nous apporter des infos sur l'interaction avec le fichier de conf, mais aussi les appels de fonctions faits par le bot.

On peut maintenant remplacer les éléments codés en dur par ceux qui sont dans notre fichier de configuration : 

<script src="https://gist.github.com/RduMarais/e1b2d4de82c72fd7485b6bb48bc45210.js"></script>

Et voilà notre script bien propre et modulaire. Ainsi, si on veut réutiliser le bot, le changer, etc : tous les changement se feront à un seul endroit.

> Vous pouvez re-tester le bot maintenant pour vérifier que tout marche bien.

### Ouvrir une case.

Nous allons maintenant créer une fonction en plus, qui a pour vocation de donner un message lu dans le fichier de conversation, uniquement si :
 * le moment est le bon ;
 * l'utilisateur est un utilisateur choisi au hasard dans le fichier de config ; 
 * Le chat dans lequel le message envoyé est le bon.

Commençons par définir dans la section "FONCTIONS" une fonction pour savoir si le moment est le bon.

<script src="https://gist.github.com/RduMarais/d2eceb28f53b3f0975ff43b09fac26df.js"></script>

Vous remarquez que cette fonction utilise des variables globales `MONTH`, `START_TIME`, `STOP_TIME` et `DEBUG` qu'on a déjà défini plus haut, dans le fichier de configuration et directement dans le script. `MONTH` et `DEBUG` ont vocation à seulement nous aider durant le développement, d'où leur présence directement dans le script.

> J'attire votre attention sur le fait que le script utilise l'heure vue par le bot, cad l'heure GMT. Donc il faut mettre `<l'heure voulue> -1` (en hiver) dans le fichier de configuration.

Ensuite nous allons ajouter les messages dans le fichier de config, dans une section avec le nom du groupe.

<script src="https://gist.github.com/RduMarais/ef820efcfbac53336a0ac22d766c253a.js"></script>

Contrairement à précédemment, cette variable est un tableau. Ici, j'utilise le format JSON, un format rudement pratique pour stocker des données complexes. Concrètement, cela veut dire que lorsque mon script cherche le fichier messages, il charge un objet qui a 25 cases. Je vous laisse deviner à quoi correspondent chacune des cases. 

Dans l'objet **messages**, on va donc stocker les messages à afficher. Pour que ce soit plus sympa, je le stocke comme un autre tableau (dans un tableau, oui) comme ça mon bot enverra plusieurs lignes. Par exemple, un meme et une citation plus sérieuse par jour.

Dans l'objet **users**, on va stocker de la même manière un tableau avec 25 cases. Chaque case contient l'identifiant de l'utilisateur qui peut ouvrir la case aujourd'hui. De même, chaque case du tableau est elle-même un tableau, ce qui permet de définir plusieurs utilisateurs. Par exemple, une des conversations sur laquelle j'utilise ce bot a une centaine d'utilisateurs qui ne sont pas toujours connectés. Je ne veux pas que le bot soit bloqué parce que l'unique personne qui peut l'ouvrir aujourd'hui a oublié de se connecter !

> Mais - vous allez me demander, tout perspicaces que vous êtes - comment récupérer les identifiants d'utilisateurs ? Et bien c'est une excellente question !

Pour l'instant, on peut remarquer que lorsque on envoie un message au bot, le bot reçoit une `update` de cette forme : 

<script src="https://gist.github.com/RduMarais/83aa97bd40f478eebfa5c8b49a1daf49.js"></script>

En ajoutant `logger.info("update : "+str(update))` à n'importe quelle fonction, vous verrez ainsi votre propre id d'utilisateur et/ou de groupe avec lequel vous testez ce bot. Pour récupérer ceux du groupe dans lequel vous comptez utiliser le bot, ce sera l'objet d'une partie suivante. En attendant, utilisez donc dans l'objet **users** votre `user_id` qui est à l'endroit de `'<sender_user_id>'`. 

Notez également votre `chat_id` qui est à l'endroit de `'<chat_id>'`. Ajoutez-le tout en haut du fichier de configuration à l'objet `conversations = {}`, pour avoir quelque chose comme : 

```
conversations = {"<chat_id>":"MACONV"}
```

Cette ligne vous permet d'utiliser votre bot sur plusieurs groupes différents. Pour chaque groupe donc l'ID est spécifié ici, le script ira chercher des messages et utilisateurs différents.

Il ne reste donc plus qu'à ajouter la fonction `open()` suivante à votre script : 

<script src="https://gist.github.com/RduMarais/4df6aba01560648c6dff34c02caff0e5.js"></script>

Enfin, ajoutons au bot la commande `/open` en décommentant de la fonction `main()` la ligne suivante : 

```python
dp.add_handler(CommandHandler("open", open))
```

> **Félicitations, votre bot est prêt !** Vous pouvez le tester sur la conversation de votre choix.

# Le résultat

> Si vous êtes venus juste pour avoir le Bot en moins de 10 minutes, voici le code à copier-coller sur votre serveur/PC.
>
>Sinon, voici à quoi devrait ressembler le code que vous avez patiemment créé.

<script src="https://emgithub.com/embed.js?target=https%3A%2F%2Fgithub.com%2FRduMarais%2Fsantelegram%2Fblob%2Fmaster%2Fsantabot.py&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on"></script>

Vous devriez aussi avoir le fichier **config.ini** suivant : 

<script src="https://emgithub.com/embed.js?target=https%3A%2F%2Fgithub.com%2FRduMarais%2Fsantelegram%2Fblob%2Fmaster%2Fconfig_example.ini&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on"></script>


 * Pour le lancer : `python3 santabot_pool.py`
 * Pour l'arrêter : `Ctrl`+`C`


# Obtenir les userid et le chat ID de vos amis

Si vous avez suivi tout le tutoriel, vous voyez bien que le seul moyen d'avoir le `user_id` de tout le monde sur le chat et le `chat_id` dudit chat, c'est que tout le monde envoie un message au chat. C'est un peu fastidieux, et surtout si vous voulez faire une surprise, c'est raté.

Heureusement, il y a un moyen de le faire "rapidement" avec 5 min de code supplémentaires.

Pour cela, il faut accéder à Télégram ligne de commande avec l'[API de Telegram](https://core.telegram.org/api#telegram-api). C'est comme l'API des bots, sauf que cette fois, c'est pas le bot que vous pilotez, mais votre propre compte !

### Obtenir votre clé API

Rendez-vous à l'adresse https://my.telegram.org/ et remplissez le questionnaire pour créer un App. Vous pouvez dire ce que vous voulez, mais le plus simple reste de dire que vous faites un bot de Noël.

Vous allez arriver à un écran avec vos clés perso. 

> **Ne les donnez à personne, c'est un accès direct à votre compte Telegram !!!** 


### Obtenir tous les groupes dont vous êtes membre

Copiez-collez le code suivant dans un fichier **telethon_get_users.py** : 

<script src="https://gist.github.com/RduMarais/6c29e5dcbd857a601afb6a208e81cb86.js"></script>

lancez ce script avec `python telethon_get_users.py`

Ce code va vous afficher la liste de vos groupes. 

Puis créez un objet `group_array` avec tous les groupes dans lesquels vous voulez utiliser le bot, et ajoutez la boucle `for` comme ci-dessous : 

<script src="https://gist.github.com/RduMarais/15e230648c0ce3606d37d1c436305824.js"></script>

Et voilà, plus qu'à noter tous les `user_id`s, et le `group_id` qui vous intéressent, et les utiliser pour remplir votre fichier de config.

# Dernier petit tip

Pour tirer aléatoirement au sort qui ouvrira les cases du calendrier, j'ai utilisé le script suivant : 

 * D'abord, faire un tableau de la forme `[<userid1>,<userid2>]` de tous les utilisateurs du chat.
 * Puis faire en ligne de commande : `python` pour accéder à la console de python. 
 * recopier ligne par ligne : 

<script src="https://gist.github.com/RduMarais/60a40d5fae8ffc63fcc16ea6c0ba67eb.js"></script>

Et pour avoir plusieurs personnes par jour : 

<script src="https://gist.github.com/RduMarais/ac2dc45651847c2804b0b68d300eb074.js"></script>

> J'espère que ce petit tuto vous a plu, profitez des fêtes et prenez soin de vos proches !
>
> Peace

# Notes

 * \* I am looking at you, VIM & Emacs
 * N'oubliez pas de supprimer le bot du groupe à la fin du mois de décembre ! C'est une mauvaise pratique de laisser des systèmes informatiques en place lorsqu'on ne les utilise plus. Comme les objets de la vie quotidienne, ils ont un cycle de vie qui a un début, mais aussi une fin, et il ne faut pas la négliger. Très souvent les vulnérabilités informatiques viennent de vieux accès qu'on a oublié de fermer ou de vieux systèmes qu'on a oublié de débrancher.
 * pour déployer le bot, j'utilise un serveur. Je copie le script avec la commande `scp`, je lance un `screen`, dans lequel j'active mon environnement virtuel et je lance mon script. Je peux quitter le `screen` et le serveur tranquille, le script tournera tranquillement.
 * Une fonction sympa serait de permettre aux utilisateurs d'envoyer leurs messages pour les autres. Mais cela signifie avoir du texte envoyé par un utilisateur qui arrive dans un script sur mon serveur. Autrement dit, il faut que je m'assure avant qu'on ne peut pas injecter de code sur mon serveur (et connaissant mes copains/collègues, je sais qu'ils vont essayer...). Tant que je ne maîtrise pas bien les mécanismes de sécurité des bots Telegram, j'évite. 

# La doc : 

 * API de Telegram : https://core.telegram.org/api#telegram-api
 * Telethon : https://github.com/LonamiWebs/Telethon/
 * choper les IDs : https://stackoverflow.com/questions/33844290/how-to-get-telegram-channel-users-list-with-telegram-bot-api
 * API python : https://python-telegram-bot.readthedocs.io/en/stable/telegram.chat.html#telegram.Chat
 * récupérer le chat ID : https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android ou https://www.wikihow.com/Know-a-Chat-ID-on-Telegram-on-PC-or-Mac

