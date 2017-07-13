# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('bacs.db')

cursor = connection.cursor()

#Create table query to create Messaging Header table with initial xml data
create_table_MessagingHeader = "CREATE TABLE IF NOT EXISTS MessagingHeader(document_number int, advice_type text, subject_first_aosn text, subject_last_aosn text,user_number int, stream_identifier int, envelope_sequence_number text, report_generation_date date, user_name text, reportType text, adviceNumber int, currentProcessingDate date)"
cursor.execute(create_table_MessagingHeader)

### MessagingHeader available in xml initially
insert_data_MessagingHeader = """INSERT INTO MessagingHeader(document_number,advice_type,subject_first_aosn,subject_last_aosn, user_number,stream_identifier,envelope_sequence_number,report_generation_date,user_name, reportType, adviceNumber, currentProcessingDate) 
VALUES
(0,'ADDACS','00000004','00000017',100288,0,'00000003', '2017-04-06', 'SS - Fundtech Barclays', 7001, 0, '2016-10-04');"""

cursor.execute(insert_data_MessagingHeader)

#Create table query to create AddresseeInformation table with initial xml data
create_table_AddresseeInformation = "CREATE TABLE IF NOT EXISTS AddresseeInformation(advice_type text,name text, address1 int, address2 int, address3 int, address4 int, address5 int)"
cursor.execute(create_table_AddresseeInformation)

### AddresseeInformation available in xml initially
insert_data_AddresseeInformation = """INSERT INTO AddresseeInformation(advice_type,name,address1,address2,address3,address4,address5) 
VALUES
('AUDDIS_Acceptance','0',0,0,0,0,0);"""
cursor.execute(insert_data_AddresseeInformation)

#Create table query to create ServiceLicenseInformation table with initial xml data
create_table_ServiceLicenseInformation = "CREATE TABLE IF NOT EXISTS ServiceLicenseInformation(advice_type text,userNumber int PRIMARY KEY, userName text)"
cursor.execute(create_table_ServiceLicenseInformation)

### ServiceLicenseInformation available in xml initially
insert_data_ServiceLicenseInformation = """INSERT INTO ServiceLicenseInformation(advice_type,userNumber,userName) 
VALUES
('ARUDD','SS - Fundtech 2048 RBS', 100266);"""

cursor.execute(insert_data_ServiceLicenseInformation)


#Create table query to create MessagingAdvice table with initial xml data
create_table_OriginatingAccount = "CREATE TABLE IF NOT EXISTS OriginatingAccount(advice_type text,number int PRIMARY KEY, name text, sortCode text, type int, bankName text, branchName text )"
cursor.execute(create_table_OriginatingAccount)

### MessagingAdvice available in xml initially
insert_data_OriginatingAccount = """INSERT INTO OriginatingAccount(advice_type,number,name,sortCode,type,bankName,branchName)
VALUES
('ARUDD',10627690,'FUNDTECH    ','20-92-08',0,'BARCLAYS BANK PLC','WAVENEY VALLEY');"""

cursor.execute(insert_data_OriginatingAccount)


#Create table query to create ReturnedDebitItem table with initial xml data
create_table_ReturnedDebitItem = "CREATE TABLE IF NOT EXISTS ReturnedDebitItem(advice_type text,ref text,transCode text,returnCode text,returnDescription text, originalProcessingDate date, valueOf float, currency text)"
cursor.execute(create_table_ReturnedDebitItem)

### ReturnedDebitItem available in xml initially
insert_data_ReturnedDebitItem = """INSERT INTO ReturnedDebitItem(advice_type,ref,transCode,returnCode,returnDescription,originalProcessingDate,valueOf,currency)
VALUES
('ARUDD','FUNDTECH 4        ','01', '0273','REFER TO PAYER','2016-09-29', 10.00,'GBP');"""

cursor.execute(insert_data_ReturnedDebitItem)

#Create table query to create ReturnedDebitItem table with initial xml data
create_table_PayerAccount = "CREATE TABLE IF NOT EXISTS PayerAccount(advice_type text,number int, ref text, name text,sortCode text, bankName text, branchName text)"
cursor.execute(create_table_PayerAccount)

### PayerAccount available in xml initially
insert_data_PayerAccount = """INSERT INTO PayerAccount(advice_type,number, ref, name,sortCode, bankName, branchName)
VALUES
('ARUDD',33479536, 'FUNDTECH 4        ','J SMITH           ','20-07-82', 'BARCLAYS BANK PLC','BIRMINGHAM EDGBASTON');"""

cursor.execute(insert_data_PayerAccount)

#Create table query to create MessagingAdvice table with initial xml data
create_table_MessagingAdvice = "CREATE TABLE IF NOT EXISTS MessagingAdvice (user_number int PRIMARY KEY, Advice_type text, record_type char, aosn text,effective_date date, reference int, payer_name text, payer_account_number int, payer_sort_code int, reason_code char, payer_new_account_number int, payer_new_sort_code int, due_date date, payment_frequency int, transaction_code text, orig_sort_code int, orig_account_number text,  original_proc_date date, originator_name text, processing_date date, originator_file_number text, work_code text, file_type text, accepted_ddi int, rejected_ddi int,vol_serial_number text, file_error_code int)"
cursor.execute(create_table_MessagingAdvice)

### MessagingAdvice available in xml initially
insert_data_MessagingAdvice = """INSERT INTO MessagingAdvice (user_number,Advice_type, record_type,aosn,effective_date,reference,payer_name,payer_account_number,payer_sort_code, reason_code, payer_new_account_number,payer_new_sort_code, due_date, payment_frequency, transaction_code, orig_sort_code, orig_account_number,  original_proc_date, originator_name, processing_date, originator_file_number, work_code, file_type, accepted_ddi, rejected_ddi,vol_serial_number, file_error_code) 
VALUES
(100288,'ADDACS','A','00000004','2017-04-07',61956964,'G -&amp; J JONES T/A',20212616,086001,'C',20212616,608301,'2017-04-07',0,'',0,'00000000','2017-1-01','', '2016-01-01','000','','',0,0,'000000',0);"""

cursor.execute(insert_data_MessagingAdvice)

connection.commit()

connection.close()
