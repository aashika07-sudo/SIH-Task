from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from database import (
    init_db,
    add_water_point,
    get_all_water_points,
    get_water_point_statistics
)

from simulator import (
    run_step_disturbance_simulation
)


# ==========================================
# FLASK APPLICATION
# ==========================================

app = Flask(__name__)


# ==========================================
# INITIALIZE DATABASE
# ==========================================

init_db()


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/")
def index():

    (
        total,
        working,
        not_working,
        uptime
    ) = get_water_point_statistics()

    return render_template(
        "index.html",
        total=total,
        working=working,
        not_working=not_working,
        uptime=uptime
    )


# ==========================================
# REGISTER WATER POINT
# ==========================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        location = request.form.get(
            "location",
            ""
        ).strip()

        status = request.form.get(
            "status",
            ""
        ).strip()

        uptime_value = request.form.get(
            "uptime",
            "0"
        ).strip()

        last_checked = request.form.get(
            "last_checked",
            ""
        ).strip()


        # ------------------------------
        # VALIDATE NAME
        # ------------------------------

        if not name:

            return render_template(
                "register.html",
                error="Water Point Name is required."
            )


        # ------------------------------
        # VALIDATE LOCATION
        # ------------------------------

        if not location:

            return render_template(
                "register.html",
                error="Location is required."
            )


        # ------------------------------
        # VALIDATE STATUS
        # ------------------------------

        if not status:

            return render_template(
                "register.html",
                error="Please select a status."
            )


        # ------------------------------
        # CONVERT UPTIME
        # ------------------------------

        try:

            uptime = float(
                uptime_value
            )

        except ValueError:

            uptime = 0


        # ------------------------------
        # LIMIT UPTIME
        # ------------------------------

        uptime = max(
            0,
            min(
                100,
                uptime
            )
        )


        # ------------------------------
        # SAVE TO DATABASE
        # ------------------------------

        add_water_point(
            name,
            location,
            status,
            uptime,
            last_checked
        )


        # ------------------------------
        # REDIRECT TO LISTING
        # ------------------------------

        return redirect(
            url_for("listing")
        )


    return render_template(
        "register.html"
    )


# ==========================================
# WATER POINT LISTING
# ==========================================

@app.route("/listing")
def listing():

    water_points = get_all_water_points()

    return render_template(
        "listing.html",
        water_points=water_points,
        readings=water_points
    )


# ==========================================
# SIMULATION
# ==========================================

@app.route(
    "/simulation",
    methods=["GET", "POST"]
)
def simulation():

    simulation_result = None

    if request.method == "POST":

        # ------------------------------
        # GET FORM VALUES
        # ------------------------------

        target = request.form.get(
            "target",
            100
        )

        initial_value = request.form.get(
            "initial_value",
            100
        )

        disturbance_time = request.form.get(
            "disturbance_time",
            10
        )

        disturbance_amount = request.form.get(
            "disturbance_amount",
            40
        )

        recovery_rate = request.form.get(
            "recovery_rate",
            0.20
        )

        total_time = request.form.get(
            "total_time",
            40
        )


        # ------------------------------
        # CONVERT VALUES
        # ------------------------------

        try:

            target = float(target)

            initial_value = float(
                initial_value
            )

            disturbance_time = int(
                disturbance_time
            )

            disturbance_amount = float(
                disturbance_amount
            )

            recovery_rate = float(
                recovery_rate
            )

            total_time = int(
                total_time
            )

        except ValueError:

            return render_template(
                "simulation.html",
                error="Please enter valid simulation values."
            )


        # ------------------------------
        # RUN SIMULATION
        # ------------------------------

        simulation_result = (
            run_step_disturbance_simulation(

                target=target,

                initial_value=initial_value,

                disturbance_time=
                    disturbance_time,

                disturbance_amount=
                    disturbance_amount,

                recovery_rate=
                    recovery_rate,

                total_time=
                    total_time
            )
        )


    # ------------------------------
    # SHOW SIMULATION PAGE
    # ------------------------------

    return render_template(
        "simulation.html",
        simulation=simulation_result
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )