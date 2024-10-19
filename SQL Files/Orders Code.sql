CREATE TABLE Orders (
  SNO int NOT NULL AUTO_INCREMENT,
  Order_ID varchar(10) NOT NULL,
  User_ID varchar(10) DEFAULT NULL,
  CreatedOn datetime DEFAULT NULL,
  Item_Name varchar(30) DEFAULT NULL,
  Quantity int DEFAULT NULL,
  Amount float DEFAULT NULL,
  Tax float DEFAULT NULL,
  Delivery_Charge float DEFAULT NULL,
  Discount float DEFAULT NULL,
  Total_Amount float DEFAULT NULL,
  Order_Status varchar(20) DEFAULT NULL,
  Item_Type varchar(20) DEFAULT NULL,
  Item_Category varchar(20) DEFAULT NULL,
  PRIMARY KEY (SNO),
  KEY orders_ibfk_1 (User_ID),
  CONSTRAINT orders_ibfk_1 FOREIGN KEY (User_ID) REFERENCES User (User_ID) ON DELETE CASCADE
);

INSERT INTO Orders (Order_ID,User_ID,CreatedOn,Item_Name,Quantity,Amount,Tax,Delivery_Charge,Discount,Total_Amount,Order_Status,Item_Type,Item_Category) VALUES
  ('ORD101','U102','2022-10-30 15:54:19','Tandoori Paneer',2,539,NULL,NULL,NULL,1078,'Active','Veg','Pizza'),
  ('ORD101','U102','2022-10-30 15:54:19','Chicken Tikka',1,359,NULL,NULL,NULL,359,'Active','Non-Veg','Pizza'),
  ('ORD101','U102','2022-10-30 15:54:19','Tear & Share',1,169,NULL,NULL,NULL,169,'Active','Veg','Sides'),
  ('ORD101','U102','2022-10-30 15:54:19','Chicken Pocket',1,139,NULL,NULL,NULL,139,'Active','Non-Veg','Sides'),
  ('ORD101','U102','2022-10-30 15:54:19','Magnum Truffle',2,76,NULL,NULL,NULL,152,'Active','Veg','Desserts'),
  ('ORD101','U102','2022-10-30 15:54:19','Final Billing Row',7,1897,80.62,60,284.55,1753.07,'Active','Both',NULL),
  ('ORD102','U102','2022-10-30 16:15:53','Margherita',2,289,NULL,NULL,NULL,578,'Active','Veg','Pizza'),
  ('ORD102','U102','2022-10-30 16:15:53','Final Billing Row',2,578,27.46,60,28.9,636.56,'Active','Veg',NULL),
  ('ORD103','U102','2022-10-30 17:18:49','Triple Chicken Feast',2,788,NULL,NULL,NULL,1576,'Active','Non-Veg','Pizza'),
  ('ORD103','U102','2022-10-30 17:18:49','Cheese Garlic Bread',2,149,NULL,NULL,NULL,298,'Active','Veg','Sides'),
  ('ORD103','U102','2022-10-30 17:18:49','Final Billing Row',4,1874,79.65,0,281.1,1672.55,'Active','Both',NULL);

SELECT * FROM Orders;