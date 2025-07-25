# URL Shortener API

A lightweight, Flask-based URL shortener service with analytics and thread-safe operations.

## Features

- **URL Shortening**: Generate 6-character alphanumeric short codes for long URLs
- **Redirect Service**: Fast O(1) lookup and redirect to original URLs  
- **Click Analytics**: Track and view click statistics for shortened URLs
- **Thread Safety**: Concurrent request handling with proper synchronization
- **URL Validation**: Input validation for proper URL format
- **In-Memory Storage**: Simple, fast storage without external database dependencies

## Technical Stack

- **Python**: 3.8+
- **Framework**: Flask 2.3.2
- **Testing**: pytest 7.4.0
- **Concurrency**: Threading with locks for thread safety

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd url-shortener
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python -m flask --app app.main run
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Shorten URL
Create a short URL from a long URL.

```http
POST /api/shorten
Content-Type: application/json

{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

### Redirect
Redirect to the original URL using the short code.

```http
GET /<short_code>
```

Returns a 302 redirect to the original URL.

### Get Statistics
View click analytics for a shortened URL.

```http
GET /api/stats/<short_code>
```

**Response:**
```json
{
  "short_code": "abc123",
  "original_url": "https://example.com",
  "click_count": 15
}
```

## Usage Examples

### Using cURL

```bash
# Shorten a URL
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'

# Follow redirect (browser or CLI)
curl -L http://localhost:5000/abc123

# Get click statistics
curl http://localhost:5000/api/stats/abc123
```

## Testing

Run the test suite:

```bash
pytest
```

### Test Coverage

The project includes comprehensive tests covering:

- **Health Check**: API status verification
- **URL Shortening**: Core shortening functionality
- **Redirect**: URL redirection behavior
- **Error Handling**: Invalid URL validation
- **Analytics**: Click statistics accuracy
- **Concurrency**: Thread-safe operations

## Architecture

### Data Structures

- `url_mappings`: Dictionary storing short_code → URLMapping objects
- `click_counts`: Dictionary tracking visit counts per short code

### Thread Safety

Critical operations are protected using Python's threading.Lock:

```python
from threading import Lock

lock = Lock()

with lock:
    # Thread-safe operations
    click_counts[short_code] += 1
```

### Performance

- **O(1) lookup time** for all operations
- **Thread-safe increments** for click tracking
- **Minimal memory footprint** with in-memory storage

## Error Handling

- **400 Bad Request**: Invalid URL format
- **404 Not Found**: Short code does not exist
- **500 Internal Server Error**: Server-side errors

## Design Decisions

### Simplicity First
- In-memory storage for MVP deployment
- Minimal external dependencies
- Clear separation of concerns

### Scalability Considerations
- Thread-safe operations for concurrent requests
- Efficient data structures for fast lookups
- Modular design for easy extension

## Development Notes

- **Development Time**: Approximately 2.5 hours
- **Primary Challenge**: Thread safety implementation
- **Code Quality**: Clean, well-documented code with comprehensive tests

## Requirements

See `requirements.txt` for complete dependency list:

```
Flask==2.3.2
pytest==7.4.0
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
