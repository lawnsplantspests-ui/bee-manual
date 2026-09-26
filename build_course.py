# Builds course.json — the full text of the course library, one entry per PDF page, so the
# app's search box can search the whole Cornell course offline.
#
# Run after build_library.py (it reads library.json):  python build_course.py
# Then bump CACHE in sw.js and push.
#
# Skips the two combined "full course" PDFs — they repeat the four module transcripts word
# for word, and indexing them would double every hit. Also skips exact duplicate files and
# image-only pages (no extractable text).
import json, re, subprocess, hashlib, io

SKIP_TITLES = {"Clean Course Content", "Complete Course Transcript"}
FOOTER = re.compile(r"©\s*\d{4}\s*Cornell University", re.I)

lib = json.load(open("library.json", encoding="utf-8"))
files, pages, seen = [], [], set()
for group in lib:
    mod = group["mod"].replace("Â·", "·")   # library.json carries a double-encoded middle dot
    for f in group["files"]:
        if not f["url"].lower().endswith(".pdf") or f["title"] in SKIP_TITLES:
            continue
        raw = subprocess.run(["pdftotext", "-enc", "UTF-8", f["url"], "-"],
                             capture_output=True).stdout.decode("utf-8", "replace")
        digest = hashlib.md5(raw.encode()).hexdigest()
        if digest in seen or not raw.strip():
            continue
        seen.add(digest)
        fi = len(files)
        files.append({"t": f["title"], "m": mod, "u": f["url"]})
        for n, text in enumerate(raw.split("\f"), 1):
            text = FOOTER.sub(" ", text)
            text = re.sub(r"-\n(?=[a-z])", "", text)        # re-join words hyphenated across lines
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) >= 40:
                pages.append([fi, n, text])

out = json.dumps({"files": files, "pages": pages}, ensure_ascii=False, separators=(",", ":"))
io.open("course.json", "w", encoding="utf-8", newline="\n").write(out)
print(f"course.json: {len(out)//1024} KB | {len(files)} files | {len(pages)} pages")
