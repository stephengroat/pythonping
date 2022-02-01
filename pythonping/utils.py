"""Module containing service classes and functions"""

import string
import random
import socket
import errno


# On Windows, the E* constants will use the WSAE* values
# So no need to hardcode an opaque integer in the sets.
_ADDR_NOT_AVAIL = {errno.EADDRNOTAVAIL, errno.EAFNOSUPPORT}
_ADDR_IN_USE = {errno.EADDRINUSE}

def system_has_ipv6() -> bool:
    if not socket.has_ipv6:
        return False
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
            sock.bind(("::1", 0))
        return True
    except OSError as e:
        if e.errno in _ADDR_NOT_AVAIL:
            return False
        if e.errno in _ADDR_IN_USE:
            # This point shouldn't ever be reached. But just in case...
            return True
        # Other errors should be inspected
        raise

def random_text(size):
    """Returns a random text of the specified size

    :param size: Size of the random string, must be greater than 0
    :type size int
    :return: Random string
    :rtype: str"""
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
