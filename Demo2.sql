CREATE DATABASE Demo2;
CREATE TABLE Customer 
(
CustomerID Int Primary key not null,
CustomerName Char(45),
Municipality Char(45),
City Char(45)
);
INSERT INTO Customer (CustomerID, CustomerName, Municipality, City)
	VALUE ('1', 'Gina de Leon', 'Apalit', 'Pampanga'),
    ('2', 'Amara Luna', 'Mexico', 'Pampanga'),
    ('3', 'Lucila Maulon', 'Angat', 'Bulacan'),
    ('4', 'Rafael Santos', 'Lumban', 'Laguna'),
    ('5', 'Maricel Moran', 'Calumpit', 'Bulacan'),
    ('6', 'Anotnio Moreno', 'Santa Maria', 'Bulcan'),
    ('7', 'Hanna Moos', 'Alaminos', 'Laguna'),
    ('8', 'Fred Gregorio', 'Lumban', 'Laguna'),
    ('9', 'Maria Andres', 'Porac', ' Pampanga'),
    ('10', 'Liza Ramos', 'Alaminos', 'Laguna');

SELECT * FROM Customer WHERE City = 'Bulacan';
SELECT * FROM Customer WHERE Municipality = 'Alaminos' AND City = 'Laguna';
SELECT * FROM Customer WHERE NOT City = 'Pampanga';