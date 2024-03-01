# Zeemaal

Bestand: [09_zeemaal.ttl](09_zeemaal.ttl)

## De resource

In dit voorbeeld hebben we te maken met twee resources: een uitgave van het toneelstuk Zeemaal en een recensie van de première van datzelfde stuk. Een exemplaar van de uitgave bevindt zich in de collectie van de Academie voor Theater en Dans. De recensie is online verschenen in de Theaterkrant.

Er zijn naast de Theaterkrant nog allerlei andere resources die een relatie met Zeemaal hebben: het is het eerste deel in een trilogie, de tekst verscheen in de reeks De Nieuwe Toneelbibliotheek en de première vond plaats tijdens het festival Zomer van Antwerpen. De relaties met de Theaterkrant, De Nieuwe Toneelbibliotheek (reeks) en het festival Zomer van Antwerpen zijn in deze uitwerking buiten beschouwing gelaten. 

## Entiteitenstructuur

Allereerst onderscheiden we in dit voorbeeld de primaire WEMI-relaties voor beide resources.

Het exemplaar van de Academie voor Theater en Dans (**ex:i50**) stelt de uitgave van de Nieuwe Toneelbibliotheek voor (**ex:m50**). Deze uitgave verwezenlijkt de Nederlandse tekst (**ex:e50**) die het toneelstuk Zeemaal (**ex:w50**) realiseert.

De recensie is een online publicatie (**ex:m51**) die de Nederlandse tekst (**ex:e52**) verwezenlijkt van het recensiewerk (**ex:w51**). Voor het ontbreken van items bij online publicaties, zie de toelichting bij [_Review of Malcolm Boyd on Bach chorales_](05_review-harmonizing-bach.md).

RDA beschouwt uitvoeringen van muziek- en theaterwerken als expressies. De première van Zeemaal (**ex:e51**) is dus een afzonderlijke expressie die, net als de tekst (**ex:e50**), het toneelstuk (**ex:w50**) realiseert. Omdat er geen opnamen van de première bekend zijn, kunnen we geen manifestatie identificeren.

Omdat de recensie specifiek betrekking heeft op de première is (anders dan bij [_Review of Malcolm Boyd on Bach chorales_](05_review-harmonizing-bach.md)) werk **ex:w51** verbonden met expressie **ex:e51** met behulp van "is evaluation of" (**rdaw:P10279**).

Wanneer andere delen van de trilogie gerealiseerd worden, zullen die, net als **ex:w50**, als deel (is part of, **rdaw:P10019**) gerelateerd worden aan **ex:w52**.

Wat deze visualisatie verder in één oogopslag duidelijk maakt, is dat Sien Vanmaele (**ex:a50**) zowel de auteur van het toneelstuk is, als speler in de première-voorstelling.


![Visualisatie Structuur](../../assets/09_zeemaal_rda-rdf_visualisatie.png)


## Representatie in RDA-RDF

Enige opmerkingen over de representatie in RDA-RDF.

{ TODO} 


Zie bestand: [09_zeemaal.ttl](09_zeemaal.ttl)
