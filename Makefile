backend_run:
	export FLASK_APP=run.py &&\
	export FLASK_ENV=development &&\
	export FLASK_DEBUG=1 &&\
	cd backend &&\
	flask run

backend_run_pro:
	export FLASK_APP=run.py &&\
	export FLASK_ENV=production &&\
	export FLASK_DEBUG=0
	cd backend &&\
	flask run

backend_shell:
	export FLASK_APP=run.py &&\
	cd backend &&\
	flask shell

backend_install:
	pipenv install

pipenv_run:
	pipenv shell