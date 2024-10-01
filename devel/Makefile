all:

dist:
	rm -rf suricata suricata-*.tar.gz
	git clone https://github.com/OISF/suricata
	cd suricata && ./scripts/bundle.sh
	cd suricata && ./autogen.sh
	cd suricata && ./configure
	cd suricata && make dist
	mv suricata/suricata-*.tar.gz .

include ../common.mk
