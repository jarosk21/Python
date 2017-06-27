CREATE DATABASE dbKancelaria1;
use dbKancelaria1;
#Użytkownicy i hasła
CREATE TABLE Users (
    id_u INT AUTO_INCREMENT NOT NULL,
    nazwa VARCHAR(15),
    haslo VARCHAR(10),
    PRIMARY KEY(id_u)
);
#Tabele Główne
#Rodzaje klientów
CREATE TABLE Rodz_kl (
id_r int not null,
nazwa_rodzaju varchar(40),
PRIMARY KEY (id_r)
);
#Klienci
CREATE TABLE Klienci (
    id_k INT AUTO_INCREMENT NOT NULL,
    imie VARCHAR(20),
    nazwisko VARCHAR(40),
    nazwa VARCHAR(40),
    pesel VARCHAR(11) UNIQUE,
    NIP INT(10) UNIQUE,
    kl_id_r int,
    PRIMARY KEY (id_k),
    FOREIGN KEY(kl_id_r) REFERENCES rodz_kl (id_r) ON UPDATE CASCADE ON DELETE NO ACTION
);

#adresy klientów
CREATE TABLE adresy (
id_adr int AUTO_INCREMENT,
ad_id_k int,
ulica VARCHAR(40),
miasto VARCHAR(40),
kod_p VARCHAR(5),
nr_tel VARCHAR(12),
adres_mail varchar (30),
PRIMARY KEY(id_adr)
);
#dodanie do tabeli klucza obcego
ALTER TABLE adresy ADD CONSTRAINT ad_id_k FOREIGN KEY(ad_id_k) REFERENCES klienci (id_k) on UPDATE CASCADE ON DELETE CASCADE;	

#Sprawy klientów
CREATE TABLE Sprawy_kl (
    id_sp INT AUTO_INCREMENT NOT NULL,
    nazwa VARCHAR(40),
    opis VARCHAR(400),
    sp_id_k int not NULL,
    sp_id_kat int,
    PRIMARY KEY (id_sp)
);
#Kategorie spraw
CREATE TABLE Kategorie (
    id_kat INT(1) NOT NULL,
    rodzaj VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_kat)
);
#dodanie kluczy obcych
ALTER TABLE sprawy_kl ADD CONSTRAINT sp_id_k FOREIGN KEY(sp_id_k) REFERENCES klienci (id_k) ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE sprawy_kl ADD CONSTRAINT sp_id_kat FOREIGN KEY(sp_id_kat) REFERENCES Kategorie (id_kat) ON UPDATE CASCADE ON DELETE CASCADE;

#Korespondencja z sądami, organami-otrzymana
CREATE TABLE Litigation (
id_l INT AUTO_INCREMENT not null,
data_otr date not null,
sygnatura VARCHAR(40) not null,
organ VARCHAR(40) not null,
opis VARCHAR (400) not null,
termin int(2) ZEROFILL not null,
PRIMARY KEY(id_l)
);
#Czynność do wykonania
CREATE TABLE Akcja (
id_a int AUTO_INCREMENT not null,
data_pocz date,
data_konc date,
opis varchar(400),
PRIMARY KEY (id_a)
);
show tables;
#dodanie wpisów w tabeli kliencie
INSERT INTO klienci (
imie, nazwisko, PESEL)
VALUES
	('Wiera', 'Grodzka',	 53102233165),
	('Mera',	 'Czabańska',	 21102975761),
	('Romana',	 'Gielnik',	 98052648666),
	('Ewald', 'Gierwatowski',	 12102771239),
	('Kryspian',	 'Filipowicz',	 42070285634),
	('Wioletta',	 'Górzyńska',	 02080692921),
	('Wanda',	 'Fidor',	 40110870921),
	('Ludomira',	 'Dziechciarska',	 03060862583),
	('Kamilla',	 'Gawrońska',	 77080440406),
	('Leokadia', 'Dębińska',	 90013023004),
	('Wioletta', 'Gutowska', 11061403186),
	('Wincenty',	 'Gawryjołek',	 54050231372),
	('Ilona',	 'Dudzińska',	 34032945442),
	('Scholastyka',	 'Golińska',	 61102694841),
	('Atalia',	 'Czyżewska',	 47071376761),
	('Wiktoria',	 'Gocińska',	 34121869346),
	('Waleria',	 'Czebotarow',	 42020967062),
	('Anna',	 'Gajcy',	 51122502106);

