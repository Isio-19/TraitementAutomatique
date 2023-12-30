
# TP1

## Création du dictionnaire

J'ouvre chaque fichier à la suite (twitter-2013train-A.txt, twitter-2013dev-A.txt et twitter-2013test-A.txt).
Pour chaque ligne de chaque fichier, je vais:
- Trouver les mots de chaque ligne avec le séparateur " "
- Filtrer et transformer mes mots selon mes filtres (stopwords, présence de liens, de majuscules, des hashtag ou de mentions, la ponctuation)

Pour chaque mot:
- Si le mot n'est pas dans mon dictionnaire, je l'y ajoute
- J'associe un ID à ce mot

## Création du svm

Une fois que j'ai mon dictionnaire de mots, je vais créer mes SVM pour chaque fichier.
J'ouvre chacun de mes fichiers et pour chaque ligne (tweet) du fichier ouvert, je vais:
- Ajouter à une string le sentiment du tweet;
- Compter le nombre de fois chaque mots uniques apparaissent dans la ligne;
- Dans l'ordre des ID des mots, ajouter l'ID du mots suivi par le nombre de fois qu'il apparait dans la ligne.
- Ajouter cette string dans une liste de string

Une fois que j'ai traité toutes les lignes d'un fichier, je récupère cette liste de string et je créer un fichier svm qui correspond à cette liste (au fichier).

<div style="page-break-after: always;"></div>

## Test 

Après avoir créer mes fichiers SVM, j'ai entrainé un modèle sur train.svm et je l'ai testé sur test.svm.
Après avoir testé plusieurs combinaisons de filtres (non exhaustives), voici les résultats de précisions de prédictions de sentiments des tweets:

> Filtering stopwords, links, caps, #, @, punc, empty:    61.0093% <br>
> Filtering stopwords, links, caps, #, @, punc:           60.7274% <br>
> Filtering stopwords, links, caps, #, @,       empty:    61.2067% <br>
> Filtering stopwords, links, caps, #,    punc, empty:    61.263%  <br>
> Filtering stopwords, links, caps,    @, punc, empty:    61.404%  <br>
> Filtering stopwords, links,       #, @, punc, empty:    60.7556% <br>
> Filtering stopwords,        caps, #, @, punc, empty:    61.3758% <br>
> Filtering            links, caps, #, @, punc, empty:    61.0093% <br>
> ---------------------------------------------------------------- <br>
> Filtering stopwords:                                    61.2912% <br>
> Filtering links:                                        61.263%  <br>
> Filtering caps:                                         62.2216% <br>
> Filtering hash:                                         61.0939% <br>
> Filtering at:                                           60.8965% <br>
> Filtering punc:                                         61.5168% <br>
> Filtering empty:                                        61.2067% <br>
> Filtering nothing:                                      61.2912% <br>
> ---------------------------------------------------------------- <br>
> Filtering stopwords and punc:                           61.5168% <br>

Dans mes tests de combinaisons, il semble que la combinaison de filtres qui donne la plus grande précision de prédiction de tweet est lorsque nous filtrons seulement les lettres majuscules (transformation des lettres majuscules en miniscules).

## Améliorations possibles

N'ayant pas utiliser le fichier dev.svm, il est possible que j'obtienne de meilleurs résultats en changeant les méta-paramètres de mon modèle.

<div style="page-break-after: always;"></div>

# TP2

## Codage et apprentissage du modèle

Après avoir repris mon programme python du TP1, j'y rajoute un réseaux de neurones et une classe pour qui a pour objectif de créer une liste de tensor qui aura une structure similaire à la liste de tweet du TP1.
J'ai aussi modifier quelques unes de mes fonctions: 
- Lorsque je créer les fichiers SVM, puisque nous utilisons seulement le fichier twitter-2013train-A.txt pour créer le dictionnaire, si un mot apparait dans un autre fichier mais pas dans le dictionnaire, on saute ce mot.

## Test du modèle

Une fois le modèle appris, j'ai créer une fonction qui vérifie les labels prédis avec les labels réels.

Pour chacun des tests, j'ai entrainer le modèle puis tester le modèle et je répète cela 4 fois de plus (5 en total).

