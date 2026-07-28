import sqlite3

DB_NAME = "water_points.db"


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================
# CREATE TABLE
# ==========================================

def init_db():

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_points (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL,
            uptime REAL DEFAULT 0,
            last_checked TEXT
        )
    """)

    conn.commit()

    conn.close()


# ==========================================
# ADD WATER POINT
# ==========================================

def add_water_point(
    name,
    location,
    status,
    uptime,
    last_checked
):

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO water_points
        (
            name,
            location,
            status,
            uptime,
            last_checked
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        location,
        status,
        uptime,
        last_checked
    ))

    conn.commit()

    conn.close()


# ==========================================
# GET ALL WATER POINTS
# ==========================================

def get_all_water_points():

    conn = get_db()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM water_points
        ORDER BY id DESC
    """)

    water_points = cursor.fetchall()

    conn.close()

    return water_points


# ==========================================
# GET WATER POINT COUNTS
# ==========================================

def get_water_point_statistics():

    conn = get_db()

    cursor = conn.cursor()


    # Total

    cursor.execute("""
        SELECT COUNT(*)
        FROM water_points
    """)

    total = cursor.fetchone()[0]


    # Working

    cursor.execute("""
        SELECT COUNT(*)
        FROM water_points
        WHERE status = 'Working'
    """)

    working = cursor.fetchone()[0]


    # Not Working

    cursor.execute("""
        SELECT COUNT(*)
        FROM water_points
        WHERE status = 'Not Working'
    """)

    not_working = cursor.fetchone()[0]


    # Uptime

    cursor.execute("""
        SELECT AVG(uptime)
        FROM water_points
    """)

    uptime_result = cursor.fetchone()[0]


    if uptime_result is None:
        uptime = 0
    else:
        uptime = round(uptime_result, 2)


    conn.close()


    return (
        total,
        working,
        not_working,
        uptime
    )