# Käyttötapaukset

## Joukkueiden hallinta
#### Joukkueen lisääminen
Käyttäjän tulee voida lisätä joukkue, jotta vetoseurantaan voidaan tallentaa vedot halutuilla joukkuetiedoilla.
Mikäli joukkueen nimi hyväksytään validoinnissa, lisätään joukkue tietokantaan komennolla
```SQL
INSERT INTO team (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, Joukkueen nimi);
```
#### Joukkueiden haku
Sovellus näyttää kaikki tietokannassa olevat joukkueet, jotta käyttäjä voi tarkastaa onko haluttu joukkue mahdollisesti jo olemassa hieman eri nimellä tai halutessaan muokata joukkueen nimeä. Haku tapahtuu kyselyllä
```SQL
SELECT team.id AS team_id, team.date_created AS team_date_created, team.date_modified AS team_date_modified, team.name AS team_name
FROM team ORDER BY team.name;
```
Kyselyn perusteella joukkueet näytetään aakkosjärjestyksessä.

#### Joukkueen nimen muokkaaminen
Sovellus mahdollistaa joukkueen nimen muokkaamisen virheellisen nimen muuttamiseksi. Tämä tapahtuu komennolla
```SQL
UPDATE team SET date_modified=CURRENT_TIMESTAMP, name=Uusi nimi WHERE team.id = Muutettavan joukkueen id;
```

## Vetojen hallinta
#### Uuden vedon lisääminen
Sovelluksen keskeisin toiminto on uuden vedon lisääminen. Toiminto tapahtuu seuraavalla komennolla
```SQL
INSERT INTO bet (date_created, date_modified, date_played, stake, odds, result, home_team_id, away_team_id, bet_type_id, bet_result_id, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, Ottelupäivä, Panos, Kerroin, 4, Kotijoukkueen id, Vierasjoukkueen id, Vetotyypin id, Pelatun tuloksen id, Käyttäjän id);
```

#### Avoimien vetojen haku
Sovelluksessa tulee voida hakea käyttäjän avoimet vedot, jotta käyttäjä voi seurata vetojaan ja päivittää niiden tuloksen, kun ottelu on pelattu. Tämä tapahtuu seuraavalla kyselyllä
```SQL
SELECT bet.id AS bet_id, bet.date_created AS bet_date_created, bet.date_modified AS bet_date_modified, bet.date_played AS bet_date_played, bet.stake AS bet_stake, bet.odds AS bet_odds, bet.result AS bet_result, bet.home_team_id AS bet_home_team_id, bet.away_team_id AS bet_away_team_id, bet.bet_type_id AS bet_bet_type_id, bet.bet_result_id AS bet_bet_result_id, bet.account_id AS bet_account_id
FROM bet
WHERE bet.result = 4
ORDER BY bet.date_played;
```

#### Vedon tuloksen päivittäminen
Käyttäjän tulee voida päivittää veto sen mukaan menikö se oikein vai väärin vai mitätöitiinkö veto. Tämä tapahtuu seuraavalla kyselyllä
```SQL
UPDATE bet SET date_modified=CURRENT_TIMESTAMP, result=Vedon tulos WHERE bet.id = Vedon id; 
```
Vedon tulokseksi valitaan 1, jos veto meni oikein, 2 jos veto meni väärin ja 3, jos veto mitätöitiin.

#### Vedon poistaminen
Tarvittaessa virheellinen veto tulee voida poistaa. Tämä tapahtuu seuraavalla kyselyllä.
```SQL
DELETE FROM bet WHERE bet.id = Vedon id;
```

#### Vetohistorian näyttäminen
Käyttäjän tulee voida seurata myös ratkenneita vetojaan. Tämä tapahtuu vetohistorian kautta. Kysely on vastaava avoimien vetojen näyttämisessä, sillä erotuksella, että sarakkeeseen bet.result arvoksi annetaan 1, jos halutaan näyttää oikein menneet vedot, väärin menneille vedoilla 2 ja mitätöidyille 3. Kysely on siis seuraava
```SQL
SELECT bet.id AS bet_id, bet.date_created AS bet_date_created, bet.date_modified AS bet_date_modified, bet.date_played AS bet_date_played, bet.stake AS bet_stake, bet.odds AS bet_odds, bet.result AS bet_result, bet.home_team_id AS bet_home_team_id, bet.away_team_id AS bet_away_team_id, bet.bet_type_id AS bet_bet_type_id, bet.bet_result_id AS bet_bet_result_id, bet.account_id AS bet_account_id
FROM bet
WHERE bet.result = Vedon tuloksen id ORDER BY bet.date_played;
```

#### Vetohistoria joukkueittain
Käyttäjä voi myös vastaavan vetohistorian joukkueittain kuin kaikkien vetojen osalta. Tämä tapahtuu kyselyllä:
```SQL
SELECT COUNT(bet.result)
FROM bet
LEFT JOIN Team ON Team.id = Bet.home_team_id OR Team.id = Bet.away_team_id
LEFT JOIN Account ON account.id = bet.account_id
WHERE Team.id = team_id AND Account.id = account_id AND Bet.result != 4;
```

#### Yhteenvetokyselyn näyttäminen
Vetojen kokonaisuuden seuraamiseksi käyttäjälle tulee myös näyttää erilaista tilastotietoa vedoista. Tässä vaiheessa on toteutettu ainoastaan kysely, jossa näytetään kokonaismäärät oikein ja väärin menneistä sekä mitätöidyistä vedoista sekä ratkenneiden vetojen kokonaismäärä. Kysely on seuraava
```SQL
SELECT COUNT(bet.result) FROM bet  LEFT JOIN Account ON account.id = bet.account_id WHERE (bet.result = Vedon tuloksen id AND account.id = Käyttäjän id);
```
Vedon tuloksen id:n arvot ovat vastaavat kuin edellisessä kyselyssä.

Ratkenneiden vetojen kokonaismäärä saadaan selville seuraavalla kyselyllä
```SQL
SELECT COUNT(bet.result) FROM bet  LEFT JOIN Account ON account.id = bet.account_id WHERE (bet.result != 4 AND account.id = Käyttäjän id)
```
