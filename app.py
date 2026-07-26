from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime


app = Flask(__name__)

DB_NAME = "water_points.db"


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/")
def index():

    conn = get_db()

    # Total records
    total = conn.execute(
        "SELECT COUNT(*) FROM readings"
    ).fetchone()[0]

    # Working records
    working = conn.execute(
        """
        SELECT COUNT(*)
        FROM readings
        WHERE flow_ok = 'Working'
        """
    ).fetchone()[0]

    # Failed records
    failed = conn.execute(
        """
        SELECT COUNT(*)
        FROM readings
        WHERE flow_ok = 'Failed'
        """
    ).fetchone()[0]

    conn.close()

    return render_template(

        "index.html",

        total=total,

        working=working,

        failed=failed

    )


# ==========================================
# REGISTER NEW READING
# ==========================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        waterpoint_id = request.form.get(
            "waterpoint_id",
            ""
        ).strip()

        habitation = request.form.get(
            "habitation",
            ""
        ).strip()

        flow_ok = request.form.get(
            "flow_ok",
            ""
        ).strip()

        usage_count = request.form.get(
            "usage_count",
            ""
        ).strip()


        # Validate Water Point ID

        if not waterpoint_id:

            return "Water Point ID is required."


        # Validate Habitation

        if not habitation:

            return "Habitation is required."


        # Validate Status

        if flow_ok not in [

            "Working",

            "Failed"

        ]:

            return "Invalid status."


        # Validate Usage Count

        try:

            usage_count = int(
                usage_count
            )

        except ValueError:

            return "Usage count must be a number."


        if usage_count < 0:

            return "Usage count cannot be negative."


        # Current date and time

        recorded_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        # Connect to database

        conn = get_db()


        # Insert new record

        conn.execute(
            """
            INSERT INTO readings
            (
                waterpoint_id,
                habitation,
                flow_ok,
                usage_count,
                recorded_at
            )

            VALUES (?, ?, ?, ?, ?)
            """,

            (

                waterpoint_id,

                habitation,

                flow_ok,

                usage_count,

                recorded_at

            )
        )


        conn.commit()

        conn.close()


        # Go to listing page

        return redirect(
            url_for("listing")
        )


    # Display register page

    return render_template(
        "register.html"
    )


# ==========================================
# LISTING
# SEARCH
# FILTER
# ORDERING
# ==========================================

@app.route("/listing")
def listing():

    # Get search value

    search = request.args.get(
        "search",
        ""
    ).strip()


    # Get selected status

    status = request.args.get(
        "status",
        "All"
    )


    # Connect to database

    conn = get_db()


    # Base SQL query

    query = """
        SELECT
            reading_id,
            waterpoint_id,
            habitation,
            flow_ok,
            usage_count,
            recorded_at

        FROM readings

        WHERE 1 = 1
    """


    # Parameters for SQL query

    params = []


    # ==========================================
    # SEARCH FILTER
    # ==========================================

    if search:

        query += """
            AND (
                waterpoint_id LIKE ?
                OR habitation LIKE ?
            )
        """


        search_value = "%" + search + "%"


        params.append(
            search_value
        )


        params.append(
            search_value
        )


    # ==========================================
    # STATUS FILTER
    # ==========================================

    if status == "Working":

        query += """
            AND flow_ok = ?
        """

        params.append(
            "Working"
        )


    elif status == "Failed":

        query += """
            AND flow_ok = ?
        """

        params.append(
            "Failed"
        )


    # ==========================================
    # ORDERING
    # ==========================================

    query += """
        ORDER BY
            CASE
                WHEN flow_ok = 'Failed'
                THEN 0
                ELSE 1
            END,
            reading_id ASC
    """


    # Execute query

    readings = conn.execute(

        query,

        params

    ).fetchall()


    # Close database

    conn.close()


    # Send data to listing.html

    return render_template(

        "listing.html",

        readings=readings,

        search=search,

        status=status

    )


# ==========================================
# DELETE A PARTICULAR RECORD
# ==========================================

@app.route(
    "/delete/<int:reading_id>",
    methods=["POST"]
)
def delete_reading(reading_id):

    conn = get_db()


    # Delete only the selected record

    conn.execute(
        """
        DELETE FROM readings
        WHERE reading_id = ?
        """,
        (reading_id,)
    )


    conn.commit()

    conn.close()


    # Return to listing page

    return redirect(
        url_for("listing")
    )


# ==========================================
# RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )