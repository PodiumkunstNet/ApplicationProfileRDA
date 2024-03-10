# Zijn bliksem, zijn donder

Bestand: [04_zijn-bliksem-zijn-donder-2.ttl](04_zijn-bliksem-zijn-donder-2.ttl)

## De resource

_Zijn bliksem, zijn donder_ is een cultuurhistorisch essay over de Mattheus-Passie van Johann Sebastian Bach en over de Nederlandse voorliefde voor dat werk. Het verscheen voor het eerst in 1997 en is meerdere keren herdrukt. De 6e druk uit 1999 is een herziene druk. Dit voorbeeld gaat uit van de vierde druk, waarvan een exemplaar aanwezig is in het depot van de Koninklijke Bibliotheek.

## Entiteitenstructuur

Dit voorbeeld gaat niet zozeer over de primaire relaties (item **ex:i7** stelt manifestatie **ex:m4** voor, die expressie **ex:e17** verwezenlijkt, die werk **ex:w17** realiseert), maar wil laten zien dat een werk ook een ander werk als onderwerp kan hebben. Het werk-als-onderwerp is hier de Mattheus-Passie (**ex:w18**) van J.S. Bach (**ex:a21**). Merk op dat Bach, net als in [_Harmonizing 'Bach' chorales_](02_harmonizing-bach.md) en [_Het ware leven van Johann Sebastian Bach_](03_ware-leven-bach-2.md), gerelateerd is aan het primaire werk in het voorbeeld. In dit geval niet rechtstreeks, maar als componist van de Mattheus-Passie.

![Visualisatie Structuur](../../assets/04_zijn-bliksem-zijn-donder_rda-rdf_visualisaties.png)

Uiteraard is de Mattheus-Passie (**ex:w18**) op zijn beurt op vele manieren gerealiseerd. Er zijn talloze genoteerde en uitgevoerde expressies van de muziek, die op hun beurt weer verwezenlijkt zijn in heel veel verschillende manifestaties. In dit voorbeeld zijn die allemaal buiten beschouwing gelaten.

## Representatie in RDA-RDF

Deze resource heeft zowel een hoofdtitel als een ondertitel. Voor beide typen titels is een specifiek element in RDA:

    rdam:P30156 "Zijn bliksem, zijn donder" @nl ; # has title proper
    rdam:P30142 "Over de Mattheus Passie van Johann Sebastian Bach" @nl ; # has other title information

Het impressum bevat naast gegevens over de uitgever ook gegevens over de drukker:

    rdam:P30083 ex:a26 ; # has publisher agent: Ambo
    rdam:P30088 ex:p10 ; # has place of publication: Baarn
    rdam:P30080 ex:a27 ; # has distributor agent: Uitg. Westland
    rdam:P30085 ex:p11 ; # has place of distribution: Schoten

De actoren en plaatsen in dit voorbeeld worden geïdentificeerd in respectievelijk [00_actoren.ttl](00_actoren.ttl) en [00_plaatsen.ttl](00_plaatsen.ttl).

Dit voorbeeld bevat ook een basale beschrijving van een muziekwerk:

    ex:w18 # Werk no. 18
      a rdac:C10001 ;
      rdfs:label "Matthäuspassion, BVW 244" ;
      skos:exactMatch <http://viaf.org/viaf/1371147270361735700006> ; # is hetzelfde als: VIAF werk 1371147270361735700006
      rdaw:P10004 rdaterm:1118 ; # has category of work: musical work
      rdaw:P10004 <https://id.loc.gov/authorities/genreForms/gf2014027062> ; # has category of work: sacred music
      rdaw:P10365 rdaep:1001 ; # has has extension plan: static plan
      rdaw:P10335 "BWV 244" ; # has thematic index number
      rdaw:P10223 "Matthäuspassion" @de ; # has preferred title of work
      rdaw:P10086 "Matthäus-Passion" @de ; # has variant title of work
      rdaw:P10086 "Mattheuspassie" @nl ; # has variant title of work
      rdaw:P10086 "St Matthew Passion" @en ; # has variant title of work
      rdaw:P10086 "Passion selon saint Matthieu" @fr ; # has variant title of work
      rdaw:P20220 <https://data.muziekschatten.nl/som/um1569> ; # has medium of performance of musical content of representative expression
      rdaw:P10053 ex:a21 . # has composer agent: J.S.Bach

Voor het uitvoeringsmedium wordt gebruik gemaakt van de terminologiebron die door _Muziekschatten_ is opgesteld. De terminologiebron _Uitvoeringsmedium_ is beschikbaar via het [NDE-Termennetwerk](https://termennetwerk.netwerkdigitaalerfgoed.nl/?datasets=https://data.muziekschatten.nl/sparql/%23uitvoeringsmedium).

Bestand: [04_zijn-bliksem-zijn-donder-2.ttl](04_zijn-bliksem-zijn-donder-2.ttl)
