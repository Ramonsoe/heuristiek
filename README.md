# Smart Grid

In de toekomst wordt een toename verwacht van huizen met zelfvoorzienende energiebronnen. Een gevolg hiervan is dat er een overschot
in energie productie ontstaat. Dit overschot kan opgevangen worden door middel van batterijen, een woonwijk wordt bijvoorbeeld aangesloten op een netwerk met meerdere batterijen. Hoe ga je alle huizen zo efficiënt mogelijk aansluiten? Wat verandert er als kabels gedeeld kunnen worden?

### Vereisten  

De code kan opzich zelf uitgevoerd worden maar voor de visualisatie is Bokeh library nodig, deze staat in de requirements.txt.
Met de instructie *pip install -r requirements.txt* zal Bokeh worden toegevoegd.

### Structuur

Alle python code staat in de folder code, daar wordt een verdeling over classes en algorithmes en vervolgens over de deelopdrachten gemaakt. In de README van het mapje code staat beschreven wat er in de files te vinden is. De structuur is als volgt op te delen:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
    - **/code/algorithms/steponeandtwo**: Het random algoritme voor de eerste deelopdracht
    - **/code/algorithms/stepthreeandfour**: Find_Nearest en Algomanhattan
  - **/code/classes**: bevat alle classes die de algoritmes nodig hebben
    - **/code/classes/output**: Bevat de file die de output genereert in correcte vorm
    - **/code/classes/standardobjects**: Alle benodigde classes zijn in deze map te vinden
    - **/code/classes/steponeandtwo**: bevat de functie file voor het random algoritme
    - **/code/classes/stepthreeandfour**: bevat de function files voor de algoritmes die gebruik maken van kabel overlap
  - **/code/visualisation**: bevat de twee visualisatie files voor random en de andere algoritmes
- **/data**: Voor alle wijken zijn hier de huizen en batterijen te vinden in csv files en tekstbestanden

### Testen

Run de command *python main.py* om het programma te starten, volg daarna het command-line menu om de verschillende algorithmes te runnen voor elke wijk. De eerste keuze die de gebruiker krijgt is de keuze voor welke wijk een smartgrid gemaakt moet worden (1, 2 of 3).
Daarna volgt een keuze voor met kabel overlap of zonder kabel overlap. Met kabeloverlap is voor de eerste twee deelopdrachten van smartgrid, zonder kabel overlap voor de laatste twee. Gekozen voor met kabel overlap volgt de output en visualisatie van het random algoritme. Gekozen voor zonder kabel overlap volgt een keuze voor het manhattan algoritme of het find nearest algoritme. Daarna volgt een keuze voor het aantal iteraties. Hierna volgt bij het manhattan algoritme nog de keuze voor hoeveel stappe nhet dept first algoritme terug moet gaan. Dit moet tussen de 5 en 90 zijn om binnen een reele tijd tot een oplossing te komen.

Voorbeeld input: 2
2
1
1
20

De visualisatie zal automatisch in een html-pagina gegenereerd worden.

### Auteurs
**Team Heureka**  
*Ramon Soesan, Layla Hoogeveen & Leon Brakkee*

### Dankwoord

Onze dank gaat uit naar alle begeleiders die ons er doorheen sleepten als we vastliepen met concepten of coderen. In het bijzonder naar Bas & Angelo, onze begeleiders die altijd meedachten als we ergens meezaten.
