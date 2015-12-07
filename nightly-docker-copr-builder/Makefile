TAG :=	jasonish/suricata-rpm-nightly-copr-builder

all: build run

build:
	docker build -t $(TAG) .

run:
	docker run -it --rm \
		-v ${HOME}/.config/copr:/root/.config/copr \
		$(TAG)
