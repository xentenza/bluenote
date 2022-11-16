# Visualiser un réseau d’instrumentistes au sein d’un label: l’exemple Blue Note (1939 - 2007)

## Introduction

Qui s’est déjà aventuré dans les crédits des albums de jazz aura certainement eu l’impression que les musiciennes et musiciens semblent naviguer plus facilement que dans d’autres genres de musique d’un ensemble musical à un autre.

Cette grande perméabilité a déjà fait l’objet de plusieurs recherches dans le domaine des humanités digitales. Nous pouvons entre autres citer le projet [LinkedJazz](https://linkedjazz.org/) du Pratt Institute School of Library Information Science, à New York, ou encore le projet [Map of Jazz](http://rainforest.compbio.cs.cmu.edu/) de University of Maryland, University of the District of Columbia et American University - Washington.

A ma connaissance, aucun travail ne s’est concentré sur l’analyse de réseaux au sein d’un seul et même label. L’objectif initial de ce travail était de vérifier, via des outils de visualisation, si un réseau plutôt dense de musiciennes et musiciens se dessine ou si, au contraire, il existe de nombreux silos.

Au moment d’écrire ces lignes, les fichiers regroupent 4’241 musiciennes et musiciens, 12’597 morceaux, pour un total de 308’939 liens.

_Le projet a été initié en 2013 et est actuellement à l’arrêt pour diverses raisons personnelles et professionnelles._

## Méthodologie

Afin de constituer ce réseau de musiciennes et musiciens chez Blue Note, je me suis focalisé sur les morceaux enregistrés au sein du label. Le premier objectif était de constituer un tableau regroupant une liste des pistes, et les interprètes jouant sur chacun d’entre eux. Si l’unité de base a été le morceau au lieu des sessions, comme cela est généralement fait dans d’autres travaux ou dans les discussions entre amatrices et amateurs du genre, c’est que celles-ci sont moins bien documentées à partir d’une certaine période. 

Cette liste d’interprètes a été réalisée principalement en se basant sur de la documentation trouvée en ligne. Deux sites ont servi de ressources principales: le premier est [Discogs.com](https://www.discogs.com), base de données collaborative; le second est [Jazzdisco.org](https://www.jazzdisco.org), géré par Nobuaki Togashi, Kohji 'Shaolin' Matsubayashi et Masayuki Hatta. Les informations manquantes ont été complétées en consultant d’autres sites comme par exemple d’autres bases de données en ligne, les sites web des artistes, mais également en épluchant des articles de presse, en recherchant des photos des 4e de couverture des albums, ainsi qu’en me basant sur des collections physiques (cédéthèque de la Bibliothèque universitaire de Lausanne, collection personnelle, etc).

Naturellement, l’impossibilité d’accéder à l’entier du catalogue physique de Blue Note et se baser sur des ressources secondaires implique deux choses: certaines informations figurant dans mes fichiers peuvent être erronées, soit parce que les sites servant de base à ce travail contenaient des fautes (certaines ont été identifiées en recoupant les ressources), soit parce que des erreurs de frappe ont eu lieu lors de la saisie. Pour certains disques, il n’a malheureusement pas été possible de trouver plus de détails mis à part le nom de l’album, l’interprète principal et le numéro de catalogue. C’est dans ce but que l’intégralité des données est mise à disposition sur GitHub: encourager des internautes à faire des pull requests et apporter des corrections.

Les informations ont été entièrement collectées à la main. Vu les ressources consultées, automatiser ce travail avec R par exemple aurait été difficile, voire impossible. La nomenclature des musiciennes et musiciens jouant sur chacun des enregistrements varie d’un site à l’autre, voire d’un disque à l’autre sur le même site. Un travail d’OCR sur les pochettes s’avèrerait également compliqué.

Les données collectées ont été en partie nettoyées lors de la saisie, afin de corriger certaines fautes de frappe dans les noms des artistes, mais également pour uniformiser les noms d’artistes crédités parfois sous leur vrai nom, parfois avec leur diminutif, et parfois avec leur nom d’artiste. La liste des modifications effectuées est listée dans le fichier [modifications.md](https://github.com/xentenza/bluenote/blob/master/modifications.md). Comme cette analyse de réseau se concentre sur les instrumentistes, les personnes accréditées sur les albums et occupant des fonctions comme arrangeurs, producteurs ou encore les directeurs. Peu d’homonymes ont été détectés.

Le tableau bn-data.csv contient les informations suivantes:
* Track: Le nom du morceau
* Alternate take: Une autre prise d’un morceau déjà publié
* Catalog: Certains numéros de catalogue des morceaux. Sert avant-tout de référence pour contrôler la source des infos.
* Recorded: Année d’enregistrement du morceau
* 1st BN Releasee: Année de la première publication du morceau
* Status: Morceau publié ou non
* autres colonnes: Noms des interprètes

Un script créé avec Python permet de générer les *nodes* et les *edges* et constituer un réseau de musiciennes et musiciens. Il parcourt le document ligne après ligne en générant les différentes combinaisons possibles d’instrumentistes, jusqu’à se heurter à une cellule vide. Parallèlement, le script génère une base de données des personnes rencontrées dans le tableau, et leur assigne un identifiant unique.

Les visualisations accompagnant ce travail ont ensuite été réalisées avec Gephi.

## Résultats

_N/A_

### Fichiers

* Raw data: [bn-data.csv](https://github.com/xentenza/bluenote/blob/main/bn-data.csv)
* Edges: [edges.csv](https://github.com/xentenza/bluenote/blob/master/edges.csv)
* Nodes: [nodes.csv](https://github.com/xentenza/bluenote/blob/master/nodes.csv)

## Discussion

_N/A_
