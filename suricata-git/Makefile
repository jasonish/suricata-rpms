SURICATA_GIT_URL := https://github.com/inliniac/suricata/archive/master.tar.gz
HTP_URL := https://github.com/OISF/libhtp/releases/download/0.5.16/htp-0.5.16.tar.gz

all: epel7

epel7: suricata.spec
	fedpkg --dist epel7 --module-name suricata mockbuild

suricata.spec: check-sources suricata.spec.in suricata-master.tar.gz
	sed -e "s#@VERSION@#$$(date +%Y%m%d%H%M%S --date @`stat -c %Y suricata-master.tar.gz`)#g" suricata.spec.in > suricata.spec

check-sources:
	@if ! test -e suricata-master.tar.gz; then \
		echo "error: suricata-master.tar.gz does not exist."; \
		echo "       run make fetch-sources"; \
		exit 1; \
	fi

fetch-sources:
	curl -L -o suricata-master.tar.gz $(SURICATA_GIT_URL)
	curl -L -O $(HTP_URL)
	md5sum suricata-master.tar.gz htp-0.5.16.tar.gz > sources

clean:
	fedpkg clean
	rm -f *~
