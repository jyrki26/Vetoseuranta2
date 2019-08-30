# Asennusohje

## Sovelluksen ja tietokannan ohjelmisto
Sovellus on toteutettu Python 3.7.4 versiolla käyttäen Flask-kirjastoa. Paikallisessa versiossa tietokantaohjelmistona toimii SQLite ja Herokun versiossa PostgreSQL. Sovellus eri versioneen löytyy GitHubista.

## Asennus paikallisesti
Sovelluksen voi ladata GitHubista osoitteesta https://github.com/jyrki26/Vetoseuranta2 valitsemalla Clone or download -kohdan ja lataamalla zip-tiedoston. Tämän jälkeen tiedosto puretaan haluttuun kansioon. Vaihtoehtoisesti sovelluksen voi ladata komentorivin kautta haluttuun kansioon siirtymällä kyseiseen kansioon ja antamalla komennon git clone https://github.com/jyrki26/Vetoseuranta.git

#### Virtuaaliympäristö Venv
Sovelluksen käyttäminen paikallisesti edellyttää virtuaaliympäristö Venvin asentamista. Venv asennetaan siirtymällä komentorivillä kansioon, jossa sovellus on ja antamalla komento
```console
python3 -m venv venv
```

Venv otetaan käyttöön komennolla
```console
source venv/bin/activate
```

####
