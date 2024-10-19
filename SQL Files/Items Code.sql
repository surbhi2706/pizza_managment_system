CREATE TABLE Items (
  ItemID int NOT NULL AUTO_INCREMENT,
  Item_Name varchar(20) DEFAULT NULL,
  Type varchar(20) DEFAULT NULL,
  Category varchar(20) DEFAULT NULL,
  Price float DEFAULT NULL,
  PRIMARY KEY (ItemID)
);

INSERT INTO Items (Item_Name,Type,Category,Price) VALUES
  ('Margherita','Veg','Pizza',289),
  ('Veggie Supreme','Veg','Pizza',609),
  ('Tandoori Paneer','Veg','Pizza',539),
  ('Veg Kabab Surprise','Veg','Pizza',359),
  ('Chicken Supreme','Non-Veg','Pizza',689),
  ('Triple Chicken Feast','Non-Veg','Pizza',788),
  ('Chicken Tikka','Non-Veg','Pizza',359),
  ('Classic Sausage','Non-Veg','Pizza',109),
  ('Tear & Share','Veg','Sides',169),
  ('Cheese Garlic Bread','Veg','Sides',149),
  ('Tear & Share','Non-Veg','Sides',189),
  ('Chicken Pocket','Non-Veg','Sides',139),
  ('Choco Lava Cake','Veg','Desserts',119),
  ('Choco Sundae','Veg','Desserts',29),
  ('Magnum Truffle','Veg','Desserts',76),
  ('Pepsi','Veg','Drinks',57),
  ('Marinda','Veg','Drinks',57),
  ('Bisleri','Veg','Drinks',48),
  ('7-Up','Veg','Drinks',57);

SELECT * FROM Items;