Avec les paramètres par défaut (2 couches cachées et 512 neuronnes par couches cachées), j'obtiens une précision d'environ 72.54%
Avec 256 neurones sur la première couche cachée, j'obtiens une précision d'environ 70.06%
Avec 256 neurones sur la deuxième couche cachée, j'obtiens une précision d'environ 72.85%
Avec 256 neurones sur les deux couches cachées, j'obtiens une précision d'environ 71.89%
Avec 1024 neurones sur la première couche cachée, j'obtiens une précision d'environ 72.06%
Avec 1024 neurones sur la deuxième couche cachée, j'obtiens une précision d'environ 70.82%
Avec 1024 neurones sur les deux couches cachées, j'obtiens une précision d'environ 72.37%

Avec une seule couche cachée de 256 neuronnes, j'obtiens une précision d'environ 73.56%
Avec une seule couche cachée de 512 neuronnes, j'obtiens une précision d'environ 73.50%
Avec une seule couche cachée de 1024 neuronnes, j'obtiens une précision d'environ 73.67%
Avec une seule couche cachée de 2048 neuronnes, j'obtiens une précision d'environ 73.08%

Avec trois couches cachée de 512 neuronnes, j'obtiens une précision d'environ 67.80%
Avec 1024 neurones sur la première couche cachée, j'obtiens une précision d'environ 62.93%
Avec 1024 neurones sur la deuxième couche cachée, j'obtiens une précision d'environ 67.83%
Avec 1024 neurones sur la troisième couche cachée, j'obtiens une précision d'environ 67.32%
Avec 1024 neurones sur la première et deuxième couches cachées, j'obtiens une précision d'environ 67.24%
Avec 1024 neurones sur la première et troisième couches cachées, j'obtiens une précision d'environ 64.11%
Avec 1024 neurones sur la deuxième et troisième couches cachées, j'obtiens une précision d'environ 70.34%
Avec 1024 neurones sur les trois couches cachées, j'obtiens une précision d'environ 70.31%

Avec 256 neurones sur la première couche cachée, j'obtiens une précision d'environ 66.82%
Avec 256 neurones sur la deuxième couche cachée, j'obtiens une précision d'environ 69.55%
Avec 256 neurones sur la troisième couche cachée, j'obtiens une précision d'environ 68.90%
Avec 256 neurones sur la première et deuxième couches cachées, j'obtiens une précision d'environ 68.93%
Avec 256 neurones sur la première et troisième couches cachées, j'obtiens une précision d'environ 70.20%
Avec 256 neurones sur la deuxième et troisième couches cachées, j'obtiens une précision d'environ 69.75%
Avec 256 neurones sur les trois couches cachées, j'obtiens une précision d'environ 68.31%

Parmis les combinaisons de couches et de nombre de neurones que j'ai entrainé, une seule couche cachée avec 1024 neurones semble donner les meilleurs résultats.

## Matrice de confusion pour le modèle avec les meilleurs résultats

Matrice de confusion pour un modèle avec une couche cachée de 1024 neuronnes:

|                  | Classes réelles | <               | <             | <             | <              |
| Classes prédites /                 /   Neutre ( 0 )  / Positif ( 1 ) / Négatif ( 2 ) / Total          |
| ^                |   Neutre ( 0 )  / 1425            | 304           | 363           | 2092 (58.98%)  |
| ^                |  Positif ( 1 )  / 88              | 1171          | 196           | 1455 (41.02%)  |
| ^                |  Négatif ( 2 )  / 0               | 0             | 0             | 0    (0.00%)   |
| ^                |      Total      / 1513 (42.66%)   | 1475 (41.58%) | 559 (15.76%)  | 3547 (100.00%) |
|------------------/-----------------/-----------------/---------------/---------------/----------------|

<table>
    <tr>
        <td></td>
        <td colspan="5" style="text-align: center;">Classes réelles</td>
    </tr>
    <tr>
        <td rowspan="5">Classes prédites</td>
        <td></td>
        <td>Neutre (0)</td>
        <td>Positif (1)</td>
        <td>Négatif (2)</td>
        <td>Total</td>
    </tr>
    <tr>
        <td>Neutre (0)</td>
        <td> 1425 </td>
        <td> 304 </td>
        <td> 363 </td>
        <td> 2092 (58.98%) </td>
    </tr>
    <tr>
        <td>Positif (1)</td>
        <td> 88 </td>
        <td> 1171 </td>
        <td> 196 </td>
        <td> 1455 (41.02%) </td>
    </tr>
    <tr>
        <td>Négatif (2)</td>
        <td> 0 </td>
        <td> 0 </td>
        <td> 0 </td>
        <td> 0 (0.00%) </td>
    </tr>
    <tr>
        <td>Total</td>
        <td> 1513 (42.66%) </td>
        <td> 1475 (41.58%) </td>
        <td> 559 (15.76%) </td>
        <td> 3547 (100.00%)</td>
    </tr>
