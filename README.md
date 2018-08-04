# Flask Fortune

A simple flask app using uWSGI to display random messages based on the [Fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)).

### Setup

Make sure you have the `python-dev` package installed in your system. It's required to install uWSGI.

```bash
$ git clone https://github.com/jonathadv/flask-fortune.git
$ cd flask-fortune/
# Create a new virtual env
$ pipenv --python python3.4 # You can use any version which you have python-dev installed.
# Start venv shell
$ pipenv  shell
# Install requirements
$ pipenv  install
```

#### Watching mode

```bash
$ make watch

```

#### Starting the server
```bash
$ make start 
[uWSGI] getting INI configuration from uwsgi.ini
*** Starting uWSGI 2.0.17.1 (64bit) on [Wed Jul 25 23:59:57 2018] ***
compiled with version: 4.9.2 on 26 July 2018 02:59:33
os: Linux-3.16.0-4-amd64 #1 SMP Debian 3.16.51-3 (2017-12-13)
nodename: jonatha-notebook
machine: x86_64
clock source: unix
pcre jit disabled
detected number of CPU cores: 4
current working directory: /home/jonatha/flask-fortune
detected binary path: /home/jonatha/.local/share/virtualenvs/flask-fortune-rGJQeLwz/bin/uwsgi
your processes number limit is 15414
your memory page size is 4096 bytes
detected max file descriptor number: 65536
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI http bound on 0.0.0.0:8080 fd 4
uwsgi socket 0 bound to TCP address 127.0.0.1:59600 (port auto-assigned) fd 3
Python version: 3.4.2 (default, Oct  8 2014, 10:47:48)  [GCC 4.9.1]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x87d4d0
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 218760 bytes (213 KB) for 2 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x87d4d0 pid: 22096 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 22096)
spawned uWSGI worker 1 (pid: 22099, cores: 1)
spawned uWSGI worker 2 (pid: 22100, cores: 1)
spawned uWSGI http 1 (pid: 22101)

```
