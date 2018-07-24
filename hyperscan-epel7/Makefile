SUBDIRS :=	hyperscan

all clean copr:
	for dir in $(SUBDIRS); do \
		(cd $$dir && $(MAKE) $@) || exit 1; \
	done
