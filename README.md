 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 6a453aef951fd12cfc80f210a0ec14c56ec4bbf8..9b5e9c256148b7e368f4b2ec756c0bcd505e8a37 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,97 @@
-# weather
\ No newline at end of file
+# Weather App
+
+This repository contains a small weather project with both a command-line
+utility and a static website. Everything runs on top of a bundled JSON dataset
+and does not rely on external APIs, so you can use it entirely offline.
+
+## Features
+
+- Responsive static website under `docs/` that you can publish directly to GitHub Pages.
+- Browse a curated list of US cities with forecast information.
+- Display a formatted multi-day forecast for a specific city (CLI and web).
+- Perform partial searches to quickly find a location.
+
+## Getting Started
+
+1. Ensure you have Python 3.9 or newer installed.
+2. Clone the repository and navigate to the project directory.
+3. Run one of the commands below.
+
+### List available cities
+
+```bash
+python -m weather_app list
+```
+
+### Show the forecast for a city
+
+```bash
+python -m weather_app show "San Francisco"
+```
+
+### Search for a city by partial name
+
+```bash
+python -m weather_app search York
+```
+
+### Use a custom data file
+
+If you would like to use your own data, pass the path to the JSON file:
+
+```bash
+python -m weather_app --data path/to/custom.json show "My City"
+```
+
+## Data format
+
+The application expects a JSON file with the following structure:
+
+```json
+[
+  {
+    "city": "Example City",
+    "state": "EX",
+    "latitude": 12.3456,
+    "longitude": -65.4321,
+    "forecast": [
+      {
+        "day": "Monday",
+        "condition": "Sunny",
+        "high": 75,
+        "low": 60,
+        "precipitation_chance": 5
+      }
+    ]
+  }
+]
+```
+
+## Static website (GitHub Pages ready)
+
+The `docs/` directory contains a self-contained HTML/CSS/JavaScript site. GitHub
+Pages will automatically serve this folder when you enable Pages in your
+repository settings.
+
+### Preview locally
+
+```bash
+python -m http.server --directory docs 8000
+```
+
+Then open <http://localhost:8000> in your browser.
+
+### Deploy manually
+
+1. Commit the project to your own GitHub repository.
+2. Push to the `main` branch (or the branch you configured for Pages).
+3. In the repository settings, enable **GitHub Pages** and choose the `docs/`
+   folder as the source.
+
+GitHub will build and publish the static site automatically—no additional build
+steps are required.
+
+## Development
+
+No external dependencies are required for the CLI or the static site. Unit
+tests can be added under a `tests/` directory if you extend the project further.
 
EOF
)
