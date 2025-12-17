from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_tool():
    tool = request.form.get('tool')
    target = request.form.get('target')
    
    if not target:
        return jsonify({'error': 'please enter domain or ip :3'}), 400
    
    commands = {
        'ping': ['ping', '-c', '4', target],
        'nslookup': ['nslookup', target],
        'traceroute': ['traceroute', target],
    }

if __name__ == '__main__':
    app.run(debug=True)