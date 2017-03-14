import platform
from psutil import virtual_memory


def get_processor():
    return platform.processor()


def get_platform():
    return platform.platform(aliased=True, terse=True)


def get_physical_memory():
    return virtual_memory().total