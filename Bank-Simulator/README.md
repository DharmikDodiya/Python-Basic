# This program allows the user to interact with a MySQL database to simulate basic banking operations. It enables the creation of a database and table and user account management. Below is the overview of the system's features

**Features**
- Database Creation & Credential Storage:

-The user is prompted to input the following details:
- Hostname
- Username
- Password
- Database name
- Table name

- The system validates the MySQL username and password. If valid, it creates the specified database and table.
- The database credentials are then encrypted and stored in a creds folder for secure access. This folder will only be created once, and future uses will retrieve credentials from it.

![image](https://github.com/user-attachments/assets/f87728c1-a7f2-4a50-afa1-dd27a83c443e)

After Display Bank Simulator Menu

**Create Account**
- User can create a new account by entering their details.
- The account PIN is stored securely in an encrypted format in the database.
  
![image](https://github.com/user-attachments/assets/6895d3ad-2153-4718-90d3-e4795f4b38df)

- pin stored in database as a encrypted mode

![image](https://github.com/user-attachments/assets/0fec5bb8-eb3e-4064-827b-64264ed47ab7)

**View Account(Check Balance)**
- Users can view their account details by entering their account PIN, which is validated before accessing account information.
![image](https://github.com/user-attachments/assets/397929bd-b208-4b54-ad44-da61d4c2ff59)

**Deposit**
- Users can deposit money into their account, and the transaction is recorded in the database.
![image](https://github.com/user-attachments/assets/2582ea9c-1e1b-4585-86aa-74d7b6155261)

**Withdraw**
- Users can withdraw money from their account after validating the transaction and available balance.
![image](https://github.com/user-attachments/assets/625cf9de-9c62-4575-8ba9-3194807f6788)

**Delete Account**
- Users can delete their account by providing their PIN for validation.
![image](https://github.com/user-attachments/assets/9fa8f010-b81f-462f-9b76-44ad64d03c19)


