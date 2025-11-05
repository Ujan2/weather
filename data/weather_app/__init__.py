 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/weather_app/__init__.py b/weather_app/__init__.py
new file mode 100644
index 0000000000000000000000000000000000000000..f7e998abe21a4ba3be3f15315435e26d34ddb26a
--- /dev/null
+++ b/weather_app/__init__.py
@@ -0,0 +1,5 @@
+"""Weather app package."""
+
+from .cli import main
+
+__all__ = ["main"]
 
EOF
)
