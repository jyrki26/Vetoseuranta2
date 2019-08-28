# Käyttöohje

## Rekisteröityminen ja kirjautuminen

#### Paikallinen käyttäminen
Sovellukseen tulee luoda käyttäjä sql-tietokantaan SQLiten:n kautta komennolla:<br/>
INSERT INTO account (name, username, password, role_id) VALUES ('nimi', 'käyttäjänimi', 'salasana', 'rooli');<br/>
Nimen, käyttäjänimen ja salasanan voi asettaa haluamakseen. Mahdollisia rooleja on kaksi: 1 = ADMIN ja 2 = USER. ADMIN-roolilla pystyy käyttämään kaikkia sovelluksen ominaisuuksia, kun taas USER-roolilla ei pysty lisäämään ja muokkaamaan joukkueita. Ensimmäiseksi käyttäjäksi tulee siis luoda ADMIN-tyyppinen käyttäjä, jotta joukkueiden lisääminen tietokantaan onnistuu käyttöliittymän kautta. <br/>

Kun käyttäjä on luotu kirjaudutaan sovellukseen osoitteessa http://127.0.0.1:5000/.

#### Herokussa käyttäminen
Sovellus tulee olla asennettu Herokuun asennusohjeiden mukaisesti ja käyttäjä lisätty vastaavalla komennolla kuin paikallisesti käytettäessä sillä erotuksella, että lisääminen tehdään PostqreSQL:n kautta.


## Pääsivu
Kirjautumisen jälkeen sovellus siirtyy pääsivulle. Pääsivulla on linkit kaikkiin sovelluksen osioihin. Linkit löytyvät myös yläpalkin kautta.

## Joukkueiden hallinta
#### Lisää joukkue
Joukkueen lisääminen tapahtuu syöttämällä joukkueen nimi ja painamalla Lisää joukkue -nappia. Mikäli nimi täyttää validaatiot lisätään joukkue tietokantaan.
#### Näytä joukkueet
Näytä joukkueet-sivulla voi katsoa jo lisättyjä joukkueita ja tarvittaessa muokata joukkueiden nimiä. Muokkaaminen tapahtuu syöttämällä nimi Uusi nimi -kenttään ja painamalla Muuta nimi -nappia. Mikäli nimi täyttää validaatiot, muuttaa sovellus joukkueen nimen.

## Vetojen hallinta
Vetojen hallinnan käyttäminen edellyttää, että edellisen kohdan kautta on lisätty vähintään kaksi joukkuetta.
#### Lisää uusi veto
Lisää uusi veto -kohdassa voi lisätä uuden vedon. Vedon tietoihin täytyy syöttää ottelupäivä, panos ja vedon kerroin. Ottelupäivä syötetään muodossa dd.mm.yyyy. Panoksessa vedon kertoimessa voi olla korkeintaan kaksi desimaalia ja desimaalierottimena käytetään pistettä. Näiden lisäksi kotijoukkue ja vierasjoukkue, vedon tyyppi ja vedon tasoitus/veto lisätään pudotusvalikoista.

