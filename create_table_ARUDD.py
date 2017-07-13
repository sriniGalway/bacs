# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('ARUDD.db')

cursor = connection.cursor()

#Create table query to create Header table with initial xml data
create_table_Header = "CREATE TABLE IF NOT EXISTS Header(reportType text PRIMARY KEY, adviceNumber int, currentProcessingDate date)"
cursor.execute(create_table_Header)

### Header available in xml initially
insert_data_MessagingHeader = """INSERT INTO Header(reportType,adviceNumber,currentProcessingDate) 
VALUES
('REFT1019', 999, '2016-10-04');"""

cursor.execute(insert_data_MessagingHeader)

#Create table query to create AddresseeInformation table with initial xml data
create_table_AddresseeInformation = "CREATE TABLE IF NOT EXISTS AddresseeInformation(name text)"
cursor.execute(create_table_AddresseeInformation)

### AddresseeInformation available in xml initially
insert_data_MessagingHeader = """INSERT INTO AddresseeInformation(name) 
VALUES
('SS - Fundtech 2048 RBS');"""

cursor.execute(insert_data_MessagingHeader)

#Create table query to create ServiceLicenseInformation table with initial xml data
create_table_ServiceLicenseInformation = "CREATE TABLE IF NOT EXISTS ServiceLicenseInformation(userNumber int PRIMARY KEY, userName text)"
cursor.execute(create_table_ServiceLicenseInformation)

### ServiceLicenseInformation available in xml initially
insert_data_ServiceLicenseInformation = """INSERT INTO ServiceLicenseInformation(userNumber,userName) 
VALUES
('SS - Fundtech 2048 RBS', 100266);"""

cursor.execute(insert_data_ServiceLicenseInformation)


#Create table query to create MessagingAdvice table with initial xml data
create_table_OriginatingAccount = "CREATE TABLE IF NOT EXISTS OriginatingAccount(number int PRIMARY KEY, name text, sortCode text, type int, bankName text, branchName text )"
cursor.execute(create_table_OriginatingAccount)

### MessagingAdvice available in xml initially
insert_data_OriginatingAccount = """INSERT INTO OriginatingAccount(number,name,sortCode,type,bankName,branchName)
VALUES
(10627690,'FUNDTECH    ','20-92-08',0,'BARCLAYS BANK PLC','WAVENEY VALLEY');"""

cursor.execute(insert_data_OriginatingAccount)


#Create table query to create ReturnedDebitItem table with initial xml data
create_table_ReturnedDebitItem = "CREATE TABLE IF NOT EXISTS ReturnedDebitItem(ref text,transCode text,returnCode text,returnDescription text, originalProcessingDate date, valueOf float, currency text)"
cursor.execute(create_table_ReturnedDebitItem)

### ReturnedDebitItem available in xml initially
insert_data_ReturnedDebitItem = """INSERT INTO ReturnedDebitItem(ref,transCode,returnCode,returnDescription,originalProcessingDate,valueOf,currency)
VALUES
('FUNDTECH 4        ','01', '0273','REFER TO PAYER','2016-09-29', 10.00,'GBP');"""

cursor.execute(insert_data_ReturnedDebitItem)

#Create table query to create ReturnedDebitItem table with initial xml data
create_table_PayerAccount = "CREATE TABLE IF NOT EXISTS PayerAccount(number int, ref text, name text,sortCode text, bankName text, branchName text)"
cursor.execute(create_table_PayerAccount)

### PayerAccount available in xml initially
insert_data_PayerAccount = """INSERT INTO PayerAccount(number, ref, name,sortCode, bankName, branchName)
VALUES
(33479536, 'FUNDTECH 4        ','J SMITH           ','20-07-82', 'BARCLAYS BANK PLC','BIRMINGHAM EDGBASTON');"""

cursor.execute(insert_data_PayerAccount)

connection.commit()

connection.close()
