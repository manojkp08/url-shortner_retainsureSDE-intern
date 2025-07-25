from flask import Flask, jsonify, redirect, request
from app.models import url_mappings, click_counts, URLMapping
from app.utils import generate_short_code, is_valid_url

app = Flask(__name__)

# Health checks (already provided)
@app.route('/')
def health_check():
    return jsonify({"status": "healthy", "service": "URL Shortener API"})

@app.route('/api/health')
def api_health():
    return jsonify({"status": "ok", "message": "URL Shortener API is running"})

# Core functionality
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    url_mappings[short_code] = URLMapping(original_url, short_code)
    click_counts[short_code] = 0

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@app.route('/<short_code>')
def redirect_to_original(short_code):
    if short_code not in url_mappings:
        return jsonify({"error": "Short code not found"}), 404

    click_counts[short_code] += 1
    return redirect(url_mappings[short_code].original_url)

@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    if short_code not in url_mappings:
        return jsonify({"error": "Short code not found"}), 404

    mapping = url_mappings[short_code]
    return jsonify({
        "url": mapping.original_url,
        "clicks": click_counts[short_code],
        "created_at": mapping.created_at.isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)