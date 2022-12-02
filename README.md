# Tietoliikenteen sovellusprojekti 2022 / Mika Väliaho

## Tavoitteet:

Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Opiskelijoiden tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. IoT-reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.

![image](https://user-images.githubusercontent.com/99818602/199468581-c733259f-269f-45a9-8278-99d370cc0fc4.png)

## Luokkittelematon data K-Means algoritmille:

Visualisoitu MatPlotLib:llä

![image](https://user-images.githubusercontent.com/99818602/203951779-796e9e43-5aba-46d2-bcbe-12dce3cd20e2.png)


Seuraavassa kuvassa on visualisoitu keskipisteiden uudelleenlaskenta 10k mittauspisteen randomoidulla datalla.

![image](https://user-images.githubusercontent.com/99818602/205254480-ed639436-7760-42de-9fff-95caaed848e5.png)

Kyseistä siirtymää tapahtuu hyvin minimaalisesti projektin datalle sen pienuuen vuoksi. Arvotut pisteet ovat lähtökohtaisesti jo hyvin lähelle oikeita paikkoja.
Ohessa kuva varsinaisen datan yhteydessä tapahtuneesta keskipisteen uudelleenlaskennasta.

![image](https://user-images.githubusercontent.com/99818602/205258427-fd7bc700-077f-40b2-a837-97a55b6fef20.png)