</table>

<div style="page-break-after: always;"></div>

# TP3

## 3 - Apprendre un modèle word2vec

Parameters for training:
- -train \<file\> <br>
        Use text data from \<file\> to train the model
- -output \<file\> <br>
        Use \<file\> to save the resulting word vectors / word clusters
- -size \<int\> <br>
        Set size of word vectors; default is 100
- -window \<int\> <br>
        Set max skip length between words; default is 5
- -sample \<float\> <br>
        Set threshold for occurrence of words. Those that appear with higher frequency in the training data will be randomly down-sampled; default is 1e-3, useful range is (0, 1e-5)
- -hs \<int\> <br>
        Use Hierarchical Softmax; default is 0 (not used)
- -negative \<int\> <br>
        Number of negative examples; default is 5, common values are 3 - 10 (0 = not used)
- -threads \<int\> <br>
        Use \<int\> threads (default 12)
- -iter \<int\> <br>
        Run more training iterations (default 5)
- -min-count \<int\> <br>
                This will discard words that appear less than \<int\> times; default is 5
- -alpha \<float\> <br>
                Set the starting learning rate; default is 0.025 for skip-gram and 0.05 for CBOW
- -classes \<int\> <br>
                Output word classes rather than word vectors; default number of classes is 0 (vectors are written)
- -debug \<int\> <br>
                Set the debug mode (default = 2 = more info during training)
- -binary \<int\> <br>
                Save the resulting vectors in binary moded; default is 0 (off)
- -save-vocab \<file\> <br>
                The vocabulary will be saved to \<file\>
- -read-vocab \<file\> <br>
                The vocabulary will be read from \<file\>, not constructed from the training data
- -cbow \<int\> <br>
                Use the continuous bag of words model; default is 1 (use 0 for skip-gram model)

<div style="page-break-after: always;"></div>

## 4 - No more magic!

