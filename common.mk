srpm:
	fedpkg --name $(NAME) --dist epel7 srpm

copr-build: srpm
	copr build $(COPR_REPO) $(NAME)*.el7.src.rpm

copr-testing: srpm
	copr build $(COPR_REPO)-testing $(NAME)*.el7.src.rpm

update-sources:
	spectool -g suricata.spec
	sha512sum --tag suricata-*.tar.gz > sources

$(DISTS):
	fedpkg --name $(NAME) --dist $@ mockbuild

clean:
	rm -f *.src.rpm
	rm -rf results_suricata