#dodanie rodzajó klientów
INSERT INTO rodz_kl (id_r, nazwa_rodzaju) VALUES 
(1, 'osfiz'),
(2, 'osfiz-przeds'),
(3, 'spj'),
(4, 'spp'),
(5, 'spk'),
(6, 'spka'),
(7, 'spzoo'),
(8, 'sa');
DESCRIBE adresy;
#dodanie adresów
INSERT into adresy 
(ad_id_k, ulica, miasto, kod_p, nr_tel)
VALUES
(1, 'Mokotowska 49', 'Warszawa', '00700', '123456789'),
(2, 'Czerska 17', 'Warszawa', '00710', '234567890'),
(3, 'Jana Pawła II 19','Warszawa', '00720', '135246098'),
(4, 'Zytnia 10','Wrszawa', '00730', '134711235'),
(5, 'Opolska', 'Kielce', '23300', '789432642'),
(6, 'Kielecka', 'Opople', '34300', '654392734'),
(7, 'Hallera', 'Gdynia', '45789', '234701000'),
(8, 'Marynarska', 'Sopot', '46980', '456432098'),
(9, 'Dubois', 'Warszawa', '00234', '102030405'),
(10, 'Ateńska', 'Kraków', '04300', '203045600');
#aktualizacja danych w tabeli klienci - dodanie rodzaju poprzez wskazanie id rodzaju dla osób urodzonych po 1950r. na podst. nr PESEL
UPDATE klienci set kl_id_r=2 where left(Pesel,2)>50;
#sprawdzenie wpisów w tabeli klienci
SELECT * from klienci;
UPDATE klienci set kl_id_r=1 where left(Pesel,2)<50;
#wyświeltnie klientów ze wskazaniem rodzaju klienta
SELECT imie, nazwisko, nazwa_rodzaju from klienci left join rodz_kl on klienci.kl_id_r=rodz_kl.id_r;
#wyświetlenie klientów i ich adresów i rodzajów
SELECT imie, nazwisko, nazwa_rodzaju, ulica, miasto, nr_tel from klienci left join rodz_kl on klienci.kl_id_r=rodz_kl.id_r left join adresy on klienci.id_k=adresy.ad_id_k;
#zliczenie liczby klientów
SELECT count(*) FROM klienci;
#uzupełnienie adresów klientów
INSERT INTO adresy (ad_id_k, ulica, miasto, kod_p, nr_tel) VALUES 
(11, 'Krakowska', 'Zakopane', '30100', '900800700'),
(12, 'Zakopiańska', 'Szczyrk', '40100', '800701820'),
(13, 'Stalowa', 'Warszawa', '00128', '666555333'),
(14, 'Ząbkowska', 'Warszawa', '02130', '333222111'),
(15, '11 Listopada', 'Warszawa', '02140', '111222444'),
(16, 'Czerwona', 'Warszawa', '01203', '222333567'),
(17, 'Biała', 'Kielce', '26200', '234432105'),
(18, 'Długa', 'Władysławowo', '07300', '450540234');
#zliczenie klientów z poszczególnych miast
SELECT count(*), miasto FROM adresy GROUP BY miasto;
#zmiana danych w tabeli adresy - poprawa błednej nazwy miasta
UPDATE adresy set miasto='Warszawa' where miasto='Wrszawa';
SELECT * from adresy;
SELECT * from klienci;
#zliczenie klientów wg rodzaju
SELECT count(*), nazwa_rodzaju from rodz_kl, klienci where klienci.kl_id_r=id_r GROUP BY nazwa_rodzaju;
DESCRIBE sprawy_kl;
DESCRIBE kategorie;
INSERT INTO kategorie (id_kat, rodzaj) VALUES
(1, 'cywilna'),
(2, 'karna'),
(3, 'admin'),
(4, 'podatkowa');
INSERT INTO sprawy_kl (nazwa, sp_id_k, sp_id_kat) VALUES 
('rozwód',1, 1 ),
('testament', 2, 1),
('odszkodowanie', 3, 1),
('kradzież', 4, 2),
('włamanie', 5, 2),
('rozbój', 6, 2),
('oszustwo', 7, 2),
('pozwolenie na budowe', 8, 3),
('warunki zabudowy', 9, 3),
('wycinka drzew', 10, 3),
('pozwolenie na broń', 11, 3),
('zaległość PIT', 12, 4),
('Zaległość VAT', 13, 4),
('optymalizacja PIT', 14, 4),
('rejestracja spółki', 15, 3),
('windykacja', 16, 1),
('windykacja', 17, 1),
('sprzedaż przedsiębiorstwa', 18, 1);
SELECT * from sprawy_kl;
#wyświetlenie klientów ze wskazaniem rodzaju i opisu sprawy
SELECT 
    imie, nazwisko, rodzaj, sprawy_kl.nazwa
FROM
    klienci
        LEFT JOIN
    sprawy_kl ON klienci.id_k = sp_id_k
        LEFT JOIN
    kategorie ON sprawy_kl.sp_id_kat = kategorie.id_kat;
#zliczenie liczby spraw wg rodzaju
SELECT 
    COUNT(*), rodzaj
FROM
    klienci,
    sprawy_kl,
    kategorie
WHERE
    klienci.id_k = sp_id_k
        AND sprawy_kl.sp_id_kat = kategorie.id_kat
GROUP BY rodzaj;
#liczba spraw ze wskazaniem rodzaju w poszczególnych miastach
SELECT 
    COUNT(*), rodzaj, miasto
FROM
    klienci,
    sprawy_kl,
    kategorie,
    adresy
WHERE
    klienci.id_k = sp_id_k
        AND sprawy_kl.sp_id_kat = kategorie.id_kat
        AND klienci.id_k = adresy.ad_id_k
