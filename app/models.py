# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata

from datetime import datetime

# In-memory "database"
url_mappings = {}
click_counts = {}

class URLMapping:
    def __init__(self, original_url, short_code):
        self.original_url = original_url
        self.short_code = short_code
        self.created_at = datetime.now()