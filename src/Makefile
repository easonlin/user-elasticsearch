install:
	cp -f etc/rsyslog.d/file.conf /etc/rsyslog.d/file.conf
	/etc/init.d/rsyslog restart
file:
	python logging_file.py
sys:
	python logging_sys.py
nginx:
	cat td-agent.conf.nginx
# Parse log
apache:
	python lex_apache.py < apache.log
