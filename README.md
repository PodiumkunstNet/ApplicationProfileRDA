# RDA-Applicatieprofiel Podiumkunst

*versie 1.1 / [Podiumkunst.net](https://podiumkunst.net/) / 2025-07-24* 

## Inhoud

- [Inleiding](#inleiding)
- [Podiumkunst.net RDA-applicatieprofiel](#podiumkunst)
- [Uitgangspunten](#uitgangspunten)
- [Applicatieprofiel als spreadsheet](#spreadsheet)
- [Voorbeeldbeschrijvingen in RDA](#voorbeelden)
- [Code-fragmenten](#code)
- [Aanzet tot sjablonen](#sjablonen)
- [Relevante documentatie](#documentatie)
- [Colofon](#colofon)


<a id="inleiding"></a>
## Inleiding
RDA (Resource Description and Access) is een verzameling van regels en richtlijnen voor het maken van metadata voor bibliotheken en erfgoedinstellingen. Deze metadata voldoet zo aan internationale standaarden voor linked data. Dat maakt informatie beter vindbaar en bruikbaar voor gebruikers. 

De RDA-standaard biedt veel opties. Om RDA goed toe te passen in de praktijk, is het belangrijk om daarin keuzes te maken en die vast te leggen in een zogenaamd **applicatieprofiel** (ook wel **toepassingsprofiel** genoemd).

In zo’n applicatieprofiel staat bijvoorbeeld:

- welke soorten informatie (entiteiten) wel of niet gebruikt worden,
- welke gegevens verplicht, optioneel of juist weggelaten worden,
- hoe de gegevens worden ingevoerd,
- en welke termenbronnen bij bepaalde velden gebruikt mogen of moeten worden.

Zo'n profiel is bedoeld voor metadataspecialisten, zoals mensen die werken aan de inrichting van een catalogiseersysteem of collectiebeheersysteem. Er wordt van hen verwacht dat ze basiskennis hebben van linked data. 

<a id="podiumkunst"></a>
## Podiumkunst.net RDA-applicatieprofiel

Het Podiumkunst.net RDA-applicatieprofiel is bedoeld om collecties van podiumkunsteninstellingen — groot of klein, simpel of complex — met elkaar te verbinden. Dit gebeurt volgens de principes van **linked data**, zoals beschreven in de [Digitaal Erfgoed Referentie Architectuur](https://netwerkdigitaalerfgoed.nl/activiteiten/dera/) (DERA) van het Netwerk Digitaal Erfgoed (NDE). Voor het beschrijven en structureren van de gegevens is gekozen voor de **RDA**-standaard. RDA biedt verschillende implementatiescenario's. Voor dit profiel is gekozen voor het Linked Open Data-scenario (implementatiescenario A), waarbij de gegevens als Linked Open Data worden gepubliceerd.

Door in de podiumkunstensector met één gezamenlijk applicatieprofiel te werken, kunnen beschrijvingen van verschillende collecties goed op elkaar aansluiten. Zo ontstaat er één gedeelde, organisatie- en collectieoverstijgende linked data-structuur (ook wel graaf genoemd). Dit biedt veel voordelen voor uiteenlopende gebruikers van de data, zoals makers in de podiumkunsten, onderzoekers, geïnteresseerden of bouwers van een website of app.

Dit RDA-applicatieprofiel voor de podiumkunsten is een initiatief van [Podiumkunst.net](https://podiumkunst.net/). Het is werk-in-uitvoering, een levend document.
Het applicatieprofiel doet in deze vorm *(vrijwel) geen uitspraken* over de te kiezen terminologiebronnen of thesauri. Een advies hierover volgt later.

Linked data- en semantischweb-representaties van de entiteiten, elementen en waardenlijsten in RDA zijn beschikbaar via de [RDA Registry](http://www.rdaregistry.info/), de volledige tekst met alle richtlijnen en instructies is beschikbaar via de [RDA Toolkit](https://www.rdatoolkit.org/).

* [Lees meer over het applicatieprofiel](https://www.podiumkunst.net/nieuws/de-basis-van-de-bibliotheek-met-de-nuances-van-het-toneel-het-podiumkunst-net-applicatieprofiel/) 

<a id="uitgangspunten"></a>
## Uitgangspunten
Een applicatieprofiel is een doordachte manier om een bestaande standaard aan te passen of te verfijnen voor een specifieke toepassing. De uitgangspunten van dit profiel richten zich op het toepassen van de RDA-standaard binnen het domein van de podiumkunsten, en zijn [hier beschreven](Principles.md).

<a id="spreadsheet"></a>
## Applicatieprofiel als spreadsheet
De bouwstenen voor het gebruik van RDA zijn de **entiteiten** en de **elementen** die *eigenschappen* of *relaties* vertegenwoordigen. Als basis voor dit toepassingsprofiel is daarom eerst, op basis van de [principes](Principles.md), bepaald welke elementen toe te passen en welke juist niet. Dit is vastgelegd in een [spreadsheet](./assets/RDA-AP_Podiumkunst-net.xlsx) volgens deze [aanpak](Spreadsheet.md).

Het spreadsheet geeft voor de belangrijkste RDA-entiteiten (werk, expressie, manifestatie en item) per element aan of het binnen dit toepassingsprofiel verplicht, aanbevolen, optioneel of juist niet gebruikt moet worden (MoSCoW) en welke registratiemethoden voor dat element verplicht, aanbevolen, optioneel of niet toegestaan zijn. In een later stadium zullen profielen voor de andere entiteiten toegevoegd worden.

Verder wordt er, in lijn met RDA, onderscheid gemaakt tussen verschillende niveaus van beschrijving: de *minimale beschrijving*, de *coherente beschrijving* en de *effectieve beschrijving* (zie ook de [principes](Principles.md)).

* [Lees meer over de gevolgde aanpak](Spreadsheet.md)
* [Download het spreadsheet](./assets/RDA-AP_Podiumkunst-net.xlsx)

<a id="voorbeelden"></a>
## Voorbeeldbeschrijvingen in RDA
Naast het spreadsheet biedt dit applicatieprofiel voorbeelden en toelichtingen. Deze voorbeelden dienen zowel ter illustratie van het spreadsheet, als ook ter aanvulling. De voorbeelden zijn door de muziek- en theaterexperts uit de werkgroep aangedragen. Ze laten zien hoe bepaalde materialen maximaal verbonden en beschreven kunnen worden volgens RDA. In een later stadium zullen varianten op de voorbeelden toegevoegd worden die illustreren hoe minder gedetailleerd ontsloten collecties beschreven kunnen worden. 

Zie de [voorbeeldbeschrijvingen](rdf/examples).

<a id="code"></a>
## Code-fragmenten
In aanvulling op de voorbeeldbeschrijvingen biedt dit applicatieprofiel ook enige code-fragmenten. Dit zijn kleine, praktische stukjes RDF, om te helpen bij het zelf opbouwen van een beschrijving in RDA in lijn met dit profiel. Ze zijn nadrukkelijk *niet* bedoeld voor bijvoorbeeld catalogiseerders, wel voor degenen die een catalogiseervoorziening of ETL-proces inrichten.

Zie de [code-fragmenten](rdf/snippets).

<a id="sjablonen"></a>
## Aanzet tot sjablonen
We streven ernaar te komen tot een aantal basis-sjablonen die gebruikt kunnen worden als kader bij het beschrijven van de verschillende soorten entiteiten die relevant zijn in de wereld van de podiumkunst.

<a id="documentatie"></a>
## Relevante documentatie
* [Evenementen in RDA](https://www.podiumkunst.net/nieuws/dans-theater-en-muziekevenementen-de-verschillen-en-overeenkomsten-in-een-metadata-model/)


<a id="colofon"></a>
## Colofon
Aan dit applicatieprofiel hebben meegewerkt: *Sylvia Alting van Geusau ([Amsterdamse Hogeschool voor de Kunsten](https://ahk.nl/)), Eric van Balkum ([Muziekschatten](https://www.muziekschatten.nl/)), Sita Bhagwandin ([Koninklijke Bibliotheek](https://kb.nl/)), Remco de Boer ([ArchiXL](https://archixl.nl)), Thomas Op de Coul (Beeld & Geluid / [Muziekweb](https://muziekweb.nl/)), Mirjam Verloop ([Podiumkunst.net](https://podiumkunst.net/)), René Voorburg ([Podiumkunst.net](https://podiumkunst.net/)), Meta van der Waal-Gentenaar ([Koninklijke Bibliotheek](https://kb.nl/)) en Lian Wintermans (zelfstandig muziek- en informatiespecialist, voorzitter [RDA-Commissie](https://rdacommissie.home.blog/)).*


<!-- Zie de [aanzet voor de nog uit te werken sjablonen](rdf/templates). -->