Vecteur du mot 'hello': <br>
hello -0.889455 -2.309539 -0.041192 -0.281227 0.395468 0.979277 1.356267 0.310518 -1.990973 -0.723721 1.428636 -0.268069 -0.596675 -1.417385 0.777671 -0.621277 1.741493 1.753633 -0.396674 -0.573816 1.147819 0.192979 0.547853 1.069347 -0.399519 -0.690093 1.480045 2.717941 -1.690826 -1.515211 3.467155 -0.924296 0.493458 -1.163861 -0.019398 2.837795 -0.019581 0.008492 1.096949 0.739065 3.587894 -0.334166 -2.772532 1.639715 -0.331153 -0.750504 -0.156602 -0.147748 1.312110 0.737765 1.437320 -0.591741 0.813758 0.722348 1.202542 1.895662 1.579985 -1.102479 -1.937637 -0.042633 0.139460 -0.191112 -2.647696 1.115861 0.775499 3.993551 3.707530 -2.312320 -2.734908 -1.718529 -2.102584 -0.723602 -0.415569 -0.921520 -0.428667 0.295248 -0.590164 -0.042712 -0.432065 -0.321144 1.912458 3.602315 -1.801562 0.797616 -0.902462 -0.199472 -0.270681 0.386516 -0.577557 -0.729609 2.738387 -1.089650 0.147540 -1.921388 0.021743 -0.400317 -0.742092 -0.887190 0.169093 1.987316 0.309268 -1.056702 1.965873 3.618670 -2.586204 -0.773380 -1.190755 0.147138 -0.464229 -2.632127 -0.761335 1.535932 0.244122 1.151671 1.117801 -0.856207 -0.644277 -0.126110 1.828791 1.066016 -0.985572 0.006175 -0.150747 2.336735 2.250925 -0.695990 -1.862571 0.920109 -0.505307 0.269930 -1.139093 -0.238626 0.963361 3.086863 -2.424605 0.592355 -0.472971 0.205957 1.506351 -0.822353 -2.582712 -0.178095 -0.769546 -1.907562 1.879868 -0.230007 -0.766772 0.833690 -1.366783 3.164398 -2.370656 -2.875646 1.822206 0.351858 -0.047326 -0.749871 1.651029 -1.733096 -3.070052 -1.763114 1.187095 -1.053187 -0.297746 0.389689 -0.628339 -1.552573 0.556443 -0.858871 -0.908921 2.455867 0.097012 -0.497532 0.649097 0.441803 -2.496355 2.487935 1.306090 0.515212 -0.823115 3.266339 -2.572322 0.047747 2.411662 0.823099 -0.391335 1.856604 -1.247693 2.083625 0.402206 -0.150826 1.442600 1.467574 -1.155450 -0.792003 2.102014 -2.451662 0.240712 -0.273782 0.740321 -0.495698 0.756923 -1.656231 -2.490973 0.631551 1.140352 -0.727671 -0.556360 -1.353745 1.511934 0.477759 1.375698 -1.876032 1.306351 0.974576 -1.124569 -0.232728 -0.614405 -0.349071 0.467342 -0.624547 0.185189 0.529939 1.833860 0.983755 -1.267912 0.103397 -2.387988 0.997998 -2.080883 -0.282848 -1.827271 1.455566 -1.460552 0.889522 -0.720318 -0.401863 3.366032 0.694364 -2.780165 -1.141760 2.724818 -1.468146 -1.897823 -0.268684 0.220642 -3.259598 -1.519152 0.240025 -0.435964 0.019751 2.378324 -1.016987 -1.303912 -0.087406 0.714465 -3.288627 0.033550 -4.532076 0.022037 0.479307 0.087679 -0.637973 3.762143 -3.475367 0.466938 0.550593 0.655827 -0.714042 0.935061 -1.134858 -4.546233 -0.537365 -2.510550 -1.530571 0.294234 -1.887271 -1.064969 0.187854 -0.669248 1.665685 1.598842 -1.651535 -0.266904 -0.719373 -0.109383 -1.903416 -0.027935 -2.191211 -0.959873 0.685889 1.266885 -2.174153 2.385852 -0.400349 -0.018428 -1.412687 0.761689 0.848514 1.261855 -0.543339 -2.365024 4.396163 -0.237962 1.893846 0.939431 0.115329 -2.029536 -0.637726 1.702893 -0.387495 1.193547 -2.165636 0.668437 -3.045094 0.716830 0.857637 0.352264 -1.206113 -1.044334 1.218324 1.231059 0.300967 -0.690376 0.543425 -1.162512 -1.449218 -1.222721 -0.058686 0.784455 0.849811 -0.670285 3.126857 0.498905 3.540712 0.712925 0.615350 0.771517 0.261774 3.711196 -3.672172 -5.111924 -1.627361 0.884880 1.286442 0.494974 -1.582183 -1.656188 -0.008855 1.800884 -2.379138 0.285551 1.754759 -0.409828 -2.161681 0.064581 -1.929328 -0.168238 0.970018 -3.369246 0.105653 -0.617266 2.400949 0.600897 0.224407 -0.289227 2.671395 0.861767 2.142713 2.512048 -1.226182 1.124873 0.522046 0.059589 -1.577973 0.027730 0.170453 1.478097 -3.716459 -0.421803 1.350209 1.457650 0.724985 -0.695576 -0.200640 -0.515642 -0.070493 1.383324 -0.286551 0.239917 0.324520 3.116766 1.182200 0.960781 -0.290873 -2.839924 0.622211 0.050013 2.179253 0.528468 -1.457646 

<div style="page-break-after: always;"></div>

## 5 - Proximité sémantique des mots
Mots proches pour le mot 'best':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                            finest              0.452976
>                                          greatest              0.392346
>                                            fondly              0.385922
>                                            better              0.385849
>                                            razzie              0.380471
>                                            oscars              0.374409
>                                             bafta              0.358662
>                                             worst              0.353870
>                                       outstanding              0.340171
>                                              well              0.334330
>                                           biggest              0.334292
>                                            awards              0.332936
>                                          filmfare              0.320405
>                                       nominations              0.315206
>                                             krush              0.309074
>                                            grammy              0.306767
>                                             award              0.303212
>                                         accolades              0.301269
>                                          eastwood              0.299114
>                                        unequalled              0.295806
>                                              emmy              0.293030
>                                          earliest              0.287866
>                                         popularly              0.286878
>                                          favorite              0.285754
>                                        underrated              0.284611
>                                           gingold              0.284282
>                                            famous              0.283403
>                                          teleplay              0.277986
>                                         favourite              0.274381
>                                          hermione              0.273712
>                                             wilde              0.272804

