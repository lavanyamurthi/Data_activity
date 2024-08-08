import pandas as pd
import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Create a table in the SQLite database."""
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        dob DATE,
        company_name TEXT,
        last_active DATE,
        score INTEGER,
        us_state TEXT,
        member_since INTEGER,
        state TEXT,
        source TEXT
    )
    '''
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()

def ingest_data(conn, df):
    """Write the DataFrame to the SQLite database."""
    df.to_sql('records', conn, if_exists='append', index=False)

def main():
    
    df = pd.read_csv('master_file.csv')
    
    # Database file
    database = 'data.db'
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create table
    create_table(conn)
    
    # Ingest data into the database
    ingest_data(conn, df)
    
    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
