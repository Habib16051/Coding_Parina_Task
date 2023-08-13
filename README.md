# Coding_Parina_Task
This task is given by one of the renown software company in Bangladesh Called Evident BD Ltd!!

I am going to desrcibe from scartch how to install this project into local machine and also test the api endpoint at the end!

# Installation Procees

1. First you need to clone this project using this command:
==> git clone https://github.com/Habib16051/Coding_Parina_Task.git
 2. Create the Virtual Environment:
   ===============================================================================
   a1.python3 -m venv env (for Linux)      
   b1.source/env/bin/activate (For Linux) - To activate the virtual environment
   ================================================================================
    a2. python -m venv env (for Windows)      
    b2. cd env/Scripts/activate (For Windows) - To activate the virtual environment
   ================================================================================
4. It's time to install the requirements.txt file using below command:
   ==> pip3 install -r requirements.txt (For Linux)
   ==> pip install -r requirements.txt (For Windows)

5. Run the server Using this command:
   ==> python3 manage.py runserver (For Linux)
   ==> python manage.py runserver (For Windows)
 

Here  are the three Tasks have been given by the Evident BD:

Section 1:

User Authentication/Registration Page

A user login and registration section. You can use whatever input fields you want (maintaining a standard)

![image](https://github.com/Habib16051/Coding_Parina_Task/assets/39822204/6f95e77c-6c18-4f55-b730-4be53f7239db)

And if we don't have account, then we can register for a new acount:

![image](https://github.com/Habib16051/Coding_Parina_Task/assets/39822204/6255bb39-ee58-4edc-b17b-79d34a6a1b1d)

After Login: We will move on for the Section 2 of the project:

Section 2:

Khoj the search Page

After login, users can access this page.
Khoj the search: In this segment(page), there will be two input fields

    Input Values: User can input comma separated integers

    Search Value: User can input only one integer 

Output: Will print True if the search value is in the input values. 


![image](https://github.com/Habib16051/Coding_Parina_Task/assets/39822204/3c81a387-8736-4e5f-8c4d-bed47dd80726)

Otherwise print False

![image](https://github.com/Habib16051/Coding_Parina_Task/assets/39822204/1a07bcaf-66ba-4efb-9969-6f96388845be)


and It's time foe the Scetion 3:

Section 3:

API Endpoints:

In this section, there will be only one API endpoints

Endpoint 1: Get All Input Values

   Check the following response format.

{
    “status”: “succes”,
    “user_id” : 1,
    “payload” : [
         {
              “timestamp” : ”2012-01-01 00:00:00”,
              “input_values” : “11, 10, 9, 7, 5, 1, 0”
          },
         {
                “timestamp” : ”2013-01-01 01:00:00”,
                 “input_values” : “13, 11, 10, 7, 5, 2, 1”
          
       ]
}

So My output for the Sections 3 is:

![section](https://github.com/Habib16051/Coding_Parina_Task/assets/39822204/febc3495-6e54-458a-9d33-e65ff1788c9f)




