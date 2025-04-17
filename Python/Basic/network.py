import socket
import logging


def check_socket(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)

        # AF_INET: address family
        # SOCK_STREAM: type for TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except OSError:
        return False
    else:
        s.close()
        return True


# basic configuration for the logging system by creating a SreamHandler with
# a default Formatter and adding it to the root logger.
logging.basicConfig(
    filename="network_log.txt", format="%(asctime)s - %(message)s", filemode="w"
)

# Return a logger with the specified name, if name is None, return the root
# logger of the hierarchy.
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if check_socket():
    logging.info("pass the network check")
