import http.server
import socketserver
import socket
import sys
import os

def main(path_to_dir):
    PORT = 80

    if path_to_dir is not None:
        os.chdir(path_to_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    pr_line = "serving at " + str(ip_address) + ":" + str(PORT)

    print(pr_line)
    httpd.serve_forever()

if __name__ == "__main__":
    argv_count = len(sys.argv)
    if argv_count == 2 and sys.argv[1] == "--help":  # Help CLI
        print("For any directory: python3 %s [PATH_TO_DIRECTORY]" % sys.argv[0])
        print("For cur directory: python3 %s" % sys.argv[0])
        sys.exit(0)
    else:
        path = None
        try:
            path = sys.argv[1]
        except:
            pass
        
        main(path)