Mots proches pour le mot 'football':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                            soccer              0.570894
>                                        basketball              0.536019
>                                            hockey              0.508449
>                                             rugby              0.507848
>                                          baseball              0.487454
>                                   interuniversity              0.448585
>                                           coached              0.434267
>                                        midfielder              0.431883
>                                          korfball              0.431444
>                                    internazionale              0.425555
>                                            sports              0.422251
>                                          lacrosse              0.418780
>                                          bulldogs              0.413020
>                                             jongg              0.410977
>                                          handball              0.410174
>                                              wafl              0.402038
>                                             teams              0.400216
>                                           snooker              0.399343
>                                           juniors              0.398930
>                                              team              0.398773
>                                              liga              0.389869
>                                           athlete              0.388115
>                                           everton              0.387792
>                                        volleyball              0.387725
>                                              ymca              0.387628
>                                          athletic              0.387585
>                                             sport              0.386183
>                                          midfield              0.385088
>                                               vfl              0.384109
>                                            tennis              0.382148
>                                        goalkeeper              0.381838
>                                            shinty              0.380477
>                                               cfl              0.378637
>                                      cheerleading              0.375055
>                                               nfl              0.374058

Mots proches pour le mot 'france':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                            french              0.569738
>                                             spain              0.525488
>                                          provence              0.514005
>                                             italy              0.487345
>                                       netherlands              0.482033
>                                           germany              0.474649
>                                           commune              0.471154
>                                          portugal              0.465591
>                                            calais              0.448412
>                                           belgium              0.445609
>                                           ferrand              0.442994
>                                            nantes              0.441642
>                                          baudouin              0.434728
>                                            alsace              0.433603
>                                         partement              0.433576
>                                             paris              0.432688
>                                            russia              0.431877
>                                        universite              0.431724
>                                             napol              0.428844
>                                            albret              0.427367
>                                         huguenots              0.424921
>                                          mulhouse              0.422658
>                                         angouleme              0.419264
>                                           hungary              0.418901
>                                           picardy              0.418679
>                                         aquitaine              0.417836
>                                          toulouse              0.415682
>                                             vichy              0.408585
>                                            valois              0.408335
>                                           britain              0.408311
>                                          belgians              0.407086
>                                             marne              0.403211
>                                             cedes              0.402594
>                                           navarre              0.402365
>                                          burgundy              0.402088

Mots proches pour le mot 'wine':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                             wines              0.510830
>                                             grape              0.484084
>                                             bread              0.483873
>                                          vermouth              0.455594
>                                           chianti              0.445718
>                                         sparkling              0.435721
>                                             casks              0.423418
>                                             drink              0.416714
>                                          currants              0.413797
>                                            stewed              0.407454
>                                             vodka              0.402700
>                                            brandy              0.402668
>                                             cidre              0.401951
>                                            claret              0.400776
>                                          cherries              0.395462
>                                             cider              0.390923
>                                           dessert              0.389671
>                                           almonds              0.387705
>                                              loaf              0.385775
>                                        unleavened              0.384532
>                                            ciders              0.384344
>                                             drank              0.383888
>                                             juice              0.374525
>                                             leche              0.373577
>                                        chocolates              0.371752
>                                            cognac              0.370446
>                                           vinegar              0.369363
>                                         libations              0.368030
>                                           liqueur              0.365041
>                                         flavoured              0.363795
>                                            brewed              0.363662
>                                             plums              0.359530
>                                            drinks              0.359487
>                                          liqueurs              0.357317
>                                        sauerkraut              0.356845

Mots proches pour le mot 'apple':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                         macintosh              0.567289
>                                              imac              0.478190
>                                         quickdraw              0.462036
>                                              iigs              0.457399
>                                             intel              0.441241
>                                          performa              0.440356
>                                         microsoft              0.437768
>                                             ibook              0.437747
>                                       macintoshes              0.433903
>                                              macs              0.433672
>                                            compaq              0.425842
>                                           wozniak              0.423945
>                                             amiga              0.423011
>                                              ipod              0.421816
>                                     microcomputer              0.416835
>                                        appleworks              0.409901
>                                         hypercard              0.409385
>                                          visicalc              0.405080
>                                                os              0.400769
>                                            raskin              0.400582
>                                             atari              0.400358
>                                            amigas              0.399242
>                                                pc              0.393165
>                                            laptop              0.391945
>                                               ibm              0.391883
>                                           macbook              0.391742
>                                               iic              0.385154
>                                          openstep              0.384996
>                                          amigaone              0.383726
>                                               trs              0.381239
>                                          mcintosh              0.379018
>                                               iie              0.379005
>                                    microcomputers              0.375965
>                                              beos              0.373867
>                                             dbase              0.371152

