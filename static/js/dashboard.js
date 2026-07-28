let uptimeChart = null;

let simulationChart = null;


/* ================================================= */
/* UPTIME CHART */
/* ================================================= */

function loadUptimeChart() {

    const canvas =
        document.getElementById(
            "uptimeChart"
        );

    if (!canvas) {
        return;
    }


    fetch(
        "/api/dashboard"
    )

    .then(
        response => response.json()
    )

    .then(
        data => {

            const working =
                data.working;

            const notWorking =
                data.not_working;


            if (uptimeChart) {

                uptimeChart.destroy();

            }


            uptimeChart =
                new Chart(
                    canvas,
                    {
                        type: "doughnut",

                        data: {

                            labels: [
                                "Working",
                                "Not Working"
                            ],

                            datasets: [
                                {

                                    data: [
                                        working,
                                        notWorking
                                    ]

                                }
                            ]

                        },

                        options: {

                            responsive: true,

                            plugins: {

                                title: {

                                    display: true,

                                    text:
                                        "Water Point Operational Status"

                                }

                            }

                        }

                    }
                );

        }
    )

    .catch(
        error => {

            console.error(
                "Dashboard error:",
                error
            );

        }
    );

}


/* ================================================= */
/* STEP DISTURBANCE SIMULATION */
/* ================================================= */

function runSimulation() {

    const target =
        document.getElementById(
            "target"
        ).value;


    const disturbanceTime =
        document.getElementById(
            "disturbanceTime"
        ).value;


    const disturbanceAmount =
        document.getElementById(
            "disturbanceAmount"
        ).value;


    const recoveryRate =
        document.getElementById(
            "recoveryRate"
        ).value;


    const url =
        `/api/simulation?` +
        `target=${target}` +
        `&disturbance_time=${disturbanceTime}` +
        `&disturbance_amount=${disturbanceAmount}` +
        `&recovery_rate=${recoveryRate}`;


    fetch(url)

    .then(
        response => response.json()
    )

    .then(
        data => {

            displaySimulationResult(
                data
            );

            drawSimulationChart(
                data
            );

        }
    )

    .catch(
        error => {

            console.error(
                "Simulation error:",
                error
            );

        }
    );

}


/* ================================================= */
/* DISPLAY SIMULATION RESULT */
/* ================================================= */

function displaySimulationResult(
    data
) {

    const result =
        document.getElementById(
            "simulationResult"
        );


    if (!result) {

        return;

    }


    if (data.recovered) {

        result.innerHTML = `

            <h2>
                Controller Result
            </h2>

            <div class="result-success">

                <strong>
                    Recovery Successful
                </strong>

                <p>

                    The controller successfully
                    brought the system output
                    close to the target.

                </p>

                <p>

                    Final Output:
                    ${data.final_value.toFixed(2)}%

                </p>

            </div>

        `;

    }

    else {

        result.innerHTML = `

            <h2>
                Controller Result
            </h2>

            <div class="result-warning">

                <strong>
                    Recovery Incomplete
                </strong>

                <p>

                    The controller was unable
                    to bring the output sufficiently
                    close to the target.

                </p>

                <p>

                    Final Output:
                    ${data.final_value.toFixed(2)}%

                </p>

            </div>

        `;

    }

}


/* ================================================= */
/* SIMULATION GRAPH */
/* ================================================= */

function drawSimulationChart(
    data
) {

    const canvas =
        document.getElementById(
            "simulationChart"
        );


    if (!canvas) {

        return;

    }


    if (simulationChart) {

        simulationChart.destroy();

    }


    simulationChart =
        new Chart(
            canvas,
            {

                type: "line",

                data: {

                    labels:
                        data.time,

                    datasets: [

                        {

                            label:
                                "Target",

                            data:
                                data.target,

                            borderWidth: 2,

                            fill: false

                        },

                        {

                            label:
                                "Actual System Output",

                            data:
                                data.actual,

                            borderWidth: 3,

                            fill: false

                        }

                    ]

                },

                options: {

                    responsive: true,

                    scales: {

                        y: {

                            min: 0,

                            max: 100,

                            title: {

                                display: true,

                                text:
                                    "Water Availability (%)"

                            }

                        },

                        x: {

                            title: {

                                display: true,

                                text:
                                    "Simulation Time"

                            }

                        }

                    },

                    plugins: {

                        title: {

                            display: true,

                            text:
                                "Controller Response to Step Disturbance"

                        }

                    }

                }

            }
        );

}


/* ================================================= */
/* PAGE LOAD */
/* ================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function() {

        loadUptimeChart();

    }
);