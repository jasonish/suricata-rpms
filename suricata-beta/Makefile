all: epel7

fetch:
	spectool -g suricata.spec

epel7:
	fedpkg --dist epel7 --module-name suricata mockbuild

clean:
	fedpkg clean
	rm -f *~


