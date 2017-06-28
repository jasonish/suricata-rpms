COPR_PROJECT :=	suricata-hyperscan-daily
DISTS :=	epel-7-x86_64 fedora-24-x86_64 fedora-25-x86_64
SPEC =		suricata.spec

include ../daily/daily.mk
include ../common.mk

pre-mock::
ifeq ($(DIST),fedora-24-x86_64)
	wget --no-clobber https://copr-be.cloud.fedoraproject.org/results/jasonish/hyperscan/fedora-24-x86_64/00561939-hyperscan/hyperscan-4.4.1-1.fc24.x86_64.rpm
	mock --configdir $(CONFIGDIR) -r $(DIST) --install \
		hyperscan*.fc24.x86_64.rpm
endif
clean::
	rm -rf RPMS
