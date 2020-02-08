from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='')

@app.route('/')
def result():
    return render_template('compare_loss.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) # FLASK_APP=compare_loss.py python -m flask run