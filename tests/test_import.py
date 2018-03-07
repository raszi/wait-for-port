
def test_import():
    import wait_for_port
    assert hasattr(wait_for_port, 'wait_for_port')

    import wait_for_port.main
    assert hasattr(wait_for_port.main, 'main')


def test_unbound_local_error():
    """
    Testing that exception and verbose=True are working together
    (test for the issue https://github.com/trbs/wait-for-port/issues/1)
    """
    import wait_for_port

    wait_for_port.wait_for_port(
        host='%$@#',  # host is incorrect and will cause an exception
        port=1,
        verbose=True
    )
