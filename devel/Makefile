all:

RELEASE :=	$(shell date +%Y%m%d%H%M)

dist:
	rm -rf suricata suricata-*.tar.gz
	git clone https://github.com/OISF/suricata
	cd suricata && ./scripts/bundle.sh
	cd suricata && ./autogen.sh
	cd suricata && ./configure
	cd suricata && make dist
	mv suricata/suricata-*.tar.gz .
	$(MAKE) update-release

update-release:
	sed -i "/^Release:/c\Release: 0.$(RELEASE)%{?dist}" suricata.spec

include ../common.mk
