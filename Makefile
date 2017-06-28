SUBDIRS := $(shell find * -maxdepth 0 -type d)

all:

clean:
	@for subdir in $(SUBDIRS); do \
		if test -e $$subdir/Makefile; then \
			$(MAKE) -C $$subdir clean; \
		fi \
	done
