from helper.filesystem import get_src_directory, get_config_directory, get_absolute_path


def test_get_src_directory():
    assert (get_src_directory() / 'requirements.txt').exists()


def test_get_config_directory():
    assert (get_config_directory() / 'sample.cfg').exists()


def test_get_absolute_path():
    path = "src/requirements.txt"
    assert (get_absolute_path(path)).exists()
