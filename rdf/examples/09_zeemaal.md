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

Wanneer andere delen van de trilogie gerealiseerd worden, zullen die net als **ex:w50** als deel (is part of, **rdaw:P10019**) gerelateerd worden aan **ex:w52**.

Wat deze visualisatie verder in één oogopslag duidelijk maakt, is dat Sien Vanmaele (**ex:a50**) zowel de auteur van het toneelstuk is, als speler in de première-voorstelling.


![Visualisatie Structuur](../../assets/09_zeemaal_rda-rdf_visualisatie.png)


## Representatie in RDA-RDF

De typeringen van de online recensie:

    rdam:P30003 rdami:1001 ; # has mode of issuance: single unit
    rdam:P30002 rdamt:1003 ; # has media type: computer
    rdam:P30001 rdact:1018 ; # has carrier type: online resource

De datum van publicatie bevat in dit voorbeeld niet alleen een jaartal, maar ook maand en dag:

    rdam:P30011 "2022-07-18" ^^xsd:date ; # has date of publication: 18 juli 2022

Het toneelstuk heeft de volgende typeringen:

    rdaw:P10365 rdaep:1001 ; # has extension plan: static
    rdaw:P10004 rdaterm:1209 ; # has category of work: dramatic work

De voorstelling is als volgt beschreven:

    ex:e51 # Expressie no. 51
      a rdac:C10006 ;
      rdfs:label "Zeemaal: première-voorstelling, Antwerpen, 29 juni 2022" ;
      rdae:P20331 rdaterm:1153 ; # has category of expression: performance
      rdae:P20312 "Zeemaal" @nl ; # has title of expression
      rdae:P20214 "2022-06-29" ^^xsd:date ; # has date of expression: 29 juni 2022
      rdae:P20306 ex:p9 ; # has related place of expression: Antwerpen
      rdae:P20006 <http://id.loc.gov/vocabulary/iso639-2/dut> ; # has language of expression: Dutch
      rdae:P20012 ex:a50 ; # has actor agent: [acteur] Sien Vanmaele
      rdae:P20031 ex:a54 ; # has stage director agent: [toneelregisseur] Jo Roets
      rdae:P20035 ex:a55 ; # has musical director agent: [muzikaal director] Jason Dousselaere
      rdae:P20036 ex:a56 ; # has costume designer agent: [kostuumontwerper] Manuela Lauwers
      rdae:P20277 ex:a57 ; # has lighting designer agent: [lichtontwerper] Thomas Stevens
      rdae:P20324 "uitvoeringsmediumIRI nog toevoegen" ; # has medium of performance of choreographic [or non-musical dramatic] content
      rdae:P20005 "Vlaamse Juryselectie 22/23" @nl ; # has award
      rdae:P20071 "Zeemaal is een productie van Laika in coproductie met Theaterproductiehuis Zeelandia/Zeeland Nazomerfestival, Vlaams Cultuurhuis de Brakke Grond, Le Channel, scène nationale de Calais en Perpodium, met steun van de Vlaamse Gemeenschap en Tax Shelter van de Belgische federale overheid via Cronos Invest." @nl ; # has note on expression
      rdae:P20231 ex:w50 . # has work expressed

Nog niet alle bij de uitvoering betrokken actoren hebben een element in RDA voor het vastleggen van hun aandeel.

Zie bestand: [09_zeemaal.ttl](09_zeemaal.ttl)
