FROM centos:centos7

RUN yum -y install epel-release
RUN yum -y install fedpkg
RUN yum -y install make
RUN echo "config_opts['macros']['%dist']" = '".el7"' >> /etc/mock/epel-7-x86_64.cfg

RUN useradd builder
RUN usermod -aG mock builder
RUN echo "export PATH=/usr/bin:$PATH" >> /home/builder/.bashrc