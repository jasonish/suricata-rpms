SUBDIRS :=	ragel \
		hyperscan \
		suricata

all clean:
	for dir in $(SUBDIRS); do \
		(cd $$dir && $(MAKE) $@) || exit 1; \
	done
