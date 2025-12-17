from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

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

    if tool not in commands:
        return jsonify({'error': 'invalid tool ruh roh'}), 400

    try:
        timeout = 60 if tool == 'traceroute' else 30
        result = subprocess.run(commands[tool], capture_output=True, text=True, timeout=timeout)
        output = result.stdout or result.stderr or '~ no output ~'
    except subprocess.TimeoutExpired:
        output = '~ command timed out ~'
    except Exception as e:
        output = f'~ error: {e} ~'

    return jsonify({'output': output})
    
if __name__ == '__main__':
    app.run(debug=True)