Mots proches pour le mot 'mouse':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                              mice              0.463279
>                                          joystick              0.445589
>                                         trackball              0.422122
>                                            cursor              0.379989
>                                         joysticks              0.377679
>                                           buttons              0.375768
>                                          mousepad              0.367109
>                                            mickey              0.360093
>                                          keyboard              0.357725
>                                          chording              0.356692
>                                             keyer              0.343882
>                                       touchscreen              0.340675
>                                        keystrokes              0.335045
>                                          logitech              0.327751
>                                           widgets              0.316795
>                                            button              0.315239
>                                         engelbart              0.310286
>                                       controllers              0.308561
>                                               pad              0.304828
>                                               vga              0.304706
>                                              guis              0.303681
>                                           chorded              0.303139
>                                              wimp              0.298564
>                                           cutouts              0.297180
>                                            lemurs              0.294759
>                                             menus              0.293770
>                                             beige              0.291658
>                                       macintoshes              0.291034
>                                         keystroke              0.290934
>                                            keypad              0.286912
>                                             xerox              0.282138
>                                              moth              0.281452
>                                            device              0.278580
>                                          wearable              0.278446
>                                          toontown              0.274431

Mots proches pour le mot 'macron':
>                                              Word       Cosine distance
>------------------------------------------------------------------------
>                                         diacritic              0.601186
>                                        circumflex              0.597843
>                                        diacritics              0.550871
>                                         diaeresis              0.543344
>                                           cedilla              0.530014
>                                            umlaut              0.528495
>                                             breve              0.516007
>                                         ligatures              0.506722
>                                             kahak              0.503483
>                                           macrons              0.499659
>                                           dotless              0.482217
>                                           buailte              0.481880
>                                       diacritical              0.478738
>                                          digraphs              0.468524
>                                          ligature              0.467399
>                                        handakuten              0.466937
>                                              alif              0.460974
>                                           digraph              0.450488
>                                             vowel              0.448412
>                                         lowercase              0.445201
>                                              ayin              0.436211
>                                             okina              0.436195
>                                        apostrophe              0.435596
>                                            accent              0.433710
>                                  transliterations              0.430250
>                                       syllabaries              0.427388
>                                         uppercase              0.422042
>                                             comma              0.420861
>                                           akshara              0.417954
>                                           dakuten              0.417680
>                                   alphabetization              0.414446
>                                         diphthong              0.413556
>                                           glottal              0.409247
>                                    palatalisation              0.408413
>                                       punctuation              0.408204

Nous remarquons de les mots "apples", "mouse" et "macron" ont des mots proches différents de ce que l'on pourrait s'attendre. 
Par exemple:
- Pour le mot "apple", au lieu de trouver des mots proches comme "pear" ou "orange" (des fruits), nous obtenons des mots proches qui sont liés au domaine de l'informatique (de l'entreprise Apple);
- Pareil pour le mot "mouse" (mots proches dans le domaine des périphériques);
- Pour le mot "macron", nous obtenous des mots qui sont liés au domaine de l'orthographe.

<div style="page-break-after: always;"></div>

## 6 - Tâche d'analogie de mot 

Analogie pour les mots 'man woman king':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                             queen              0.448882
>                                         betrothed              0.419719
>                                          daughter              0.414255
>                                            valois              0.400882
>                                             anjou              0.393321
>                                           castile              0.371971
>                                           heiress              0.370141
>                                         melisende              0.365816
>                                           marries              0.362188
>                                              wife              0.359855
>                                          isabella              0.355864
>                                           infanta              0.353706
>                                               vii              0.353283
>                                            aragon              0.352626
>                                          burgundy              0.350524
>                                            boleyn              0.350160
>                                           consort              0.349351
>                                         elizabeth              0.347465
>                                            dagmar              0.347443
>                                          braganza              0.346603
>                                             kings              0.345010
>                                        montferrat              0.344996
>                                          abdicate              0.342168
>                                         sigismund              0.340333
>                                         ahasuerus              0.339673
>                                           duchess              0.339611
>                                          philippa              0.339359
>                                              vasa              0.338464
>                                          eleonora              0.338232
>                                           emperor              0.337099


