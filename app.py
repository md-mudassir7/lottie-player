from flask import Flask, render_template, request
import os

app = Flask(__name__)

LOTTIES_FOLDER = os.path.join('static', 'lotties')

@app.route('/')
def index():
    lottie_files = [f for f in os.listdir(LOTTIES_FOLDER) if f.endswith('.json')]

    selected_file = request.args.get('filename') if request.args.get('filename') else None

    return render_template('index.html', lottie_files=lottie_files, selected_file=selected_file)


if __name__ == '__main__':
    app.run(debug=True)
