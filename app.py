from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve the main HTML file
@app.route('/')
def serve_index():
    return send_from_directory('/Users/ishayu/Documents/2 Year Website', 'index.html')

# Route to serve static files (e.g., images, text files, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('/Users/ishayu/Documents/2 Year Website', filename)

if __name__ == '__main__':
    app.run(debug=True)
