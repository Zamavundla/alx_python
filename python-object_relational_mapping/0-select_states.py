"""Write a script that lists all states from the database hbtn_0e_0_usa:
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Your code should not be executed when imported.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    try:
        """Connect to the MySQL server.
        """
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        """Create a cursor to interact with the database.
        """
        cursor = db.cursor()

        """Execute the SQL query to fetch states.
        """
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        """Fetch all rows.
        """
        rows = cursor.fetchall()

        """Print the results.
        """
        for row in rows:
            print(row)

        """Close the cursor and database connection.
        """
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
