srpm:
	fedpkg --name $(NAME) --dist epel7 srpm

copr-build: srpm
	for repo in $(COPR_REPO); do \
		echo "Push to $$repo"; \
		copr build $$repo $(NAME)*.el7.src.rpm; \
	done

copr-testing: srpm
	copr build $(COPR_TESTING) $(NAME)*.el7.src.rpm

update-sources:
	spectool -g suricata.spec
	sha512sum --tag suricata-*.tar.gz > sources

$(DISTS):
	fedpkg --name $(NAME) --dist $@ mockbuild

clean:
	rm -f *.src.rpm
	rm -rf results_suricata
