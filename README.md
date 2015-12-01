# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Setup for tracking Fedora Suricata RPM

git remote add fedora-suricata git://pkgs.fedoraproject.org/suricata
git fetch fedora-suricata
git subtree add --squash --prefix=stable/ fedora-suricata master

## Update to latest Fedora RPM

git fetch fedora-suricata
git subtree merge --squash --prefix=stable/ fedora-suricata/master
