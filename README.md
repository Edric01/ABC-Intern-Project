


# **_ABC-Intern-Project_**


![download](https://user-images.githubusercontent.com/70839857/132458514-37d8aa30-a29e-4f2d-bb45-6b012e8e0310.png)
![download (1)](https://user-images.githubusercontent.com/70839857/132459145-07b63c70-6881-4d62-acab-5f804f7a8a16.png)
![2918581](https://user-images.githubusercontent.com/70839857/132460006-385b7725-cdbd-47cf-a7da-502aed8ef10d.png)








<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
<li>
      <a href="#about-the-project">About The Project</a>
      <ul>
<li>
      <a href="#project-description">Project Description</a>
      <ul>
        </ul>
        </li>
<li>
 <a href="#getting-started">Getting Started</a>
      <ul>  


<li>
      <a href="#installation">Installation</a>

<li>
      <a href="#development">Development</a>
        </ul>
        </li>

<li>
      <a href="#contributing">Contributing / Adding features</a>
        </ul>
    </li>
  </ol>


#### About the Project

#### Project Description

1.Backend Framework: **Django**

2.Front-end Framework: **Bootstrap**

3.Database used: **PostgreSQL**

#### Getting Started

####  Installation


1.Fork and Clone

  i.Fork the ABC-Intern-Project Repository
  
  ii.Clone the repo to your local system.
  
2.Create a Virtual Environment for the Project

In Windows

    pip install virtualenv

    virtualenv venv
    
    venv\Scripts\activate

In Ubuntu/MacOS
    
    python -m virtualenv venv

    source venv/bin/activate

If you are using another name for the virtual environment other than venv, then please mention it in .gitignore.

3.Install all the requirements

    pip install -r requirements.txt
    
####  Development

4. Checkout to a different branch

    git status
    
    git pull
    
    git branch
    
    git checkout -b <your-branch-here>

  
  
**Note: the python-openid and python3-openid package that come alone with the social-auth package are bugged. to fix this issue, run the following command:**
  
      pip uninstall python-openid && pip uninstall python3-openid
  
  **press 'y' if asked for authorisation.**
  
  **then reinstall the uninstalled packages**
  
      pip install python-openid && pip install python3-openid
  
  **and then continue with the following instructions**
  
  5.Connecting to Database:

Prior to migrating the tables, you need to connect postgresql with your application. To do so, you need to have an account of postgresql in your device and also pgadmin software. If you do not have these you can download it using the given links:
  
Link to download PostgreSQL :
  https://www.postgresql.org/download/
  
  
Link to download PgAdmin :
  https://www.pgadmin.org/download/

  
  After Downloading both PostgreSQL and PgAdmin, you need to connect PostgreSQL to PgAdmin and then enter your PostgreSQL username and Password in the following page :
  
  
  ![Screenshot (856)](https://user-images.githubusercontent.com/70839857/132460232-24ff6acb-87a8-4c07-8b73-5f1de2d770c0.png)

  
  
  
####  Contributing
  
  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.


####  Documentation
  
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
  
  <li>
  <a href="#logging-in">Logging in</a>
  <ul>
  Login in
  
  Forgot/Reset Password
  
  Log out
    </ul>
    </li>
<li>
  <a href="#services">Services</a>
  <ul>
    <a href="#kyc">KYC</a>
  <ul>
  Create KYC
    
  View KYC
  
  Edit KYC
  </ul>
  </ul>
 <ul>
   <a href="#accounts">Accounts</a>
  <ul> 
Create Account
    
View Account
   </ul>
    </ul>
    </li>
  </ol>

####  Logging in

####  Log in 
  
You can log in using the credetials and then clicking on Log In.

![kk](https://user-images.githubusercontent.com/70839857/132461939-046043d0-1cc9-4fdd-8e53-cafcb713de4c.jpg)


  
Once Logged in, you should be seeing the following landing page.

![1caddbad-e9da-4bd8-b5ce-b31866387461](https://user-images.githubusercontent.com/70839857/132462044-341e4345-706a-4fef-a071-6efc86891ea9.jpg)

 

####  Forgot/Reset Password

Click on the Forgot/ Reset Password on the Log in page if the Credentials are forgotten. On clicking it you will be landing on the following page.

![Screenshot (852)](https://user-images.githubusercontent.com/70839857/132462474-0a03f16a-5c9a-4af1-98fc-ed5f0a47b1b8.png)

  
  
Once you have changed your password you may try to log in. Upon Success you  will be landed on the Home page.
  
####  Log out

To log out, click on the option next to your username, which landed you to the Log in  Page.


![1caddbad-e9da-4bd8-b5ce-b31866387461 - Copy](https://user-images.githubusercontent.com/70839857/132462561-e9592eaf-7d3f-45a7-874a-4635d44b315e.jpg)
  

![kk](https://user-images.githubusercontent.com/70839857/132462799-28bb2569-5139-4c33-816c-27143f4a9e1d.jpg)

  
  
####  Services
On clicking on the services option on the home page you will be directed to the following page. 
  
![1caddbad-e9da-4bd8-b5ce-b31866387461 - Copy (2)](https://user-images.githubusercontent.com/70839857/132462957-9d6b1591-5d7b-43b2-9c8a-7b079bc16318.jpg)
  
![6a8661a6-3276-4d91-a440-a7321f26b559](https://user-images.githubusercontent.com/70839857/132463079-819f403d-31df-43d8-a466-db0639afcc0c.jpg)

 
  
For easy access to the options of services, hover over the services option on the index page and you get the related dropdown box.
  
![6cc6b7cb-32fc-4289-b732-993d5ddecd30](https://user-images.githubusercontent.com/70839857/132463126-8bf88354-b8a1-4d4f-9231-be1666503348.jpg)


  
####  KYC
  
The KYC option contains 3 sub options which include Creation, Edit and View. To access those options click on the KYC option in the services page which will land you to the following page.
 
![6a8661a6-3276-4d91-a440-a7321f26b559 - Copy](https://user-images.githubusercontent.com/70839857/132475639-978ea15e-0652-4c12-9ad1-8c7b98fa0250.jpg)

![0bbf057d-a469-450f-862d-448e77e9029e](https://user-images.githubusercontent.com/70839857/132475825-77355f43-2577-4569-bb58-aeca8e50db6f.jpg)

  
####  Create KYC

To create the KYC form click on the KYC option of the following page (Services -> KYC) and fill the following details on submission you will land on the KYC page and the details will be stored in the database.

![0bbf057d-a469-450f-862d-448e77e9029e - Copy (2)](https://user-images.githubusercontent.com/70839857/132476240-bfaf63f3-73ef-4f81-9798-727a7780cd38.jpg)
  
![Screenshot (853)](https://user-images.githubusercontent.com/70839857/132476714-e0235f54-03a6-4b78-9597-1f1d9a54fdf7.png)




  
####  View KYC

To view the created KYC forms click on the view KYC option which will land you on the following page.
  
![0bbf057d-a469-450f-862d-448e77e9029e - Copy](https://user-images.githubusercontent.com/70839857/132476946-71d15581-86c6-4955-a394-848b277c26be.jpg)
  
  
Enter the required details to view the KYC form which on clicking submit button provides the respective complete KYC form.

![4ade457f-4313-4db0-8205-1215c85a1c7a](https://user-images.githubusercontent.com/70839857/132477084-ebe12bb6-a6ae-405b-b664-c71e2c0e9d26.jpg)

![skan](https://user-images.githubusercontent.com/70839857/132479161-83208aad-f9b4-4176-8475-3a407078e5f9.png)


  
To verify the form click on verify button which will land you on the following page

![6709e0d2-9dad-4385-8863-ee71b08d1c4d](https://user-images.githubusercontent.com/70839857/132477537-7485ad19-df1e-4d4b-a606-a66eec65573a.jpg)
  
Enter the required details along with the option to Verified or Not Verified and click on Submit which will save the changes made and land you on the given page.

![2722cddf-d474-42dd-8650-292a1a8685ad](https://user-images.githubusercontent.com/70839857/132477641-d724162f-58e2-49cc-9731-1262a1f96297.jpg)
  
####  Edit KYC
  
To edit the details of a KYC form click on the edit KYC option which will land you on the following page.

![0bbf057d-a469-450f-862d-448e77e9029e - Copy (3)](https://user-images.githubusercontent.com/70839857/132477134-c39b65b0-1abe-4932-9cb8-674c7ab9cf0d.jpg)

![4ade457f-4313-4db0-8205-1215c85a1c7a](https://user-images.githubusercontent.com/70839857/132477221-adb88e71-aed5-4215-a91f-bad223fb4da0.jpg)

  
Enter the required details to edit the KYC form which on clicking submit button provides the respective form.

![c80e661a-c80f-4f96-ad43-6d08327b231b](https://user-images.githubusercontent.com/70839857/132476342-d11555bf-a8b1-4d69-9698-add2f3273204.jpg)
  
Once the changes are done click on Submit button to save the changes made.
  
####  Accounts
  
To perform various operations related to accounts click on the Accounts option on the Services page. The following page will be loaded.
  
![6a8661a6-3276-4d91-a440-a7321f26b559 - Copy (2)](https://user-images.githubusercontent.com/70839857/132498218-e544405a-09b3-4bba-8551-0d220583bee3.jpg)

![Screenshot (849)](https://user-images.githubusercontent.com/70839857/132498412-cd7a26d8-3837-481c-8f66-05f8d3aa506c.png)

  
####  Create Account
  
To create account click on the create account option on the accounts page. Enter the account number generated when the KYC form is verified. Enter the required details and click on Submit. The Account will be generated and you will be directed to the Accounts page.

![Screenshot (849) - Copy](https://user-images.githubusercontent.com/70839857/132498475-c6aad3ae-d4fc-4fa5-81d1-df337f38cfce.png)

![Screenshot (850)](https://user-images.githubusercontent.com/70839857/132498552-2a3dad27-c10e-4892-ae22-bfa98faf67c3.png)

  
 ![Screenshot (854)](https://user-images.githubusercontent.com/70839857/132498596-e84ef64a-959a-4ac0-aac2-101b6dc81d45.png)


  
####  View Account
  
To view account click ont the view account option on the accounts page. Enter the account number to view the respective account.

![Screenshot (850) - Copy](https://user-images.githubusercontent.com/70839857/132498657-161ccbdf-2e86-4a4f-8180-31403a50c3cc.png)

  
![Screenshot (850)](https://user-images.githubusercontent.com/70839857/132498552-2a3dad27-c10e-4892-ae22-bfa98faf67c3.png)  
  
![Screenshot (851)](https://user-images.githubusercontent.com/70839857/132498724-9b56bdf4-9c14-4a73-a831-0c3aac85b3c4.png)

  
  
