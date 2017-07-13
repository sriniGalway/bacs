# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('AUDDIS_BankReturn.db')

cursor = connection.cursor()

#Create table query to create MessagingHeader table with initial xml data
create_table_MessagingHeader = "CREATE TABLE IF NOT EXISTS MessagingHeader(document_number int,advice_type text,subject_first_aosn text,subject_last_aosn text,user_number int,stream_identifier int,envelope_sequence_number text,report_generation_date date,user_name text,report_type int)"
cursor.execute(create_table_MessagingHeader)


### MessagingHeader available in xml initially
insert_data_MessagingHeader = """INSERT INTO MessagingHeader(document_number, advice_type, subject_first_aosn, subject_last_aosn, user_number, stream_identifier, envelope_sequence_number, report_generation_date,user_name, report_type) 
VALUES
(0,'AUDDIS','00489089', '00489105',112233,0, '00010433', '2006-10-17', 'HHHHHHH GGGGGGGGG IIIIIIIIIII', 7002);"""

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
create_table_MessagingAdvice = "CREATE TABLE IF NOT EXISTS MessagingAdvice(user_number text, record_type char, effective_date date, reference text, payer_name text, payer_account_number text, payer_sort_code text, reason_code char, payer_new_account_number text, payer_new_sort_code text, aosn text, transaction_code text, orig_sort_code int, orig_account_number text,  original_proc_date date, originator_name text)"
cursor.execute(create_table_MessagingAdvice)


### MessagingAdvice available in xml initially
insert_data_MessagingAdvice = """INSERT INTO MessagingAdvice(user_number, record_type, effective_date, reference, payer_name, payer_account_number, payer_sort_code, reason_code, payer_new_account_number, payer_new_sort_code, aosn, transaction_code, orig_sort_code, orig_account_number,  original_proc_date, originator_name) 
VALUES
(856664,'S','2017-03-23','A09031702','','00000019','600001', 'V','','','00009743','0S',600001,'00000019','2017-03-23','Test1');"""

cursor.execute(insert_data_MessagingAdvice)

connection.commit()

connection.close()
