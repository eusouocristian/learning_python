-- (CTRL + SHIFT + E) to execute the selected code from Query
SELECT * FROM Person.Person

SELECT FirstName AS 'First Name',
       LastName AS 'Last Name'
FROM Person.Person WHERE LastName = 'Watson';

SELECT FirstName AS 'First Name',
       LastName AS 'Last Name'
FROM Person.Person WHERE LastName != 'Watson';

SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate > '2014';


SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate = '2014' 
        OR LastName = 'Watson'
        OR LastName = 'Collins'
        OR LastName = 'Patel' 
-- The above statement is equal to:
SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate = '2014' OR LastName IN ('Watson', 'Collins', 'Patel');


SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate = '2014' 
        OR LastName != 'Watson'
        OR LastName != 'Collins'
        OR LastName != 'Patel' 
-- The above statement is equal to:
SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate = '2014' OR LastName NOT IN ('Watson', 'Collins', 'Patel');

SELECT FirstName AS 'First Name',
        LastName AS 'Last Name',
        ModifiedDate AS 'Modified'
FROM Person.Person WHERE ModifiedDate BETWEEN '2015' AND '2016'