Cette analogie marche.

Analogie pour les mots 'athens greece paris':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                            france              0.465426
>                                             seine              0.378663
>                                              vres              0.377249
>                                             vichy              0.374667
>                                            nantes              0.367706
>                                             italy              0.364457
>                                           etienne              0.357040
>                                          histoire              0.353895
>                                           ditions              0.352531
>                                      dictionnaire              0.351502
>                                            cortot              0.351228
>                                         normandie              0.349700
>                                             cedes              0.345735
>                                          provence              0.345214
>                                          mulhouse              0.345076
>                                               rie              0.344566
>                                         gallimard              0.343604
>                                          grenoble              0.343590
>                                             dijon              0.342114
>                                               sur              0.339459
>                                    radiodiffusion              0.338813
>                                            french              0.336841
>                                             marne              0.333744
>                                         marseille              0.333009
>                                          centrale              0.332651
>                                             tudes              0.331333
>                                           commune              0.330878
>                                            calais              0.330829
>                                           germany              0.330808
>                                              cnrs              0.329811
>                                         huguenots              0.328310
>                                           ferrand              0.328053
>                                          biblioth              0.324942

Cette analogie marche.

Analogie pour les mots 'berlin germany madrid':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                             spain              0.485459
>                                             italy              0.379350
>                                            france              0.375143
>                                         argentina              0.374665
>                                           badajoz              0.373356
>                                            toledo              0.361353
>                                          portugal              0.351603
>                                              coru              0.347187
>                                         tarragona              0.337825
>                                          sociedad              0.337135
>                                          valencia              0.335203
>                                          asturias              0.334601
>                                              xith              0.329584
>                                         andalusia              0.327415
>                                              psoe              0.324784
>                                         deportivo              0.322478
>                                         navarrese              0.320108
>                                            cortes              0.319564
>                                           galicia              0.312220
>                                            blanco              0.311116
>                                            huelva              0.310174
>                                             japan              0.307222
>                                            lleida              0.306919
>                                              arag              0.306647
>                                            felipe              0.304844
>                                       publicacion              0.301963
>                                            huesca              0.300649
>                                       guadalajara              0.296416
>                                             anzio              0.296158
>                                      nationalists              0.296070
>                                          sicilies              0.295050
>                                             cedes              0.295041
>                                            franco              0.294387

Cette analogie marche.

Analogie pour les mots 'man woman son': 
>                                              Word              Distance
>------------------------------------------------------------------------
>                                          daughter              0.608468
>                                              wife              0.488741
>                                            mother              0.465415
>                                            father              0.450804
>                                         betrothed              0.443534
>                                           married              0.433579
>                                            sister              0.428826
>                                            cousin              0.426640
>                                         concubine              0.420003
>                                           husband              0.418612
>                                         daughters              0.406584
>                                           widowed              0.405468
>                                           brother              0.389006
>                                          faustina              0.388968
>                                          fathered              0.388850
>                                       grandmother              0.387737
>                                              aunt              0.387542
>                                             child              0.386403
>                                              sons              0.383729
>                                         melanippe              0.382587
>                                         childless              0.380492
>                                          eleonore              0.379241
>                                     granddaughter              0.379156
>                                             niece              0.378666
>                                           widower              0.376805
>                                           heiress              0.376495
>                                            custis              0.375563
>                                            teresa              0.373175
>                                             agnes              0.371967
>                                          consorts              0.367847
>                                      stepdaughter              0.366773
>                                        noblewoman              0.361985
>                                         remarried              0.361814

Cette analogie marche.

Analogie pour les mots 'write writes descrease':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                         increases              0.426667
>                                          increase              0.365341
>                                         decreases              0.350800
>                                        decreasing              0.331337
>                                        overwhelms              0.325865
>                                           reduces              0.309061
>                                         increased              0.291546
>                                        increasing              0.280990
>                                        elasticity              0.277132
>                                           optimal              0.274059
>                                        imbalances              0.269223
>                                         reduction              0.266876
>                                         imbalance              0.264296
>                                            reduce              0.262351
>                                    underestimates              0.262120
>                                      experiencing              0.259781
>                                            lowers              0.257782
>                                          predicts              0.256048
>                                          hampered              0.255496
>                                           leakage              0.254416
>                                    asymptotically              0.252193
>                                          breakage              0.251142
>                                         decreased              0.250525
>                                       selfishness              0.247496
>                                         deflation              0.246863
>                                           itching              0.242773
>                                           reduced              0.242434
>                                          improves              0.242215
>                                        likelihood              0.241621
>                                      atheromatous              0.240840
>                                       diminishing              0.240764
>                                         fragility              0.240102
>                                       contributes              0.239197

