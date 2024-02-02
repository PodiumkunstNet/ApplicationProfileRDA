# Harmonizing 'Bach' chorales

Bestand: [02_harmonizing-bach.ttl](02_harmonizing-bach.ttl)

## De resource

_Harmonizing 'Bach' chorales_ is een beknopt boekje voor muziekstudenten, dat veel gebruikt is als lesboek bij het vak harmonieleer. Het stamt uit 1967 en is diverse keren heruitgegeven, soms in combinatie met _Bach's instrumental counterpoint_ van dezelfde auteur. In dit voorbeeld is uitgegaan van de zadelsteekbanduitgave uit 1987 in het bezit van één van de werkgroepleden.

Het voorbeeld [_Review of Malcolm Boyd on Bach chorales_](https://github.com/renevoorburg/ApplicationProfileRDA/blob/main/rdf/examples/05_review-harmonizing-bach.md) is een recensie van dit werk.

## Entiteitenstructuur

Dit voorbeeld laat in de eerste plaats de primaire relaties tussen een werk, expressie, manifestatie en item zien. Deze relaties zijn verplicht om tot een _coherente beschrijving_ te komen. Samen met een benaming van de entiteit (een titel, naam of identifier; de zogeheten _minimale beschrijving_) vormt dit het absolute minimum om resources met elkaar te verbinden in de Podiumkunst-graaf.

Het voorbeeld toont hoe een concreet item (hier geïdentificeerd met de compacte IRI **ex:i4**) een manifestatie (hier geïdentificeerd als **ex:m2**) voorstelt. Deze manifestatie representeert alle items met dezelfde (oorspronkelijke) eigenschappen als het item in dit voorbeeld.
Dit zal catalografen vertrouwd voorkomen: aan de hand van een concreet exemplaar beschrijf je een publicatie.

De manifestatie verwezenlijkt een expressie (hier geïdentificeerd als **ex:e14**), die op zijn beurt een werk (hier geïdentificeerd als **ex:w14**) realiseert. Zowel expressie als werk hebben betrekking op de meer inhoudelijke aspecten van de resource, zoals (in dit voorbeeld) de aard van de inhoud (tekst), de taal (Engels), de auteur (Malcolm Boyd) en het onderwerp (Johann Sebastian Bach).

Verder laat dit voorbeeld zien dat actoren heel verschillende relaties met de resource kunnen hebben. In de visualisatie hieronder zien we de relatie van het werk met Malcolm Boyd (hier geïdentificeerd als **ex:a20**) en Johann Sebastian Bach (hier geïdentificeerd als **ex:a21**) weergegeven. In de RDF-uitwerking vind je ook nog een uitgever, een drukker (beide gerelateerd aan de manifestatie) en een eigenaar (gerelateerd aan het item).


![Visualisatie Structuur](../../assets/02_harmonizing-bach_rda-rdf_visualisatie.png)

NB deze visualisatie geeft dus niet alle entiteiten uit de RDF-uitwerking weer. Evenmin zijn alle eigenschappen van de afgebeelde entiteiten weergegeven.

Ook is het goed je te realiseren dat niet altijd alle resource entitites (werk, expressie, manifestatie, item) aanwezig hoeven zijn. Dit is in een aantal andere voorbeelden terug te zien.

Het is in dit applicatieprofiel van belang om bij een _coherente beschrijving_ van de resource de richting van de relaties in de gaten te houden. Wie een item identificeert moet ook een relatie met een manifestatie leggen, wie een manifestatie identificeert moet ook een relatie met een expressie leggen en wie een expressie identificeert moet ook een relatie met een werk leggen. Het identificeren van een werk betekent echter niet dat er ook een relatie met een expressie moet zijn, het identificeren van een expressie betekent niet dat er ook een relatie met een manifestatie moet zijn, etc.


## Representatie in RDA-RDF

{tekstje waarin wat toelichting op de RDA-RDF gegeven wordt} 

Bestand: [02_harmonizing-bach.ttl](02_harmonizing-bach.ttl)
