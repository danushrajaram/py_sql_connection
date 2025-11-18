from db_connect import get_db_connection

def fetch_large(query, chunk_size=1000):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute(query)

    while True:
        rows = cursor.fetchmany(chunk_size)
        if not rows:
            break
        for row in rows:
            yield row

    cursor.close()
    db.close()


if __name__ == "__main__":
    total = 0
    print("Streaming...")

    for row in fetch_large("SELECT * FROM employees", 5000):
        total += 1

        if total % 100000 == 0:
            print("Processed →", total)

    print("DONE. TOTAL:", total)
