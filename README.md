# Suricata RPMs

Spec files and build infrastucture for building Suricata RPMs.

## Setup for tracking Fedora Suricata RPM

git remote add fedora-suricata git://pkgs.fedoraproject.org/suricata
git fetch fedora-suricata
git subtree add --squash --prefix=suricata-test/ fedora-suricata 88f8f438a3d7403e0226d6b9267fc638b824dd05

## Update to latest Fedora RPM

git fetch fedora-suricata
git subtree merge --squash --prefix=suricata-test/ fedora-suricata/master
