from authproxy.webapp import app
from authproxy.settings import host, port, debug

if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
