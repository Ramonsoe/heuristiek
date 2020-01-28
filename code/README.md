## Code

Alle code is verdeeld over de deelopdrachten. Dit is terug te zien in de structuur van de repository: mappen met de naam *steponeandtwo* horen bij de eerste twee deelopdrachten, *stepthreeandfour* bij de laatste twee deelopdrachten.

### Classes
In de folder *standardobjects* staan de files die voor alle deelopdrachten nodig zijn. Hier worden alle objecten gecreëerd.
In de mappen *steponeandtwo* en *stepthreeandfour* staan files met functies die voor de algoritmes zijn gebruikt.

### Algorithms  
In de eerste twee deelopdrachten is het de bedoeling om alle huizen aan een batterij te verbinden. Dit gebeurt in *randomgrid.py*, er wordt per batterij een random huis gekozen. Vervolgens wordt er een verbinding gemaakt, hierbij worden de huizen in de batterij geplaatst en daarna worden pas daadwerkelijk kabels getrokken.

De hieronder beschreven algoritmes zijn voor de laatste twee deelopdrachten. In deze deelopdrachten mogen huizen kabels delen.

Manhattan dept-first algorithm: in dit algoritme wordt bij elke stap de kortst mogelijke connectie tussen een huis en een powersource        gemaakt. Powersources zijn hier de batterijen, aangesloten huizen en gelegde kabels. Als het algoritme geen oplossing kan vinden, gaat het algoritme n stappen terug, waar n door de gebruiker is aangegeven. 

Find nearest algorithm: in dit algoritme wordt er bij elke stap een random -nog niet aangesloten- huis geselecteerd en vervolgens wordt deze aangesloten aan de dichtbijzijnde nog beschikbare powersource. 

### Visualisation
Tevens in visualisation is er een scheiding van de opdracht, het randomalgoritme wordt geplot met de random file in visualisation en find_nearest en algomanhattan met de manhattan file.
