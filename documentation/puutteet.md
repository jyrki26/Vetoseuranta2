# Sovelluksen puutteet ja jatkokehitysideat
Tässä dokumentissa on mainittu joitakin keskeisiä puutteita, joita sovelluksen mahdollisissa myöhemmissä versioissa tulisi kehittää, jotta sovellus olisi todellisuudessa hyödyllinen työkalu vedonlyöjälle. Tällä hetkellä sovellusta voi lähinnä käyttää yhden tyyppisten vetojen seuraamiseen ja se ei tarjoa juurikaan tilastollisia työkaluja vetojen seuraamiseen.

## Vetotyyppien laajentaminen
Tällä hetkellä sovelluksessa voi tallentaa ainoastaan vetoja, joissa on kaksi joukkuetta. Erilaisten vetotyyppien, kuten voittajavetojen lisääminen tekisi sovelluksesta hyödyllisemmän.

## Tilastojen laajentaminen
Ainoat sovelluksessa olevat tilastot ovat tällä hetkellä vetojen kokonaismäärää eri tulosten mukaan seuraava tilasto ja vastaava tilasto joukkueittain. Todellisuudessa tämä ei ole kovinkaan hyödyllinen tilasto, vaan vedonlyöjän kannalta hyödyllisempiä tilastoja olivat esimerkiksi palautusprosentti, keskimääräinen panos ja mahdollisuus lajitella vetoja esimerkiksi lajien mukaan.

## Vetotyyppien validointi
Uudelle vedolle voi tällä hetkellä lisätä minkä tahansa vetotyypin mukaisen tasoituksen/vedon. Jatkokehityksessä olisi hyödyllistä näyttää tasoitus/veto niin, että pudotusvalikosta tarjottaisiin ainoastaan kyseisen vetotyypin mukaisia vaihtoehtoja.

## Valuutan ja kertoimien käsittely
Tällä hetkellä valuuttaa ja vetojen kertoimia käsitellään numeric-muotoisina. Tämä johtaa pyöristysvirheisiin, jos myöhemmissä versiossa luodaan ominaisuuksia, kuten pelikassa, joka seuraa vedonlyöjän pelikassan kehitystä. Lukuja olisi siis järkevämpää tallentaa integer-muodossa, niin että vedon suuruus tallennettaisiin sentteinä, ei euroina.

