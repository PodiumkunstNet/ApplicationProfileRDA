# De principes achter toepassingsprofiel RDA Podiumkunst

## 0. Gebruik linked data
De standaard RDA kan in een traditionele recordsgebaseerde werkwijze ingezet worden. Dit toepassingsprofiel gaat uit van het werken met linked data (RDF) en linked data-principes.

Werken volgens linked data principes betekent onder andere dat relaties gelegd worden door middel van IRIs en niet met behulp van ingangen ("access points" in RDA).

## 1. Volg de officiële RDA standaard
Dit toepassingsprofiel is gebaseerd op de officiële RDA standaard en de beschrijvingen van de klassen en elementen zoals te vinden op de [RDA Registry](http://www.rdaregistry.info/). De zogenaamde "deprecated" en "soft deprecated" elementen maken geen onderdeel uit van dit toepassingsprofiel. 

### Werk vanuit beschrijvingsniveaus
Belangrijk in de benadering die RDA biedt, is dat beschrijvingen op verschillende niveaus van detaillering gemaakt kunnen worden. Daarbij wordt onderscheid gemaakt tussen:

* **Minimale beschrijving**: omvat alleen de meest essentiële elementen die nodig zijn om een bron uniek te identificeren,
* **Coherente beschrijving**:  biedt voldoende informatie om de bron te beschrijven binnen de context van de collectie en gebruikers in staat te stellen te beoordelen of de bron relevant is voor hun behoeften. Omvat onder andere relaties tussen de WEMI-entititeiten ('Work', 'Expression', 'Manifestation' en 'Item').
* **Effectieve beschrijving**: stelt gebruikers in staat om een diepgaand begrip van de bron te krijgen en hoe deze zich verhoudt tot andere bronnen.

### Gebruik van optioneel aanvullende vocabulaires

Dit RDA-toepassingsprofiel sluit gebruik van andere aanvullende vocabulaires niet uit, in die gevallen waarin dit een vereiste verrijking van de beschrijvingen oplevert die semantisch niet strijdig is met RDA. Zo is het bijvoorbeeld zeer welkom om beschrijvingen ook van een `rdfs:label` te voorzien.

Het is niet strijdig met de principes van dit toepassingsprofiel om via `owl:sameAs`-relaties equivalente kenmerken als alias te creëeren en toe te passen (zoals gedaan binnen [RDA toepassingsprofiel Nederlandse bibliografie](https://netwerk-digitaal-erfgoed.github.io/rdanl/)), bijvoorbeeld om daarmee de leesbaarheid van de RDF voor mensen te vergroten.


## 2. Typeer alle entiteiten expliciet

Om eventuele onduidelijkheden te voorkomen worden alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ex:ding is een RDA-Work

## 3. Gebruik beperkte set met actor-relaties

RDA biedt relaties in varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`. Deze variëteiten zijn een linked data-toepassing niet nodig en creëeen onnodige complexiteit. In dit toepassingsprofiel beperken we ons daarom tot gebruik van enkel die relaties met de meest breed toepasbare waarden voor `rdfs:range` en `rdfs:domain`.

Ter illustratie kent RDA het element `rdaw:P10561` ("has television director family") met als `rdfs:range` de klasse `rdac:C10008` ("family"). Aangezien `rdac:C10008` een subklasse is van `rdac:C10002` (actor / "agent") en er ook een element `rdaw:P10015` ("has television director agent") is, gebruiken we hier dat generiekere element. De lijst met te gebruiken RDA-elementen kan zo sterk beperkt worden, zonder af te doen aan de semantische zeggingskracht.

Bemerk dat sommige actor-relaties in RDA niet op het niveau van `rdac:C10002` ("agent") gedefinieerd zijn, omdat ze bijvoorbeeld alleen betekenis hebben op het niveau van een persoon. Gebruik hier de best passend relatie.

## 4. Verwijs van specifiek naar generiek

Relatie-elementen binnen RDA kennen vaak ook een element dat de inverse relatie aanduidt. Hoewel het semantisch geen verschil maakt of de relatie van `A` naar `B` of de inverse relatie van `B` naar `A` toegepast wordt, kiezen we binnen dit toepassingsprofiel om prakische redenen  bijvoorkeur voor de volgende aanpak:

* Relaties tussen WEMI ("work", "expression", "manifestation" en "item")-entiteiten en de actor altijd **vanuit WEMI-entiteit** leggen.
* Primaire WEMI-relaties leggen we “van onder naar boven”, dus **van concreter niveau naar abstracter niveau**. D.w.z. een item linken we aan manifestatie, manifestatie aan expressie en expressie aan werk.
*  Werk-naar-werk-relaties leggen we “**van onder naar boven**” wanneer er sprake is van een hiërarchie. Van “**later werk naar eerder werk”** .

Bemerk dat sommige relaties zichzelf als inverse hebben.


## 5. Principes voor identifiers

### Interne en externe identifiers

Een identifier is een uniek kenmerk of *label* dat gebruikt wordt om een specifieke entiteit te identificeren en te onderscheiden van andere entiteiten. Binnen linked data is het gangbaar en wenselijk dat vooral IRIs als identifier gebruikt worden.

In een metadata-beschrijving worden identifiers gebruikt om de beschreven entiteit *zelf* van een uniek kenmerk te voorzien, maar identifiers worden ook gebruikt om aan te geven dat het beschrevene gelijk - of gelijkwaardig - is aan een enititeit elders. Zo zijn er dus 'eigen' of interne identifiers enerzijds en externe identifiers anderzijds.

### Relaties voor gelijkheid of gelijkwaardigheid

Er zijn verschillende manieren om aan te geven dat de beschreven enititeit gelijk of gelijkwaardig is aan een enititeit die aangeduid wordt met een externe identifier.  


De gangbare manier om aan te geven dat een entiteit gelijk is aan een externe entiteit is door gebruik te maken van de `owl:sameAs`-relatie.

	@prefix owl: <http://www.w3.org/2002/07/owl#> .
	
	intern:ex1 owl:sameAs extern:ex_a . 

De semantiek van `owl:sameAs` is streng. Het betekent dat alle kenmerken van de éne entiteit uitwisselbaar zijn met die van de andere entiteit, en andersom. Gebruik `owl:sameAs` alleen als die uitwisselbaarheid niet alleen nu geldt, maar ook in verleden én toekomst. Als daar niet met zekerheid bevestigend op geantwoord kan worden dat is `owl:sameAs` niet de beste keuze.

Als de entiteiten equivalent zijn in de zin van betekenis en gebruik, maar mogelijk niet identiek in een strikte logische zin, dan is `skos:exactMatch` een goede keuze. Als er behoefte is aan een nog zwakkere relatie kan er gekozen worden voor `skos:closeMatch`, te gebruiken als de concepten sterk gelijkwaardig zijn maar niet volledig uitwisselbaar.

	@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
	
	intern:ex2 skos:exactMatch extern:ex_b . 
	intern:ex3 skos:closeMatch extern:ex_c . 


### Identifiers als label of literal

Externe entiteiten of concepten hebben hebben als identifier dikwijls een `rdfs:Literal` label en geen IRI. De relaties `owl:sameAs`, `skos:exactMatch` en `skos:closeMatch` kunnen dan niet gebruikt worden. RDA hier hier een oplossing in de vorm van de 




### Werken met RDA-identifiers





## 6. Uitgangspunten voor gebruik van datums en tijdspannes

TODO


## Representatieve expressies

... TODO

## Terminologie-bronnen

... TODO

## Tot slot: openstaande vragen

### Entity-boundaries

### Wijze van vastlegging








