import sqlite3
import logging

DATABASE_NAME = 'task_management.db'

class Task:
    @staticmethod
    def create(title, status, project_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO tasks (title, status, project_id) VALUES (?, ?, ?)',
                               (title, status, project_id))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Exception in create: {e}")

    @staticmethod
    def delete(task_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
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
                cursor.execute('SELECT * FROM tasks')
                tasks = cursor.fetchall()
                return tasks
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return []
        except Exception as e:
            logging.error(f"Exception in get_all: {e}")
            return []

    @staticmethod
    def find_by_id(task_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
                task = cursor.fetchone()
                return task
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return None
        except Exception as e:
            logging.error(f"Exception in find_by_id: {e}")
            return None
