# Village Water Point Uptime Monitoring System

## Project Overview

The Village Water Point Uptime Monitoring System is a web-based application developed to monitor and manage the operational status and uptime of water points in rural villages.

Water points such as borewells, hand pumps, community water tanks, and public water taps are important sources of water for rural communities. When these water points become unavailable due to technical problems or other disturbances, it may be difficult to identify the issue and monitor the recovery process.

This project provides a centralized platform to register water points, store their information, monitor their operational status, calculate uptime, and analyze system recovery through simulation.

The system also includes a step-disturbance simulation that demonstrates how a water availability system responds to a sudden disturbance and gradually recovers toward a desired target value.

---

## Objectives

The main objectives of this project are:

1. To provide a centralized system for monitoring village water points.
2. To register and maintain information about individual water points.
3. To monitor the working and non-working status of water points.
4. To calculate the overall uptime percentage.
5. To provide a user-friendly dashboard for monitoring water infrastructure.
6. To simulate sudden disturbances in water availability.
7. To analyze controller response and system recovery.
8. To visualize simulation results using graphical representation.

---

## Key Features

### Dashboard

The dashboard provides an overview of the village water infrastructure.

It displays important information such as:

- Total number of water points
- Number of working water points
- Number of non-working water points
- Overall uptime percentage

The dashboard allows users to quickly understand the current condition of the water point infrastructure.

### Water Point Registration

Users can register new water points by providing relevant information, such as:

- Water Point Name
- Location
- Operational Status
- Uptime Percentage
- Last Checked Date

The registered information is stored in the SQLite database.

### Water Point Readings

The system provides a centralized page for viewing registered water points and their information.

Users can view:

- Water Point ID
- Water Point Name
- Location
- Status
- Uptime
- Last Checked Information

### Uptime Monitoring

The application calculates the overall uptime percentage based on the operational status of registered water points.

This helps users understand the reliability and availability of the village water infrastructure.

### Control System Simulation

The project includes a step-disturbance simulation to demonstrate the behavior of a water availability system.

The simulation includes:

- Normal system operation
- Sudden disturbance
- Reduction in water availability
- Controller response
- Recovery toward the target value

Users can configure parameters such as:

- Target Water Availability
- Initial Water Availability
- Disturbance Time
- Disturbance Amount
- Recovery Rate
- Total Simulation Time

### Simulation Graph

The simulation results are displayed using a graph.

The graph represents:

- Target Water Availability
- Actual Water Availability
- Disturbance
- Controller Action

This allows users to understand how the system responds to a sudden disturbance and how it gradually recovers toward the desired target value.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend web framework |
| HTML5 | Webpage structure |
| CSS3 | User interface design and styling |
| JavaScript | Frontend functionality |
| Chart.js | Simulation graph visualization |
| SQLite | Database management |
| Jinja2 | Dynamic HTML templating |
| Git | Version control |
| GitHub | Source code hosting |

---

## Project Structure

```text
Village-Water-Point-Monitoring/
│
├── app.py
├── database.py
├── simulator.py
├── state_machine.py
├── presentation.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── listing.html
│   └── simulation.html
│
└── static/
    ├── css/
    │   └── pages.css
    │
    └── js/
        └── script.js
