import sqlite3
import logging

DATABASE_NAME = 'task_management.db'

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    @staticmethod
    def create(username, email):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
                conn.commit()
        except sqlite3.IntegrityError as e:
            logging.error(f"Integrity error: {e}")
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"Exception in create: {e}")

    @staticmethod
    def delete(user_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
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
                cursor.execute('SELECT * FROM users')
                users = cursor.fetchall()
                return users
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return []
        except Exception as e:
            logging.error(f"Exception in get_all: {e}")
            return []

    @staticmethod
    def find_by_id(user_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
                user = cursor.fetchone()
                return user
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            return None
        except Exception as e:
            logging.error(f"Exception in find_by_id: {e}")
            return None
