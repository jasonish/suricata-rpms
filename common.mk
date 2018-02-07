RPMSPEC =	rpmspec -E '%undefine dist'

NAME ?=		suricata
SPEC ?=		$(NAME).spec
VERSION =	$(shell $(RPMSPEC) -P $(SPEC) | awk '/^Version/ { print $$2 }')
RELEASE =	$(shell $(RPMSPEC) -P $(SPEC) | awk '/^Release/ { print $$2 }')
SRPM =		$(NAME)-$(VERSION)-$(RELEASE).src.rpm

all: fetch $(DISTS)

fetch::
	spectool -g $(SPEC)

srpm: fetch
	rpmbuild \
		--define '_sourcedir .' \
		--define '_specdir .' \
		--define '_builddir .' \
		--define '_srcrpmdir .' \
		--define '_builddir .' \
		--define '_rpmdir .' \
		--eval '%undefine dist' \
		-v -bs $(SPEC)
	@ls -l $(SRPM)

local: fetch
	rpmbuild \
		--define "_sourcedir `pwd`" \
		--define "_specdir `pwd`" \
		--define "_rpmdir `pwd`/RPMS" \
		--eval '%undefine dist' \
		-v -ba $(SPEC)

copr: srpm
	copr build $(COPR_PROJECT) $(SRPM)

pre-mock::

mock: CONFIGDIR := $(shell test -e ../mock/$(DIST).cfg && \
	echo ../mock || echo /etc/mock)
mock: srpm pre-mock
	mock --configdir $(CONFIGDIR) -r $(DIST) \
		--resultdir output/$(DIST) \
		--enable-network \
		--no-clean \
		$(SRPM)

update-sources: SOURCES=$(shell spectool -l $(SPEC) | basename `awk '/:\/\// { print $$2 }'`)
update-sources:
	md5sum $(SOURCES) > sources

$(DISTS):
	$(MAKE) mock DIST="$@"

clean::
	rm -rf output
