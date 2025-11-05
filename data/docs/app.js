 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/docs/app.js b/docs/app.js
new file mode 100644
index 0000000000000000000000000000000000000000..89d1270232253a8c09efd4b9d5b9bd322190edc8
--- /dev/null
+++ b/docs/app.js
@@ -0,0 +1,95 @@
+const searchInput = document.querySelector('#search');
+const resultCount = document.querySelector('#result-count');
+const totalCount = document.querySelector('#total-count');
+const resultsContainer = document.querySelector('#results');
+const cityTemplate = document.querySelector('#city-template');
+
+let cities = [];
+
+const formatTemperature = (value) => `${value}\u00b0F`;
+const formatPrecipitation = (value) => `${value}% chance of precipitation`;
+
+async function loadCities() {
+  try {
+    const response = await fetch('forecasts.json');
+    if (!response.ok) {
+      throw new Error(`Failed to load dataset: ${response.status} ${response.statusText}`);
+    }
+
+    cities = await response.json();
+    totalCount.textContent = cities.length;
+    render(cities);
+  } catch (error) {
+    console.error(error);
+    resultsContainer.innerHTML = `<p class="error">${error.message}</p>`;
+  }
+}
+
+function render(collection) {
+  resultsContainer.innerHTML = '';
+  resultCount.textContent = collection.length;
+
+  const fragment = document.createDocumentFragment();
+
+  collection.forEach((city) => {
+    const node = cityTemplate.content.cloneNode(true);
+    const title = node.querySelector('.city-card__title');
+    const subtitle = node.querySelector('.city-card__subtitle');
+    const latitude = node.querySelector('.city-card__latitude');
+    const longitude = node.querySelector('.city-card__longitude');
+    const forecastList = node.querySelector('.city-card__forecast');
+
+    title.textContent = city.city;
+    subtitle.textContent = `${city.state} · ${city.forecast.length}-day forecast`;
+    latitude.textContent = `${city.latitude.toFixed(4)}°`;
+    longitude.textContent = `${city.longitude.toFixed(4)}°`;
+
+    city.forecast.forEach((entry) => {
+      const listItem = document.createElement('li');
+      listItem.className = 'forecast-day';
+      listItem.innerHTML = `
+        <span class="forecast-day__heading">${entry.day}</span>
+        <span>${entry.condition}</span>
+        <span>High: ${formatTemperature(entry.high)}</span>
+        <span>Low: ${formatTemperature(entry.low)}</span>
+        <span>${formatPrecipitation(entry.precipitation_chance)}</span>
+      `;
+      forecastList.appendChild(listItem);
+    });
+
+    fragment.appendChild(node);
+  });
+
+  if (!collection.length) {
+    const emptyState = document.createElement('p');
+    emptyState.className = 'empty-state';
+    emptyState.textContent = 'No cities match the current search.';
+    resultsContainer.appendChild(emptyState);
+    return;
+  }
+
+  resultsContainer.appendChild(fragment);
+}
+
+function filterCities(query) {
+  const normalized = query.trim().toLowerCase();
+  if (!normalized) {
+    render(cities);
+    return;
+  }
+
+  const filtered = cities.filter((city) => {
+    return (
+      city.city.toLowerCase().includes(normalized) ||
+      city.state.toLowerCase().includes(normalized)
+    );
+  });
+
+  render(filtered);
+}
+
+searchInput.addEventListener('input', (event) => {
+  filterCities(event.target.value);
+});
+
+loadCities();
 
EOF
)
