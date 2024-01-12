# Principes toepassingsprofiel RDA Podiumkunst

## Alle entiteiten worden expliciet getypeerd

Om eventuele onduidelijkheden te voorkomen moeten alle entiteiten van een expliciete typering voorzien worden, bijvoorbeeld:

	ex:ding a rdac:C10001 .   # ding is een Work

## Beperking actor-relaties

RDA biedt relaties in varianten die enkel verschillen in `rdfs:domain` en `rdfs:range`. Deze variëteit is een linked data-toepassing niet zinvol en creëert onnodige complexiteit. In dit toepassingsprofiel beperken we ons daarom tot gebruik van enkel de relaties met de meest breed toepasbare waarden voor `rdfs:range` en `rdfs:domain`.