Non, cela ne marche pas, nous obtenons "increases" et "increase" avec le mot "decreases"

Analogie pour les mots 'man woman husband':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                          daughter              0.434027
>                                              wife              0.427856
>                                               her              0.426929
>                                               she              0.426287
>                                         remarried              0.411402
>                                          marriage              0.396511
>                                           married              0.387893
>                                           widowed              0.381624
>                                           widower              0.379954
>                                             jeane              0.379841
>                                            spouse              0.379778
>                                         betrothed              0.378628
>                                              aunt              0.377929
>                                             fianc              0.366504
>                                            joanie              0.365866
>                                            gracen              0.363751
>                                             lover              0.360324
>                                             agnes              0.360217
>                                            sister              0.358003
>                                            custis              0.355441
>                                          cornelia              0.354438
>                                             niece              0.352712
>                                           divorce              0.349104
>                                         daughters              0.345218
>                                            teresa              0.345038
>                                            mother              0.344534
>                                          divorced              0.344528
>                                         messalina              0.339607
>                                          eleonore              0.338656
>                                            eloped              0.337795
>                                               wed              0.333641
>                                             raped              0.333402
>                                     granddaughter              0.330951

Non, cela ne marche pas. Nous obtenons le mot "daughter" avant le mot "wife"

Analogie pour les mots 'us italy hamburger':
>                                              Word              Distance
>------------------------------------------------------------------------
>                                          cagliari              0.455069
>                                          lombardy              0.432284
>                                            padova              0.426529
>                                           romagna              0.424231
>                                             parma              0.422045
>                                           toscana              0.412906
>                                             colli              0.409025
>                                          calabria              0.400989
>                                           perugia              0.393690
>                                        autostrada              0.392910
>                                           brescia              0.392589
>                                            friuli              0.390381
>                                              riso              0.389767
>                                            trento              0.388198
>                                           filippo              0.385828
>                                            milano              0.385331
>                                            farina              0.384632
>                                            genova              0.383858
>                                            modena              0.378955
>                                          trentino              0.378292
>                                             gucci              0.378159
>                                           tuscany              0.377831
>                                        mozzarella              0.375090
>                                            veneto              0.373310
>                                          piacenza              0.372088
>                                        prosciutto              0.370272
>                                             eifel              0.369940
>                                           polenta              0.369250
>                                            latium              0.368742
>                                            ancona              0.368625
>                                             genoa              0.367380
>                                           venezia              0.367331

Non, cela ne marche pas. Le mot "bologna" n'apparait pas dans les mots proches du mot "hamburger" avec pour vecteur "us > italy".

Analogie pour les mots 'us australia hamburger': 
>                                              Word              Distance
>------------------------------------------------------------------------
>                                          tasmania              0.395597
>                                            sydney              0.366852
>                                          desserts              0.347704
>                                               nsw              0.345757
>                                           manukau              0.345564
>                                          brisbane              0.345011
>                                         groningen              0.338323
>                                            hobart              0.334758
>                                          sausages              0.331388
>                                              lner              0.328904
>                                             lager              0.325371
>                                        distillery              0.321240
>                                        queensland              0.319690
>                                            brewed              0.318225
>                                               ale              0.317751
>                                            monash              0.317670
>                                            mashed              0.311434
>                                         kreuzberg              0.311259
>                                         fremantle              0.310838
>                                               rtd              0.310031
>                                            crisps              0.309333
>                                    conservatorium              0.307429
>                                             otago              0.305566
>                                          heineken              0.303471
>                                       australasia              0.300119
>                                           burgers              0.300041
>                                      christchurch              0.299290
>                                           wallaby              0.298795
>                                             perth              0.296527
>                                            pickle              0.296260
>                                            twente              0.295502
>                                          doenjang              0.295338

Non, cela ne marche pas. Le mot "hotdog" n'apparait pas dans les mots proches du mot "hamburger" avec pour vecteur "us > australia".
