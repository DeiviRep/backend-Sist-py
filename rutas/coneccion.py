from pymysql import connect

def con():
    db = connect(
        host='localhost',
        user='root', 
        password = "",
        db='pweb_python',
        )
    cur = db.cursor()
    cur.execute("SELECT * from login")
    data = cur.fetchone()
    print(data)
    return (data)