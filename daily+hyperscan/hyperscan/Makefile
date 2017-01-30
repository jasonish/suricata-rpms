NAME :=	hyperscan

COPR_PROJECT :=	suricata-hyperscan-daily

DISTS ?=	epel-7-x86_64 \
		fedora-23-x86_64 \
		fedora-24-x86_64 \
		fedora-25-x86_64 \
		fedora-26-x86_64

include ../../common.mk

pre-mock::
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		clean
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		--install ../colm/output/$(DIST)/colm-*.x86_64.rpm
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		--install ../ragel/output/$(DIST)/ragel-*.x86_64.rpm
