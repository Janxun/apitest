def test_version():
    from one_apitest import __version__
    assert isinstance(__version__,str)