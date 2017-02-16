NAME :=	ragel

COPR_PROJECT :=	hyperscan-epel7

DISTS ?= epel-7-x86_64

include ../../common.mk

pre-mock::
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		clean
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) \
		--install ../colm/output/$(DIST)/colm-*.x86_64.rpm
