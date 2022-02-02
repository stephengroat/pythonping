import unittest
import socket
from pythonping.network import Socket
from pythonping.utils import system_has_ipv6


class UtilsTestCase(unittest.TestCase):
    """Tests for Socket class"""

    def test_raise_explicative_error_on_name_resolution_failure(self):
        """Test a runtime error is generated if the name cannot be resolved"""
        with self.assertRaises(RuntimeError):
            Socket('cant.resolve.this.address.localhost', 'raw')

    def test_ipv6(self):
        sock = Socket('ipv6.google.com', 'raw')
        self.assertEqual(sock.socket.family, socket.AF_INET6)

    def test_ipv4_dns(self):
        sock = Socket('ipv4.google.com', 'raw')
        self.assertEqual(sock.socket.family, socket.AF_INET)

    def test_ipv6_address(self):
        sock = Socket('2001:4860:4860::8888', 'raw')
        self.assertEqual(sock.socket.family, socket.AF_INET6)

    def test_ipv4_address(self):
        sock = Socket('8.8.8.8', 'raw')
        self.assertEqual(sock.socket.family, socket.AF_INET)

    def test_dualstack(self):
        sock = Socket('google.com', 'raw')
        self.assertEqual(sock.socket.family, socket.AF_INET6)

    def test_dualstack_inet(self):
        sock = Socket('google.com', 'raw', family=socket.AF_INET)
        self.assertEqual(sock.socket.family, socket.AF_INET)