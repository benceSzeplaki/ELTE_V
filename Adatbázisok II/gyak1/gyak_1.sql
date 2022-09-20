--I. Gyakorlat feladatai

--1. feladat:
--Kinek a tulajdonában van a DBA_TABLES nevű nézet,
--illetve a DUAL nevű tábla? [owner, object_name, object_type]

SELECT OWNER, OBJECT_NAME, OBJECT_TYPE
FROM ALL_OBJECTS
WHERE OBJECT_NAME='DBA_TABLES' AND OBJECT_TYPE != 'SYNONYM'
   OR OBJECT_NAME='DUAL' AND OBJECT_TYPE != 'SYNONYM';

--2. feladat:
--Kinek a tulajdonában van a DBA_TABLES nevű, illetve a DUAL nevű szinonima? [owner, object_name, object_type]
--Az iménti két lekérdezés megmagyarázza, hogy miért tudjuk elérni a DUAL táblát, illetve a DBA_TABLES
--nézetet anélkül, hogy minősítenénk őket a tulajdonos nevével így -> tulajdonos.objektum.

SELECT OWNER, OBJECT_NAME, OBJECT_TYPE
FROM ALL_OBJECTS
WHERE OBJECT_NAME='DBA_TABLES' AND OBJECT_TYPE='SYNONYM'
   OR OBJECT_NAME='DUAL' AND OBJECT_TYPE='SYNONYM';

--3. feladat:
--Milyen típusú objektumai vannak az orauser nevű felhasználónak az adatbázisban? [object_type]

SELECT OBJECT_TYPE
FROM ALL_OBJECTS
WHERE OWNER='ORAUSER' GROUP BY OBJECT_TYPE;

--4. feladat:
--Hány különböző típusú objektum van nyilvántartva az adatbázisban? [darab]

WITH tmpTable (OBJECT_TYPES) AS
(SELECT OBJECT_TYPE
FROM ALL_OBJECTS GROUP BY OBJECT_TYPE)
SELECT COUNT(OBJECT_TYPES) AS OBJECT_TYPES FROM tmpTable;

SELECT COUNT(OBJECT_TYPE) AS OBJECT_TYPES FROM (SELECT OBJECT_TYPE
FROM ALL_OBJECTS GROUP BY OBJECT_TYPE);

--5. feladat:
--Melyek ezek a típusok? [object_type]

SELECT OBJECT_TYPE
FROM ALL_OBJECTS GROUP BY OBJECT_TYPE;

--6. feladat:
--Kik azok a felhasználók, akiknek több mint 10 féle objektumuk van? [owner]

WITH TMP_TABLE (OWNER, NUMBER_OF_OBJECTS) AS (
    SELECT OWNER, COUNT(OBJECT_ID) NumberOfObjects FROM ALL_OBJECTS GROUP BY OWNER)
SELECT * FROM TMP_TABLE WHERE NUMBER_OF_OBJECTS > 10;

SELECT * FROM
    (SELECT OWNER, COUNT(OBJECT_ID) NumberOfObjects FROM ALL_OBJECTS GROUP BY OWNER)
WHERE NumberOfObjects > 10;

-- 7. feladat:
-- Kik azok a felhasználók, akiknek van table és nézete is? [owner]

SELECT OWNER
FROM ALL_OBJECTS WHERE OBJECT_TYPE='VIEW' GROUP BY OWNER
INTERSECT
SELECT OWNER
FROM ALL_OBJECTS WHERE OBJECT_TYPE='TABLE' GROUP BY OWNER; -- ?? HOGY LEHET TRIGGERT LEKÉRDEZNI

-- 8. feladat:
-- Kik azok a felhasználók, akiknek van nézete, de nincs table? [owner]

SELECT OWNER
FROM ALL_OBJECTS WHERE OBJECT_TYPE='VIEW' GROUP BY OWNER
MINUS
SELECT OWNER
FROM ALL_OBJECTS WHERE OBJECT_TYPE='TABLE' GROUP BY OWNER;

-- 9.
-- Kik azok a felhasználók, akiknek több mint n táblájuk, de maximum m indexük van? [owner]
-- (n és m értékét adjuk meg úgy, hogy kb. 1-15 között legyen a sorok száma, pl. n=20, m=15)

