"""
Database saving simulation results for future analysis.
"""
from contextlib import closing
import sqlite3

def export(probabilities, search_distances, base_lengths):
    """
    Save the probabilities, search distances, and base lengths to a
    three-column sqlite3 database.
    """
    with closing(sqlite3.connect("results.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("DROP TABLE results")
            cursor.execute("CREATE TABLE results(probability, distance, base)")
            cursor.executemany("INSERT INTO results VALUES(?, ?, ?)",
                               zip(probabilities, search_distances, base_lengths))
            connection.commit()
            

