import sqlite3


def get_user(username):

    connection = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE username='" + username + "'"

    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchone()

    connection.close()

    return result



def delete_user(username):

    connection = sqlite3.connect("users.db")

    query = "DELETE FROM users WHERE username='" + username + "'"

    connection.execute(query)

    connection.commit()

    connection.close()