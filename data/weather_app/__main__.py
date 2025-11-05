 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/weather_app/__main__.py b/weather_app/__main__.py
new file mode 100644
index 0000000000000000000000000000000000000000..bfdcd0c1158dff4fcc25157b317419f0a89dd33f
--- /dev/null
+++ b/weather_app/__main__.py
@@ -0,0 +1,4 @@
+from .cli import main
+
+if __name__ == "__main__":
+    raise SystemExit(main())
 
EOF
)
