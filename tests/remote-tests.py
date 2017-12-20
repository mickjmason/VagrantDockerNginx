def test_docker_installed_and_running(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled
  
def test_nginx_site_is_available_on_docker_host(host):
    assert host.socket("tcp://0.0.0.0:18081").is_listening

def test_docker_is_running_alpine_linux(host):
    assert host.check_output("docker exec nginx_alpine cat /etc/alpine-release") == "3.7.0"

def test_nginx_is_running_in_container(host):
    assert host.check_output("docker exec nginx_alpine pgrep '/usr/sbin/nginx'") == "1"

