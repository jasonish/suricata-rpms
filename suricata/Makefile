# Usage:
#
# Get a shell in Docker:
#
#    make docker-epel7
#
# Start the build:
#
#    make mockbuild
#
# There are currenly issues executing fedpkg/mock directly in the container,
# which is why we first need to get a shell in the container.

all:

docker-epel7:
	cd ../docker/centos-7-x64-builder && make build
	docker run --privileged \
		-v `pwd`/cache:/var/cache -it \
		-v `pwd`/../:/build \
		-u builder \
		-e DIST="--dist epel7" \
		local/centos-7-x64-suricata-builder \
		bash -c 'cd /build/suricata && exec bash'

mockbuild:
	fedpkg $(DIST) --module-name suricata mockbuild
