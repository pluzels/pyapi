from flask import Flask, jsonify, request, render_template
from playmusic import get_youtube_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/playmusic', methods=['GET'])
def playmusic():
    query = request.args.get('query')
    if not query:
        return jsonify({'status': 400, 'message': 'query parameter is missing'}), 400
    
    data = get_youtube_data(query)
    if data:
        return jsonify({'status': 200, 'message': 'success', 'result': data})
    else:
        return jsonify({'status': 500, 'message': 'Failed to retrieve data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
