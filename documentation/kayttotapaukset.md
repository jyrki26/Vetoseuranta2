# Käyttötapaukset

## Joukkueiden hallinta
#### Joukkueen lisääminen
Käyttäjän tulee voida lisätä joukkue, jotta vetoseurantaan voidaan tallentaa vedot halutuilla joukkuetiedoilla.
Mikäli joukkueen nimi hyväksytään validoinnissa, lisätään joukkue tietokantaan komennolla
```SQL
INSERT INTO team (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, Joukkueen nimi)
```
#### Joukkueiden haku
Sovellus näyttää kaikki tietokannassa olevat joukkueet, jotta käyttäjä voi tarkastaa onko haluttu joukkue mahdollisesti jo olemassa hieman eri nimellä tai halutessaan muokata joukkueen nimeä. Haku tapahtuu kyselyllä
```SQL
SELECT team.id AS team_id, team.date_created AS team_date_created, team.date_modified AS team_date_modified, team.name AS team_name
FROM team ORDER BY team.name
```
Kyselyn perusteella joukkueet näytetään aakkosjärjestyksessä.
