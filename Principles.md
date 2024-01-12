# Principes toepassingsprofiel RDA Podiumkunst

## Officiële RDA standaard
Dit toepassingsprofiel is gebaseerd op de officiële RDA standaard en de beschrijvingen van de klassen en elementen zoals te vinden op de [RDA Registry](http://www.rdaregistry.info/). De zogenaamde "deprecated" en "soft deprecated" elementen maken geen onderdeel uit van dit toepassingsprofiel. 

## Alle entiteiten worden expliciet getypeerd

Om eventuele onduidelijkheden te voorkomen worden alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ding is een Work

## Beperking actor-relaties

RDA biedt relaties in varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`. Deze variëteit is een linked data-toepassing niet zinvol en creëert onnodige complexiteit. In dit toepassingsprofiel beperken we ons daarom tot gebruik van enkel de relaties met de meest breed toepasbare waarden voor `rdfs:range` en `rdfs:domain`.

Ter illustratie kent RDA het element `rdaw:P10561` ("has television director family") met als `rdfs:range` de klasse `rdac:C10008` ("family"). Aangezien `rdac:C10008` een subklasse is van `rdac:C10002` ("agent") en er ook een element `rdaw:P10015` ("has television director agent") is, gebruiken we hier dat generiekere element. De lijst met te gebruiken RDA-elementen kan zo sterk beperkt worden, zonder af te doen aan de semantische zeggingskracht.

Bemerk dat sommige actor-relaties in RDA niet op het niveau van `rdac:C10002` ("agent") gedefinieerd zijn, omdat ze bijvoorbeeld alleen betekenis hebben op het niveau van een persoon.

## Verwijzingen van specifiek naar generiek

Relatie-elementen in RDA kennen vaak ook een element dat de inversie relatie aanduidt. Hoewel het semantisch geen verschil maakt of de relatie van `A` naar `B` of de inverse relatie van `B` naar `A` toegepast wordt, kiezen we om prakische redenen binnen dit toepassingsprofiel bijvoorkeur voor de volgende aanpak:

* Relaties tussen WEMI-entiteiten en Actor altijd vanuit WEMI-entitei leggen.
* Primaire WEMI-relaties leggen we “van onder naar boven”, dus van concreter niveau naar abstracter niveau. D.w.z. een item linken we aan manifestatie, manifestatie aan expressie en expressie aan werk.
*  Werk-naar-werk-relaties leggen we “van onder naar boven” wanneer er sprake is van een hiërarchie. Van “later werk” naar “eerder werk” .

Bemerke dat sommige relaties zichzelf als inverse hebben.

## Representatieve expressies

... TODO

## Access points

... TODO






