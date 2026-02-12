DROP TABLE IF EXISTS EMPLOYES ;
CREATE TABLE IF NOT EXISTS EMPLOYES (
    ID_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    WORK_EXPERIENCE INTEGER
);

INSERT INTO EMPLOYES (ID_NO, NAME, ADDRESS, PHONE, WORK_EXPERIENCE) VALUES
(1, 'Liam', 'New York', '**********', 3),
(2, 'Emma', 'New York', '**********', 9),
(3, 'Lucas', 'Houston', '**********', 18),
(4, 'Ethan', 'Los Angeles', '**********', 5),
(5, 'Liam', 'Chicago', '**********', 5),
(6, 'Mateo', 'Houston', '**********', 1);

SELECT * FROM EMPLOYES;

SELECT * FROM EMPLOYES WHERE ADDRESS = 'New York';

SELECT * FROM EMPLOYES WHERE WORK_EXPERIENCE = 18;

SELECT * FROM EMPLOYES WHERE NAME = 'Liam';

SELECT * FROM EMPLOYES WHERE WORK_EXPERIENCE = 5;