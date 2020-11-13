import psycopg2

def db_conn():
    """
    Description:
        function to get a connection to a database
    
    Parameters:
    
    Returns:
        a connection object
    """
    conn = psycopg2.connect("host='localhost' dbname='sensors360' user='sensors360admin' password='saquyu-8BDNKT8pK'")