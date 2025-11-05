 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/weather_app/data.py b/weather_app/data.py
new file mode 100644
index 0000000000000000000000000000000000000000..70f95fe88ce0d361b5185b08445e564a621153ef
--- /dev/null
+++ b/weather_app/data.py
@@ -0,0 +1,54 @@
+"""Utilities for loading and querying weather data."""
+
+from __future__ import annotations
+
+import json
+from pathlib import Path
+from typing import Iterable, List, Optional
+
+from .models import DailyForecast, LocationForecast
+
+
+class WeatherDatabase:
+    """Loads and serves forecasts from a JSON data file."""
+
+    def __init__(self, source: Path) -> None:
+        self._source = source
+        self._forecasts: List[LocationForecast] = []
+
+    def load(self) -> None:
+        if not self._source.exists():
+            raise FileNotFoundError(f"Weather data file not found: {self._source}")
+
+        raw = json.loads(self._source.read_text())
+        self._forecasts = [self._parse_location(entry) for entry in raw]
+
+    def _parse_location(self, entry: dict) -> LocationForecast:
+        forecast = [self._parse_forecast(item) for item in entry.get("forecast", [])]
+        return LocationForecast(
+            city=entry["city"],
+            state=entry["state"],
+            latitude=entry["latitude"],
+            longitude=entry["longitude"],
+            forecast=forecast,
+        )
+
+    def _parse_forecast(self, entry: dict) -> DailyForecast:
+        return DailyForecast(
+            day=entry["day"],
+            condition=entry["condition"],
+            high=entry["high"],
+            low=entry["low"],
+            precipitation_chance=entry["precipitation_chance"],
+        )
+
+    @property
+    def locations(self) -> Iterable[LocationForecast]:
+        return tuple(self._forecasts)
+
+    def find(self, query: str) -> Optional[LocationForecast]:
+        query_lower = query.lower()
+        for entry in self._forecasts:
+            if query_lower in entry.city.lower() or query_lower == entry.full_name.lower():
+                return entry
+        return None
 
EOF
)
