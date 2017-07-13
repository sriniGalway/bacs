import xml.dom.minidom

def main():
    #use the parse() function to load and parse the XML file
    doc = xml.dom.minidom.parse('ARUDD_20170607-141010.xml')

    ServiceLicenseInformation = doc.getElementsByTagName("ServiceLicenseInformation")
    print "ServiceLicenseInformation:"
    print "userName: " + ServiceLicenseInformation[0].getAttribute("userName") + " & userNumber: " + ServiceLicenseInformation[0].getAttribute("userNumber")

    OriginatingAccount = doc.getElementsByTagName("OriginatingAccount")
    print "OriginatingAccount:"
    for account in OriginatingAccount:
        print "name: " + account.getAttribute("name") + " number :" + account.getAttribute("number") + " sortCode :" + account.getAttribute("sortCode")

    ReturnedDebitItem = doc.getElementsByTagName("ReturnedDebitItem")
    print "ReturnedDebitItem:"
    for item in ReturnedDebitItem:
        print "ref: " + item.getAttribute("ref") + " transCode :" + item.getAttribute("transCode") + " valueOf :" + item.getAttribute("valueOf")

    PayerAccount = doc.getElementsByTagName("PayerAccount")
    print "PayerAccount:"
    for paccount in PayerAccount:
        print "number: " + paccount.getAttribute("number") + " name :" + paccount.getAttribute("name") + "sortCode :" + paccount.getAttribute("sortCode")
if __name__ == "__main__":
    main()