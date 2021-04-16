# P29_langage_signes_alphabet

*Aude, Ronan, Ludivine*

## Le projet

Le challenge ici consiste à reconnaître l'alphabet de la langue des signes françaises en direct sur une vidéo. Les différentes lettres de l'alphabet sont signées avec la main droites, face caméra.

Pour répondre à différentes contraintes de luminosité, de distance par rapport à la caméra, de background (couleur des vêtements, présence de mances sur les vêtements, etc.), nous avons choisi de procéder en deux temps :
- d'abord, détecter et extraire l'image de la main dans la vidéo, 
- ensuite, classifier l'image extraite pour reconnaître le signe effectué.

## Méthodologie

Pour la détection de la main dans l'image, nous avons fait un premier essai avec Tensorflow Detection API et le modèle EfficientDet-d0 préentrainé sur le dataset Coco.<br> 
Les résultats de ce transfert d'apprentissage étant très décevants, nous avons décidé d'utiliser un module de détection des mains existant issu de la bibliothèque [Mediapipe](https://mediapipe.dev/) développée par Google. Ce module, [Mediapipe Hands](https://google.github.io/mediapipe/solutions/hands), est entraîné à inférer d'une image 21 points 3D situés à des endroits stratégiques de la main (phalanges, base du poignet, etc.).<br>

Une possibilité pour réaliser la classification aurait été d'exploiter les coordonnées relatives de ces 21 points. Ce travail ayant déjà été réalisé par d'autres groupes avant nous, nous avons préféré construire un modèle différent afin de pouvoir comparer les résultats.<br>
Notre reconnaissance des signes se base donc sur un CNN de classification d'images. Il est entraîné dans le [notebook 02](02_classification_signes.ipynb).

## Dataset

Les circonstances particulières dans lesquelles a été réalisé ce travail ont posé quelques limites pour la construction du dataset d'entraînement.

Si les premiers essais avec Tensorflow Detection API ont pu être réalisés sur le dataset commun à l'ensemble de la classe, nous avons par la suite perdu l'accès aus données. <br>
Nous avons donc du reconstruire rapidement, pour l'entrainement du modèle présenté, un dataset en local. Si le dataset final est peu fourni et peu diversifié, le code développé pour cette mise en place peut néanmoins être réexploité pour construire un dataset dense et de qualité. <br>

Le [notebook 01](01_capture_webcam.ipynb) présente la façon dont on peut prendre et enregistrer de photos via la webcam, soit en cascade, soit en appuyant sur une touche du clavier.


## Résultats

Si les résultats de la détection avec Médiapipe sont exellents (on peut observer ces résultats en lançant la détection vidéo du [notebook 03](03_reconnaissance_signes_video.ipynb)), notre modèle de classification souffre de la médiocrité du dataset utilisé. Nous avons tenté de réduire le nombre de classes détectées à 7 (les lettres de "LEARNING"), mais les résultats restent médiocres.

__Il est nécessaire de réentrainer le modèle sur un dataset plus consistant afin d'optenir de réels résultats__



blablablabla
