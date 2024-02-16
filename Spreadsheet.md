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

* Elementaanduiding (blauwe koppen)
  * RDA Toolkit name: de naam van het element zoals gebruikt in de [RDA Toolkit](http://access.rdatoolkit.org/)
  * RDA Registry curie: de compacte URI van het element zoals gegeven in de [RDA Registry](http://www.rdaregistry.info/)
  * AP-laag: de laag ("layer") van het applicatieprofiel waartoe het element behoort, bijvoorbeeld "minimumbeschrijving", "coherente beschrijving", "effectieve beschrijving: generiek", "effectieve beschrijving: muziek"
  * pk.net scope: een eerste poging om de elementen te rubriceren voor Podiumkunst-gebruik
  * pk.net label: elementlabels die in de context van Podiumkunst gebruikt kunnen worden in plaats van de formele labels, bijvoorbeeld in een invoerformulier
  * domein: de entiteit waartoe het element behoort
  * bereik: de entiteit waarnaar het (relatie-)element verwijst, bevat "nvt" bij attribuutelementen
  * inversie: de curie van het bijbehorende inversie-element
  * subproperty van: de curie van het bovenliggende element in de hiërarchie
* Verplichting & herhaalbaarheid (gele koppen)
