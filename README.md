# Bussiness-bank
INTRODUCTION:
The bank account management system is an application allowing customers to perform basic transactions from an automatic machine Bank, telephone, via a computer or with a smartphone via the Internet. The system allows the customer to create an account, deposit / withdraw money from his account, as well as view reports from all accounts present.
Customers can access the banks' website to view their account details and perform the transactions on their account according to their requirements. The connection is made by secure access.
From managing the customer information, account information to the transaction happening every minute or second. It does not only preserve the details of the transaction and other information but generates the report to further banking functions. In this banking management system, there are many operations that are automated which ease the work for the working of the bank.
This reduces the requirement for manual labor and the automated tasks will be error-free as they will only work as they are programmed whereas doing work manually there is always a possibility of human error.

AIM OF THE PROJECT:
The main aim of Bank Management Mini DBMS project is to keep record of customer transactions in the bank.We aim to demonstrate the use of create ,read,update,and delete MySQL operations through this project.
The existing bank system is slow as every task is being performed by the human being and comparing the computer task speed with a computer is not fair. The complexity of this system is increased when an increase in the number of customers and with that there will be a number of transactions will be performed now everything needs to log in to a file for reference in the future which is simply not the kind of scenario we need at this time.

The major modules of this system are as follows:
Branch (Bank)
Customer
Accounts
Customer Credit Card
Loan
Employess(Bank)


Major Modules of Banking Management System:
Bank Branch:
This entity contains the details about the location of the branch. This will not help management but separate the employee from branch to branch and customers.
The attributes of this entity are:
Branch-id:This will be the primary key for the entity. This will help to search and sorting uniquely in the table of branch entity.
Branch-name:This attribute will help in verifying the identity of the branch if the branch is led to confusion.
Branch-city:It will contain the city where the branch is located.
Branch-phone:This phone number will be helped in communicating with the branch. This number is only for banking use not for public use. For the public, there will be a single number at all the bank branches.

Employee:
The employee entity contains all the information about the employees working in different branches of the bank. This will enable them to manage the employee data easily. Searching for the information will just a few clicks. It will have all the necessary attributes required for the employer.
It has the following attributes:
Employee-id:This will be the primary key for this entity. It will help in identifying the particular employee easily. This gets useful when two employees have similar name-like conditions.
Employee-name:This is required for the verification purpose. Usually on government issued id cards it has a name as identification.
Employee-address:In any case when the employee’s address needed for example sending an email or documents at the employee’s residence.
Employee-phone:It is good to have employee’s contact number to have immediate communication.
Employee-email:It is required when a bank needs to make an announcement. So, they will select the employees emailed and simply broadcast the announcement.


Customer:
This entity of the banking management system has the details of the customer. It will not contain the banking details but the personal details of the customer which will link to the account by the account number of the customer. After opening an account every user will get one unique account number.
It has the following attributes:
Customer-id:This is the primary key the particular table. It will be used to find the customers personal details.
Customer-name:The customer will be for the document verification for the account opening.
Customer-address:To send any envelope to the customer’s residence or any contact to the address.
Customer-phone:To communicate with the customers over the phone.
Customer-email:To send any offer from the bank to the customer or formal communication with the customer.

Accounts:
This table will contain all the banking account details of the customer. The balance and type of account such type of information will be contained by this entity.
It has the following attributes:
Account-number:This is the primary key for the particular table. It will be linked with the customer table’s attribute of customer id. Each customer id will have a separate account number.
Branch-id:To identify the location of the branch where the customer has opened the account.
Customer-id:This is required to link the correct account number to particular customer id.
Account-type:This will give the idea about the type of account the customer is holding like it could be saving or current or something according to that interest will be calculated.
Balance:How much money a customer has left in the account.
Interest-rate:The interest is given by the bank to the customer for crediting the money into the account.
Account-status:If the customer’s account has been idle for a particular time, then it should be disabled. The customer should make a transaction to keep their account active.


Loan:
This entity of banking management system is for the customer who has applied for a loan from the bank. This will hold the details of the loan for a particular account number. If the customer does not have any loan, it will have null values for the particular account.
It will have the following attributes:
Load-id:This is the primary key in this table. This will be linked with an account number so direct information can be fetched if required.
Account-number:To link the customer details with the loan id.
Interest-rate:The rate of interest bank is charging on the loan given to the customer.
Duration:The duration of the loan that how much time it will take to complete when the user starts to credit the installments of the loan.
Start-date:From when the instalment started to credit the account.
Due-amount:It will hold how much the amount has been credited and how much is left more. “Banking Management System” keeps the track of day and time’s tally record as a complete banking process. It can keep the information of the Account and Search the transaction, Transaction report, Individual account opening form, Group Account.
It displays Transaction reports, Statistical Summary of Account type, and Interest Information. This provides all-time service to the customer provided by the other banks.


