# -*- coding: utf-8 -*-

class CasesOps:
   def new_case (self):
      print ('Wybierz rodzaj sprawy\n')
      self.sql_types = 'SELECT * FROM kategorie'
      self.cursor.execute(self.sql_types)
      self.results = self.cursor.fetchall()
      print ('%15s%15s' % ('id kategorii', 'kategoria'))
      for row in self.results:
         self.id_kat = row[0]
         self.case_type = row[1]
         print ('%15s%15s' % (self.id_kat, self.case_type))  
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