# Build docker image allowing passing more args using ARGS variable.
build:
	docker build $(ARGS) -t flask-fortune .

start:
	uwsgi --ini uwsgi.ini

startbg:
	uwsgi --ini uwsgi.ini &

watch:startbg
	@ echo 'Watching...'
	trap "kill -3 $$(pidof uwsgi | tr ' ' '\n' | sort | head -1); sleep 2; exit" 0 1 2 5 15 ; \
	while true; do \
	  inotifywait -e modify -r . ; \
	  kill -1 $$(pidof uwsgi | tr ' ' '\n' | sort | head -1) ; \
	done
