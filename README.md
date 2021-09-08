


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

  
 
