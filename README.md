# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Building

Building these RPMs requires a recent Fedora or EL release with the
following packages installed:

- copr
- mock
- make
- spectool

Building will require a proper Fedora 44 or like installation. If just prepping
the files for COPR then a distrobox running Fedora 44 is probably enough.

## Setup

To test/debug builds locally you will need to add your user to the `mock` group,
then re-login.

## Makefile Targets

### local

Builds the RPM locally with rpmbuild. This does require that all the
dependencies are installed.

### $(DIST)

Build for a specific distribution supported by Mock. For example:

```
make epel-10-x86_64
```

See common.mk for a list of active `DISTS`.

### mock-all

Build all `DISTS` in `mock`.

### copr-testing

Upload SRPM to the testing project on COPR.

By default this is: `@oisf/suricata-${VERSION}-testing`

### copr-release

Upload SRPM to the release project on COPR.

By default this is: `@oisf/suricata-${VERSION}`

## Updating for a Patch Release

### The easy way

- Use the update-version script:
    ```
    cd 8.0
    ./update-version.py 8.0.7
    ```
- Run `git diff` to verify the changes.
- If you are not Jason, please update the changelog entry to your name and email.
- Update the sources:
    ```
    make update-sources
    ```
- Run a test build:
    ```
    make copr-testing
    ```
    - If all looks good:
    ```
    make copr-release
    ```

### Or the more detailed way

Given an update from version 8.0.6 to 8.0.7, the process of an update
might look like (note all commands are to be run in the directory
corresponding to the version being updated):

- Edit `8.0/suricata.spec`
  - Update `Version` to `8.0.7`
  - If `Release` is different than `1%{?dist}`, change it back to `1%{?dist}`
  - Add a new entry to the top of the `%changelog` section
- Run: `make update-sources`
  - This will download the new release file and generate checksums for
    it
- Push to testing COPR project:
  - `make copr-testing`
- Monitor the build at
  https://copr.fedorainfracloud.org/coprs/g/oisf/suricata-8.0-testing/monitor/
- If successful, push to the COPR release repo:
  - `make copr-release`

## Distrobox Initialization

If not running on a recent Fedora version, Distrobox can be used.

* `distrobox assemble create`
* `distrobox enter suricata-rpms`

This should drop you into a Fedora environment suitable for building RPMs and
uploading them to COPR.

To clean-up after, run:

``` shell
distrobox assemble rm
```

