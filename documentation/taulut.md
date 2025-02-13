# Vetoseuranta2 tietokantataulut

### Account
```SQL
CREATE TABLE account (
    id            INTEGER       NOT NULL,
    date_created  DATETIME,
    date_modified DATETIME,
    name          VARCHAR (144) NOT NULL,
    username      VARCHAR (144) NOT NULL,
    password      VARCHAR (144) NOT NULL,
    role_id       INTEGER       NOT NULL,
    PRIMARY KEY (
        id
    ),
    FOREIGN KEY (
        role_id
    )
    REFERENCES role (id) 
);
```

### Bet
```SQL
CREATE TABLE bet (
    id            INTEGER  NOT NULL,
    date_created  DATETIME,
    date_modified DATETIME,
    date_played   DATE     NOT NULL,
    stake         NUMERIC  NOT NULL,
    odds          NUMERIC  NOT NULL,
    result        INTEGER,
    home_team_id  INTEGER  NOT NULL,
    away_team_id  INTEGER  NOT NULL,
    bet_type_id   INTEGER  NOT NULL,
    bet_result_id INTEGER  NOT NULL,
    account_id    INTEGER  NOT NULL,
    PRIMARY KEY (
        id
    ),
    FOREIGN KEY (
        home_team_id
    )
    REFERENCES team (id),
    FOREIGN KEY (
        away_team_id
    )
    REFERENCES team (id),
    FOREIGN KEY (
        bet_type_id
    )
    REFERENCES bet_type (id),
    FOREIGN KEY (
        bet_result_id
    )
    REFERENCES bet_result (id),
    FOREIGN KEY (
        account_id
    )
    REFERENCES account (id) 
);
```

### Bet_result
```SQL
CREATE TABLE bet_result (
    id     INTEGER      NOT NULL,
    result VARCHAR (40) NOT NULL,
    PRIMARY KEY (
        id
    )
);
```

### Bet_type
```SQL
CREATE TABLE bet_type (
    id   INTEGER      NOT NULL,
    type VARCHAR (40) NOT NULL,
    PRIMARY KEY (
        id
    )
);
```

### Bet_typeBet_result
```SQL
CREATE TABLE bet_typeBet_result (
    bet_type   INTEGER,
    bet_result INTEGER,
    FOREIGN KEY (
        bet_type
    )
    REFERENCES bet_type (id),
    FOREIGN KEY (
        bet_result
    )
    REFERENCES bet_result (id) 
);
```


### Role
```SQL
CREATE TABLE role (
    id   INTEGER NOT NULL,
    name VARCHAR NOT NULL,
    PRIMARY KEY (
        id
    )
);
```

### Team
```SQL
CREATE TABLE team (
    id            INTEGER       NOT NULL,
    date_created  DATETIME,
    date_modified DATETIME,
    name          VARCHAR (144) NOT NULL,
    PRIMARY KEY (
        id
    )
);
```