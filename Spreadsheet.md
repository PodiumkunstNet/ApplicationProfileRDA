# Gevolgde aanpak spreadsheet

[Download het spreadsheet](../assets/RDA-AP_Podiumkunst-net.xlsx)

## Brondata

Het spreadsheet is gebaseerd op csv-data uit de [RDA Registry](http://www.rdaregistry.info/). De volgende gegevens zijn gebruikt:

* Werk: [https://www.rdaregistry.info/Elements/w/](https://www.rdaregistry.info/Elements/w/) [Q1 2023]
* Expressie: [https://www.rdaregistry.info/Elements/e/](https://www.rdaregistry.info/Elements/e/) [Q1 2023]
* Manifestatie: [https://www.rdaregistry.info/Elements/m/](https://www.rdaregistry.info/Elements/m/) [Versie: [v5.0.9](https://github.com/RDARegistry/RDA-Vocabularies/releases/tag/v5.0.9); Datum: 07-04-2023]
* Item: [https://www.rdaregistry.info/Elements/i/](https://www.rdaregistry.info/Elements/i/) [Versie: [v5.0.9](https://github.com/RDARegistry/RDA-Vocabularies/releases/tag/v5.0.9); Datum: 07-04-2023]
* Alignment from soft-deprecated to recommended elements: [http://www.rdaregistry.info/Aligns/alignSoft2Rec.html](http://www.rdaregistry.info/Aligns/alignSoft2Rec.html) [Q1 2023]

## Werkbladen

Het spreadsheet bevat de volgende werkbladen:

* Werk, Expressie, Manifestatie (compleet), Item: het RDA-Applicatieprofiel Podiumkunst voor de genoemde entiteiten
* alignSoft2Rec, rdaw, rdae, rdam, rdai: de gedownloade gegevens uit de RDA Registry

## Structuur

De werkbladen met het RDA-Applicatieprofiel Podiumkunst zijn op de volgende manier opgebouwd:

* **Elementaanduiding** (blauwe koppen)
  * _RDA Toolkit name_: de naam van het element zoals gebruikt in de [RDA Toolkit](http://access.rdatoolkit.org/)
  * _RDA Registry curie_: de compacte URI van het element zoals gegeven in de [RDA Registry](http://www.rdaregistry.info/)
  * _AP-laag_: de laag ("layer") van het applicatieprofiel waartoe het element behoort, bijvoorbeeld "minimumbeschrijving", "coherente beschrijving", "effectieve beschrijving: generiek", "effectieve beschrijving: muziek"
  * _pk.net scope_: een eerste poging om de elementen te rubriceren voor Podiumkunst-gebruik
  * _pk.net label_: elementlabels die in de context van Podiumkunst gebruikt kunnen worden in plaats van de formele labels, bijvoorbeeld in een invoerformulier
  * _domein_: de entiteit waartoe het element behoort
  * _bereik_: de entiteit waarnaar het (relatie-)element verwijst, bevat "nvt" bij attribuutelementen
  * _inversie_: de curie van het bijbehorende inversie-element
  * _subproperty van_: de curie van het bovenliggende element in de hiërarchie
* **Verplichting & herhaalbaarheid** (gele koppen)
  * _verplichting_: aanduiding van de verplichting van het element volgens de MoSCoW-methode
  * _herhaalbaar_: aanduiding van de herhaalbaarheid van het element
  * _min_ & _max_: vertaling van verplichting en herhaalbaarheid naar minimum en maximum aantal occurrences
* **Registratiemethode** (groene koppen): per registratiemethode een aanduiding van de verplichting ervan voor het betreffende element volgens de MoSCoW-methode
* **Vocabulary & String Encoding Schemes** (oranje koppen)
  * _VES (naam)_: de naam van het vocabulaire dat bij het betreffende element gebruikt moet worden
  * _VES (IRI)_: de curie van het betreffende vocabulaire
  * _SES_: String Encoding Scheme waarnaar de waarde in het element moet voldoen
* **Aantekeningen** (grijze koppen)
  * _toelichting_: een korte toelichting op de gekozen verplichting en herhaalbaarheid
  * _policy statement_: beknopt policy statement, bijvoorbeeld om een bepaalde optie uit de RDA Toolkit voor dit element te volgen
  * _aantekening_: aanvullende vragen en opmerkingen van de werkgroep

De kolommen met blanco kop die hierop volgen bevatten gegevens uit de RDA Registry.
