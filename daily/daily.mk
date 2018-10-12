DAILY_VERSION := $(shell date +%Y.%m.%d.%s)

all:

fetch::
	test -e suricata && \
		(cd suricata && git pull) || \
		git clone https://github.com/inliniac/suricata.git
	test -e suricata/libhtp && \
		(cd suricata/libhtp && git pull) || \
		(cd suricata && git clone https://github.com/OISF/libhtp.git)
	tar zcf suricata.tar.gz suricata
	sed -e "s#%%VERSION%%#$(DAILY_VERSION)#g" \
		suricata.spec.in > suricata.spec

dist-clean: clean
	rm -rf suricata

clean::
	rm -f suricata.spec
	rm -f *.rpm *.tar.gz
