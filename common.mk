COPR ?=		@oisf
NAME :=		suricata
MAJOR :=	$(shell basename $(shell pwd))
LATEST :=	$(shell cat ../LATEST)
SRCDIR :=	$(shell pwd)

VERSION := $(shell rpm --undefine 'dist' -q --qf "%{VERSION}-%{RELEASE}\n" --specfile suricata.spec| head -n1)

# Current support RPM distribution releases. This relate to the
# support chroots in COPR.
DISTS :=	fedora-38-x86_64 \
		fedora-37-x86_64 \
		alma+epel-9-x86_64 \
		alma+epel-8-x86_64 \
		epel-7-x86_64

# The default make target. Builds the SRPM then build Suricata for
# each supported distributions.
all:
	$(MAKE) update-sources
	$(MAKE) srpm
	@for dist in $(DISTS); do \
		$(MAKE) "$$dist"; \
	done

srpm:
	rm -f *.src.rpm
	rpmbuild \
		--define "_sourcedir $(PWD)" \
		--define "_specdir $(PWD)" \
		--define "_builddir $(PWD)" \
		--define "_srcrpmdir $(PWD)" \
		--define "_rpmdir $(PWD)" \
		--eval "%undefine dist" \
		--define "_rpmfilename %%{ARCH}/%%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm" \
		--nodeps \
		-bs suricata.spec

update-sources:
	spectool -g suricata.spec
	rm -f sources
	for source in $$(spectool -l suricata.spec | awk '/^Source.*http/ { print $$2 }'); do \
		echo $$source; \
		sha512sum --tag $$(basename $$source) >> sources; \
	done

$(DISTS):
	bash -xc "mock -r $@ --resultdir output/$@ suricata-$(VERSION).src.rpm"

local:
	$(MAKE) update-sources
	$(MAKE) srpm
	rpmbuild --rebuild suricata-$(VERSION).src.rpm

copr-build: srpm
	@if [ "$(COPR)" = "" ]; then \
		echo "error: COPR environment variable must be set"; \
		exit 1; \
	fi
	copr build $(COPR)/suricata-$(MAJOR) suricata-$(VERSION)*.src.rpm
	$(MAKE) copr-build-latest

copr-build-latest: srpm
	if [ "$(MAJOR)" = "$(LATEST)" ]; then \
		copr build $(COPR)/suricata-latest suricata-$(VERSION).src.rpm; \
	fi

copr-testing: srpm
	@if [ "$(COPR)" = "" ]; then \
		echo "error: COPR environment variable must be set"; \
		exit 1; \
	fi
	copr build $(COPR)/suricata-$(MAJOR)-testing \
		suricata-$(VERSION).src.rpm

clean:
	rm -rf *.src.rpm *.tar.gz output
