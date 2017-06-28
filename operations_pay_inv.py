# -*- coding: utf-8 -*-
import pymysql


class Payments_invoices:
    def payments_read(self):
        print ('Lista otrzymanych płatności')
        self.sql = 'SELECT id_k, imie, nazwisko, platnosci.kwota, data_otrz, faktury.kwota, sprawy_kl.id_sp from klienci LEFT join sprawy_kl on sprawy_kl.sp_id_k = klienci.id_k join faktury on sprawy_kl.id_sp = fv_id_sp join platnosci on pl_id_f = id_f order by data_otrz desc'
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        print ('%5s%15s%15s%15s%15s%20s%15s' % ('id_k','imie','nazwisko','kwota otrzymana','data otrzymania','kwota należna', 'id sprawy'))
        for row in self.results:
            self.id_k = row [0]
            self.name = row[1]
            self.last = row[2]
            self.pay_rec = row[3]
            self.date_rec = row[4]
            self.pay_inv = row[5]
            self.case_id = row [6]
            print ('%5s%15s%15s%15s%15s%20s%15s' % (self.id_k, self.name, self.last, self.pay_rec, self.date_rec, self.pay_inv, self.case_id))
    
    def invoice_read(self):
        print ('Jakie faktury chcesz wyświetlić')
        self.choice = int(input ('1 - wszystkie wystawione\n2 - do wystawienia\n3 - nieopłacone\n4 - anuluj, wróć do menu głównego'))
        if (self.choice == 1):
            self.invoices_all()
        elif (self.choice == 2):
            self.invoices_todo()
        elif (self.choice == 3):
            self.invoices_unpaid()
        elif (self.choice == 4):
            self.wybor()        
        else:
            print ('Nie ma takiej opcji, wybierz ponownie')
            self.invoice_read()
            
    def invoices_all(self):
        self.sql = 'SELECT * FROM Klienci_faktury;'
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        print ('%5s%15s%15s%15s%15s%20s' % ('id_k','imie','nazwisko','id faktury','id sprawy','kwota należna'))
        for row in self.results:
            self.id_k = row [0]
            self.name = row[1]
            self.last = row[2]
            self.inv_id = row[3]
            self.case_id = row[4]
            self.amount = row[5]
            print ('%5s%15s%15s%15s%15s%20s' % (self.id_k, self.name, self.last, self.inv_id, self.case_id, self.amount))
            
    def invoices_todo(self):
        self.sql = 'SELECT id_k, imie, nazwisko, klienci.nazwa, id_sp, sprawy_kl.nazwa from fv_do_wystawienia natural left join sprawy_kl left join klienci on sprawy_kl.sp_id_k = klienci.id_k'
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        print ('%5s%15s%15s%15s%15s%20s' % ('id_k','imie','nazwisko', 'nazwa','id sprawy','nazwa sprawy'))
        for row in self.results:
            self.id_k = row [0]
            self.name = row[1]
            self.last = row[2]
            self.compname = row[3]
            self.case_id = row[4]
            self.case_desc = row[5]
            print ('%5s%15s%15s%15s%15s%20s' % (self.id_k, self.name, self.last, self.compname, self.case_id, self.case_desc))
            
    def invoices_unpaid(self):
        self.sql = 'SELECT * FROM nieoplacone;'
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        print ('%5s%15s%15s%15s%15s' % ('id_k','imie','nazwisko', 'zaległość','id faktury'))
        for row in self.results:
            self.id_k = row [0]
            self.name = row[1]
            self.last = row[2]
            self.debt = row[3]
            self.inv_id = row[4]
            print ('%5s%15s%15s%15s%15s' % (self.id_k, self.name, self.last, self.debt, self.inv_id))
            
    def new_invoice(self):
        self.case_id = input('Podaj id sprawy')
        self.amount = input('Podaj kwotę do zapłaty')
        self.issuance_date = input('Podaj datę wystawienia w formacie rrrr-mm-dd')
        self.pay_deadline = input ('Podaj termin płatności')
        self.sql = 'INSERT INTO faktury (fv_id_sp, kwota, data_wyst, termin_p) values (%s, %s, %s, %s)'
        self.cursor.execute(self.sql,(self.case_id, self.amount, self.issuance_date, self.pay_deadline))
        self.conn.commit()
        print ('Dodano fakturę')
    
    def new_payment(self):
        self.invoice_id = input ('Podaj id faktury')
        self.amount = input('Podaj otrzymaną kwotę')
        self.rec_date = input('Podaj datę otrzymania w formacie rrrr-mm-dd')
        self.sql = 'INSERT INTO platnosci (pl_id_f, kwota, data_otrz) values (%s, %s, %s)'
        self.cursor.execute(self.sql,(self.invoice_id_id, self.amount, self.rec_date))
        self.conn.commit()
        print ('Dodano płatność')        
    
    def invoice_del(self):
        self.lp = input('podaj id faktury do usuniecia')
        self.sql4 = 'delete from faktury where id_f=%s'
        self.dec = str.lower(input('Czy na pewno chcesz usunąć? t/n'))
        if (self.dec == 't'):
            self.cursor.execute(self.sql4,(self.lp))
            print ('usunięto')
            self.conn.commit()
        else:
            print('anulowano')
        self.wybor()          
        
    def payments_del(self):
        self.lp = input('podaj id płatności do usuniecia')
        self.sql4 = 'delete from platnosci where id_p=%s'
        self.dec = str.lower(input('Czy na pewno chcesz usunąć? t/n'))
        if (self.dec == 't'):
            self.cursor.execute(self.sql4,(self.lp))
            print ('usunięto')
            self.conn.commit()
        else:
            print('anulowano')
        self.wybor()        
        
    def payments_mod(self):
        self.sql = 'UPDATE platnosci set pl_id_f = %s, kwota = %s, data_otrz = %s where id_p = %'
        self.lp = input('Podaj id płatności do modyfikacji\n')
        self.new_data = input('Podaj id powiązanej faktury\n')
        self.new_data1 = input('Podaj kwotę\n')
        self.new_data2 = input('Podaj datę otrzymania w formacie rrrr-mm-dd\n')
        print ('Dla płatności o nr id '+self.lp+' wprowadzono nowe dane:\n powiązana faktura - \n'+self.new_data+'\nKwota - \n'+self.new_data1+'\nData otrzymania - '+self.new_data2+'\n')
        self.cursor.execute(self.sql,(self.new_data, self.new_data1, self.new_data2, self.lp))
        self.conn.commit()
        
    def invoice_mod(self):
        self.sql = 'UPDATE faktury set nr_f = %s, fv_id_sp = %s, kwota = %s, data_wyst = %s, termin_p = %s where id_f = %s'
        self.lp = input('Podaj id faktury do modyfikacji\n')
        self.new_data = input('Wprowadź numer faktury\n')
        self.new_data1 = input('Wprowadź id powiązanej sprawy\n')
        self.new_data2 = input('Wprowadź kwotę\n')
        self.new_data3 = input('Wprowadź datę wystawienia w formacie rrrr-mm-dd\n')
        self.new_data4 = input('Wprowadź termin płatności\n')
        self.cursor.execute(self.sql,(self.new_data, self.new_data1, self.new_data2, self.new_data3, self.new_data4, self.lp))
        self.conn.commit()