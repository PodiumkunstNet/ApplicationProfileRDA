# De principes achter toepassingsprofiel RDA Podiumkunst

## 0. Gebruik linked data
De standaard RDA kan in een traditionele recordsgebaseerde werkwijze ingezet worden. Dit toepassingsprofiel gaat uit van het werken met linked data en linked data-principes.

Werken volgens linked data principes betekent onder andere dat relaties gelegd worden door middel van IRIs en niet met behulp van ingangen ("access points").

## 1. Volg de officiële RDA standaard
Dit toepassingsprofiel is gebaseerd op de officiële RDA standaard en de beschrijvingen van de klassen en elementen zoals te vinden op de [RDA Registry](http://www.rdaregistry.info/). De zogenaamde "deprecated" en "soft deprecated" elementen maken geen onderdeel uit van dit toepassingsprofiel. 

### Werk vanuit beschrijvingsniveaus
Belangrijk in de benadering die RDA biedt, is dat beschrijvingen op verschillende niveaus van detaillering gemaakt kunnen worden. Daarbij wordt onderscheid gemaakt tussen:

* **Minimale beschrijving**: omvat alleen de meest essentiële elementen die nodig zijn om een bron uniek te identificeren,
* **Coherente beschrijving**:  biedt voldoende informatie om de bron te beschrijven binnen de context van de collectie en gebruikers in staat te stellen te beoordelen of de bron relevant is voor hun behoeften. Omvat onder andere relaties tussen de WEMI-entititeiten ('Work', 'Expression', 'Manifestation' en 'Item').
* **Effectieve beschrijving**: stelt gebruikers in staat om een diepgaand begrip van de bron te krijgen en hoe deze zich verhoudt tot andere bronnen.

### Gebruik optioneel aanvullende vocabulaires

Dit RDA-toepassingsprofiel sluit gebruik van andere aanvullende vocabulaires niet uit, in die gevallen waarin dit een vereiste verrijking van de beschrijvingen oplevert die semantisch niet strijdig is met RDA. Zo is het bijvoorbeeld raadzaam om beschrijvingen ook van een `rdfs:label` te voorzien.

Het is niet strijdig met de principes van dit toepassingsprofiel om via `owl:sameAs`-relaties equivalente kenmerken als alias te creëeren en toe te passen (cf. [RDA toepassingsprofiel Nederlandse bibliografie](https://netwerk-digitaal-erfgoed.github.io/rdanl/)), bijvoorbeeld om daarmee de leesbaarheid voor mensen te vergroten.


## 2. Typeer alle entiteiten expliciet

Om eventuele onduidelijkheden te voorkomen worden alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ex:ding is een RDA-Work

## 3. Beperk de actor-relaties

RDA biedt relaties in varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`. Deze variëteit is een linked data-toepassing niet zinvol en creëert onnodige complexiteit. In dit toepassingsprofiel beperken we ons daarom tot gebruik van enkel de relaties met de meest breed toepasbare waarden voor `rdfs:range` en `rdfs:domain`.

Ter illustratie kent RDA het element `rdaw:P10561` ("has television director family") met als `rdfs:range` de klasse `rdac:C10008` ("family"). Aangezien `rdac:C10008` een subklasse is van `rdac:C10002` ("agent") en er ook een element `rdaw:P10015` ("has television director agent") is, gebruiken we hier dat generiekere element. De lijst met te gebruiken RDA-elementen kan zo sterk beperkt worden, zonder af te doen aan de semantische zeggingskracht.

Bemerk dat sommige actor-relaties in RDA niet op het niveau van `rdac:C10002` ("agent") gedefinieerd zijn, omdat ze bijvoorbeeld alleen betekenis hebben op het niveau van een persoon.

## 4. Verwijs van specifiek naar generiek

Relatie-elementen in RDA kennen vaak ook een element dat de inversie relatie aanduidt. Hoewel het semantisch geen verschil maakt of de relatie van `A` naar `B` of de inverse relatie van `B` naar `A` toegepast wordt, kiezen we om prakische redenen binnen dit toepassingsprofiel bijvoorkeur voor de volgende aanpak:

* Relaties tussen WEMI-entiteiten en Actor altijd vanuit WEMI-entitei leggen.
* Primaire WEMI-relaties leggen we “van onder naar boven”, dus van concreter niveau naar abstracter niveau. D.w.z. een item linken we aan manifestatie, manifestatie aan expressie en expressie aan werk.
*  Werk-naar-werk-relaties leggen we “van onder naar boven” wanneer er sprake is van een hiërarchie. Van “later werk” naar “eerder werk” .

Bemerk dat sommige relaties zichzelf als inverse hebben.


## 5. Principes voor identifiers

TODO

## 6. Principes voor gebruik van datums en tijdspannes

TODO


## Representatieve expressies

... TODO

## Access points

... TODO

## Tot slot: openstaande vragen

### Entity-boundaries

### Wijze van vastlegging








