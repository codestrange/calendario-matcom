backend_host = 0.0.0.0
backend_port = 5000

backend_run:
	@export FLASK_APP=run.py &&\
	export FLASK_ENV=development &&\
	export FLASK_DEBUG=1 &&\
	cd backend &&\
	flask run --host=${backend_host} --port=${backend_port}

backend_run_pro:
	@export FLASK_APP=run.py &&\
	export FLASK_ENV=production &&\
	export FLASK_DEBUG=0
	cd backend &&\
	flask run --host=${backend_host} --port=${backend_port}

backend_shell:
	@export FLASK_APP=run.py &&\
	cd backend &&\
	flask shell

backend_install:
	@pipenv install

backend_db_init:
	@export FLASK_APP=run.py &&\
	cd backend &&\
	flask db init

backend_db_migrate:
	@export FLASK_APP=run.py &&\
	cd backend &&\
	flask db migrate

backend_db_upgrade:
	@export FLASK_APP=run.py &&\
	cd backend &&\
	flask db upgrade

backend_db_delete:
	@sudo rm -r backend/migrations &&\
	sudo rm backend/app/data_dev.sqlite

backend_db_start: backend_db_init backend_db_migrate backend_db_upgrade ;
	@export FLASK_APP=run.py &&\
	cd backend &&\
	flask init

backend_db_restart: backend_db_delete backend_db_start ;

pipenv_run:
	@pipenv shell

frontend_run:
	@cd frontend &&\
	npm run serve

frontend_install:
	@cd frontend &&\
	sudo npm install
