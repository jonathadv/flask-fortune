# export PATH removing any non-system wide Python installation
export PATH=${PATH/:\/opt\/anaconda3\/bin/}

# Export any additional lib if needed
# export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu

uwsgi --ini uwsgi.ini

