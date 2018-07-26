start:
	uwsgi --ini uwsgi.ini

startbg:
	uwsgi --ini uwsgi.ini &

watch:startbg
	@ echo 'Watching...'
	bash -c "trap \"kill -s SIGQUIT $$(pidof uwsgi | tr ' ' '\n' | sort | head -1) && sleep 2 && exit\" 0 1 2 5 15; while true; do inotifywait -e modify -r .; kill -s SIGHUP $$(pidof uwsgi | tr ' ' '\n' | sort | head -1); done;"