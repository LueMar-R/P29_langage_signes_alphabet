# P29_langage_signes_alphabet

*Aude, Ronan, Ludivine*

## Le projet

Le challenge ici consiste à reconnaître l'alphabet de la langue des signes françaises en direct sur une vidéo. Les différentes lettres de l'alphabet sont signées avec la main droites, face caméra.

Pour répondre à différentes contraintes de luminosité, de distance par rapport à la caméra, de background (couleur des vêtements, présence de mances sur les vêtements, etc.), nous avons choisi de procéder en deux temps :
- d'abord, détecter et extraire l'image de la main dans la vidéo, 
- ensuite, classifier l'image extraite pour reconnaître le signe effectué.

## Méthodologie

Pour ce qui est de la classification, nous avons entrainé un modèle de reconnaissance d'images avec un classificateur linéaire de type perceptron multi-couches (MLP-classifier). Ce modèle donne d'excellents résultats sur notre base de données de test.

Pour la détection de la main dans l'image, nous avons fait un premier essai avec Tensorflow Detection API et le modèle EfficientDet-d0 préentrainé sur le dataset Coco.<br> 
Les résultats de ce transfert d'apprentissage étant très décevants, nous avons décidé d'utiliser un module de détection des mains existant issu de la bibliothèque [Mediapipe](https://mediapipe.dev/) développée par Google. Ce module, [Mediapipe Hands](https://google.github.io/mediapipe/solutions/hands), est entraîné à inférer d'une image 21 points 3D situés à des endroits stratégiques de la main (phalanges, base du poignet, etc.)
