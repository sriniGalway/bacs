import xml.dom.minidom
import sqlite3

def main():
    #use the parse() function to load and parse the XML file
    doc = xml.dom.minidom.parse('ADDACS_20170607-141103.xml');

    TABLE_NAME = 'MessagingAdvice'

    MessagingAdvice = doc.getElementsByTagName("MessagingAdvice")
    print "%d MessagingAdvice:" % MessagingAdvice.length
    for user in MessagingAdvice:
        print "user-number: " + user.getAttribute("user-number") + " reference :" + user.getAttribute("reference")

    connection = sqlite3.connect('ADDACS.db')
    cursor = connection.cursor()

    query = "SELECT * FROM {table}".format(table=TABLE_NAME)
    result = cursor.execute(query)
    MA = []
    for row in result:
        MA.append({'user_number': row[0], 'record_type': row[1], 'effective_date': row[2], 'reference': row[3],
                   'payer_name': row[4], 'payer_account_number': row[5], 'payer_sort_code': row[6], 'due_date': row[7],
                   'payment_frequency': row[8], 'reason_code': row[9], 'payer_new_account_number': row[10],
                   'payer_new_sort_code': row[11], 'aosn': row[12]})
    connection.close()
    print MA

if __name__ == "__main__":
    main()