# Het ware leven van Johann Sebastian Bach

Bestand: [03_ware-leven-bach-2.ttl](03_ware-leven-bach-2.ttl)

## De resource

_Het ware leven van Johann Sebastian Bach_ verscheen oorspronkelijk in het Duits in 1999, de Nederlandse vertaling kwam uit in 2000. Dit voorbeeld gaat uit van het KB-exemplaar van de gebonden uitgave uit 2000. Gegevens over de oorspronkelijke versie zijn toegevoegd op basis van het colofon in de Nederlandse editie. Er zijn meer vertalingen (o.a. een Engelse en een Spaanse), maar die hebben we bij het uitwerken van dit voorbeeld buiten beschouwing gelaten.

## Entiteitenstructuur

De primaire relaties gaan in dit voorbeeld van item **ex:i6** naar manifestatie **ex:m3** naar expressie **ex:e15** naar werk **ex:w15**. We weten dat er tenminste één andere expressie is die hetzelfde werk realiseert: de oorspronkelijke Duitse tekst (**ex:e16**). De twee expressies hebben ook een onderlinge relatie: de ene (**ex:e15**) is een vertaling van de andere (**ex:e16**). Deze relatie (**rdae:P20141**) maken we expliciet, omdat hij niet vanzelfsprekend volgt uit het feit dat beide expressies hetzelfde werk realiseren.

Uiteraard bestaat er ook tenminste één manifestatie die de oorspronkelijke Duitse tekst verwezenlijkt. Die hebben we bij de uitwerking buiten beschouwing gelaten, omdat we daar op basis van het colofon maar heel weinig over weten ("Uitgave: Piper Verlag GmbH, München").

In dit voorbeeld zien we, naast de relaties tussen werk en actor die ook in [_Harmonizing 'Bach' chorales_](02_harmonizing-bach.md) voorkomen, een maker-relatie tussen een expressie en een actor. Hans Driessen (**ex:a24**) heeft de Nederlandse vertaling gemaakt.

![Visualisatie Structuur](../../assets/03_ware-leven-bach_rda-rdf_visualisaties.png)

## Representatie in RDA-RDF

Deze resource is in een reeks verschenen (Open Domein). Dat wordt op de volgende manier vastgelegd:

    ex:w15 # Werk no. 15
      rdfs:label "Wahre Leben des J.S. Bach, von Klaus Eidam" ;
      skos:exactMatch <http://viaf.org/viaf/2545153954868605680004> ; # is hetzelfde als: VIAF werk 2545153954868605680004
      rdaw:P10004 rdaterm:1165 ; # has category of work: textual work
      rdaw:P10365 rdaep:1001 ; # has has extension plan: static plan
      rdaw:P10004 <http://id.loc.gov/authorities/genreForms/gf2014026049> ; # has category of work: biography (form)
      rdaw:P10102 ex:w16 ; # is issue of = in series: Open domein

    ex:w16 # Werk no. 16
	  a rdac:C10001 ;
      rdfs:label "Open domein (reeks)" ;
      skos:exactMatch <http://viaf.org/viaf/178645273> ; # is hetzelfde als: VIAF werk 178645273
      rdaw:P10365 rdaep:1005 ; # has extension plan: successive indeterminate plan
      rdaw:P10004 rdaterm:1127 ; # has category of work: aggregating work
      rdaw:P10004 rdaterm:1081 ; # has category of work: series
      rdaw:P10088 "Open domein" @nl . # has title of work

Merk op dat beide werken ook geïdentificeerd zijn in [VIAF](https://viaf.org/). Dat is hier vastgelegd met `skos:exactMatch`. Voor een toelichting op de typeringen zie [_Harmonizing 'Bach' chorales_](02_harmonizing-bach.md#representatie-in-rda-rdf).

Bestand: [03_ware-leven-bach-2.ttl](03_ware-leven-bach-2.ttl)
