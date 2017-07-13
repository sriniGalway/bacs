# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('AUDDIS_Acceptance.db')

cursor = connection.cursor()

#Create table query to create MessagingHeader table with initial xml data
create_table_MessagingHeader = "CREATE TABLE IF NOT EXISTS MessagingHeader(subject_first_aosn int,user_name text, document_number int, report_type int, user_number int, stream_identifier int, report_generation_date date, advice_type text, reprint_indicator int, subject_last_aosn int, envelope_sequence_number int)"
cursor.execute(create_table_MessagingHeader)

### MessagingHeader available in xml initially
insert_data_MessagingHeader = """INSERT INTO MessagingHeader(subject_first_aosn,user_name, document_number, report_type, user_number, stream_identifier, report_generation_date, advice_type, reprint_indicator, subject_last_aosn, envelope_sequence_number) 
VALUES
(0,'SS - Fundtech 2048 RBS',0,7003,100266,0,'2016-09-23','AUDACC',0,0,0);"""

cursor.execute(insert_data_MessagingHeader)

#Create table query to create AddresseeInformation table with initial xml data
create_table_AddresseeInformation = "CREATE TABLE IF NOT EXISTS AddresseeInformation(name text, address1 int, address2 int, address3 int, address4 int, address5 int)"
cursor.execute(create_table_AddresseeInformation)

### AddresseeInformation available in xml initially
insert_data_AddresseeInformation = """INSERT INTO AddresseeInformation(name,address1,address2,address3,address4,address5) 
VALUES
('0',0,0,0,0,0);"""

cursor.execute(insert_data_AddresseeInformation)

#Create table query to create MessagingAdvice table with initial xml data
create_table_MessagingAdvice = "CREATE TABLE IF NOT EXISTS MessagingAdvice (user_number int PRIMARY KEY, record_type char, aosn int, processing_date date, originator_file_number text, work_code text, file_type text, accepted_ddi int, rejected_ddi int,vol_serial_number text, file_error_code int)"
cursor.execute(create_table_MessagingAdvice)


### MessagingAdvice available in xml initially
insert_data_MessagingAdvice = """INSERT INTO MessagingAdvice(user_number, record_type, aosn, processing_date, originator_file_number, work_code, file_type, accepted_ddi, rejected_ddi,vol_serial_number, file_error_code) 
VALUES
(100266,'V',418,'2016-09-26','001','1 DAILY','LIVE',2,0,'009727',0);"""

cursor.execute(insert_data_MessagingAdvice)


connection.commit()

connection.close()
