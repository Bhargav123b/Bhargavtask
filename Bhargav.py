from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sql_injection():
    payload = request.json.get('payload', '')
    pattern = re.compile('[;\'\"]')
    if pattern.search(payload):
        result = 'unsanitized'
    else:
        result = 'sanitized'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
