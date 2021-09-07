












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
  
####  Contributing
  
  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.
