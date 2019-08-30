# Asennusohje

## Sovelluksen ja tietokannan ohjelmisto
Sovellus on toteutettu Python 3.7.4 versiolla käyttäen Flask-kirjastoa. Paikallisessa versiossa tietokantaohjelmistona toimii SQLite ja Herokun versiossa PostgreSQL. Sovelluksen käyttäminen edellyttää, että edellä mainitut ohjelmistot on asennettu käyttöympäristöön.

## Asennus paikallisesti
Sovelluksen voi ladata GitHubista osoitteesta https://github.com/jyrki26/Vetoseuranta2 valitsemalla Clone or download -kohdan ja lataamalla zip-tiedoston. Tämän jälkeen tiedosto puretaan haluttuun kansioon. Vaihtoehtoisesti sovelluksen voi ladata komentorivin kautta haluttuun kansioon siirtymällä kyseiseen kansioon ja antamalla komennon
```console
git clone https://github.com/jyrki26/Vetoseuranta2.git
```

#### Sovelluksen riippuvuudet
Sovelluksen käyttämiseksi tulee sen vaatimat riippuvuudet asentaa. Tämä tehdään komentorivillä sovelluksen kansiossa komennolla
```console
pip install -r requirements.txt
```

#### Sovelluksen käynnistäminen
Nyt sovellus on valmis käynnistettäväksi. Käynnistys tapahtuu antamalla sovelluksen kansiossa komentorivillä komento
```console
python3 run.py
```
Sovellusta voi nyt käyttää osoitteessa http://127.0.0.1:5000/

## Asentaminen Herokuun
Tiedosto tulee olla ladattu ja purettu vastaavasti kuin paikallisessa asennuksessa. Lisäksi tulla olla luotuna Heroku-tili osoitteessa www.heroku.com. Lisäksi asennettuna tulee olla Heroku Cli.

#### Heroku-sovelluksen luominen
Sovellus lähetetään Herokuun komentorivillä sovelluksen kansiossa komennolla
```console
heroku create sovelluksen_nimi
```
Sovelluksen nimen tulee olla uniikki, joten komentoon kohtaan sovelluksen_nimi tulee vaihtaa käyttäjän haluama nimi. Vaihtoehtoisesti kohdan voi jättää tyhjäksi, jolloin Heroku luo satunnaisen nimen.

#### Sovelluksen lähettäminen Herokuun
Sovellus lähetetään Herokuun komennolla
```console
git push heroku master
```

Tämän jälkeen sovellus löytyy ja on käytettävissä osoitteessa sovelluksen_nimi.herokuapp.com

#### PostgreSQL:n käyttöönotto
Mikäli Herokussa halutaan ottaa käyttöön PostgreSQL, tulee komentorivillä sovelluksen kansiossa antaa seuraavat komennot
```console
heroku config:set HEROKU=1
```
```console
heroku addons:add heroku-postgresql:hobby-dev
```
Nyt sovelluksella on myös Herokussa käytössä tietokanta. Tämän jälkeen tietokantaan voi ottaa yhteyden komennolla
```console
heroku pg:psql
```
ja lisätä haluamansa käyttäjät käyttöohjeiden mukaisesti.