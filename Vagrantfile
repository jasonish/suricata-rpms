# Vagrantfile to setup a box to build RPMs with a .el7 dist tag not containing
# .centos.

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "jasonish/centos7-x64-minimal"

  config.vm.provider "virtualbox" do |vb|
     # Don't boot with headless mode
     # vb.gui = true
  end

  config.vm.provision "shell" do |shell|
    shell.inline = $script
  end

end

$script = <<SCRIPT
yum -y install epel-release
yum -y install fedpkg
echo "config_opts['macros']['%dist']" = '".el7"' >> /etc/mock/epel-7-x86_64.cfg
usermod -aG mock vagrant
SCRIPT
