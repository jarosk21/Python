# -*- coding: utf-8 -*-
import pymysql
from operations_cases import *
from operations_clients import *
from operations_pay_inv import *

class MenuDB(ClientOps, Payments_invoices, CasesOps):
    def __init__(self):
        print('Logowanie do bazy danych')
        self.uname = input('podaj login ')
        self.upass = input('podaj haslo ')        
        self.conn = pymysql.connect ('localhost', self.uname, self.upass, 'dbKancelaria1')
        self.logowanie()
        #login 
    def logowanie(self):
        print ('Logowanie użytkownika')
        self.sqlp = 'Select * from Users where user_name=%s and pass=%s'
        self.cursor = self.conn.cursor()
        self.login = input('podaj login\n')
        self.password = input('podaj hasło\n')
        self.cursor.execute(self.sqlp,(self.login, self.password))
        if (self.cursor.rowcount == 1):
            print ('Zalogowano')
            self.wybor()
        else: 
            print ('bledny login lub hasło')
            self.logowanie()
        #main menu
    def wybor(self):
        self.uname = self.login
        print ('Witaj '+self.uname)
        self.i = str.lower(input('Co chcesz zrobić?\n s - wyświetl dane z bazy\n i - dodawanie wpisów\n m - modyfikacja wpisu\n d - usuniecie wpisu\n\n q -wyjscie \n:'))
        if (self.i == 's'):
            self.odczyt()
            self.wybor()
        elif (self.i == 'i'):
            self.wprowadzanie()
            self.odczyt()
            self.wybor()
        elif (self.i == 'm'):
            self.modyfikacja()
        elif (self.i == 'd'):
            self.usuwanie()      
        elif (self.i == 'q'):
            print ('zakończenie programu')
        else:
            print ('wprowadziłeś niezrozumiałą komendę')
            self.wybor()
            
        #submenu - input choice
    def wprowadzanie (self):
        self.choice_input = str.lower(input('Co chcesz dodać?\n k - nowy klient\n s - nowa sprawa\n p - nowa płatność\n f - nowa faktura\n'))
        if (self.choice_input == 'k'):
            self.new_client()
            self.continuance = str.lower(input ('Czy chcesz dodać kolejnego klienta ?\n T - Tak\n N - Nie \n'))
            if (self.continuance == 't'):
                self.new_client()
            else:
                self.wybor()
        elif (self.choice_input == 's'):
            self.new_case ()
            self.continuance = str.lower(input ('Czy chcesz dodać kolejną sprawę ?\n T - Tak\n N - Nie \n'))
            if (self.continuance == 't'):
                self.new_case()
            else:
                self.wybor()     
        elif (self.choice_input == 'p'):
            self.new_payment()
            self.continuance = str.lower(input ('Czy chcesz dodać kolejną płatność ?\n T - Tak\n N - Nie \n'))
            if (self.continuance == 't'):
                self.new_payment()
            else:
                self.wybor()
        elif (self.choice_input == 'f'):
            self.new_invoice()
            self.continuance = str.lower(input ('Czy chcesz dodać kolejną fakturę ?\n T - Tak\n N - Nie \n'))
            if (self.continuance == 't'):
                self.new_invoice()
            else:
                self.wybor()
        else:
            print ('Wprowadziłeś niezrozumiałą komendę, wprowadź jeszcze raz')
            self.wybor()
            
       
        #submenu - read choice
    def odczyt (self):
        self.choice_input = str.lower(input('Co chcesz odczytać?\n k - dane klientów\n s - lista spraw\n p - lista płatności\n f - lista faktur\n'))
        if (self.choice_input == 'k'):
            self.client_read()
            self.wybor()
        elif (self.choice_input == 's'):
            self.case_read ()
            self.wybor()
        elif (self.choice_input == 'p'):
            self.payments_read()
            self.wybor()
        elif (self.choice_input == 'f'):
            self.invoice_read()
            self.wybor()
           
        #submenu - modification choice
    def modyfikacja (self):
        self.choice_input = input ('Co chcesz zmodyfikować?\n k - dane klienta\n s - sprawę\n f- faktury\n p - płatności\n')
        if (self.choice_input == 'k'):
            self.client_mod()
            self.wybor()
        elif (self.choice_input == 's'):
            self.case_mod ()
            self.wybor()
        elif (self.choice_input == 'p'):
            self.payments_mod()
            self.wybor()
        elif (self.choice_input == 'f'):
            self.invoice_mod()
            self.wybor()        
   
        
        #submenu - delete
    def usuwanie (self):
        self.choice_input = input ('Co chcesz usunąć?\n k - dane klienta\n s - sprawę\n f- faktury\n p - płatności\n')
        if (self.choice_input == 'k'):
            self.client_del()
            self.wybor()
        elif (self.choice_input == 's'):
            self.case_del()
            self.wybor()
        elif (self.choice_input == 'p'):
            self.payments_del()
            self.wybor()
        elif (self.choice_input == 'f'):
            self.invoice_del()
            self.wybor()                


p1 = MenuDB()

