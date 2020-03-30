copr-build:
	fedpkg --name $(NAME) --dist epel7 srpm
	copr build $(COPR_REPO) $(NAME)*.el7.src.rpm

$(DISTS):
	fedpkg --name $(NAME) --dist $@ mockbuild

clean:
	rm -f *.src.rpm
	rm -rf results_suricata
