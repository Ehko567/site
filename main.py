from flask import Flask, render_template, redirect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '423h1g5kgjh12fj43gf5h3524u5g43u52ug54iy26g58fd5g98d5g8fd5g98d5gxbh7gdfhcht7wnr0d8f7qd3'


@app.route('/')
def start():
    return render_template('main.html', title='Ausz')

def main():
    app.run()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
