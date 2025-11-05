 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/weather_app/models.py b/weather_app/models.py
new file mode 100644
index 0000000000000000000000000000000000000000..ddc3d8703281cd87a8b6646dd96b84777068c5f7
--- /dev/null
+++ b/weather_app/models.py
@@ -0,0 +1,45 @@
+"""Data models for the weather application."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Iterable, List
+
+
+@dataclass
+class DailyForecast:
+    """Represents a daily weather forecast for a location."""
+
+    day: str
+    condition: str
+    high: int
+    low: int
+    precipitation_chance: int
+
+    def describe(self) -> str:
+        """Return a human readable description of the forecast."""
+
+        precip = f"{self.precipitation_chance}% chance of precipitation"
+        temps = f"high of {self.high}\N{DEGREE SIGN}F and low of {self.low}\N{DEGREE SIGN}F"
+        return f"{self.day}: {self.condition} with a {temps} ({precip})."
+
+
+@dataclass
+class LocationForecast:
+    """Represents the forecast for a particular location."""
+
+    city: str
+    state: str
+    latitude: float
+    longitude: float
+    forecast: List[DailyForecast]
+
+    @property
+    def full_name(self) -> str:
+        return f"{self.city}, {self.state}"
+
+    def describe(self) -> Iterable[str]:
+        yield f"Weather outlook for {self.full_name}"
+        yield f"Coordinates: {self.latitude:.4f}, {self.longitude:.4f}"
+        for entry in self.forecast:
+            yield entry.describe()
 
EOF
)
