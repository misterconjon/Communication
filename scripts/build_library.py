#!/usr/bin/env python3
"""Merge all source files into artifact/library.json, the data layer for the interactive library.

Inputs:
  data/stage1/*.json              core book deep-dives
  data/stage3/extracted/*.json    expansion sources (books and papers)
  data/additions/*.json           new sources you add later (same schema)
  data/learning-path.json         narrative arc (Stage 2)
  data/situations.json            situation playbooks (optional)
Output:
  artifact/library.json

Run: python3 scripts/build_library.py
"""
import json, glob, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TAXONOMY = [
    ("foundations", "Foundations", [("mindset","Communication mindset"),("audience-goals","Audience and goals"),("anxiety","Managing speaking anxiety"),("spontaneous-speaking","Spontaneous speaking"),("message-structures","Core message structures")]),
    ("relationships", "Relationships and connection", [("rapport","Rapport"),("trust-vulnerability","Trust and vulnerability"),("listening","Active and reflective listening"),("question-design","Question design"),("empathy","Empathy"),("nonverbal","Reading nonverbal cues"),("networking","Networking")]),
    ("personal-life", "Personal life", [("partners","Partners"),("family","Family"),("friendships","Maintaining friendships"),("supporting-distress","Supporting someone in distress"),("repair","Repairing relationships")]),
    ("conversations", "Conversations and socializing", [("small-talk","Small talk"),("storytelling","Storytelling"),("humor","Humor"),("group-dynamics","Group dynamics"),("introductions","Introductions")]),
    ("professional", "Professional communication", [("meetings","Meetings"),("status-updates","Status updates"),("executive-communication","Executive communication"),("managing-up","Managing up"),("negotiation","Negotiation")]),
    ("written-digital", "Written and digital communication", [("email","Email"),("chat","Slack and chat"),("proposals-memos","Proposals and memos"),("executive-writing","Executive writing"),("clarity-structure","Clarity and structure"),("video-calls","Video calls"),("async","Asynchronous communication"),("tone-misreading","Tone and misreading")]),
    ("influence", "Influence and persuasion", [("framing","Framing"),("credibility","Credibility"),("persuasive-structure","Persuasive structure"),("memorable-messages","Memorable messages"),("overcoming-resistance","Overcoming resistance"),("reciprocity","Reciprocity")]),
    ("difficult", "Difficult conversations", [("conflict","Conflict"),("bad-news","Delivering bad news"),("giving-feedback","Giving feedback"),("receiving-feedback","Receiving feedback"),("saying-no","Saying no"),("apologies","Apologies"),("boundaries","Boundary-setting")]),
    ("public-speaking", "Public speaking and presence", [("structure","Structure"),("delivery","Delivery"),("qa","Handling Q&A"),("impromptu","Impromptu moments"),("virtual","Virtual presentations")]),
]
SITUATIONS = ("situations", "Situations in practice")
VALID = {c: {s for s, _ in subs} | {SITUATIONS[0]} for c, _, subs in TAXONOMY}
SKILL_TYPES = {"mental model", "technique", "framework"}
CONFIDENCE = {"High", "Medium", "Low"}
DASHES = re.compile("[–—]")

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def main():
    errors, warnings = [], []
    files = sorted(glob.glob(os.path.join(ROOT, "data/stage1/*.json")))
    files += sorted(glob.glob(os.path.join(ROOT, "data/stage3/extracted/*.json")))
    files += sorted(glob.glob(os.path.join(ROOT, "data/additions/*.json")))
    sources, insights, supports = [], {}, []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        raw = open(path, encoding="utf-8").read()
        if DASHES.search(raw):
            errors.append(f"{rel}: contains an em or en dash")
        d = json.loads(raw)
        b = d["book"]
        sid = b.get("book_id") or os.path.splitext(os.path.basename(path))[0]
        core = b.get("core", "/stage1/" in path)
        sources.append({
            "source_id": sid, "title": b.get("title", ""), "subtitle": b.get("subtitle", ""),
            "authors": b.get("authors", []), "year": b.get("year"), "publisher": b.get("publisher", ""),
            "edition": b.get("edition", ""), "isbn": b.get("isbn", ""),
            "source_type": b.get("source_type", "book"), "core": bool(core),
            "author_credibility": b.get("author_credibility", ""), "evidence_base": b.get("evidence_base", ""),
            "legal_access": b.get("legal_access", []),
        })
        for i in d.get("insights", []):
            iid = i.get("id")
            if not iid:
                errors.append(f"{rel}: insight without id"); continue
            if iid in insights:
                errors.append(f"{rel}: duplicate id {iid}"); continue
            for k in ("name", "explanation", "when_to_use", "worked_example", "confidence", "categories"):
                if not i.get(k):
                    errors.append(f"{iid}: missing {k}")
            if i.get("confidence") not in CONFIDENCE:
                errors.append(f"{iid}: confidence must be High, Medium or Low")
            if i.get("skill_type") not in SKILL_TYPES:
                errors.append(f"{iid}: skill_type must be one of {sorted(SKILL_TYPES)}")
            for c in i.get("categories", []):
                if c.get("category") not in VALID or c.get("subcategory") not in VALID.get(c.get("category"), set()):
                    errors.append(f"{iid}: unknown category {c}")
            insights[iid] = {
                "id": iid, "source_id": sid, "name": i.get("name", ""), "takeaway": i.get("takeaway", ""), "skill_type": i.get("skill_type", ""),
                "explanation": i.get("explanation", ""), "when_to_use": i.get("when_to_use", ""),
                "worked_example": i.get("worked_example", ""), "common_mistakes": i.get("common_mistakes", []),
                "steps": [s for s in i.get("steps", []) if s], "categories": i.get("categories", []),
                "situations": i.get("situations", []), "source": i.get("source", {}),
                "confidence": i.get("confidence", ""), "confidence_rationale": i.get("confidence_rationale", ""),
                "flags": [f for f in i.get("flags", []) if f and f != "none"], "supporting_evidence": [],
            }
        for s in d.get("supports_existing", []):
            supports.append((sid, s, rel))
    for sid, s, rel in supports:
        target = insights.get(s.get("insight_id"))
        if not target:
            warnings.append(f"{rel}: supports_existing points to unknown id {s.get('insight_id')}"); continue
        target["supporting_evidence"].append({"source_id": sid, "relation": s.get("relation", "supports"), "note": s.get("note", "")})
    lp = load(os.path.join(ROOT, "data/learning-path.json"))
    for st in lp.get("stages", []):
        missing = [x for x in st.get("insight_ids", []) if x not in insights]
        if missing:
            warnings.append(f"learning path {st.get('id')}: unknown ids {missing}")
        st["insight_ids"] = [x for x in st.get("insight_ids", []) if x in insights]
    situations = []
    sp = os.path.join(ROOT, "data/situations.json")
    if os.path.exists(sp):
        raw = open(sp, encoding="utf-8").read()
        if DASHES.search(raw):
            errors.append("data/situations.json: contains an em or en dash")
        for st in json.loads(raw).get("situations", []):
            used = set(st.get("insight_ids", [])) | {x for step in st.get("approach", []) for x in step.get("insight_ids", [])}
            bad = sorted(x for x in used if x not in insights)
            if bad:
                errors.append(f"situation {st.get('id')}: unknown insight ids {bad}")
            if st.get("category") not in VALID:
                errors.append(f"situation {st.get('id')}: unknown category {st.get('category')}")
            situations.append(st)
    takeaways = {}
    tp = os.path.join(ROOT, "data/takeaways.json")
    if os.path.exists(tp):
        raw = open(tp, encoding="utf-8").read()
        if DASHES.search(raw):
            errors.append("data/takeaways.json: contains an em or en dash")
        takeaways = json.loads(raw)
    for iid, ins in insights.items():
        t = ins.get("takeaway") or takeaways.get(iid)
        if t:
            ins["takeaway"] = t
        else:
            warnings.append(f"{iid}: no takeaway (add one in the insight or data/takeaways.json)")
    lib = {
        "schema_version": 1,
        "generated": datetime.date.today().isoformat(),
        "taxonomy": [{"id": c, "name": n, "subcategories": [{"id": s, "name": sn} for s, sn in subs] + [{"id": SITUATIONS[0], "name": SITUATIONS[1]}]} for c, n, subs in TAXONOMY],
        "sources": sources,
        "insights": list(insights.values()),
        "situations": situations,
        "learning_path": {"stages": lp.get("stages", [])},
        "convergent_concepts": lp.get("convergent_concepts", []),
        "related_insights": lp.get("related_insights", []),
    }
    for w in warnings: print("WARNING:", w)
    for e in errors: print("ERROR:", e)
    if errors:
        print(f"{len(errors)} error(s); library.json not written."); sys.exit(1)
    out = os.path.join(ROOT, "artifact/library.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(lib, f, ensure_ascii=False, indent=1)
    print(f"Wrote {os.path.relpath(out, ROOT)}: {len(sources)} sources, {len(insights)} insights, {len(supports)} supporting links, {len(situations)} situations")

if __name__ == "__main__":
    main()
