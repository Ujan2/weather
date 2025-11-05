 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/weather_app/cli.py b/weather_app/cli.py
new file mode 100644
index 0000000000000000000000000000000000000000..47a4bc9091327d031ad215220b3ab0abc3f79a2e
--- /dev/null
+++ b/weather_app/cli.py
@@ -0,0 +1,86 @@
+"""Command line interface for the weather app."""
+
+from __future__ import annotations
+
+import argparse
+from pathlib import Path
+from typing import Iterable
+
+from .data import WeatherDatabase
+from .models import LocationForecast
+
+
+def build_parser() -> argparse.ArgumentParser:
+    parser = argparse.ArgumentParser(
+        prog="weather",
+        description="Explore a small catalog of US city weather forecasts.",
+    )
+    parser.add_argument(
+        "--data",
+        type=Path,
+        default=Path(__file__).resolve().parent.parent / "data" / "forecasts.json",
+        help="Path to the JSON file that stores the weather forecasts.",
+    )
+
+    subparsers = parser.add_subparsers(dest="command", required=True)
+
+    subparsers.add_parser("list", help="List all cities that have available forecasts.")
+
+    show_parser = subparsers.add_parser("show", help="Display the forecast for a city.")
+    show_parser.add_argument("query", help="Name of the city, e.g. 'San Francisco'.")
+
+    search_parser = subparsers.add_parser(
+        "search", help="Search for a city by partial name and show its forecast."
+    )
+    search_parser.add_argument("query", help="Text to search for in the city name.")
+
+    return parser
+
+
+def format_locations(locations: Iterable[LocationForecast]) -> str:
+    rows = ["City", "State", "Latitude", "Longitude"]
+    lines = [" | ".join(rows), "-" * 52]
+    for entry in locations:
+        lines.append(
+            f"{entry.city:<18} | {entry.state:<5} | {entry.latitude:>8.4f} | {entry.longitude:>9.4f}"
+        )
+    return "\n".join(lines)
+
+
+def format_forecast(forecast: LocationForecast) -> str:
+    lines = list(forecast.describe())
+    separator = "\n" + "=" * 60 + "\n"
+    return separator.join(lines)
+
+
+def list_locations(db: WeatherDatabase) -> str:
+    if not list(db.locations):
+        return "No locations found in the database."
+    return format_locations(db.locations)
+
+
+def show_location(db: WeatherDatabase, query: str) -> str:
+    location = db.find(query)
+    if not location:
+        return f"No forecast available for '{query}'."
+    return format_forecast(location)
+
+
+def main(argv: list[str] | None = None) -> int:
+    parser = build_parser()
+    args = parser.parse_args(argv)
+
+    db = WeatherDatabase(args.data)
+    db.load()
+
+    if args.command == "list":
+        print(list_locations(db))
+    elif args.command in {"show", "search"}:
+        print(show_location(db, args.query))
+    else:
+        parser.error(f"Unknown command: {args.command}")
+    return 0
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
 
EOF
)
