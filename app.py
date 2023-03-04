from flask import Flask
import socket

app = Flask(__name__)

def get_ip():
    # IPv4
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        pass

    # IPv6
    try:
        return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
    except:
        pass

    return 'localhost'

@app.route("/")
def index():
    html = "<h3>Bonjour!</h3>" \
	   "<b>IP Address:</b> {ipaddr}<br/>" \
	   "<b>Container :</b> {container}<br/><br/>" \
	   "<b>If you see this page, this means that the Bonjour web server is successfully installed and working.</b><br/><br/>" \
       "<div>Thanks for using Bonjour</div><br/>" \
       "<div>GitHub: https://github.com/ldatb/bonjour</div>"
    return html.format(ipaddr=get_ip(), container=socket.gethostname())
