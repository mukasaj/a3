<h1>COMP 3005 - Assignment 3</h1>
<hr/>
<h2>Setup:</h2>

Use the provided setup.sql found in the database_scripts folder to populate the database.
It will create the students table and add the default student values.

The database must be created manually first.

The following python packages will need to be installed:

```pip install psycopg```
```pip install "psycopg[binary,pool]"```

Once installed the global variables for DBNAME, USER, PASSWORD, HOST, PORT will need to be edited in main.py.
These variables are located at the top of the script and have their values set to None.
Replace None with the appropriate values for your setup.

Once all of this is done the python script should be ready to run

<hr/>
<h2>Running:</h2>
You can simply run the python script using the following command

```
python3 main.py
```

You'll be greeted with a menu providing the following 5 option:
```
1 - Print all students
2 - Add a student
3 - Update a student's email address
4 - Delete a student
q - Exit
```
You can select any of these options and then follow the prompts. 

<hr/>
Youtube Link: https://youtu.be/DRKRlMQ-YuE