GROUP BY rodzaj , miasto;
#dodanie kolumny do tabeli sprawy_kl - status sprawy aktywna/nieaktywna
ALTER TABLE sprawy_kl ADD COLUMN stan varchar(15) default 'aktywna';
SELECT * from sprawy_kl;
# dodanie tabel z fakturami i płatnościami
CREATE TABLE Faktury (
    id_f INT AUTO_INCREMENT NOT NULL,
    nr_f INT(5) ZEROFILL UNIQUE,
    fv_id_sp int,
    kwota FLOAT,
    data_wyst DATE,
    termin_p INT(3) ZEROFILL,
    PRIMARY KEY (id_f),
    FOREIGN KEY (fv_id_sp) REFERENCES sprawy_kl (id_sp)
);
CREATE TABLE Platnosci (
    id_p INT AUTO_INCREMENT NOT NULL,
    pl_id_f int,
    kwota FLOAT NOT NULL DEFAULT 0,
    data_otrz DATE,
    PRIMARY KEY (id_p)
);
INSERT INTO faktury (nr_f, fv_id_sp, kwota, data_wyst, termin_p) values
(1,1,1000, '2017-05-17', 14),
(2, 2, 2000, '2017-05-14', 7),
(3, 3, 1500, '2017-04-03', 21),
(4,4, 5000, '2017-04-10', 30),
(5, 5, 10000, '2017-05-20', 14),
(6,6, 4500, '2017-05-22',21),
(7,8, 4000, '2017-05-23',20),
(8,1, 4000, '2017-05-01',21),
(9,9, 3250, '2017-04-29',7),
(10,3, 3400, '2017-05-05',7);

INSERT INTO Platnosci (pl_id_f, kwota, data_otrz) 
values 
(1, 1000, '2017-05-23'),
(2, 2000, '2017-05-23'),
(3, 500, '2017-05-15'),
(4, 5000, '2017-05-20'),
(5, 6000, '2017-05-21'),
(6, 4500, '2017-05-23'),
(7, 3000, '2017-05-24'),
(8, 4000, '2017-05-20'),
(9, 1250, '2017-05-05'),
(10, 2400, '2017-05-06');
#lista faktur ze wskazaniem czy opłacona w całości 
SELECT 
    id_f,
    CASE
        WHEN faktury.kwota > platnosci.kwota THEN 'nieopłacona'
        ELSE 'opłacona'
    END AS 'status zapłaty'
FROM
    faktury, platnosci
WHERE
faktury.id_f=platnosci.pl_id_f;
SELECT datediff(data_otrz, data_wyst) from faktury, platnosci WHERE faktury.id_f=platnosci.pl_id_f;
SELECT * from platnosci;
UPDATE faktury set id_f = id_f-10;
#widok klientów z nieopłaconymi fakturami
CREATE VIEW nieoplacone AS
    SELECT 
        id_k, imie, nazwisko, faktury.kwota - platnosci.kwota AS zaleglosc, faktury.id_f
    FROM
        klienci
            LEFT JOIN
        sprawy_kl ON klienci.id_k = sprawy_kl.sp_id_k
            RIGHT JOIN
        faktury ON sprawy_kl.id_sp = faktury.fv_id_sp
            LEFT JOIN
        platnosci ON faktury.id_f = platnosci.pl_id_f
			Where 
		faktury.kwota - platnosci.kwota > 0;
#widok klientów z aktywnymi sprawami
CREATE VIEW aktywne as SELECT 
    CONCAT_WS(' ', imie, nazwisko) AS 'dane osobowe',
    sprawy_kl.nazwa,
    stan
FROM
    klienci
        LEFT JOIN
    sprawy_kl ON klienci.id_k = sprawy_kl.sp_id_k
    HAVING
    stan='aktywna';
#zmiana statusu spraw dla klientów wg pesel
UPDATE sprawy_kl, klienci set stan='nieaktywna' where left(klienci.pesel,2)>60 and klienci.id_k=sprawy_kl.sp_id_k;
#widok spraw dla których nie wystawiono jeszcze faktur
CREATE VIEW fv_do_wystawienia as select id_sp, nazwa, nr_f from sprawy_kl LEFT join faktury on id_sp=fv_id_sp HAVING nr_f is null;
CREATE VIEW Fakury_klienci as SELECT id_f, id_k, imie, nazwisko, platnosci.kwota as 'kwota otrzymana', data_otrz, faktury.kwota as 'kwota należna', sprawy_kl.id_sp from klienci LEFT join sprawy_kl on sprawy_kl.sp_id_k = klienci.id_k join faktury on sprawy_kl.id_sp = fv_id_sp join platnosci on pl_id_f = id_f order by data_otrz desc;
CREATE VIEW Klienci_faktury as SELECT id_k, imie, nazwisko, id_f, id_sp, kwota from klienci left join sprawy_kl on sprawy_kl.sp_id_k = klienci.id_k left JOIN faktury on sprawy_kl.id_sp = fv_id_sp;
