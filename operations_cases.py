# -*- coding: utf-8 -*-

class CasesOps:
   def new_case (self):
      print ('Wybierz rodzaj sprawy\n')
      self.case_types_printer()  
      self.case_type_choice = input('Wprowadź id wybranej kategorii\n')
      self.case_client = input('Wprowadź id klienta\n')
      self.case_name = input('Wprowadź nazwę sprawy\n')
      self.case_desc = input('Wprowadź opis sprawy\n')
      self.case_sql = 'INSERT INTO sprawy_kl (nazwa, opis, sp_id_k, sp_id_kat) values (%s,%s,%s,%s)'
      self.cursor.execute(self.case_sql,(self.case_name, self.case_desc, int(self.case_client), int(self.case_type_choice)))
      self.conn.commit()
      print ('Dodałeś sprawę '+self.case_name+' dla klienta o id '+self.case_client+'\n Czy chcesz dodać kolejną?\n')
      self.case_continue = str.lower(input('T - tak  N - nie'))
      if (self.case_continue == 't'):
         self.new_case()
      else:
         self.wybor()
         
   def case_types_printer(self):
      self.sql_types = 'SELECT * FROM kategorie'
      self.cursor.execute(self.sql_types)
      self.results = self.cursor.fetchall()
      print ('%15s%15s' % ('id kategorii', 'kategoria'))
      for row in self.results:
         self.id_kat = row[0]
         self.case_type = row[1]
         print ('%15s%15s' % (self.id_kat, self.case_type))      
         
   def case_read (self):
      self.sql = 'select id_sp, nazwa, opis, sp_id_k, stan, rodzaj from sprawy_kl left join kategorie on kategorie.id_kat = sprawy_kl.sp_id_kat ORDER BY id_sp'
      self.cursor.execute(self.sql)
      self.results = self.cursor.fetchall()
      print ('%15s%35s%35s%15s%15s%15s' % ('id sprawy', 'nazwa', 'opis', 'id klienta', 'stan', 'rodzaj'))
      for row in self.results:
         self.id_sp = row[0]
         self.case_n = row[1]
         self.case_d = row[2]
         self.id_kli = row[3]
         self.case_stat = row [4]
         self.case_t = row [5]
         print ('%15s%35s%35s%15s%15s%15s' % (self.id_sp, self.case_n, self.case_d, self.id_kli, self.case_stat, self.case_t))   
         
   def case_del(self):
      self.lp = input('podaj id sprawy do usuniecia')
      self.sql4 = 'delete from sprawy_kl where id_sp=%s'
      self.dec = input('Czy na pewno chcesz usunąć? t/n')
      if (self.dec == 't'):
         self.cursor.execute(self.sql4,(self.lp))
         print ('usunięto')
         self.conn.commit()
      else:
         print('anulowano')
      self.wybor()      
      
   def case_mod(self):
      self.case_read()
      self.lp = input('podaj id sprawy do edycji')
      print ('Co chcesz edytować?\n 1 - id klienta \n2 - nazwę i opis \n 3 - kategorię \n 4 - stan\n')
      self.choice = int(input('Wprowadź wybór: '))
      if (self.choice == 1):
         self.sql = 'UPDATE sprawy_kl set sp_id_k = %s where id_sp = %s'
         self.new_data = input('Wprowadź nowe id klienta')
         self.cursor.execute(self.sql,(self.new_data,self.lp))
         self.conn.commit()
      elif (self.choice == 2):
         self.sql = 'UPDATE sprawy_kl set nazwa = %s, opis = %s where id_sp = %s'
         self.new_data = input('Wprowadź nowe nową nazwę')
         self.new_data2 = input('Wprowadź nowy opis')
         self.cursor.execute(self.sql,(self.new_data, self.new_data2, self.lp))
         self.conn.commit()
      elif (self.choice == 3):
         self.case_types_printer()
         self.sql = 'UPDATE sprawy_kl set sp_id_kat = %s where id_sp = %s'
         self.new_data = input('Wprowadź nową kategorię: \n')
         self.cursor.execute(self.sql,(self.new_data, self.lp))
         self.conn.commit()
      elif (self.choice == 4):
         self.sql = 'UPDATE sprawy_kl set stan = %s where id_sp = %s'
         self.stat1 = 'aktywna'
         self.stat2 = 'nieaktywna'
         self.case_stat = int(input('Ustal status:\n 1 - aktywna\n 2 - nieaktywna'))
         if (self.case_stat == 1):
            self.cursor.execute(self.sql,(self.stat1, self.lp))
            self.conn.commit()
         elif (self.case_stat == 2):
            self.cursor.execute(self.sql,(self.stat2, self.lp))
            self.conn.commit()            
         else:
            print ('Błąd - złe wprowadzenie')
      else:
         print('Wprowadzono niezrozumiałą komendę, co dalej?\n 1 - edytuj ponownie\n 2 - menu główne\n')
         self.choice_cont = int(input('Wprowadź wybór: '))
         if (self.choice_cont == 1):
            self.case_mod()
         else: 
            self.wybor()