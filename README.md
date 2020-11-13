# Sensors 360

_Sensors 360_ is intended to demonstrate how to implement a dashboard providing real time
update for streamed or high frequency data. The application uses a React front-end and a 
Python Flask backend. It also uses WebSocket to establish a full duplex communication channel
between the client and the server.

## Purpose

The immediate purpose of this project i monitoring the health of sensors so defective ones can
be replaced, but the ultimate goal will be running analytics on sensor data to accurately predict
their failure and perform preventative maintenance or replacement. 

The following are some questions that can be answered by the data:

* How many percent of sensors have not sent a healthcheck for more than 10 minutes
* What is the average time duration between consecutive heartbeats
* What is the average lifespan of a sensor

## Setup

* Install `Python > 3.6`
* Install `pip3`
* Install `postgres`
* Install `npm`
* Open an Bash shell and run `export FLASK_APP=sensors360.py`
* To setup the database:
    * Connect to the postgres server
    * Create a database called `sensors360`
    * Create a postgres user called `sensors360admin` with password `saquyu-8BDNKT8pK`
    * Run `python backend/gen_db_schema.py`
    * Run `python backend/gen_db_data.py`
* To start the API backend server receiving sensor heartbeats:
    * Run `flask run`
* To send heartbeats to the database run `bash backend/gen_heartbeats.sh`
* To start the websocket backend server run `python backend/app/websocket.py`
* To set start the front-end:
    * Navigate to front-end
    * run `npm install`
    * run `npm run`
    * A window will open in your default web browser and the console should display
    communication with the server via websockets
## Data Model

This project connects to a Postgres database and creates 3 tables:

1. `user`: Containing information of user who will lot into the client to monitor sensors health
    * `id`: monotonically increasing primary key 
    * `username`: username for authenticating via the client (indexed field) 
    * `password_hash`: self-explanatory 

2. `sensor`: sensor identification information
    * `id`: monotonically increasing primary key
    * `tags`: sensor identification tag (indexed field)
    
3. `heartbeats`: recors of heartbeats sent by sensors
    * `id`: monotonically increasing primary key id
    * `sensor_id`: (foreign key, indexed field)
    * `timestamp`: time at which the sensor sent the heartbeat in epoch format

## Project Structure

### Source Code

```bash
├── README.md - This file.
├── backend/
	└── requirements.py # Python libraries necessaries for all modules to work
	└── sensors360.py # Flask initialization file
	└── gen_db_data.py # Generate initial sensor data
	└── gen_db_schema.py # Persist schema to DB
	└── gen_heartbeats.py # Generates a heartbeat signal for a random sensor every 5 seconds
	└── confi.py # containing app configuration such as db credentials
	└── gen_heartbeats.py # Generates a heartbeat signal for a random sensor every 5 seconds
	└── migrations/ # DB schema update information automatically generated whenever the schema changes
	└── app/ # Flask folder with crucial modules
	└── credilitycs.py # Python script containing the tasks and depencdencies of the DAG
	└── credilitycs.py # Python script containing the tasks and depencdencies of the DAG
        	└── credilitycs.py # Python script containing the tasks and depencdencies of the DAG
           	└── credilitycs.py # Python script containing the tasks and depencdencies of the DAG

├── frontend/ React application setup using `create-react-app`
	├── src
		└──  Dashboard.js # File containing main UI code establising websocket connection with backend
    └── index.html # simpler websocket code for debugging purposes
```

## TODO

* Using a protocol more secured than `HTTP` for the communication between sesnorsSecuring the API used for communication with sensors:
    * Using a protocol more secured that `HTTP`
* Adding user authentication to the client.
* Redesigning the architecture to for high availability and scalability:
    * Containerizing the frontend and backend (docker and kubernetes)
    * Running the database from a different server
    * Provisioning replicas for the database
    * Investigating performance gain that could be achieved by switchign to NoSQL database
    * Placing a queue between the sensors and the servers
    * Investigating in technology designed to harvest sensor data such AWS Greengrass
    * Storing database backups and log files to long term low cost durable cloud storage

## Example Queries

** How many percent of sensors have not sent a healthcheck for more than 10 minutes**

```
    SELECT DISTINCT ON (s.name), h.timestamp
    FROM
    Sensor s
    INNER JOIN
    Heartbeat h
    ON s.id = h.sensor_id
    WHERE h.timestamp < (now()::time - INTERVAL '10 min')
    ORDER BY h.timestamp DESC
```