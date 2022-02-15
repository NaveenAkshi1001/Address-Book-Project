class AddressBook:

    def init(self):
        self.contactname=""
        self.emailid=""

    def givecontactdetails(self):
        self.contactname=input("\nEnter person name:")
        self.emailid=input("Enter EmailID:")

    def display(self):
        print("Contact Name:",self.contactname)
        print("EmailID:",self.emailid)
        print("\n")

contactList=[]

choice='y'
while (choice == 'y'):
    print("1.Add New Contact\n2.Display Contacts")
    response=int(input("\nEnter your choice:"))

    if(response==1):
      contact=AddressBook()
      contact.givecontactdetails()
      contactList.append(contact)

    elif(response==2):
        for x in contactList:
            x.display()

    else:
        print("Please Check Your Response!!!")

    choice=input("\nPress 'y' To Continue:") 
    
