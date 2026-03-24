import pyodbc

def connection():
    s = "192.95.39.99,1501"
    d = "PROSPERIDAD"
    u = "sa"
    p = "Infotec123"

    cstr = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+s+";DATABASE="+d+";UID="+u+";PWD="+p+";"
    conn = pyodbc.connect(cstr)

    return conn