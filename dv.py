from flask import Flask, render_template, request
import urllib.request
import operator
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form.get("Name")
        x = "https://en.wikipedia.org/wiki/"
        if x in url:
            weburl = urllib.request.urlopen(url)
            soup = BeautifulSoup(weburl, 'html.parser')
            
            for s in soup(["s", "style"]):
                s.decompose()
            s = list(soup.stripped_strings)
            jj = []
            for i in s:
                jj.append(i.split(" "))
            f = {}

            for i in range(len(jj)):
                for j in jj[i]:
                    if j in f:
                        f[j] += 1
                    else:
                        f[j] = 1

            y = dict(sorted(f.items(), key=operator.itemgetter(1), reverse=True))
            z = y.items()
            v = list(z)[:10]
            p = dict(v)

            result = request.form
            return render_template("result.html", p=p)
        else:
            e = "it is not wikipedia link, enter valid wikipedia link"
            print(e)
            return render_template("index.html", e=e)

if __name__ == '__main__':
    app.run(debug=True)
