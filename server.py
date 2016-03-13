from config import WATCH_DIR
from urlparse import urlparse, parse_qs
import subprocess
import re

from flask import Flask, request

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get('url')
    rawurl = re.sub(r'\?.*', '', url)
    title = parse_qs(urlparse(url).query)['title'][0]

  # subprocess.call(['wget', str(url), '-P', WATCH_DIR])
    print "curl -L -o {0}{1}.torrent --compressed {2}".format(WATCH_DIR, title, rawurl)
    curl_sp = subprocess.call([
        'curl', '-L', '-o', WATCH_DIR + title + '.torrent', '--compressed', rawurl
    ])

    if curl_sp.returncode is 0:
        return 200

@app.route("/test")
def test():
    return 'this is a test'

if __name__ == "__main__":
    app.run()
