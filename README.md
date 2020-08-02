## TXTANALYSIS

<img src="https://de.cleanpng.com/png-69s53d/" width="100" height="100">
_Die wichtigsten Utils für meine Textanalysen_

1. Git clone the File to your Python library (in my Case: /Users/Fabi/anaconda3/lib/python3.7)
```shell
sudo git clone https://github.com/FAD28/txtanalysis 
```

2. USAGE:
```python
	from txtanalysis import DataCleaner as DC
	from txtanalysis import DataWrangling as DW
	from txtanalysis.emotion import Emotionen_nrc as nrc
	from txtanalysis.emotion import Emotionen_rklinger as rklinger
```

Funktionen:
---
**DataCleaner**

-`DC.clean_list(liste)`

-`DC.soft_clean(liste)`

-`DC.clean_filename(liste)`

___________________
**DataWrangling**

-`DW.load_stopwords(my_stopwords)`

-`DW.remove_stopwords(my_list, stopwords)`

-`DW.get_all_paths()`

-`DW.merge_data(data)`

-`DW.split(data)`	
(Splittet die Daten und merged sie wieder zusammen in einer einzigen Methode)

___________________

**Emotionen_nrc**

-`nrc.NRC_analysis(token_c)`

Return:

|Anzahl |Wert|
|--- |--- |
|1 (EI) | Emotionsindex|
|2 (cc) | Emotionen gesamt count|
|3 (CountOhneSTP) | Wörter ohne Stoppwörter|
|4 (faktor) | Faktor = Emotionsindex / Emotionen gesamt count| 
|5 (zorn_liste) | FURCHT    NRC Emotion|
|6 (erwartung_liste) | ERWARTUNG    NRC Emotion|
|7 (furcht_liste) | FURCHT    NRC Emotion|
|8 (freude_liste) | FREUDE    NRC Emotion|
|9 (traurigkeit_liste) | TRAUER   NRC Emotion|
|10 (überraschung_liste) | ÜBERRASCHUNG    NRC Emotion|
|11 (vertrauen_liste) | VERTRAUEN   NRC Emotion|

___________________
**Emotionen_rklinger**

-`rklinger.show()`

-`rklinger.load_ekel()`

-`rklinger.load_freude()`

...