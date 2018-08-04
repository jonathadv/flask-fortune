# Build docker image allowing passing more args using ARGS variable.
build:
	docker build $(ARGS) -t flask-fortune .

start:
	pipenv run uwsgi --ini uwsgi.ini

watch:
	@if which inotifywait > /dev/null; then \
	  pipenv run uwsgi --ini uwsgi.ini & \
	  trap "kill -3 $$(pidof uwsgi | tr ' ' '\n' | sort | head -1); sleep 2; exit" 0 1 2 5 15 ; \
      while true; do \
	    inotifywait -e modify -r . ; \
	    kill -1 $$(pidof uwsgi | tr ' ' '\n' | sort | head -1) ; \
      done; \
	else \
     echo 'No binary `inotifywait` found. Please install it into the system to run watch mode. Exiting...'; \
	fi

