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
git clone https://github.com/manojkp08/url-shortner_retainsureSDE-intern.git
cd url-shortner_retainsureSDE-intern
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
POST http://localhost:5000/api/shorten
Content-Type: application/json

{
  "url": "https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258"
}
```

**Response:**
```json
{
  "short_code": "xyh635",
  "short_url": "http://localhost:5000/xyh635"
}
```

### Redirect
Redirect to the original URL using the short code.

```http
GET http://localhost:5000/<short_code>
example:
GET http://localhost:5000/xyh635
```

Returns a 302 redirect to the original URL.

### Get Statistics
View click analytics for a shortened URL.

```http
GET http://localhost:5000/api/stats/<short_code>
example:
GET http://localhost:5000/api/stats/xyh635
```

**Response:**
```json
{
  "short_code": "xyh635",
  "original_url": "https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258",
  "click_count": 15
}
```

## Usage Examples

# URL Shortener API Commands

## For Mac/Linux

### Step 1: Shorten a URL
```bash
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258"}'
```

### Step 2: Follow redirect (browser or CLI)
```bash
curl -L http://localhost:5000/<short-code>
```
**NOTE:** Replace `<short-code>` with the actual code from Step 1 (e.g., `xyh635`)

### Step 3: Get click statistics
```bash
curl http://localhost:5000/api/stats/xyh635
```

---

## For Windows (Command Prompt)

### Step 1: Shorten a URL
```cmd
curl -X POST http://localhost:5000/api/shorten ^
  -H "Content-Type: application/json" ^
  -d "{\"url\":\"https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258\"}"
```

### Step 2: Follow redirect (browser or CLI)
```cmd
curl -L http://localhost:5000/<short-code>
```
**NOTE:** Replace `<short-code>` with the actual code from Step 1 (e.g., `xyh635`)

### Step 3: Get click statistics
```cmd
curl http://localhost:5000/api/stats/xyh635
```

---

## For Windows (PowerShell)

### Step 1: Shorten a URL
```powershell
curl -X POST http://localhost:5000/api/shorten `
  -H "Content-Type: application/json" `
  -d '{"url":"https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258"}'
```

### Step 2: Follow redirect (browser or CLI)
```powershell
curl -L http://localhost:5000/<short-code>
```
**NOTE:** Replace `<short-code>` with the actual code from Step 1 (e.g., `xyh635`)

### Step 3: Get click statistics
```powershell
curl http://localhost:5000/api/stats/xyh635
```

---

## Key Differences

- **Mac/Linux**: Uses backslash `\` for line continuation and single quotes for JSON
- **Windows CMD**: Uses caret `^` for line continuation and escaped double quotes `\"` for JSON
- **Windows PowerShell**: Uses backtick `` ` `` for line continuation and single quotes for JSON (similar to Mac/Linux)


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
