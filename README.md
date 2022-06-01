# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Building

Building these RPMs requires a recent Fedora or CentOS release with the
following packages installed:
- fedpkg
- copr
- mock

### Building Locally

To build an RPM locally, enter the directory for the version you want to build
and run commands like the following:

```
make update-sources
make srpm
rpmbuild --rebuild suricata-6.0.5-2.src.rpm
```

This will attempt to build the RPM locally which means all the
dependencies need to be installed. It may be more useful to build with
mock, which also allows building for a different version of CentOS or
Fedora.  For example, to build for CentOS 7:

```
mock -r epel-7-x86_64 --resultdir . --rebuild suricata-6.0.5-2.src.rpm
```

Or to build for AlmaLinux 8:

```
mock -r alma+epel-8-x86_64 --resultdir . --rebuild suricata-6.0.5-2.src.rpm
```

### Building on COPR

To build on COPR you must have COPR projects created with the following pattern:
- suricata-MAJOR_VERSION
- suricata-MAJOR_VERSION-testing

Then the following commands can be used to start a build on COPR:
- `COPR=YOUR_COPR_USERNAME make copr-testing`
- `COPR=YOUR_COPR_USERNAME make copr-build`

Where the `testing` variation will start the build on the `-testing` project.

Example:

```
make update-sources
COPR=jasonish make copr-testing
```
