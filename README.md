# envsens

- sudo adduser netdata dialout
- cp envsens.chart.py /usr/libexec/netdata/python.d
- echo 'envsens: yes' >> /usr/lib/netdata/conf.d/python.d.conf
