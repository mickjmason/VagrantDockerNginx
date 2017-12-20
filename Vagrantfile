VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 18081, host: 18081
  config.vm.network "private_network", ip: "172.1.0.250"
  config.vm.provision "file", source: "./docker", destination: "/tmp"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "docker.yml"
  end
end 
