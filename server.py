from config import WATCH_DIR
from urlparse import urlparse, parse_qs
import subprocess
import re

from flask import Flask, request

app = Flask(__name__)

@app.route("/download")
def download():
    print '/download'
    url = request.args.get('url')
    print 'url: ' + url
    rawurl = re.sub(r'\?.*', '', url)
    print 'rawurl: ' + rawurl
    title = parse_qs(urlparse(url).query)['title'][0]
    print 'title:'
    print title


  # subprocess.call(['wget', str(url), '-P', WATCH_DIR])
    subprocess.call([
        'curl', '-L', '-o', WATCH_DIR + title + '.torrent', '--compressed', rawurl
    ])

@app.route("/test")
def test():
    return 'this is a test'

if __name__ == "__main__":
    app.run()
