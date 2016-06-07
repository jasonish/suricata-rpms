NAME :=	hyperscan

COPR_PROJECT :=	suricata-hyperscan-daily

DISTS ?= epel-7-x86_64 fedora-22-x86_64 fedora-23-x86_64

include ../../common.mk

pre-mock::
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		clean
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		--install ../ragel/output/$(DIST)/ragel-*.x86_64.rpm
