# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Building

Building these RPMs requires a recent Fedora or CentOS release with the
following packages installed:
- fedpkg
- copr

### Building Locally

To build an RPM locally, enter the directory for the version you want to build
and run commands like the following:

```
make update-sources
fedpkg --name suricata --dist epel8 mockbuild
```

Replace the `--dist` argument with another valid mock distribution to build for
a different version. For example `--dist f32` or `--dist epel7`.

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
