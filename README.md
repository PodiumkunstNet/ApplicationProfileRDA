# RDA-Applicatieprofiel Podiumkunst

*Werk in uitvoering / Concept 1 / [Podiumkunst.net](https://podiumkunst.net/) / 2024-01-18* 

## Inleiding
RDA, _Resource Description and Access_, is een pakket van data-elementen, richtlijnen en instructies voor het maken van metadata voor bibliotheken en erfgoedinstellingen, die voldoen aan internationale modellen voor gebruikersgerichte linked data-applicaties. RDA biedt veel keuzemogelijkheden bij toepassing van de standaard. Om in de praktijk met RDA te kunnen werken is het van belang die keuzes te maken en vast te leggen in een zogeheten **applicatieprofiel**. 

Het RDA-applicatieprofiel Podiumkunst richt zich op het verbinden van collecties van verschillende omvang, inhoud en volwassenheid in het domein van de podiumkunsten. In lijn met de [Digitaal Erfgoed Referentie Architectuur](https://netwerkdigitaalerfgoed.nl/activiteiten/dera/) (DERA) van het Netwerk Digitaal Erfgoed (NDE) wordt het fundament daarvan gevormd door **linked data**-principes. De **RDA**-standaard is gekozen als basis voor de datamodellering en voor het beschrijven van de collecties.

Door in het domein van de podiumkunsten met een gedeeld applicatieprofiel te werken, kunnen beschrijvingen van verschillende collecties op elkaar aangesloten worden. Het applicatieprofiel maakt het mogelijk te komen tot één gedeelde, organisatie- en collectieoverstijgende, linked data-graaf. Dit biedt veel voordelen voor uiteenlopende gebruikers van de data, zoals een onderzoeker, een geïnteresseerde leek of de bouwer van een app.

Dit RDA-applicatieprofiel voor de podiumkunsten is een initiatief van [Podiumkunst.net](https://podiumkunst.net/). Het is werk-in-uitvoering, een levend document. Het applicatieprofiel doet in deze vorm *(vrijwel) geen uitspraken* over de te kiezen terminologiebronnen voor waardenlijsten of thesauri. Een advies over gezamenlijk te hanteren terminologiebronnen is in voorbereiding.

Linked data- en semantischweb-representaties van de entiteiten, elementen en waardelijsten in RDA zijn beschikbaar via de [RDA Registry](http://www.rdaregistry.info/), de volledige tekst met alle richtlijnen en instructies is beschikbaar via de [RDA Toolkit](https://www.rdatoolkit.org/).

Aan dit applicatieprofiel hebben meegewerkt: *Sylvia Alting van Geusau ([Amsterdamse Hogeschool voor de Kunsten](https://ahk.nl/)), Eric van Balkum ([Muziekschatten](https://www.muziekschatten.nl/)), Sita Bhagwandin, ([Koninklijke Bibliothee](https://kb.nl/)), Remco de Boer([ArchiXL](https://archixl.nl)), Thomas op de Coul ([Muziekweb](https://muziekweb.nl/)), Mirjam Verloop ([Podiumkunst.net](https://podiumkunst.net/)), René Voorburg ([Podiumkunst.net](https://podiumkunst.net/)), Meta van der Waal-Gentenaar ([Koninklijke Bibliothee](https://kb.nl/)) en Lian Wintermans (zelfstandig muziek- en informatiespecialist, voorzitter [RDA-Commissie](https://rdacommissie.home.blog/)).*

## Gehanteerde principes
Een toepassingprofiel biedt een weloverwogen inperking of verfijning van een bestaande standaard. Principes achter dit profiel gericht op de toepassing van de RDA-standaard binnen het domein van de podiumkunsten worden [hier beschreven](Principles.md).

## Toepassingsprofiel als spreadsheet
De bouwstenen voor het gebruik van RDA zijn de **entiteiten** (zoals werk, expressie, manifestatie en item) en de **elementen** die *eigenschappen* of *relaties* vertegenwoordigen. Als basis voor dit toepassingsprofiel is daarom eerst, op basis van de [principes](Principles.md), bepaald welke elementen toe te passen en welke juist niet. Dit is uitgewerkt in een [spreadsheet](RDA-AP_Podiumkunst-net.xlsx).

Het spreadsheet geeft voor de belangrijkste RDA-entiteiten per element aan of het binnen dit toepassingsprofiel verplicht, aanbevolen, optioneel of juist niet gebruikt moet worden (MoSCoW). Er is daarbij onderscheid gemaakt tussen de *minimale beschrijving*, de *coherente beschrijving* en de *effectieve beschrijving* (zie ook de [principes](Principles.md)).

* [Download spreadsheet](RDA-AP_Podiumkunst-net.xlsx).

## Voorbeeldbeschrijvingen in RDA
Naast het spreadsheet biedt dit profiel voorbeelbeschrijvingen. Deze voorbeelden dienen zowel ter illustratie van het spreadsheet, als ook ter  aanvulling. De voorbeelden zijn gebaseerd op de praktijk van de deelnemers van de werkgroep gevormd rondom het toepassingsprofiel en zijn gezamenlijk besproken. Ze vormen een aanvulling op het spreadsheet in de zin dat ze de toepassing van RDA *in context* tonen en laten bovendien zien hoe gegevens binnen RDA vastgelegd kunnen worden. 

Zie [voorbeeldbestanden](rdf/examples).

## Code-fragmenten
In aanvulling op de voorbeeldbeschrijvingen biedt dit profiel ook enige code-fragmenten. Dit zijn praktische, kleine stukjes RDF, om te helpen bij het zelf opbouwen van een beschrijving in RDA, in lijn met dit profiel. Ze zijn nadrukkelijk *niet* bedoeld voor bijvoorbeeld catalogiseerders, wel voor degene die een catalogiseervoorziening inricht.

Zie [code-fragmenten](rdf/snippets).

## Aanzet tot sjablonen
Een streven is om te komen tot een beperkt aantal basisjablonen die gebruikt kunnen worden als kader bij het beschrijven van de verschillende soorten entiteiten die relevant zijn in de wereld van de podiumkunst.

Zie [aanzet voor de nog uit te werken sjablonen](rdf/templates).

