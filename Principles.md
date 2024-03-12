# De principes achter het RDA-applicatieprofiel Podiumkunst

## 0. Gebruik linked data
De standaard RDA kan goed in een traditionele recordsgebaseerde werkwijze ingezet worden, maar dit applicatieprofiel gaat uit van een toepassing als  linked data (RDF) en de bijbehorende **linked data-principes**. Dat betekent onder andere dat er **entiteiten** gedefinieerd worden voor de centrale objecten die beschreven worden. Deze entiteiten worden geïdentificeerd met een **IRI** (~ **URI**), een identifier in de vorm van een URL (webadres).

Niet alles in linked data is per sé een entiteit met een IRI. Sommige entiteiten hebben alleen maar betekenis in de context van één bovenliggende entiteit. In zo'n geval kan er voor gekozen worden die entiteit geen IRI te geven. Dit bespaart op beheer. Bedenk dat IRI's geacht worden om **duurzame identifiers** te zijn. Dat komt noodzakelijkerwijs met administratieve en technische lasten. Soms is de keuze voor een `blank node`, een entiteit zonder IRI, dus verstandig (zie het voorbeeld verderop over Identifiers). Daarnaast is het om praktische redenen niet, of nog niet, doenlijk om van alles een entiteit te maken. Zo wordt de bladmuziek van [Muziekschatten.nl](https://www.muziekschatten.nl/) als volwaardige entiteiten beschreven maar wordt er van de uitgevers van de bladmuziek slechts de naam genoemd, zonder deze als een entiteit te representeren. De praktische keuze die hier gemaakt is, heeft onder andere te maken met een gebrek aan voldoende passende **terminologiebronnen** of **theasauri**.

## 1. Volg de officiële RDA-standaard
Dit applicatieprofiel is gebaseerd op de beschrijvingen van de klassen en elementen en op de instructies, richtlijnen en waardenlijsten in de [officiële RDA-standaard](http://access.rdatoolkit.org/). De zogeheten "*deprecated*" en "*soft deprecated*" elementen maken geen onderdeel uit van dit applicatieprofiel. 

### Werk vanuit beschrijvingsniveaus
Belangrijk in de benadering die RDA biedt, is dat beschrijvingen op verschillende niveaus van detaillering gemaakt kunnen worden. Daarbij wordt onderscheid gemaakt tussen:

* **Minimumbeschrijving**: deze omvat alleen de meest basale elementen die nodig zijn om een entiteit te beschrijven,
* **Coherente beschrijving**: deze verbindt de primaire werk-, expressie-, manifestatie- en item-entiteiten die bij een resource (~*bron*) horen met elkaar,
* **Effectieve beschrijving**: deze stelt gebruikers in staat om een resource beter te vinden, uitgebreider te identificeren en in een context te plaatsen, ook krijgt de gebruiker informatie over de toegang tot een resource.

In dit applicatieprofiel wordt de **effectieve beschrijving** onderverdeeld in verschillende met elkaar samenhangende "lagen", van generiek of algemeen geldend naar specifiek voor bepaalde typen werken (bv. muziekwerken) of dragers (zoals boeken of cd's).

De **minimumbeschrijving** en de **coherente beschrijving** zijn verplicht in het RDA-Applicatieprofiel Podiumkunst (een "must") en komen overeen met "vindbaar" in de terminologie van het Netwerk Digitaal Erfgoed. De **effectieve beschrijving** is aanbevolen (een "should") ofwel verplicht indien de data voorhanden is en komt overeen met het [NDE-begrip "bruikbaar"](https://netwerkdigitaalerfgoed.nl/bruikbaar/).

De verplichting van een element in het applicatieprofiel geldt binnen de context van de gegeven laag. Dus wanneer bijvoorbeeld de oorspronkelijke bezetting van een muziekwerk verplicht is, geldt dat alleen wanneer je de effectieve beschrijving van een muziekwerk toepast. Wanneer je deze laag uit het applicatieprofiel niet gebruikt, bijvoorbeeld omdat je geen muziekwerk beschrijft of omdat je je praktisch tot de minimaal verplichte lagen van de minimumbeschrijving en de coherente beschrijving moet beperken, geldt ook de verplichting van dit element niet.

### Volg de RDA-registratiemethoden

RDA onderscheidt vier verschillende registratiemethoden voor het vastleggen van de waarde in een element:
* **Ongestructureerde beschrijving**: een combinatie van transcriptie (tekst overgenomen uit de resource) en vrije tekst,
* **Gestructureerde beschrijving**: gestandaardiseerde tekst ontleend aan vocabulaires en coderingssystemen, zoals een term of naam uit een thesaurus,
* **Identifier**: codes of nummers ter identificatie, dit kunnen locale identifiers (zoals recordnummers) zijn of gestandaardiseerde identifiers als ISBN, ISSN, nummeraanduidingen van muziekwerken etc.,
* **IRI**: Internationalized Resource Identifier, ofwel persistente links die door machines geïnterpreteerd kunnen worden.

Een voorbeeld van een mogelijke invulling van de verschillende registratiemethoden voor een specifieke elementwaarde:

![Voorbeeld registratiemethoden](./assets/5%20-%202024-02-29_RDA-Toolkit_applicatieprofielen_v5_dia-11.png)

Vanuit een RDF-perspectief zijn zowel ongestructureerde en gestructureerde beschrijvingen als identifiers "literals" (`rdfs:Literal`). Benamingen van RDA-entiteiten (zoals namen, titels en identifiers) kunnen als een `rdfs:Literal`opgenomen worden, maar RDA biedt ook de mogelijkheid om van zo'n benaming *een entiteit op zich* te maken (dit wordt wel *reïficatie* genoemd). Deze naamsentiteit is dan van het het type **Nomen**. Het nut van deze aanpak is dat het de mogelijkheid biedt om meer over de naam te zeggen. 

Code-voorbeelden 1 en 2 tonen hoe een identifer via reïficatie verrijkt kan worden:

	intern:ex4 rdax:P00018 "12345-78-9" . 

*Voorbeeld 1: Een identifier als een literal-waarde. Betekenis is niet duidelijk.*

	intern:ex4 rdax:P00018 [
		a rdac:C10012 ;                                     # dit is een nomen
		rdan:P80068 "12345-78-9" ;                          # "has nomen string" , de identifier-waarde
		rdan:P80069 <http://vocab.getty.edu/aat/300417443>  # "scheme of Nomen" 
	] .

*Voorbeeld 2: Dezelfde identifier na reïficatie, verrijkt met "scheme of Nomen". Betekenis is duidelijk.*

Het RDA-Applicatieprofiel Podiumkunst gebruikt de Nomen-entiteit voor benamingen zodra er meer over de benaming gezegd moet worden dan alleen de letterlijke waarde. Dat gaat bijvoorbeeld over een typering van de naam (dit is een plaatsingscode) of een aanduiding van het gebruikte schema voor de naam (dit is een ISBN).

## 2. Keuzes gemaakt bij de toepassing van RDA

Een belangrijke stap bij het vaststellen van het applicatieprofiel is bepalen welke elementen je niet nodig hebt. Onderstaande uitgangspunten zijn vanuit die gedachte opgesteld.

### Subtypering van actoren niet in relatie-elementen

De actor-entiteit in RDA kent diverse subklassen:
* Persoon
* Collectieve actor
  * Corporatie
  * Familie

Relaties met deze entiteiten als domein of bereik zijn (op enkele uitzonderingen na) in vijfvoud gedefinieerd. Aangezien het applicatieprofiel in de toekomst uitgebreid zal worden met actoren volgens de meest specifieke subklassen, is het niet nodig de subtypering van actoren in het relatie-element tot uitdrukking te laten komen. De lijst met te gebruiken RDA-elementen kan zo sterk ingeperkt worden, zonder af te doen aan de semantische zeggingskracht.

Dit applicatieprofiel gebruikt dus bijvoorbeeld wel het element `rdaw:P10015` (*has television director agent*), maar niet het element `rdaw:P10561` (*has television director family*) of `rdaw:P10420` (*has television director person*).

Sommige actor-relaties in RDA zijn niet op het niveau van `rdac:C10002` (*agent*) gedefinieerd, omdat ze bijvoorbeeld alleen betekenis hebben op het niveau van een persoon. In die gevallen zijn de specifiekere elementen in dit applicatieprofiel uiteraard wel toegestaan.

Volgens deze logica is binnen dit applicatieprofiel ook gekozen voor het gebruik van het generieke element `rdaw:P10256` (_has subject_) in plaats van bijvoorbeeld `rdaw:P10319` (_has subject agent_). 

Dit principe zou nog breder toegepast kunnen worden (bijvoorbeeld wanneer het gaat over relatie-varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`), maar dat hebben we vooralsnog niet of maar beperkt gedaan.

### Beschrijf representatieve expressies op werkniveau

Omdat bepaalde eigenschappen van expressies als canoniek of oorspronkelijk beschouwd kunnen worden, introduceert RDA de **representatieve expressie** als een expressie die het dichtst bij de intenties van de maker van het werk ligt.

Omdat dit onderscheid ook voor gebruikers relevant is, neemt dit applicatieprofiel de representatieve expressie over.

Kenmerken van representatieve expressies leggen we vast op werkniveau. Dat wil zeggen, we gebruiken de attribuut-elementen in het werkdomein met "... of representative expression" in de naam. We houden er rekening mee dat gegevens over de representatieve expressie niet altijd beschikbaar zullen zijn. De belangrijkste reden voor vastlegging op werkniveau is dat we het beheer ervan willen koppelen aan het beheer van de werken. Bij bepaalde typen werken is dit bovendien de enige manier om representatieve expressies vast te leggen.

Bij het beschrijven van een expressie leggen we de betreffende kenmerken nogmaals vast, ook als ze gelijk zijn aan de waarde van de representatieve expressie.

### Gebruik geen benamingen die bij andere RDA-implementatiescenario's horen

RDA biedt een specifiek type benaming, namelijk _access points_ of "ingangen". Dergelijke ingangen spelen een belangrijke rol bij RDA-toepassingen in traditionele bibliotheekcatalogi (RDA-implementatiescenario C) en zijn opgebouwd volgens een vast stramien, doorgaans bestaande uit elementen die ook in afzonderlijke properties vastgelegd worden.

Omdat dit applicatieprofiel IRI's gebruikt voor het identificeren van werken, expressies, actoren en dergelijke, en omdat er afzonderlijke elementen zijn waarin de verschillende onderdelen van een ingang kunnen worden vastgelegd, worden benamingen van het type "access point" niet toegestaan in dit applicatieprofiel.

### Vermijd shortcuts, modelleer zoveel mogelijk uit

RDA kent diverse elementen die als "shortcut elements" bestempeld kunnen worden. Shortcuts zijn relatie-elementen die twee entiteiten, die indirect aan elkaar gerelateerd zijn via één of meer tussenliggende entiteiten, direct met elkaar verbinden. Omdat op deze manier de tussenliggende entiteit(en) niet geïdentificeerd word(t/en) terwijl het aantal mogelijke paden door de graaf alleen maar toeneemt, gebruiken we _shortcut elements_ in principe niet. Een voorbeeld van een shortcut die we niet gebruiken is `rdaw:P10205` (_has librettist agent_). In plaats daarvan relateren we een muziekwerk aan een werk van het type libretto met `rdaw:P10165` (_has libretto work_) en verbinden we het libretto met de auteur met `rdaw:P10061` (_has author agent_).

Hieraan verwant is het uitgangspunt om vrijetekstelementen (zoals bijvoorbeeld de reeksvermelding) zoveel mogelijk aan te vullen met of te vervangen door een uitgemodelleerde variant die gebruikt maakt van relatie-elementen.

### Vermijd inversies

Voor ieder relatie-element in RDA is een element gedefinieerd dat de inverse relatie aanduidt. Hoewel het semantisch geen verschil maakt of de relatie van `A` naar `B` of de inverse relatie van `B` naar `A` toegepast wordt, kiezen we er in dit applicatieprofiel voor om waar mogelijk slechts één van beide varianten te gebruiken. Daarbij hanteren we de volgende algemene richtlijnen:

* De primaire WEMI-relaties leggen we **van het meest concrete niveau naar het meest abstracte niveau**. Anders gezegd, we maken een coherente beschrijving door een item te linken aan een manifestatie, een manifestatie aan een expressie en een expressie aan een werk.
* Relaties tussen WEMI-entiteiten  (werken, expressies, manifestaties, items) en actoren leggen we altijd **vanuit de WEMI-entiteit**.
* Werk-naar-werk-relaties leggen we **van het (kleinere) deel naar het (grotere) geheel** en **van het latere werk naar het eerdere werk**. Realiseer je dat sommige werk-werk-relaties zichzelf als inversie hebben.

Volgens deze uitgangspunten gebruikten we bijvoorbeeld wel `rdaw:P10053` (_has composer agent of work_) maar niet `rdaa:P50187` (_is composer agent of work of_), wel `rdaw:P10142` (_is adaptation of work_) en subelementen maar niet `rdaw:P10155` (_is adapted as work_) en subelementen.


## 3. Gelijkheidsrelaties

Er zijn verschillende manieren om aan te geven dat de beschreven entiteit gelijk of gelijkwaardig is aan een entiteit in een externe bron. We gaan hierbij uit van het gebruik van IRIs.  

De gangbare manier om aan te geven dat een entiteit gelijk is aan een externe entiteit is door gebruik te maken van de `owl:sameAs`-relatie.

	@prefix owl: <http://www.w3.org/2002/07/owl#> .
	
	intern:ex1 owl:sameAs extern:ex_a .  # identieke entiteiten

De semantiek van `owl:sameAs` is streng. Het betekent dat alle kenmerken van de éne entiteit uitwisselbaar zijn met die van de andere entiteit, en andersom. Gebruik `owl:sameAs` alleen als die uitwisselbaarheid niet alleen nu geldt, maar ook in verleden én toekomst. Als daar niet met zekerheid bevestigend op geantwoord kan worden dat is `owl:sameAs` niet de beste keuze.

Als de entiteiten equivalent zijn in de zin van betekenis en gebruik, maar mogelijk niet identiek in een strikte logische zin, dan is `skos:exactMatch` een goede keuze. Als er behoefte is aan een nog zwakkere relatie kan er gekozen worden voor `skos:closeMatch`, te gebruiken als de concepten sterk gelijkwaardig zijn maar niet volledig uitwisselbaar.

	@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
	
	intern:ex2 skos:exactMatch extern:ex_b . 
	intern:ex3 skos:closeMatch extern:ex_c . 


Het is niet strijdig met de principes van dit applicatieprofiel om via `owl:sameAs`-relaties equivalente kenmerken als alias te creëeren en toe te passen (zoals gedaan binnen [RDA applicatieprofiel Nederlandse bibliografie](https://netwerk-digitaal-erfgoed.github.io/rdanl/)), bijvoorbeeld om daarmee de leesbaarheid van de RDF voor mensen te vergroten.


## 4. Vormprincipes

### Typeer entiteiten expliciet

Om eventuele onduidelijkheden te voorkomen worden alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ex:ding is een RDA-Work


### Gebruik language-tags

RDA biedt een eigen manier om de taal van bijvoorbeeld en titel aan te geven. Binnen RDA kan dat door van de titel een nomen-entiteit te maken en daar dan het passende RDA-kenmerk aan te hangen. Binnen dit profiel geven we er de voorkeur aan om zo veel mogelijk al bestaande internetstandaarden en -gebruiken te volgen. De aanduiding van de taal van een literal gebeurt dan ook met zogenaamde language tags ([BCP47](https://www.rfc-editor.org/info/bcp47)). Bijvoorbeeld:

	ex:compositie rdaw:P10088 "Das wahre Leben des Johann Sebastian Bach"@de .


### Werken met datums en tijdspannes

RDA biedt de mogelijkheid om een "timespan"-entiteit te definiëren (`rdac:C10010`). Binnen dit applicatieprofiel is voorlopig het advies om daar beperkt gebruik van te maken. Voor 'gewone' datum zoals de datum van een uitvoering gebruiken we iso-geformatteerde datums, met toevoeging van de datatype-aanduiding,  zoals gangbaar in linked data. Laat het datatype weg, als de datum niet iso-geformatteerd is.

	ex:ding1 rdam:P30007 "1969"^^xsd:gYear .                         # copyright date, as a year
	ex:ding2 rdam:P30009 "1969-03-20"^^xsd:date .                    # publication date, as an iso date
	ex:ding3 rdaw:P10219 "195X".                                     # date of work - onzeker


Tijdspannes gebruiken we wanneer we zeer nadrukkelijk een periode willen beschrijven. Vaak is het handig om zo'n tijdspanne van een eigen IRI te voorzien omdat er doorgaans vaker naar verwezen zal moeten worden:

	ex:thing_2 rdaw:P10317 ex:tijdspanne1 .                         # timespan of work
	
	ex:tijdspanne1 
        a rdac:C10010 ;                                             # a timespan
       rdat:P70017 "Theaterseizoen 1957-1958"@nl ;                  # name of timespan
       rdat:P70039 "1957-10-01"^^xsd:date ;                         # start date of timespan
       rdat:P70040 "1958-07-01"^^xsd:date .                         # end date of timespan
    

### Bied een `rdfs:label`

Het gebruik van een goed gekozen `rdfs:label` per entiteit helpt de gebruiker om makkelijker de aard van het ding te begrijpen. Bemerk dat dikwijls de waarde van een RDA-ingang (een "access point"- die we dit profiel niet als zodanig gebruiken) vaak een prima keuze is voor het `rdfs:label`. Een `rdfs:label` zou ook gautomatiseerd samengesteld kunnen worden, bijvoorbeeld bij de export naar RDF uit het catalogiseersysteem. 

	ex:bladmuziek1 rdfs:label "Andriessen, Hendrik. Quartetto in stile antico. Muzieknotatie"@nl .

### Vermijd `rdfs:List`

In een beschrijving in RDF heeft de volgorde waarin elementen opgenomen staan geen betekenis. Een generiek toepasbare manier om volgorde aan te duiden is het gebruik van de `rdfs:List`-constructie. Gebruik leidt echter tot complexe, lastig te interpreteren structuren. De voorkeur is dus om `rdfs:List` zo veel mogelijk te vermijden. Zo biedt RDA bijvoorbeeld het element `rdaw:P10012`
"*has numbering of part*" om voor een deelwerk aan te geven op welke positie het deel uitmaakt van een hoofdwerk.


## 5. Tot slot: enige openstaande vragen

Dit applicatieprofiel is werk in uitvoering. Belangrijk aandachtspunten voor de doorontwikkeling om te komen tot één verbonden linked data-graaf voor de podiumkunsten zijn:

### Een volledige en op RDA-gebaseerde ontologie voor de podiumkunsten

In de huidige vorm, als een op linked data-gebaseerde standaard en toegepast binnen RDF, is de wereldwijd de ervaring met RDA nog beperkt. RDA wordt vooral gebruikt binnen de wereld van bibliotheken. Daar begint nu uit te kristalliseren hoe het bibliografische domein beschouwd kan worden vanuit IFLA-LRM (het conceptueel model achter RDA) en RDA. Binnen het domein van de podiumkunsten is nog niet uitgekristalliseerd hoe alle te te beschrijven zaken in entiteiten volgens LRM of RDA uitgedrukt kunnen worden. Bijvoorbeeld, hoe modelleren we een theaterproductie in RDA? Of hoe beschrijven we een requisiet uit een museumcollectie? Wanneer is een werk een werk? Beschrijven we een deel van een symfonie ook als een werk, met een eigen IRI? Kunnen een zakpartituur en een studiepartituur tot de zelfde expressie behoren?

Dit applicatieprofiel is in deze vorm vooral een eerste aanzet te komen tot een wijze van beschrijven van het domein van de podiumkunsten. Zie ook [aanzet voor de nog uit te werken sjablonen](rdf/templates)

### Terminologiebronnen en waardenlijsten

Om linked data met elkaar te kunnen delen, en zo tot een gedeelde linked data-graaf te komen, is het ook belangrijk om een gedeelde terminologie en gedeelde waardenlijsten of thesauri te gebruiken. Dit is werk in uitvoering.
