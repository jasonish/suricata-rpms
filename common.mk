NAME :=		suricata
MAJOR :=	$(shell basename $(shell pwd))
LATEST:=	$(shell cat ../LATEST)

VERSION := $(shell rpm --define 'dist .el7' -q --qf "%{VERSION}-%{RELEASE}\n" --specfile suricata.spec| head -n1)

DISTS :=	epel8 epel7 f33 f32 f31

srpm:
	fedpkg --name $(NAME) --dist epel7 srpm

copr-build: srpm
	@if [ "$(COPR)" = "" ]; then \
		echo "error: COPR environment variable must be set"; \
		exit 1; \
	fi
	copr build $(COPR)/suricata-$(MAJOR) suricata*.el7.src.rpm

	if [ "$(MAJOR)" = "$(LATEST)" ]; then \
		copr build $(COPR)/suricata-latest suricata*.el7.src.rpm; \
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
	sha512sum --tag `basename $$(spectool -l suricata.spec | awk '/^Source0/ { print $$2 }')` > sources

$(DISTS):
	fedpkg --name $(NAME) --dist $@ mockbuild

clean:
	rm -f *.src.rpm
	rm -rf results_suricata
