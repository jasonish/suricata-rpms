NAME :=		suricata
MAJOR :=	$(shell basename $(shell pwd))
LATEST :=	$(shell cat ../LATEST)
SRCDIR :=	$(shell pwd)

VERSION := $(shell rpm --undefine 'dist' -q --qf "%{VERSION}-%{RELEASE}\n" --specfile suricata.spec| head -n1)

RELEASES :=	$(shell fedpkg releases-info --join)

srpm:
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

copr-build: srpm
	@if [ "$(COPR)" = "" ]; then \
		echo "error: COPR environment variable must be set"; \
		exit 1; \
	fi
	copr build $(COPR)/suricata-$(MAJOR) suricata-$(VERSION).src.rpm

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

update-sources:
	spectool -g suricata.spec
	rm -f sources
	for source in $$(spectool -l suricata.spec | awk '/^Source.*http/ { print $$2 }'); do \
		echo $$source; \
		sha512sum --tag $$(basename $$source) >> sources; \
	done

$(RELEASES):
	fedpkg --name $(NAME) --release $@ mockbuild


MOCK_RESULTDIR := ./mock-results
mock:
	mock -r alma+epel-9-x86_64 --resultdir $(MOCK_RESULTDIR) suricata-$(VERSION).src.rpm
	mock -r alma+epel-8-x86_64 --resultdir $(MOCK_RESULTDIR) suricata-$(VERSION).src.rpm
	mock -r epel-7-x86_64      --resultdir $(MOCK_RESULTDIR) suricata-$(VERSION).src.rpm
	mock -r fedora-37-x86_64   --resultdir $(MOCK_RESULTDIR) suricata-$(VERSION).src.rpm
	mock -r fedora-36-x86_64   --resultdir $(MOCK_RESULTDIR) suricata-$(VERSION).src.rpm

clean:
	rm -f *.src.rpm
	rm -rf results_suricata
