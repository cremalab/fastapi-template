# Crema Fast-API Backend Template

### 🧰 Tools Used
1. **Alembic** (Database migration tool for usage with SQLAlchemy/Python): https://alembic.sqlalchemy.org/en/latest/ 
2. **Pydantic** (Data validation library for Python): https://docs.pydantic.dev/latest/ 
3. **SQLAlchemy** (Object Relational Mapper/ORM and Python SQL toolkit): https://www.sqlalchemy.org/ 
4. **Adminer** (DB management tool that provides editor/ GUI for db): https://www.adminer.org/ 
5. **Redis** (Data platform for caching and message broker): https://redis.io/docs/latest/ 
6. **Celery** (Asynchronous task or job queue): https://docs.celeryq.dev/en/stable/getting-started/introduction.html 
7. **Pytest** (Python testing framework): https://docs.pytest.org/en/stable/ 


### 🔌 Integrations
Integrations(any external service ie AWS, Auth0, etc) to be documented here

## 🚧 Template Instructions (**Remove once configured and serving as project repo**) 
1. Rename all instances of `database_name` and `app_name` to desired name
2. Before running, delete all `alembic/versions/X...` files (otherwise you will have to fix the alembic heads)-- these are just here for example
3. Delete any example.py files as needed. These are here to serve as a template for how files/code should be standardized

## 🏗 Setup
1. Ensure you have Docker Desktop installed: https://www.docker.com/products/docker-desktop/
2. You should have Python installed, current image is 3.12 (ideal to have same image as repo). https://mac.install.guide/python/brew 
    - TODO note: To ensure seamless set up, we can later introduce `pyenv` to manage virtual environments that match the repo
3. Your .env file should be located at `./config/.env` and have the following fields: (update these both in the ReadME and in the sample.env file as the project progresses)

```
ENVIRONMENT=   #Set to "DEV" or something other than "PRODUCTION" to enable reloading

#Update these as appropriate for the project
VARIABLE_NAME = "example

etc
```

## 👟 Run

The easiest way to run app for development purposes is to run services in Docker while using VSCode in a virtual env. 
To do so, open up a terminal within your directory, and a shell for each of the following: 

### 1. 🐋 Docker

Ensure Docker desktop is open and run the following command: `make`

This will start each of the containers in Docker compose, and once healthy/running, you may open the Swagger docs at http://localhost:3000/docs 

(See below for all commands included in MakeFile related to Adminer, requirements, etc)

*App logs are included by default in the app container, but please see additional logging commands below*

### 2. 🖥️ venv

After Docker containers are running, you can create a virtual environment, install the requirements, and open VSCode as follows:
1. Open a new terminal shell
2. run `python3 -m venv env_name` *Replace `env_name` with whatever you want to call it* 
3. run `. env_name/bin/activate`  *Replace `env_name` with name from step 2* 
3. Naviate to project `cd /whatever/your/repo/path/is`
4. Run `pip3 install -r requirements.txt`
5. Run `code . ` *This will open VSCode from within the virtual environment, ensuring packages are recognized* 

**Note:**
Once this is done for the first time, you can start with step 3 to activate the already created venv, and you only need to install requirements when there has been a change or addition
Depending on your setup, you may also be able to navigate directly to your repo, and run step 5, which may trigger your .venv automatically 

## 📦 Package Changes

Any new packages should be added to the `requirements.in` file, and then run the command `make requirements` to generate a new requirements.txt file with appropriate versioning

When changes occur in the `requirements.txt` file, you will need to run `docker compose stop app worker worker-beat && make` for Docker, and re-run step 4 above for your virtual env

## 🗒️ Commands

- `make requirements`: runs pip-compile to generate a new requirements.txt file based on packages listed in requirements.in
- `make linting`: runs Black for linting
- `make pytest`: runs unit tests
- `make open-adminer`: opens Adminer GUI for DB management
- `make logs-all`: runs logs for all docker containers
- `make logs-redis`: runs logs for redis container
- `make logs-worker`: runs logs for both worker containers
- `make stop`: stop containers
- `make remove`: remove Docker containers and volumes

## 📊 Database & Migration

Running the project via the `make` command also runs PostGreSQL via Docker. As noted above, `make open-adminer` will open a GUI to inspect and manage the database
The initial SQL script is found within `support/docker/pg/init.sql` and this will need to be modified from the template for the actual `database_name` (remove this note when template is utilized)

## 🛸 Migration
By default, the folder `alembic/versions` should be included here. If it is not, be sure to run `mkdir alembic/versions` so that migrations can be created
**To create new migration:** Run `make migration name=name_of_your_migration` *This will generate a new file inside `alembic/versions` which must be edited before proceeding*
**To apply new migration:** Run `make migrate` *This will apply the migration*

Please note that if you create a migration locally while another dev also has one locally, the second person to merge will need to create a migration that resolves the "multiple heads" conflict. 

To resolve head conflicts:
1. Identify the conflict:
    - After Pulling latest changes from the main branch, you can run the following command to check for multiple heads: `alembic heads`
2. Merge Heads
    - If you see multiple heads, you need to merge them by creating a new migration that combines them by running `alembic merge <head1> <head2>` *replace with actual head IDs*
3. Edit Merge Migration
    - This will generate a new merge migration file in the `alembic/versions` directory. Open this file and ensure it correctly represents the desired state
4. Apply
    - Apply merge migration by running `make migrate`

## 🏛 Structure

```

┌─■ README.md # You are here
├─■ Makefile  # Commands 
├─■ requirements.in # Add new packages here
├─■ requirements.txt # Output from requirements.in
├─■ Dockerfile 
├─■ docker-compose.yaml
│
├─■ run_server       # create .venv, install requirements and run server.py
├─■ server.py        # main file
│
├─■ run_worker
├─■ run_beat         # celery beat / cronjob
├─■ worker.py        # worker entrypoint
├─┐tasks
│ ├─■ worker.py      # celery instance
│ └─■ tasks.py       # registered tasks
│
│
├─■ run_migration
├─■ alembic.init
├─┐alembic           # responsible for db migrations
│ ├─■ env.py
│ ├─■ script.py.make
│ └─┐versions
│   └─■ *.py         # migrations
│
├─┐source
│ ├─┐models # refers to the SQLAlchemy model, representing the database table and handles the ORM tasks
│ │ └─■ example.py
│ |
│ ├─┐schemas # refers to Pydantic models, handling the validation of incoming and outgoing data
│ │ └─■ example.py
│ |
│ └─┐integrations # transport layer which should not contain any business logic 
│ | ├─■ db/
|   | └─■ example.py # each db integration should only make use of the .save (add/update) and .filter (retrieving) functions to maintain simplicity
│ | └─■ redis/
│ |
│ ├─┐services # responsible for business logic and interacting with integrations 
│ │ └─■ example.py
│ |
│ └─┐routes # presentation layer which provides interface to service layer. This should not contain any business logic
│   └─■ example.py
│
├─┐config
│ ├─■ settings.py
│ └─■ utils.py
│
├─┐tests
│ ├─■ example.py #add tests here
│
│
└─┐docs
  ├─┐ architecture
  │ └─decisions
  │ | └─■ * Add ADRs here

```


