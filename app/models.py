from datetime import datetime
from threading import Lock

# Shared resources with locks
url_mappings = {}
click_counts = {}
url_lock = Lock()  # For URL creation
click_lock = Lock()  # For click tracking

class URLMapping:
    def __init__(self, original_url, short_code):
        self.original_url = original_url
        self.short_code = short_code
        self.created_at = datetime.now()