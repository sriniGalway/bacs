



#MessagingAdvice
ADDACS
user_number,record_type,aosn,effective_date,reference,payer_name,payer_account_number,payer_sort_code, reason_code, payer_new_account_number,payer_new_sort_code,due_date, payment_frequency)

ARUDD
No data on MessagingAdvice

AUDDIS_Bank Return
user_number,record_type,aosn,effective_date,reference,payer_name,payer_account_number,payer_sort_code, reason_code, payer_new_account_number, payer_new_sort_code, transaction_code, orig_sort_code, orig_account_number,  original_proc_date, originator_name)

AUDDIS_Acceptance / Rejection
user_number, record_type, aosn, processing_date, originator_file_number, work_code, file_type, accepted_ddi, rejected_ddi,vol_serial_number, file_error_code)


#bacs
user_number,record_type,aosn,effective_date,reference,payer_name,payer_account_number,payer_sort_code, reason_code, payer_new_account_number,payer_new_sort_code,due_date, payment_frequency, transaction_code, orig_sort_code, orig_account_number,  original_proc_date, originator_name, processing_date, originator_file_number, work_code, file_type, accepted_ddi, rejected_ddi,vol_serial_number, file_error_code)

#Create table query to create MessagingAdvice table with initial xml data
create_table_MessagingAdvice = "CREATE TABLE IF NOT EXISTS MessagingAdvice
(user_number int PRIMARY KEY, Advice_type text, record_type char, aosn text,effective_date date,
reference int, payer_name text, payer_account_number int, payer_sort_code int, reason_code char,
payer_new_account_number int, payer_new_sort_code int, due_date date, payment_frequency int,
transaction_code text, orig_sort_code int, orig_account_number text,  original_proc_date date,
originator_name text, processing_date date, originator_file_number text, work_code text, file_type text,
accepted_ddi int, rejected_ddi int,vol_serial_number text, file_error_code int)"
cursor.execute(create_table_MessagingAdvice)

### MessagingAdvice available in xml initially
insert_data_MessagingAdvice = """INSERT INTO MessagingAdvice (
user_number,Advice_type, record_type,aosn,effective_date,
reference,payer_name,payer_account_number,payer_sort_code, reason_code,
payer_new_account_number,payer_new_sort_code, due_date, payment_frequency,
transaction_code, orig_sort_code, orig_account_number,  original_proc_date,
originator_name, processing_date, originator_file_number, work_code, file_type,
accepted_ddi, rejected_ddi,vol_serial_number, file_error_code)
VALUES
(100288,'ADDACS','A','00000004','2017-04-07',
61956964,'G -&amp; J JONES T/A',20212616,086001,'C',
20212616,608301,'2017-04-07',0,
'',0,'00000000','2017-1-01',
'', '2016-01-01','000','','',
0,0,'000000',0);"""

cursor.execute(insert_data_MessagingAdvice)
