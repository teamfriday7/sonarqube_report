import sqlite3


connection=sqlite3.connect(
    "users.db"
)


def get_users():


    cursor=connection.cursor()


    query="""

    SELECT * FROM users

    """


    cursor.execute(query)


    data=cursor.fetchall()


    return data



def find_user(name):


    query = (
        "select * from users where name='"
        + name
        +"'"
    )


    cursor=connection.cursor()

    cursor.execute(query)


    return cursor.fetchone()