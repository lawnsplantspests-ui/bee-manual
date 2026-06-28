# Copies all course PDFs (+ treatment GIF) into bee-manual/library/ with URL-safe
# names, grouped into modules, and writes library.json for the app.
import os, re, shutil, json

SRC = r"C:\Users\leasy\Desktop\Cornell Master Beekeeping"
DST = r"C:\Users\leasy\bee-manual\library"
BASE = "library/"   # relative; the app resolves against its own host

def safe(name):
    stem, ext = os.path.splitext(name)
    stem = re.sub(r'[+_]+', '-', stem)
    stem = re.sub(r'[^A-Za-z0-9()\-. ]', '', stem)
    stem = re.sub(r'\s+', '-', stem).strip('-')
    stem = re.sub(r'-+', '-', stem)
    return (stem + ext.lower())[:90]

def title(name):
    t = os.path.splitext(name)[0]
    t = re.sub(r'^ptrent00\d[_-]?', '', t, flags=re.I)
    t = re.sub(r'[+_]+', ' ', t)
    t = re.sub(r'\s*\(\d+\)$', '', t)        # drop "(1)" dup markers
    t = re.sub(r'[-]{1,}', ' ', t) if t.count('-') > 2 else t.replace('-', ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    t = t[:1].upper() + t[1:]
    fixes = {
        'Course transcript':'Course transcript', 'Course project':'Course project',
        'V2':'', 'V3':'', '2022':'', '2020':'', '2014':'',
    }
    return t

# Module folder -> nice label
FOLDER_LABEL = {
    "Honey Bee Evolution, Biology, and Behavior 1": "1 · Evolution, Biology & Behavior",
    "The Science and Art of Beekeeping 2":          "2 · The Science & Art of Beekeeping",
    "Managing Pests and Diseases 3":                "3 · Managing Pests & Diseases",
    "Rewards and Contributions of Beekeeping 4":    "4 · Rewards & Contributions",
}
# Top-level file -> (bucket, nice title). Anything unlisted falls into "More resources".
TOP = {
    "HIVE INSPECTION GUIDE (R2).pdf":               ("Quick Reference (field)", "Hive Inspection Guide"),
    "Varroa treatment guide.pdf":                   ("Quick Reference (field)", "Varroa Treatment Guide"),
    "Honey Bee Diseases and Pests Chart.pdf":       ("Quick Reference (field)", "Diseases & Pests Chart"),
    "Honey+Bee+Disease+Symptom+Chart.pdf":          ("Quick Reference (field)", "Disease Symptom Chart"),
    "Beekeeping_Calendar_for_the_Northeast.pdf":    ("Quick Reference (field)", "Beekeeping Calendar (Northeast)"),
    "Example+Varroa+control+calendars.pdf":         ("Quick Reference (field)", "Varroa Control Calendars"),
    "illustration-of-treatment-hierarchy_V2.gif":   ("Quick Reference (field)", "Treatment Hierarchy diagram"),
    "Reputable_Varroa_Resistant_Bee_Breeders_US.pdf":("Quick Reference (field)", "Varroa-Resistant Bee Breeders (US)"),
    "Tropi-STOP-ID.pdf":                            ("Quick Reference (field)", "Tropilaelaps Mite ID"),
    "CORNELL MBK FULL SYLLABUS.pdf":                ("Exam prep", "Full Syllabus"),
    "ORAL TOPIC LIST.pdf":                          ("Exam prep", "Oral Topic List"),
    "Oral Exam Rubric.pdf":                         ("Exam prep", "Oral Exam Rubric"),
    "Virtual Field Exam Part 1 Rubric.pdf":         ("Exam prep", "Field Exam Part 1 Rubric"),
    "CORNELL MBK  - FINAL EXAM VIDEO OUTLINE.pdf":  ("Exam prep", "Final Exam Video Outline"),
    "Master_Beekeeping_Complete_Transcript.pdf":    ("Full course text & summaries", "Complete Course Transcript"),
    "COLONY DRIFT (FINAL).pdf":                     ("More resources", "Colony Drift (research)"),
    "FromhoneybeestoInternetserversNakrani.pdf":    ("More resources", "From Honey Bees to Internet Servers"),
}
# Claude-folder summaries
CLAUDE = {
    "Master_Beekeeping_Clean_Content.pdf": ("Full course text & summaries", "Clean Course Content"),
    "Master_Beekeeping_Key_Points.pdf":    ("Full course text & summaries", "Key Points Summary"),
}

ORDER = ["Quick Reference (field)",
         "1 · Evolution, Biology & Behavior",
         "2 · The Science & Art of Beekeeping",
         "3 · Managing Pests & Diseases",
         "4 · Rewards & Contributions",
         "Full course text & summaries", "Exam prep", "More resources"]

buckets = {}   # label -> list of (title, relpath, size)
def add(label, ttl, srcpath, sub):
    os.makedirs(os.path.join(DST, sub), exist_ok=True)
    fn = safe(os.path.basename(srcpath))
    dstpath = os.path.join(DST, sub, fn)
    shutil.copy2(srcpath, dstpath)
    rel = BASE + sub + "/" + fn
    buckets.setdefault(label, []).append({"title": ttl, "url": rel, "kb": os.path.getsize(srcpath)//1024})

if os.path.isdir(DST): shutil.rmtree(DST)
os.makedirs(DST, exist_ok=True)

# top-level files
for f in os.listdir(SRC):
    p = os.path.join(SRC, f)
    if not os.path.isfile(p): continue
    if not f.lower().endswith(('.pdf', '.gif')): continue
    if f in TOP:
        label, ttl = TOP[f]
    else:
        label, ttl = "More resources", title(f)
    add(label, ttl, p, "misc")

# module subfolders
for folder, label in FOLDER_LABEL.items():
    fp = os.path.join(SRC, folder)
    if not os.path.isdir(fp): continue
    sub = re.sub(r'[^0-9]', '', folder) or label[:1]
    sub = "module" + (re.findall(r'\d', folder) or ['x'])[-1]
    for f in sorted(os.listdir(fp)):
        if f.lower().endswith('.pdf'):
            add(label, title(f), os.path.join(fp, f), sub)

# Claude summaries
cdir = os.path.join(SRC, "Claude")
for f, (label, ttl) in CLAUDE.items():
    p = os.path.join(cdir, f)
    if os.path.isfile(p): add(label, ttl, p, "summaries")

# order + emit
LIB = []
for label in ORDER:
    if label in buckets:
        files = sorted(buckets[label], key=lambda x: x["title"].lower())
        LIB.append({"mod": label, "files": files})
for label in buckets:               # any leftover labels
    if label not in ORDER:
        LIB.append({"mod": label, "files": sorted(buckets[label], key=lambda x: x["title"].lower())})

json.dump(LIB, open(r"C:\Users\leasy\bee-manual\library.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
total = sum(f["kb"] for b in LIB for f in b["files"])
print("Buckets:", len(LIB), "| files:", sum(len(b["files"]) for b in LIB), "| total:", total//1024, "MB")
for b in LIB: print(f"  {b['mod']}: {len(b['files'])}")
