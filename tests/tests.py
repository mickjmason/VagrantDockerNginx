def test_nginx_listening_local(host):
    assert host.socket("tcp://0.0.0.0:18081").is_listening



