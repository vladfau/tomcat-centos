# -*- mode: ruby -*-
# vi: set ft=ruby :
$script = <<SCRIPT
  echo I am provisioning...
  sudo su
  yum -y update
  yum -y groupinstall 'Development Tools'
  yum -y install vim
  date > /etc/vagrant_provisioned_at
SCRIPT


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "chef/centos-6.5"
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision "shell", inline: $script
end
