import sqlite3
import click
from lib.models.user import User
from lib.models.project import Project
from lib.models.task import Task

@click.group()
def cli():
    pass

@cli.group()
def user():
    pass

@user.command()
@click.argument('username')
@click.argument('email')
def create(username, email):
   
    """Create a new user"""
    try:
        User.create(username, email)
        click.echo(f"User {username} created successfully.")
    except sqlite3.IntegrityError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@user.command()
@click.argument('user_id')
def delete(user_id):
    """Delete a user by ID"""
    try:
        User.delete(user_id)
        click.echo(f"User with ID {user_id} deleted.")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@user.command()
def list():
    """List all users"""
    try:
        users = User.get_all()
        for user in users:
            click.echo(user)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@user.command()
@click.argument('user_id')
def find(user_id):
    """Find a user by ID"""
    try:
        user = User.find_by_id(user_id)
        if user:
            click.echo(user)
        else:
            click.echo(f"No user found with ID {user_id}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@cli.group()
def project():
    pass

@project.command()
@click.argument('name')
@click.argument('description')
@click.argument('deadline')
@click.argument('user_id')
def create(name, description, deadline, user_id):
    """Create a new project"""
    try:
        Project.create(name, description, deadline, user_id)
        click.echo(f"Project {name} created successfully.")
    except sqlite3.IntegrityError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@project.command()
@click.argument('project_id')
def delete(project_id):
    """Delete a project by ID"""
    try:
        Project.delete(project_id)
        click.echo(f"Project with ID {project_id} deleted.")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@project.command()
def list():
    """List all projects"""
    try:
        projects = Project.get_all()
        for project in projects:
            click.echo(project)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@project.command()
@click.argument('project_id')
def find(project_id):
    """Find a project by ID"""
    try:
        project = Project.find_by_id(project_id)
        if project:
            click.echo(project)
        else:
            click.echo(f"No project found with ID {project_id}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@cli.group()
def task():
    pass

@task.command()
@click.argument('title')
@click.argument('status')
@click.argument('project_id')
def create(title, status, project_id):
    """Create a new task"""
    try:
        Task.create(title, status, project_id)
        click.echo(f"Task {title} created successfully.")
    except sqlite3.IntegrityError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@task.command()
@click.argument('task_id')
def delete(task_id):
    """Delete a task by ID"""
    try:
        Task.delete(task_id)
        click.echo(f"Task with ID {task_id} deleted.")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@task.command()
def list():
    """List all tasks"""
    try:
        tasks = Task.get_all()
        for task in tasks:
            click.echo(task)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

@task.command()
@click.argument('task_id')
def find(task_id):
    """Find a task by ID"""
    try:
        task = Task.find_by_id(task_id)
        if task:
            click.echo(task)
        else:
            click.echo(f"No task found with ID {task_id}")
    except Exception as e:
        click.echo(f"Unexpected error: {e}")

if __name__ == '__main__':
    cli()
