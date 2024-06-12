import sqlite3
import logging

DATABASE_NAME = 'task_management.db'

class Project:
    @staticmethod
    def create(name, description, deadline, user_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO projects (name, description, deadline, user_id) VALUES (?, ?, ?, ?)',
                    (name, description, deadline, user_id)
                )
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Exception in create: {e}")

    @staticmethod
    def delete(project_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Exception in delete: {e}")

    @staticmethod
    def get_all():
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM projects')
                projects = cursor.fetchall()
                return projects
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return []
        except Exception as e:
            logging.error(f"Exception in get_all: {e}")
            return []

    @staticmethod
    def find_by_id(project_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
                project = cursor.fetchone()
                return project
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return None
        except Exception as e:
            logging.error(f"Exception in find_by_id: {e}")
            return None
