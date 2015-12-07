FROM fedora:23
MAINTAINER Jason Ish <ish@unx.ca>

RUN dnf -y install \
    git \
    tar \
    copr-cli \
    make

RUN dnf -y install \
    rpmdevtools

# Seed the image with the code at the time of image creation.
RUN mkdir /work && \
    cd /work && \
    git clone https://github.com/jasonish/suricata-rpms.git && \
    cd suricata-rpms/nightly && \
    make fetch

COPY /build.sh /

ENTRYPOINT /build.sh