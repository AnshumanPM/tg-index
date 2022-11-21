from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = int(os.getenv("PORT", "8080"))
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = os.getenv("INDEX_SETTINGS").strip()
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.getenv("SESSION_STRING")
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.getenv("HOST", "0.0.0.0")
debug = bool(os.getenv("DEBUG"))
block_downloads = bool(os.getenv("BLOCK_DOWNLOADS"))
results_per_page = int(os.getenv("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.getenv("TGINDEX_USERNAME", "")
password = os.getenv("PASSWORD", "")
file_icon_path = "app/icons/document-icon.png"
SHORT_URL_LEN = int(os.getenv("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.getenv("SESSION_COOKIE_LIFETIME") or "60")
SECRET_KEY = os.getenv("SECRET_KEY")
