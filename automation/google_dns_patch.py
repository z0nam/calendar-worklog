import socket

# JRI office network Google API hang bypass patch
# Filters out blocked anycast IP 216.239.36.223 and IPv6 addresses (no route).
orig_getaddrinfo = socket.getaddrinfo
def patched_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    res = orig_getaddrinfo(host, port, family, type, proto, flags)
    filtered = []
    for r in res:
        ip = r[4][0]
        if r[0] == socket.AF_INET and ip != "216.239.36.223":
            filtered.append(r)
    return filtered if filtered else res

socket.getaddrinfo = patched_getaddrinfo

# Intercept connect to resolve using patched getaddrinfo to bypass C-level getaddrinfo.
orig_connect = socket.socket.connect
def patched_connect(self, address):
    host, port = address
    if isinstance(host, str) and not host.replace('.', '').isdigit():
        try:
            ips = socket.getaddrinfo(host, port)
            if ips:
                target_addr = ips[0][4]
                return orig_connect(self, target_addr)
        except Exception:
            pass
    return orig_connect(self, address)

socket.socket.connect = patched_connect
