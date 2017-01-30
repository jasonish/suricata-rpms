COPR_PROJECT :=	suricata-hyperscan-daily
DISTS :=	epel-7-x86_64 fedora-22-x86_64 fedora-23-x86_64
SPEC =		suricata-daily.spec

include daily.mk
include ../../common.mk

pre-mock::
	mock --configdir $(CONFIGDIR) \
		-r $(DIST) --install \
		../colm/output/$(DIST)/colm-*.x86_64.rpm \
		../ragel/output/$(DIST)/ragel-*.x86_64.rpm \
		../hyperscan/output/$(DIST)/hyperscan-*.x86_64.rpm