WITH TMP AS (SELECT OWNER, OBJECT_TYPE, COUNT(OBJECT_TYPE)
FROM ALL_OBJECTS WHERE OBJECT_TYPE='TABLE'
GROUP BY OWNER, OBJECT_TYPE HAVING COUNT(OBJECT_TYPE) > 20)
SELECT ALL_OBJECTS.OWNER
FROM ALL_OBJECTS, TMP WHERE TMP.OWNER = ALL_OBJECTS.OWNER AND ALL_OBJECTS.OBJECT_TYPE = 'INDEX'
GROUP BY ALL_OBJECTS.OWNER HAVING COUNT(ALL_OBJECTS.OBJECT_TYPE) < 26;

-- 10.
-- Melyek azok az objektum típusok, amelyek tényleges tárolást igényelnek, vagyis
-- tartoznak hozzájuk adatblokkok?

SELECT DISTINCT OBJECT_TYPE FROM (
    SELECT OBJECT_TYPE FROM ALL_OBJECTS WHERE DATA_OBJECT_ID IS NOT NULL);

-- 11.
-- Melyek azok az objektum típusok, amelyek nem igényelnek tényleges tárolást, vagyis nem
-- tartoznak hozzájuk adatblokkok? [object_type]

SELECT DISTINCT OBJECT_TYPE FROM (
    SELECT OBJECT_TYPE FROM ALL_OBJECTS WHERE DATA_OBJECT_ID IS NULL);

-- 12.
-- Keressük meg az utóbbi két lekérdezés metszetét. [object_type]

SELECT DISTINCT OBJECT_TYPE FROM (
    SELECT OBJECT_TYPE FROM ALL_OBJECTS WHERE DATA_OBJECT_ID IS NOT NULL)
INTERSECT
SELECT DISTINCT OBJECT_TYPE FROM (
    SELECT OBJECT_TYPE FROM ALL_OBJECTS WHERE DATA_OBJECT_ID IS NULL);

-- 13.
-- Hány oszlopa van a nikovits.emp táblának? [darab]

SELECT COUNT(COLUMN_NAME) FROM DBA_TAB_COLUMNS
WHERE OWNER = 'NIKOVITS' AND TABLE_NAME='EMP';

-- 14.
-- Milyen típusú a nikovits.emp tábla 6. oszlopa? [data_type]

SELECT COLUMN_NAME, DATA_TYPE FROM DBA_TAB_COLUMNS
WHERE OWNER='NIKOVITS' AND TABLE_NAME='EMP' AND COLUMN_ID=6;

-- 15.
-- Adjuk meg azoknak a tábláknak a tulajdonosát és nevét, amelyeknek van 'Z' betűvel
-- kezdődő oszlopa.

SELECT DISTINCT OWNER, TABLE_NAME FROM DBA_TAB_COLUMNS
WHERE COLUMN_NAME LIKE 'Z%';

-- 16.
-- Adjuk meg azoknak a tábláknak a tulajdonosát és nevét, amelyeknek legalább 8
-- darab dátum tipusú oszlopa van. [owner, table_name]

SELECT OWNER, TABLE_NAME, COUNTED FROM (
SELECT OWNER, TABLE_NAME, COUNT(DATA_TYPE) AS COUNTED
FROM DBA_TAB_COLUMNS WHERE DATA_TYPE='DATE' GROUP BY OWNER, TABLE_NAME) WHERE COUNTED >= 8;

-- 17.
-- Adjuk meg azoknak a tábláknak a tulajdonosát és nevét, amelyeknek 1. es 4. oszlopa is
-- VARCHAR2 tipusú, az oszlop hossza mindegy. [owner, table_name]

WITH TMP AS (SELECT OWNER, TABLE_NAME, COLUMN_ID, DATA_TYPE FROM DBA_TAB_COLUMNS
WHERE COLUMN_ID = 1 AND DATA_TYPE='VARCHAR2' OR COLUMN_ID = 4 AND DATA_TYPE='VARCHAR2')
SELECT T1.OWNER AS OWNER, T1.TABLE_NAME AS TABLE_NAME FROM TMP T1, TMP T2
WHERE T1.TABLE_NAME = T2.TABLE_NAME AND T1.COLUMN_ID = 1 AND T2.COLUMN_ID = 4;

