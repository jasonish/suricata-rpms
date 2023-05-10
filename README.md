# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Building

Building these RPMs requires a recent Fedora or EL release with the
following packages installed:
- copr
- mock

## Makefile Targets

### Default (all)

This target will build RPMs for all currently supported distributions
using Mock.

### local

Builds the RPM locally with rpmbuild. This does require that all the
dependencies are installed.

### $(DIST)

Build for a specific distribution supported by Mock. For example:

```
make epel-7-x86_64
```

### copr-testing

Upload SRPM to the testing project on COPR.

By default this is: `@oisf/suricata-${VERSION}-testing`

### copr-build

Upload SRPM to the release project on COPR.

By default this is: `@oisf/suricata-${VERSION}`

## Updating for a Patch Release

Given an update from version 6.0.10 to 6.0.11, the process of an
update might look like (note all commands are to be run in the
directory corresponding to the version being updated):

- Edit `6.0/suricata.spec`
  - Update `Version` to `6.0.11`
  - If `Release` is different than `1%{?dist}`, change it back to `1%{?dist}`
  - Add a new entry to the top of the `%changelog` section
- Run: `make update-sources`
  - This will download the new release file and generate checksums for
    it
- Push to testing COPR project:
  - `make copr-testing`
- Monitor the build at https://copr.fedorainfracloud.org/coprs/g/oisf/suricata-6.0/monitor/
- If successful, push to the COPR release repo:
  - `make copr-build`

