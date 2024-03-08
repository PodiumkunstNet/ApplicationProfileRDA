# De principes achter het RDA-applicatieprofiel Podiumkunst

## 0. Gebruik linked data
De standaard RDA kan goed in een traditionele recordsgebaseerde werkwijze ingezet worden, maar dit applicatieprofiel gaat uit van een toepassing als  linked data (RDF) en de bijbehordende **linked data-principes**. Dat betekent onder andere dat er **entiteiten** gedefinieerd worden voor de centrale objecten die beschreven worden. Deze entiteiten worden geïdentificeerd met een **IRI**, een identifier in de vorm van een URL (webadres).

Niet alles in linked data is per sé een entiteit met een IRI. Sommige entiteiten hebben alleen maar betekenis in de context van één bovenliggende entiteit. In zo'n geval kan er voor gekozen worden die entiteit geen IRI te geven. Dit bespaart op beheer. Bedenk dat IRI's geacht worden om **duurzame identifiers** te zijn. Dat komt noodzakelijkerwijs met administratieve en technische lasten. Soms is de keuze voor een `blank node`, een entiteit zonder IRI, dus verstandig (zie het voorbeeld verderop over Identifiers). Daarnaast is het om praktische redenen niet, of nog niet, doenlijk om van alles een entiteit te maken. Zo wordt de bladmuziek van [Muziekschatten.nl](https://www.muziekschatten.nl/) als volwaardige entiteiten beschreven maar wordt er van de uitgevers van de bladmuziek slechts de naam genoemd, zonder deze als een entiteit te representeren. De praktische keuze die hier gemaakt is heeft onder andere te maken met een gebrek aan voldoende passende **terminologiebronnen** of **theasauri**.


## 1. Volg de officiële RDA-standaard
Dit applicatieprofiel is gebaseerd op de beschrijvingen van de klassen en elementen en op de instructies, richtlijnen en waardelijsten in de [officiële RDA-standaard](http://access.rdatoolkit.org/). De zogeheten "*deprecated*" en "*soft deprecated*" elementen maken geen onderdeel uit van dit applicatieprofiel. 

### Werk vanuit beschrijvingsniveaus
Belangrijk in de benadering die RDA biedt, is dat beschrijvingen op verschillende niveaus van detaillering gemaakt kunnen worden. Daarbij wordt onderscheid gemaakt tussen:

* **Minimumbeschrijving**: omvat alleen de meest basale elementen die nodig zijn om een entiteit te beschrijven,
* **Coherente beschrijving**: verbindt de primaire werk-, expressie-, manifestatie- en item-entiteiten die bij een resource (~*bron*)horen met elkaar,
* **Effectieve beschrijving**: stelt gebruikers in staat om een resource beter te vinden, uitgebreider te identificeren en in een context te plaatsen, ook krijgt de gebruiker informatie over de toegang tot een resource.

In dit applicatieprofiel wordt de **effectieve beschrijving** onderverdeeld in verschillende met elkaar samenhangende "lagen", van generiek of algemeen geldend naar specifiek voor bepaalde typen werken (bv. muziekwerken) of dragers (zoals boeken of cd's).

De **minimumbeschrijving** en de **coherente beschrijving** zijn verplicht in het RDA-Applicatieprofiel Podiumkunst (een "must") en komen overeen met "vindbaar" in de terminologie van het Netwerk Digitaal Erfgoed. De **effectieve beschrijving** is aanbevolen (een "should") ofwel verplicht indien de data voorhanden is en komt overeen met het [NDE-begrip "bruikbaar"](https://netwerkdigitaalerfgoed.nl/bruikbaar/).

De verplichting van een element in het applicatieprofiel geldt binnen de context van de gegeven laag. Dus wanneer bijvoorbeeld de oorspronkelijke bezetting van een muziekwerk verplicht is, geldt dat alleen wanneer je de effectieve beschrijving van een muziekwerk toepast. Wanneer je deze laag uit het applicatieprofiel niet gebruikt, bijvoorbeeld omdat je geen muziekwerk beschrijft of omdat je je praktisch tot de minimaal verplichte lagen van de minimumbeschrijving en de coherente beschrijving moet beperken, geldt ook de verplichting van dit element niet.

### Gebruik van aanvullende linked data-standaarden

Dit RDA-applicatieprofiel sluit het gebruik van andere aanvullende linked data-standaarden niet uit, in die gevallen waarin dit een vereiste verrijking van de beschrijvingen oplevert die semantisch niet strijdig is met RDA. Zo is het bijvoorbeeld zeer welkom om beschrijvingen ook van een `rdfs:label` te voorzien.

Het is niet strijdig met de principes van dit applicatieprofiel om via `owl:sameAs`-relaties equivalente kenmerken als alias te creëeren en toe te passen (zoals gedaan binnen [RDA applicatieprofiel Nederlandse bibliografie](https://netwerk-digitaal-erfgoed.github.io/rdanl/)), bijvoorbeeld om daarmee de leesbaarheid van de RDF voor mensen te vergroten.

## 2. Uitgangspunten ten aanzien van identifiers

### Achtergrond: interne en externe identifiers

Een identifier is een uniek kenmerk of *label* dat gebruikt wordt om een specifieke entiteit te identificeren en te onderscheiden van andere entiteiten. Binnen linked data is het gangbaar en wenselijk dat vooral IRI's als identifier gebruikt worden.

In een metadata-beschrijving worden identifiers gebruikt om de beschreven entiteit *zelf* van een uniek kenmerk te voorzien, maar identifiers worden ook gebruikt om aan te geven dat het beschrevene gelijk - of gelijkwaardig - is aan een enititeit elders. Zo zijn er dus 'eigen' of interne identifiers enerzijds en externe identifiers anderzijds.

RDA onderscheidt vier verschillende registratiemethoden voor het vastleggen van de waarde in een element:
* Ongestructureerde beschrijving: een combinatie van transcriptie (tekst overgenomen uit de resource) en vrije tekst,
* Gestructureerde beschrijving: gestandaardiseerde tekst ontleend aan vocabulaires en coderingssystemen, zoals een term of naam uit een thesaurus,
* Identifier: codes of nummers ter identificatie, dit kunnen locale identifiers (zoals recordnummers) zijn of gestandaardiseerde identifiers als ISBN, ISSN, nummeraanduidingen van muziekwerken etc.,
* IRI: Internationalized Resource Identifier, ofwel persistente links die door machines geïnterpreteerd kunnen worden.

Een voorbeeld van een mogelijke invulling van de verschillende registratiemethoden voor een specifieke elementwaarde:


### Relaties voor gelijkheid of gelijkwaardigheid

Er zijn verschillende manieren om aan te geven dat de beschreven entiteit gelijk of gelijkwaardig is aan een entiteit die aangeduid wordt met een externe identifier.  


De gangbare manier om aan te geven dat een entiteit gelijk is aan een externe entiteit is door gebruik te maken van de `owl:sameAs`-relatie.

	@prefix owl: <http://www.w3.org/2002/07/owl#> .
	
	intern:ex1 owl:sameAs extern:ex_a .  # identieke entiteiten

De semantiek van `owl:sameAs` is streng. Het betekent dat alle kenmerken van de éne entiteit uitwisselbaar zijn met die van de andere entiteit, en andersom. Gebruik `owl:sameAs` alleen als die uitwisselbaarheid niet alleen nu geldt, maar ook in verleden én toekomst. Als daar niet met zekerheid bevestigend op geantwoord kan worden dat is `owl:sameAs` niet de beste keuze.

Als de entiteiten equivalent zijn in de zin van betekenis en gebruik, maar mogelijk niet identiek in een strikte logische zin, dan is `skos:exactMatch` een goede keuze. Als er behoefte is aan een nog zwakkere relatie kan er gekozen worden voor `skos:closeMatch`, te gebruiken als de concepten sterk gelijkwaardig zijn maar niet volledig uitwisselbaar.

	@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
	
	intern:ex2 skos:exactMatch extern:ex_b . 
	intern:ex3 skos:closeMatch extern:ex_c . 


### Identifiers als label of literal

Externe entiteiten of concepten hebben hebben als identifier dikwijls een `rdfs:Literal`-label en geen IRI. De relaties `owl:sameAs`, `skos:exactMatch` en `skos:closeMatch` kunnen dan niet gebruikt worden. Om in deze gevallen gelijkheid van gelijkwaardigheid aan te duiden gebruiken we het RDA element `rdax:P00018` "has identifier for RDA entity". Dit kan eenvoudig op de volgende wijze gebruikt worden:

	
	intern:ex4 rdax:P00018 "12345-78-9" . 

Probleem hierbij is dat niet duidelijk is wat "12345-78-9" is. Binnen dit applicatieprofiel is die constructie daarom alleen toegestaan voor interne identifiers (anders dan IRI's). Voor externe identifiers moet daarom het volgende partroon worden gevolgd waarbij via een Nomen-entiteit de benodigde informatie over de identifier verstrekt kan worden:

	# dit voorbeeld geeft aan dat "12345-78-9" een barcode is:
	intern:ex4 rdax:P00018 [
		a rdac:C10012 ;                                     # dit is een nomen
		rdan:P80068 "12345-78-9" ;                          # "has nomen string" , de identifier
		rdan:P80069 <http://vocab.getty.edu/aat/300417443>  # "scheme of Nomen" 
	] .

Het is niet nodig een IRI aan de nomen-entiteit toe te kennen, daarom is er hier gekozen om een zogenaamde `blank node`-entiteit te creëeren. 

NB: Het streven is om te komen tot vaste waardenlijsten voor de "*scheme of Nomen*." 

## 3. Keuzes ten aanzien van de toepassing van RDA

### Beperk de set met relaties

RDA biedt relaties in varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`. Deze variëteiten zijn een linked data-toepassing niet nodig en creëeen onnodige complexiteit. In dit applicatieprofiel beperken we ons daarom tot gebruik van enkel die relaties met de meest breed toepasbare waarden voor `rdfs:range` en `rdfs:domain`.

Ter illustratie kent RDA het element `rdaw:P10561` ("*has television director family*") met als `rdfs:range` de klasse `rdac:C10008` ("*family*"). Aangezien `rdac:C10008` een subklasse is van `rdac:C10002` (actor / "*agent*") en er ook een element `rdaw:P10015` ("*has television director agent*") is, gebruiken we hier dat generiekere element. De lijst met te gebruiken RDA-elementen kan zo sterk beperkt worden, zonder af te doen aan de semantische zeggingskracht.

Bemerk dat sommige actor-relaties in RDA niet op het niveau van `rdac:C10002` ("*agent*") gedefinieerd zijn, omdat ze bijvoorbeeld alleen betekenis hebben op het niveau van een persoon. Gebruik hier de best passend relatie.

Volgens deze logica wordt binnen dit applicatieprofiel gekozen voor de gebruik van de generieke relaties `rdax:P00014` "*subject of*" en `rdax:P00018`.

### Beschrijf representatieve expressies op werkniveau

Kenmerken van representatieve expressies leggen we vast op werkniveau. Dat wil zeggen, we gebruiken de attribuut-elementen in het werkdomein met "... of representative expression" in de naam. We houden er rekening mee dat gegevens over de representatieve expressie niet altijd beschikbaar zullen zijn. De belangrijkste reden voor vastlegging op werkniveau is dat we het beheer ervan willen koppelen aan het beheer van de werken. We willen voorkomen dat dataleveranciers elk naar eigen inzicht expressies als representatief gaan markeren of dat er “verkeerde” manifestaties of actoren aan gelinkt worden.

### Gebruik geen benamingen die bij andere RDA-implementatiescenario's horen

RDA biedt de mogelijkheid om entiteiten te identificeren met een "ingang" (of "*authorized access point*"). Dergelijke ingangen spelen een belangrijke rol bij RDA-toepassingen in traditionele bibliotheekcatalogi en zijn opgebouwd volgens een vast stramien, doorgaans bestaande uit elementen die ook in afzonderlijke properties vastgelegd worden.

### Verwijs van specifiek naar generiek

Relatie-elementen binnen RDA kennen vaak ook een element dat de inverse relatie aanduidt. Hoewel het semantisch geen verschil maakt of de relatie van `A` naar `B` of de inverse relatie van `B` naar `A` toegepast wordt, kiezen we binnen dit applicatieprofiel om prakische redenen  bijvoorkeur voor de volgende aanpak:

* Relaties tussen WEMI ("work", "expression", "manifestation" en "item")-entiteiten en de actor altijd **vanuit WEMI-entiteit** leggen.
* Primaire WEMI-relaties leggen we “van onder naar boven”, dus **van concreter niveau naar abstracter niveau**. D.w.z. een item linken we aan manifestatie, manifestatie aan expressie en expressie aan werk.
*  Werk-naar-werk-relaties leggen we “**van onder naar boven**” wanneer er sprake is van een hiërarchie. Van “**later werk naar eerder werk”** .

Bemerk dat sommige relaties zichzelf als inverse hebben.

## 4. Vormprincipes

### Typeer entiteiten expliciet

Om eventuele onduidelijkheden te voorkomen worden alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ex:ding is een RDA-Work


### Gebruik language-tags

RDA biedt een eigen manier om de taal van bijvoorbeeld en titel aan te geven. Binnen RDA kan dat door van de titel een nomen-eniteit te maken en daar dan het passende RDA-kenmerk aan te hangen. Binnen dit profiel geven we er de voorkeur aan om zo veel mogelijk al bestaande internetstandaarden en -gebruiken te volgen. De aanduiding van de taal van een literal gebeurt dan ook met zogenaamde language tags ([BCP47](https://www.rfc-editor.org/info/bcp47)). Bijvoorbeeld:

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








