# Käyttöohje

## Rekisteröityminen ja kirjautuminen

#### Paikallinen käyttäminen
Sovellukseen tulee luoda käyttäjä sql-tietokantaan SQLiten:n kautta komennolla:<br/>
INSERT INTO account (name, username, password, role_id) VALUES ('nimi', 'käyttäjänimi', 'salasana', 'rooli');<br/>
Nimen, käyttäjänimen ja salasanan voi asettaa haluamakseen. Mahdollisia rooleja on kaksi: 1 = ADMIN ja 2 = USER. ADMIN-roolilla pystyy käyttämään kaikkia sovelluksen ominaisuuksia, kun taas USER-roolilla ei pysty lisäämään ja muokkaamaan joukkueita. Ensimmäiseksi käyttäjäksi tulee siis luoda ADMIN-tyyppinen käyttäjä, jotta joukkueiden lisääminen tietokantaan onnistuu käyttöliittymän kautta. <br/>

Kun käyttäjä on luotu kirjaudutaan sovellukseen osoitteessa http://127.0.0.1:5000/.

#### Herokussa käyttäminen
Sovellus tulee olla asennettu Herokuun asennusohjeiden mukaisesti ja käyttäjä lisätty vastaavalla komennolla kuin paikallisesti käytettäessä sillä erotuksella, että lisääminen tehdään PostqreSQL:n kautta.
