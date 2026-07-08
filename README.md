# senior-architect-agent

รุ่นปัจจุบัน: `v2.0.0 — Knowledge-Graph-Assisted Architecture Passes`

> Cognitive framework ที่เปลี่ยน AI agents ให้เป็น senior architects — evidence-first system understanding, honest uncertainty mapping, architecture debt and convention assessment, knowledge-graph-assisted dependency mapping, impact and blast radius analysis, และ architecture reasoning ก่อนลงมือ

**Skill นี้บังคับให้ agent inspect, map, assess, document, validate, และรายงานระบบที่มีอยู่จริง ก่อนเสนอการเปลี่ยนแปลงสถาปัตยกรรม — โดยเริ่มจาก smallest safe architecture pass (Scan Mode) และขยายเมื่อ scope, evidence, risk, หรือ handoff needs ต้องการ**

---

## เมื่อใดควรใช้

| ใช้ ✅ | ไม่ใช้ ❌ |
|:------|:----------|
| Agent ต้อง map existing codebase หรือระบบซอฟต์แวร์ | งานเป็นไอเดียดิบล้วนๆ ใช้ `idea-to-architecture-agent` แทน |
| ต้องการสแกนหา architecture debt, convention drift, boundary violations, flow conflicts | แค่ implementation fix เล็กๆ ที่ไม่มีผลต่อสถาปัตยกรรม |
| ทีมต้องการ module maps, Mermaid diagrams, handoff notes | Output จะกลายเป็น decorative documentation |
| review การเปลี่ยนแปลงสถาปัตยกรรมก่อน approve | |

---

## Core Flow

```txt
Intake → Inspect → Classify → Question → Map → Assess → Document → Validate → Report
```

เลือก smallest safe pass:
- **Scan Mode** — compact architecture note สำหรับงาน bounded หรือ exploratory
- **Focus Mode** — หนึ่ง module, workflow, หรือ boundary
- **Full Mode** — whole-system mapping, handoff, 3+ modules interacting, persistence, security, integrations

Pass จะเลื่อนขึ้นเมื่อ scope, evidence, risk, หรือ handoff requirements ต้องการ — ไม่ promote จาก speculation

---

## ภาพรวม

Skill นี้เป็นชั้นระเบียบวินัยทางความคิด:

1. Inspect ระบบจริงก่อน — ใช้ file search, git history, Mermaid checks, และ codebase graph queries (เมื่อมี MCP)
2. Map dependencies และ boundaries — optional knowledge-graph-assisted mapping: graph data ใช้เร่งการหา dependency chains, blast radius, และ circular dependencies โดย graph data แปลงเป็น evidence taxonomy เดิม (`Direct`/`Inferred`) และ file reading ชนะเมื่อ graph ขัดแย้ง
3. Assess ระบบ: ชี้ architecture debt, convention drift, boundary violations, flow conflicts — ทุก finding ต้องมี evidence, impact, severity, confidence, และ smallest safe correction
4. Validate ผ่าน 3 gates ก่อนรายงาน — claim traceability, scope alignment, handoff readiness
5. Output เป็น architecture overview, module map, data flow, workflow map, debt register, risk register, open questions, ai-agent notes, Mermaid diagrams

---

## สิ่งที่รวมในรุ่นนี้ (v2.0.0)

- ตัด Idea-to-Architecture Mode → route ไป sibling skill
- เพิ่ม Assess step พร้อม `rules/assessment-rules.md` และ `templates/debt-register.md`
- เพิ่ม optional knowledge-graph-assisted mapping และ assessment: graph cycles, fan-in outliers, layer violations — signal ป้อน dimension เดิม, ไม่ใช่ finding category ใหม่
- 7 rules files, 11 templates, example output

ดูรายละเอียดเพิ่มใน [CHANGELOG.md](CHANGELOG.md)

---

## ติดตั้ง

ดู [INSTALL.md](INSTALL.md) สำหรับ Codex, Claude Code, Antigravity, AGENTS.md, และ manual

```txt
aetox-skills/senior-architect-agent
```

---

## โครงสร้างไฟล์

```
senior-architect-agent/
├── README.md / SKILL.md / INSTALL.md / CHANGELOG.md / LICENSE
├── assets/visuals/         # infographic, workflow GIF, Mermaid source
├── scripts/                # build tooling
├── agents/                 # interface metadata (openai.yaml)
├── adapters/               # AGENTS.example.md
├── docs/                   # philosophy, workflow, anti-patterns, model requirements
├── rules/                  # 7 rule files
├── templates/              # 11 output templates
└── examples/               # example output
```

---

## คำแนะนำโมเดล

ต้องการ long context (128K+ ปกติ, 200K+ สำหรับ multi-service) และ instruction following ที่แข็งแรง 32K ก็พอสำหรับ Scan Mode เล็กๆ

ดู [Model Requirements](docs/model-requirements.md)

---

## License

MIT
