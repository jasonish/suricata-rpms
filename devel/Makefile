RELEASE :=	$(shell date +%Y%m%d%H%M)

all:
	$(MAKE) fetch-sources
	$(MAKE) dist
	$(MAKE) update-release
	$(MAKE) update-sources
	$(MAKE) srpm
	@echo "===> SRPM is now ready"

dist:
	cd suricata && ./autogen.sh
	cd suricata && ./configure
	cd suricata && make dist
	mv suricata/suricata-*.tar.gz .
	$(MAKE) update-release

fetch-sources:
	rm -rf suricata suricata-*.tar.gz
	git clone https://github.com/OISF/suricata
	cd suricata && ./scripts/bundle.sh

update-release:
	sed -i "/^Release:/c\Release: 0.$(RELEASE)%{?dist}" suricata.spec

include ../common.mk
