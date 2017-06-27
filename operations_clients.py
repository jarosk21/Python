# -*- coding: utf-8 -*-

class ClientOps:
    def new_client (self):
        print ('Wybierz rodzaj klienta')
        self.sql_types = 'SELECT * FROM rodz_kl'
        self.cursor.execute(self.sql_types)
        self.results = self.cursor.fetchall()
        print ('%15s%15s' % ('id rodzaju', 'rodzaj'))
        for row in self.results:
            self.id_r = row[0]
            self.cl_type = row[1]
            print ('%15s%15s' % (self.id_r, self.cl_type))
        self.client_type = int(input('Wprowadź id rodzaju\n'))
        if (self.client_type == 1 or self.client_type == 2):
            self.new_natural_person ()
        else:
            self.new_company ()
                
    def new_adress(self):
        self.cursor.execute('SELECT id_k from klienci order by id_k desc limit 1')
        self.ad_id_k = int(self.cursor.fetchone()[0])
        print ('dodajesz adres dla klietnta nr '+str(self.ad_id_k))
        self.street = input ('podaj nazwę ulicy i numer\n')
        self.city = input ('podaj miasto\n')
        self.post_code = input ('podaj kod pocztowy\n')
        self.tel_num = input ('podaj numer kontaktowy klienta\n')
        self.adr_sql = 'INSERT INTO adresy (ad_id_k, ulica, miasto, kod_p, nr_tel) values (%s, %s, %s, %s, %s)'
        self.cursor.execute (self.adr_sql,(int(self.ad_id_k), self.street, self.city, self.post_code, self.tel_num))
        self.conn.commit()
        
    def new_natural_person ():
        self.cl_name = input ('podaj imię klienta\n')
        self.cl_lastname = input ('podaj nazwisko klienta\n')
        self.pesel = input ('podaj PESEL klienta')
        if (len(self.pesel) == 11):
            print ('Chcesz dodać klienta '+self.cl_name+' '+self.cl_lastname+' nr PESEL '+self.pesel+'?')
            self.confirm = str.lower(input('T - potwierdź\n N - anuluj\n'))
            if (self.confirm == 't'):
                self.add_client_sql = 'INSERT INTO klienci (imie, nazwisko, pesel, kl_id_r) values (%s,%s,%s,%s)'
                self.cursor.execute (self.add_client_sql,(self.cl_name, self.cl_lastname, self.pesel, int(self.client_type)))
                self.conn.commit()
                print ('Dodano nowego klienta, czy chcesz dodać adres?')
                self.ad_confirm = str.lower(input('T - tak\n N - nie\n'))
                if (self.ad_confirm == 't'):
                    print ('dodawanie adresu')
                    self.new_adress()
                    print (self.adr_sql)
                    
                    print ('dodano adres dla klienta '+self.cl_name+' '+self.cl_lastname)
                    
            else:
                print ('\nAnulowano')
                self.wybor()
        else:
            
            print ('błędny pesel')
            self.new_client()
        
    def new_company (self):
        self.company_name = input('Wprowadź nazwę klienta\n')
        self.company_NIP = input('Wprowadź numer NIP\n')
        print ('Chcesz dodać klienta '+self.company_name+' nr NIP '+self.company_NIP+'?')
        self.confirm = str.lower(input('T - potwierdź\n N - anuluj'))
        if (self.confirm == 't'):
            self.add_client_sql = 'INSERT INTO klienci (nazwa,NIP, kl_id_r) values (%s,%s,%s)'
            self.cursor.execute(self.add_client_sql,(self.company_name, int(self.company_NIP), int(self.client_type)))
            self.conn.commit()
            print ('Dodano nowego klienta, czy chcesz dodać adres?')
            self.ad_confirm = str.lower(input('T - tak\n N - nie\n'))
            if (self.ad_confirm == 't'):
                print ('dodawanie adresu')
                self.new_adress()
                print (self.adr_sql)
                print ('dodano adres dla klienta '+self.company_name)
        else:
            print ('Anulowano')
            self.wybor()
            
    def client_read (self):
        self.sql = 'SELECT id_k, imie, nazwisko, pesel, miasto, ulica, nr_tel from klienci left join adresy on klienci.id_k=adresy.ad_id_k'
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        print ('%5s%15s%15s%15s%15s%20s%15s' % ('id_k','imie','nazwisko','pesel','miasto','ulica', 'nr_tel'))
        for row in self.results:
            self.id_k = row [0]
            self.name = row[1]
            self.last = row[2]
            self.pesel = row[3]
            self.city = row[4]
            self.street = row [5]
            self.phonenum = row [6]
            print ('%5s%15s%15s%15s%15s%20s%15s' % (self.id_k, self.name, self.last, self.pesel, self.city, self.street, self.phonenum))    
            
    def client_del(self):
        self.client_read()
        self.lp = input('podaj id klienta do usuniecia')
        self.sql4 = 'delete from klienci where id_k=%s'
        self.dec = input('Czy na pewno chcesz usunąć? t/n')
        if (self.dec == 't'):
            self.cursor.execute(self.sql4,(self.lp))
            print ('usunięto')
            self.conn.commit()
        else:
            print('anulowano')
        self.wybor()      