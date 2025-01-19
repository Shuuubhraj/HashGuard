from flask import Flask, render_template, request, redirect, url_for
import hashlib
import os
import webbrowser
import threading
import zlib  # For CRC32

app = Flask(__name__)

# Create the uploads directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

def calculate_hashes(file_path):
    """Calculate MD5, SHA-1, SHA-256, and CRC32 hashes for a given file."""
    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()
    hash_sha256 = hashlib.sha256()
    crc32 = 0
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
                hash_sha1.update(chunk)
                hash_sha256.update(chunk)
                crc32 = zlib.crc32(chunk, crc32)  # Update CRC32
                
            return {
                'MD5': hash_md5.hexdigest(),
                'SHA-1': hash_sha1.hexdigest(),
                'SHA-256': hash_sha256.hexdigest(),
                'CRC32': format(crc32 & 0xFFFFFFFF, '08x')  # Format as hex
            }
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        hash_results = calculate_hashes(file_path)
        os.remove(file_path)  # Clean up the uploaded file
        return render_template('index.html', hash_results=hash_results, selected_file=file.filename)

def open_browser():
    """Open the web browser to the Flask app."""
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Start the browser in a new thread
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
