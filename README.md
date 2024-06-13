Task Management System
by rocliff kadaji
The Task Management System is a command-line application that allows users to manage projects and tasks. 
It supports operations for creating, deleting, listing, and finding users, projects, and tasks within a SQLite database.
This README file describes the important files in the project and their functionalities.

CLI Script
menu.py
menu.py is the main entry point of the application.
It uses the click library to define a command-line interface (CLI) with various commands to manage users, projects, and tasks.

CLI Commands
user Group:

create(username, email): Creates a new user with the specified username and email.
delete(user_id): Deletes the user with the given ID.
list(): Lists all users.
find(user_id): Finds and displays the user with the specified ID.
project Group:

create(name, description, deadline, user_id): Creates a new project with the specified name, description, deadline, and user ID.
delete(project_id): Deletes the project with the given ID.
list(): Lists all projects.
find(project_id): Finds and displays the project with the specified ID.
task Group:

create(title, status, project_id): Creates a new task with the specified title, status, and project ID.
delete(task_id): Deletes the task with the given ID.
list(): Lists all tasks.
find(task_id): Finds and displays the task with the specified ID.
Setup Script
setup_database.py
setup_database.py is responsible for setting up the SQLite database and creating the necessary tables if they do not already exist. 
This script should be run before using the application to ensure the database schema is correctly initialized.

Functions
get_db_connection(): Establishes a connection to the SQLite database.
setup_database(): Creates the users, projects, and tasks tables in the database if they do not exist.
Models
lib/models/user.py
This file defines the User class, which encapsulates all operations related to the users table in the database.

Methods
create(username, email): Inserts a new user with the specified username and email into the database.
delete(user_id): Deletes the user with the specified ID from the database.
get_all(): Retrieves all users from the database.
find_by_id(user_id): Finds and returns the user with the specified ID.
lib/models/project.py
This file defines the Project class, which handles all operations related to the projects table in the database.

Methods
create(name, description, deadline, user_id): Inserts a new project with the specified details into the database.
delete(project_id): Deletes the project with the specified ID from the database.
get_all(): Retrieves all projects from the database.
find_by_id(project_id): Finds and returns the project with the specified ID.
lib/models/task.py
This file defines the Task class, which manages all operations related to the tasks table in the database.

Methods
create(title, status, project_id): Inserts a new task with the specified details into the database.
delete(task_id): Deletes the task with the specified ID from the database.
get_all(): Retrieves all tasks from the database.
find_by_id(task_id): Finds and returns the task with the specified ID.


Usage
To set up the database, run:
python3 setup_database.py
To use the CLI, run:
python3 menu.py [command]
For example, to create a new user:
python3 menu.py user create 'username' 'user@example.com'
For a full list of commands and options, use the --help flag with any command:
python3 menu.py --help


Conclusion
This Task Management System provides a basic framework for managing users, projects, and tasks through a CLI. 
The project can be extended further by adding more functionalities or improving existing ones. 
The code is structured to be modular and easy to maintain, with clear separation between the CLI commands and database operations.
