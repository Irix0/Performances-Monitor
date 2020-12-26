import platform
import socket
import ipgetter2
import speedtest


# SYSTEM
def get_os():
    a = platform.system() + " " + platform.release()
    return a


def get_system_name():
    return platform.node()


# NETWORK

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_external_ipv4():
    """Return string with the IPv4
        Use get_external_ip to get IPv6 in first option and then IPv4"""
    a = ipgetter2.IPGetter()
    batch = ["https://v4.ipv6-test.com/api/myip.php", "https://api.ipify.org", "https://v4.ident.me/",
             "https://ip4.seeip.org"]
    ipv4 = a.get_from_batch(batch)
    if ipv4.is_valid():
        if ipv4.v4 != ipv4.DEFAULT_IPV4_ADDRESS:
            return ipv4.v4
        elif ipv4.v4 == ipv4.DEFAULT_IPV4_ADDRESS:
            return "No IPv4 found."
        else:
            return "No external IP found. Check your connection."


def get_external_ipv6():
    """Return string with the IPv6
        Use get_external_ip to get IPv6 in first option and then IPv4"""
    a = ipgetter2.IPGetter()
    batch = ["https://v6.ipv6-test.com/api/myip.php", "https://api64.ipify.org", "https://v6.ident.me/",
             "https://ip6.seeip.org"]
    ipv6 = a.get_from_batch(urls=batch)
    if ipv6.is_valid():
        if ipv6.v6 != ipv6.DEFAULT_IPV6_ADDRESS:
            return ipv6.v6
        elif ipv6.v6 == ipv6.DEFAULT_IPV6_ADDRESS:
            return "No IPv6 found."
        else:
            return "No external IPv6 found. Check your connection."


def get_external_ip():
    """Return string with the IPv6 or IPv4
        Return IPv6 if available (use get_external_ipv4 for IPv4)"""
    a = ipgetter2.IPGetter()
    batch = ["https://ipv6-test.com/api/myip.php", "https://bot.whatismyipaddress.com", "https://ident.me/",
             "https://ip.seeip.org"]
    ip = a.get_from_batch(urls=batch)
    if ip.is_valid():
        if ip.v4 == ip.DEFAULT_IPV4_ADDRESS and ip.v6 != ip.DEFAULT_IPV6_ADDRESS:
            return ip.v6
        elif ip.v4 != ip.DEFAULT_IPV4_ADDRESS and ip.v6 == ip.DEFAULT_IPV6_ADDRESS:
            return ip.v4
        elif ip.v4 == ip.DEFAULT_IPV4_ADDRESS and ip.v6 == ip.DEFAULT_IPV6_ADDRESS:
            return "No external IP found. Check your connection."


def do_speedtest():
    """Return the results of the speedtest.net"""
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=None)
    s.upload(threads=None)
    results = s.results.dict()
    return results


class Speedtest:

    def __init__(self):
        self.results = do_speedtest()
        self.server_raw = self.results['server']
        self.results.__delitem__('server')

    def re_do_speedtest(self):
        self.results = do_speedtest()
        """Should be used to actualize results of the speedtest"""

    def get_download(self):
        """Return float with the download in MB"""
        return self.results['download'] / 1e+6  # Megabytes conversion

    def get_upload(self):
        """Return float with the upload in MB"""
        return self.results['upload'] / 1e+6  # Megabytes conversion

    def get_ping(self):
        """Return float with the ping"""
        return self.results['ping']

    def get_server_name(self):
        """Return string with the server name/country
            Examples : Louvain-La-Neuve, Liège"""
        return self.server_raw['name']

    def get_sever_sponsor(self):
        """Return string with the server sponsor
            Examples : Arcadiz, Université Catholique de Louvain"""
        return self.server_raw['sponsor']


if __name__ == '__main__':
    # print(get_external_ipv4())
    # print(get_external_ipv6())
    # print(get_external_ip())
    # s = Speedtest()
    # print(s.get_server_name())
    # print(s.get_download())
    # print(s.get_upload())
    # print(get_system_name())
    pass
