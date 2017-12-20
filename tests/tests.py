def test_nginx_listening_local(host):
    assert host.socket("tcp://0.0.0.0:8081").is_listening



