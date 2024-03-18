<h1>COMP 3005 - Assignment 3</h1>
<hr/>
<h2>Setup:</h2>

Use the provided setup.sql found in the database_scripts folder to populate the database.
It will create the students table and add the default student values.

The database most be created manually first in PgAdmin

The following python packages will need to be installed:

```pip install psycopg```
```pip install psycopg[binary,pool]```

Once installed the global variables for DBNAME, USER, PASSWORD, HOST, PORT will need to be defined.
These variables are located at the top of the script and have their values set to None.
Replace None with the appropriate values for your setup.

Once all of this is done the python script should be ready to run

<hr/>
<h2>Running:</h2>
To run this application simply change the global variables at the top of the script with values appropriate for you system

After that you can simply run the python script

You'll be greeted with a menu providing the following 4 option:
1 - Print all students
2 - Add a student
3 - Update a student's email address
4 - Delete a student

<hr/>
Youtube Link: 