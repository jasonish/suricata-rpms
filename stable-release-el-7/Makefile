SPEC := suricata-stable-release.spec

.PHONY:	sources

all:
	rpmbuild --target noarch \
		--define '_sourcedir .' \
		--define '_specdir .' \
		--define '_builddir .' \
		--define '_srcrpmdir ./output' \
		--define '_builddir .' \
		--define '_rpmdir ./output' \
		--define 'dist .el7' \
		-v -ba $(SPEC)

sources:
	md5sum suricata-beta.repo > sources

clean:
	rm -rf output
