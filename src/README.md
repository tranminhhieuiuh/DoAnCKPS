
$ python
$ from application import db
$ db.create_all()
```
```
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) UNIQUE, 
	hash VARCHAR(200) NOT NULL, 
	cash INTEGER
);
CREATE TABLE portfolio (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	user_id INTEGER, 
	symbol VARCHAR(5), 
	current_shares INTEGER
);
CREATE TABLE bought (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	buyer_id INTEGER, 
	time VARCHAR(100), 
	symbol VARCHAR(5), 
	shares_bought INTEGER, 
	price_bought FLOAT
);
CREATE TABLE sold (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	seller_id INTEGER, 
	time VARCHAR(100), 
	symbol VARCHAR(5), 
	shares_sold INTEGER, 
	price_sold FLOAT
);
CREATE TABLE cash_history (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	user_id INTEGER,
	cash FLOAT
);
```


