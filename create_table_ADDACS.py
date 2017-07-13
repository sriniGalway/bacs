# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('ADDACS.db')

cursor = connection.cursor()

#Create table query to create MessagingHeader table with initial xml data
create_table_MessagingHeader = "CREATE TABLE IF NOT EXISTS MessagingHeader (document_number int PRIMARY KEY, advice_type text, subject_first_aosn text, subject_last_aosn text,user_number int, stream_identifier int, envelope_sequence_number text, report_generation_date date, user_name text, report_type int)"
cursor.execute(create_table_MessagingHeader)

### MessagingHeader available in xml initially
insert_data_MessagingHeader = """INSERT INTO MessagingHeader(document_number,advice_type,subject_first_aosn,subject_last_aosn, user_number,stream_identifier,envelope_sequence_number,report_generation_date,user_name, report_type) 
VALUES
(0,'ADDACS','00000004','00000017',100288,0,'00000003', '2017-04-06', 'SS - Fundtech Barclays', 7001);"""

cursor.execute(insert_data_MessagingHeader)

#Create table query to create AddresseeInformation table with initial xml data
create_table_AddresseeInformation = "CREATE TABLE IF NOT EXISTS AddresseeInformation(name text)"
cursor.execute(create_table_AddresseeInformation)

### AddresseeInformation available in xml initially
insert_data_AddresseeInformation = """INSERT INTO AddresseeInformation(name) 
VALUES
(' ');"""

cursor.execute(insert_data_AddresseeInformation)

#Create table query to create MessagingAdvice table with initial xml data
create_table_MessagingAdvice = "CREATE TABLE IF NOT EXISTS MessagingAdvice (user_number int PRIMARY KEY, record_type char, effective_date date, reference int, payer_name text, payer_account_number int, payer_sort_code int, due_date date, payment_frequency int, reason_code char, payer_new_account_number int, payer_new_sort_code int, aosn text)"
cursor.execute(create_table_MessagingAdvice)

### MessagingAdvice available in xml initially
insert_data_MessagingAdvice = """INSERT INTO MessagingAdvice (user_number,record_type,effective_date,reference,payer_name,payer_account_number,payer_sort_code, due_date, payment_frequency, reason_code, payer_new_account_number,payer_new_sort_code,aosn) 
VALUES
(100288,'A','2017-04-07',61956964,'G -&amp; J JONES T/A',20212616,086001,'2017-04-07',0,'C',20212616,608301,'00000004');"""

cursor.execute(insert_data_MessagingAdvice)


connection.commit()

connection.close()
