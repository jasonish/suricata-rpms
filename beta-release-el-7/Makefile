.PHONY:	sources

all:
	fedpkg --dist epel7 --module-name suricata-beta-release-el mockbuild

sources:
	md5sum suricata-beta.repo > sources

clean:
	fedpkg clean
	rm -f *~
