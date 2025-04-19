import sqlite3


class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count


class WinSum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def value(self):
        return self.count

    def inverse(self, value):
        self.count -= value

    def finalize(self):
        return self.count


def sqlite_memory():
    ret = {}
    try:
        conn = sqlite3.connect(":memory:")
        conn.create_aggregate("mysum", 1, MySum)

        cur = conn.execute("CREATE TABLE test(i)")
        cur.execute("INSERT INTO test(i) VALUES(1)")
        cur.execute("INSERT INTO test(i) VALUES(2)")
        cur.execute("SELECT mysum(i) FROM test")

    except sqlite3.Error as e:
        ret["e_msg"] = f"Error: {e}"
        return ret

    else:
        ret["db_ver"] = sqlite3.sqlite_version
        ret["fetch"] = cur.fetchone()[0]
        return ret

    finally:
        if conn:
            conn.close()


def sqlite_file():
    ret = {}
    try:
        conn = sqlite3.connect("testDB.db")
        conn.create_window_function("sumint", 1, WinSum)

        cur = conn.execute("DROP TABLE IF EXISTS test")
        cur.execute("CREATE TABLE test(x, y)")

        values = [
            ("a", 4),
            ("b", 5),
            ("c", 3),
            ("d", 8),
            ("e", 1),
        ]

        cur.executemany("INSERT INTO test VALUES(?, ?)", values)
        conn.commit()

        cur.execute(
            """
            SELECT *, sumint(y) OVER (
                ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
            ) AS sum_y
            FROM test ORDER BY x
        """
        )
        ret["fetch_1"] = cur.fetchall()

        cur.execute(
            """
            SELECT *, sumint(y) OVER (
                ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
            ) AS sum_y
            FROM test ORDER BY x
        """
        )
        ret["fetch_2"] = cur.fetchall()

    except sqlite3.Error as e:
        ret["e_msg"] = f"Error: {e}"
        return ret

    else:
        ret["db_ver"] = sqlite3.sqlite_version
        return ret

    finally:
        if conn:
            conn.close()


# sqlite3 testDB.db
# .tables
# .schema tablename
# SELECT * FROM tablename;
# .help
# .q
