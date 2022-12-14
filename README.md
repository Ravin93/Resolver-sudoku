# Resolver-sudoku
Consigne : 
  Le projet est à effectuer seul ou en groupe de deux maximum. Il y a deux problèmes à résoudre ainsi que vos propres tests à écrire cette fois ci.

  Ces problèmes sont assez ouverts et possèdent plein de solutions.

  Le premier exercice est bien plus facile que le second, il est recommandé de les faire ensemble si vous êtes deux. Ne vous séparez pas le travail. Le premier exercice vous aidera à être plus à l’aise sur le second.

  Vous avez le droit d’utiliser les opérations python de votre choix pour ce projet, mais il n’est pas nécéssaire d’utiliser plus que des boucles et des tableaux.

  Exercice 1: Vérifier une grille de sudoku
  Vous devez compléter l’algorithme dans le fichier grille_valide.py qui permettra de vérifier qu’une grille 9x9 de sudoku passée en paramètre est valide.

  Pour rappel, une grille de sudoku est valide si:

  Chaque ligne contient tous les chiffres de 1 à 9 sans répétitions.
  Chaque colonne contient tous les chiffres de 1 à 9 sans répétitions.
  Chaque carré de 3 par 3 contient tous les chiffres de 1 à 9 sans répétitions.
  Votre algorithme doit seulement vérifier que la disposition de la grille passée est correcte, il n’est pas nécéssaire de vérifier s’il existe une solution (ce sera pour l’exercice 2 ça).

  Les grilles sont représentées par un tableau à deux dimensions de chaines de caractères. Les cases vides sont représentées par des points et les chiffres par les caractères de 1 à 9. Les grilles se lisent de gauche à droite et de haut en bas.

  Exemples de grille
  Dans cette grille, la première ligne contient les chiffres 1, 3, 2 et possède 6 cases vides.

  La troisième colonne contient les valeurs 1, 7, 6, 9, 4, 2 et possède 3 cases vides.

  grille_facile = [
      [".", ".", "1", "3", ".", "2", ".", ".", "."],
      [".", ".", ".", "8", "1", ".", ".", "4", "2"],
      [".", "9", ".", ".", ".", ".", "3", ".", "."],
      ["3", ".", "7", "6", "9", "8", "1", "2", "."],
      ["1", ".", "6", "2", ".", "5", "4", "7", "9"],
      ["5", ".", "9", ".", "4", ".", ".", ".", "."],
      [".", "1", ".", ".", ".", "6", ".", "9", "3"],
      [".", "6", "4", ".", ".", ".", "2", "5", "."],
      [".", ".", "2", ".", "8", ".", ".", ".", "."]
  ]
  grille_vide = [
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."]
  ]
  Si vous voulez créer vos propres grilles, rendez vous sur https://sudoku.com/ et générez des plateaux que vous pouvez recopier ensuite dans votre code

  Indices pour la résolution
  Pour cet algorithme, ne vous compliquez pas la vie. La solution intuitive de vérifier toutes les contraintes fonctionne. Le plus dur dans cet exercice est l’écriture du code et la manipulation des tableaux à deux dimensions.
  Si votre code devient trop long et ilisible, vous avez le droit de créer vos propres fonctions pour organiser votre code. Si vous ne savez pas faire, vous pouvez toujours me demander sur Teams ou voir avec vos camarades.
  Vous aurez surement besoin des opérateurs in et not in de python pour vous simplifier la vie dans ce problème. Voici un tutoriel en anglais qui est bien (les tutos en français sont vraiment naze) https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
  Exercice 2: Résoudre une grille de sudoku
  Vous devez compléter l’algorithme dans le fichier resoudre_sudoku.py afin qu’il complète une grille de sudoku passée en paramètre avec la bonne solution et la retourne. La grille est passée via un tableau à deux dimensions sous le même format que l’exercice précédent.

  Le but est de compléter toutes les cases vide qui sont représentée par le caractère “.”

  Vous pouvez modifier le tableau passé en paramètre directement, pas besoin de le copier.
  Votre algorithme n’a pas besoin de gérer les grilles invalides. Vous supposerez que toutes les grilles envoyées possèdent une solution.
  Indices pour la résolution
  Il n’est pas nécéssaire de réutiliser l’algorithme de l’exercice 1 pour résoudre ce problème. Vous pouvez récupérer certains bouts de code qui seront utiles cependant.
  Je vous conseille de commencer par écrire un test. Prenez une grille facile ainsi que sa solution, et testez votre algorithme dessus pour voir si vous vous rapprochez de la bonne solution.
  Si vous essayez de résoudre ce problème de la même manière que vous résolvez un sudoku “à la main”, vous n’allez pas réussir. La solution algorithmique est très différente de la méthode qu’un humain va utiliser.
  S’il vous vient à l’esprit l’idée de “tester toutes les combinaisons possibles jusqu’à trouver une disposition qui fonctionne”, ce n’est pas une si mauvaise idée. Le temps d’exécution de votre algorithme sera très élevé, mais une des solution optimale repose sur ce principe. Comment pouvez vous améliorer cette idée en exploitant les contraintes du sudoku ?
  Sur ce genre de problème, le nombre de cases vides d’une grille peut augmenter de manière exponentielle le temps d’exécution. Si votre algorithme n’est pas performant, il se peut qu’il ne termine jamais. Commencez par tester sur une grille avec peu de cases vides au début, afin de ne pas vous soucier trop de la performance. Utilisez des grilles plus complexes par la suite.
  
  
  
 Avis personel : 
   J'ai eu la chance de effectuer cette excercie avec Engels Lou car on avais pas même vision pour resoudre cette algo mais ces idées m'on permis de voir de nouvelle angle.
   C'est un excercice assez simple mais qui demande pas mal de reflection.
   J'ai pas mal bloquer sur la verification du 3x3 car on devais pas mal jouer avec les boucles for. 
   
