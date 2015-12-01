RPMSPEC := rpmspec -E '%undefine dist'

NAME := suricata
SPEC := $(NAME).spec
VERSION := $(shell $(RPMSPEC) -P $(SPEC) | awk '/^Version/ { print $$2 }')
RELEASE := $(shell $(RPMSPEC) -P $(SPEC) | awk '/^Release/ { print $$2 }')
SRPM :=	$(NAME)-$(VERSION)-$(RELEASE).src.rpm

all: fetch $(DISTS)

fetch:
	spectool -g $(SPEC)

srpm:
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

copr: srpm
	copr build $(COPR_PROJECT) $(SRPM)

mock: CONFIGDIR := $(shell test -e ../mock/$(DIST).cfg && \
	echo ../mock || echo /etc/mock)
mock: srpm
	mock --configdir $(CONFIGDIR) -r $(DIST) \
		--resultdir output/$(DIST) $(SRPM)

$(DISTS):
	$(MAKE) mock DIST="$@"

clean:
	rm -rf output
