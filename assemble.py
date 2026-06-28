# Injects data.json into the app template to produce the self-contained index.html.
# Run after build_data.py. Keeps index.html offline-capable (data baked in).
data = open("data.json", encoding="utf-8").read()
html = open("index.html", encoding="utf-8").read()

START = "window.DATA = "
i = html.index(START) + len(START)
j = html.index(";\n", i)
html = html[:i] + data + html[j:]
open("index.html", "w", encoding="utf-8").write(html)
print("index.html rebuilt with fresh data.json")
