# Tietoliikenteen sovellusprojekti 2022 / Mika Väliaho

## Tavoitteet:

Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Opiskelijoiden tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. IoT-reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa MySQL-tietokantaan.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoitukseen.

![image](https://user-images.githubusercontent.com/99818602/207807702-23a2ea11-1679-4214-8704-9ed2f99f2b62.png)

### Arduino kiihtyvyysmittaukset ja mittausten siirto radiorajapinnan yli
![image](https://user-images.githubusercontent.com/99818602/207810639-d100bd6d-40cf-4544-93b8-ad80415bb6ca.png)

Ensimmäisessä vaiheessa Arduino Uno mikrokontrollerin ja GY-61 kiihtyvyysanturin avulla mitattiin dataa kuudessa eri asennossa ja tämä data lähetettiin 433Mhz radiorajapinnan yli Rasberry Pi:n tehdylle IoT-reitittimelle, jossa data tallennettiin MySQL tietokantaan. Datan lähetykseen annettiin osittain valmis koodi joka koodattiin valmiiksi.

### Python HTTP Api client ja K-means algoritmi

Seuraavassa vaiheessa Pythonilla koodattiin lyhyt ohjelma joka haki HTTP Api kautta mittaustiedot ja tallensi ne CSV tiedostoon. K-means algoritmi koodattiin seuraavaksi ja sen avulla saatiin luetteloitua datasta kuusi eri datajoukkiota, joiden keskipisteet K-means algoritmi laski. 

![image](https://user-images.githubusercontent.com/99818602/207824741-c42fa3a4-6bbc-41e8-af50-aad3dd6c3271.png)

Kuvassa näkyy sinisellä mittausdatan pisteet ja punaiset tähdet edustavat algoritmin laskemia keskipisteitä.

![image](https://user-images.githubusercontent.com/99818602/207825510-300322cc-94bf-44de-b937-74cbdadd3434.png)

Oheissa kuvassa näkyy algoritmin keskipisteiden liikkuminen algoritmin käydessä iterointeja läpi. Koska alkuperäinen data on niin pieni ja keskipisteet löytyvät heti, kyseistä liikkummista ei tapahdu kuin vähäisessä määrin, joten kyseistä kuvaa varten generoitiin 10000 riviä satunnaisdataa. Punainen piste edustaa arvottua lähtöpistetä ja vihreä piste laskettua loppupistettä.

### K-means mallin implementointi Arduinolle

Seuraavassa vaihessa Pythonin K-means algoritmin antamat keskipisteet kirjoitettiin C++ yhteensopivaan muotoon ja toteutettiin malli Arduinolla. Malli toimi erinomaisesti ja osasi antaa vastauksena aina oikean kiihtyvyysanturin suunnan.

![image](https://user-images.githubusercontent.com/99818602/207831386-afe50f36-7329-4d54-a35a-a483319b6beb.png)

Kuvassa serial monitorin tulostamassa datassa ensimmäinen numero edustaa anturin oikeaa asentoa joka on käsin määritetty ja toinen arvo mallin antamaa ennustettua arvoa.

![image](https://user-images.githubusercontent.com/99818602/207832160-968f4622-442c-4f17-a1b8-b181ac9c8af5.png)

Lopputulokset kirjattiin tiedostoon ja tästä datasta laskettiin vielä Pythonin avulla confusion matrix, joka on oiva apu tulosten tarkasteluun.

### Loppusanat

Kaiken kaikkiaan projekti oli erittäin mielenkiintoinen ja monivivahteinen. Paljon asiaa opittavaksi ja varsinkin Pythonilla K-means algoritimin koodaaminen oli erittäinen mielenkiintoinen tehtävä, joka imaisi mukaansa.
