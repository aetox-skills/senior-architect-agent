# senior-architect-agent

รุ่นปัจจุบัน: `v2.0.0 — Knowledge-Graph-Assisted Architecture Passes`

> Cognitive framework ที่เปลี่ยน AI agents ให้เป็น senior architects — evidence-first system understanding, honest uncertainty mapping, architecture debt and convention assessment, knowledge-graph-assisted dependency mapping, impact and blast radius analysis, และ architecture reasoning ก่อนลงมือ

Skill นี้บังคับให้ agent inspect, map, assess, document, validate, และรายงานระบบที่มีอยู่จริง ก่อนเสนอการเปลี่ยนแปลงสถาปัตยกรรม โดยเริ่มจาก smallest safe architecture pass เสมอ

---

## Core Flow

```txt
Intake → Inspect → Classify → Question → Map → Assess → Document → Validate → Report
```

เลือก smallest safe pass:

| Mode | เมื่อไหร่ | Output |
|:-----|:----------|:-------|
| **Scan** | งาน bounded, exploratory, low-risk | 1 compact architecture note |
| **Focus** | 1 module, workflow, หรือ boundary ที่ชัดเจน | 1-3 artifacts |
| **Full** | Whole-system, handoff, 3+ modules interacting, persistence, security, integrations | Full output package |

เริ่มที่ Scan เสมอ — เลื่อนขึ้นเมื่อ scope, evidence, risk, หรือ handoff needs ต้องการ โดยต้องมี trigger + evidence + risk statement

---

<p align="center">
  <a href="assets/visuals/from_powerful_models_to_elite_architects.png">
    <img src="assets/visuals/from_powerful_models_to_elite_architects.png" alt="From powerful models to elite senior architect infographic" width="980">
  </a>
  <br>
  <strong>From powerful models to elite senior architects</strong>: skill เพิ่มชั้น cognitive framework รอบโมเดลที่มีความสามารถ
</p>

<p align="center">
  <a href="assets/visuals/senior_architect_agent_workflow_infographic.png">
    <img src="assets/visuals/senior_architect_agent_workflow_infographic.png" alt="Senior Architect Agent workflow infographic" width="980">
  </a>
  <br>
  <strong>Full workflow infographic</strong>: core flow, mode selection, evidence gates, repository anatomy, และ expected outputs
</p>

<p align="center">
  <a href="assets/visuals/senior_architect_agent_core_flow.gif">
    <img src="assets/visuals/senior_architect_agent_core_flow.gif" alt="Senior Architect Agent animated core flow" width="920">
  </a>
  <br>
  <strong>Core flow animation</strong>: inspect → classify → question → map → assess → document → validate → report
</p>

---

## ใช้เมื่อ

| ใช้ ✅ | ไม่ใช้ ❌ |
|:------|:----------|
| Agent ต้อง map existing codebase หรือระบบซอฟต์แวร์ | งานเป็นไอเดียดิบล้วนๆ — ใช้ `$idea-to-architecture-agent` แทน |
| ต้องการหา architecture debt, convention drift, boundary violations, flow conflicts | แค่ implementation fix เล็กๆ ที่ไม่มีผลต่อสถาปัตยกรรม |
| ทีมต้องการ module maps, Mermaid diagrams, handoff notes | Output จะกลายเป็น decorative documentation |
| review การเปลี่ยนแปลงสถาปัตยกรรมก่อน approve | |

---

## สิ่งที่ skill นี้ทำ

1. **Inspect** ระบบจริงก่อน — file search, git history, Mermaid checks, และ codebase graph queries (เมื่อมี MCP)
2. **Map** dependencies และ boundaries — optional knowledge-graph-assisted: graph data เร่งหา dependency chains, blast radius, circular dependencies โดย map เข้า evidence taxonomy เดิม (`Direct`/`Inferred`) — file reading ชนะเมื่อ graph ขัดแย้ง
3. **Assess** — ชี้ debt, drift, boundary violations, flow conflicts ทุก finding ต้องมี evidence, impact, severity, confidence, smallest safe correction
4. **Validate** — 3 gates: claim traceability, scope alignment, handoff readiness
5. **Output** — architecture overview, module map, data flow, workflow map, debt register, risk register, open questions, ai-agent notes, Mermaid diagrams

---

## การเลือกใช้ Skill ที่เกี่ยวข้อง

| Skill | ใช้เมื่อ |
|:------|:--------|
| `senior-architect-agent` **(นี้)** | ระบบที่มีอยู่, existing + proposed changes, architecture review, handoff |
| `$idea-to-architecture-agent` | ไอเดียดิบ, product concept, feature request, เป้าหมายธุรกิจที่ยังไม่มี implementation |

---

## สิ่งที่รวมในรุ่นนี้ (v2.0.0)

- **ตัด Idea-to-Architecture Mode** → route ไป `$idea-to-architecture-agent`
- **เพิ่ม Assess step** — `rules/assessment-rules.md`, `templates/debt-register.md`
- **Knowledge-graph-assisted mapping และ assessment (optional)** — graph cycles, fan-in outliers, layer violations → signal ป้อน dimension เดิม, ไม่ใช่ finding category ใหม่
- **Rule 0** — default Scan Mode, promotion ต้องมี trigger + evidence + risk
- **7 rules files**, **11 templates**, **example output**

ดูทั้งหมดใน [CHANGELOG.md](CHANGELOG.md)

---

## ตัวอย่าง Output

```txt
examples/basic-web-app/output/
├── architecture-overview.md
├── system-boundary.md
├── module-map.md
├── data-flow.md
├── workflow-map.md
├── file-responsibility-map.md
├── debt-register.md
├── risk-register.md
├── diagram.mmd / diagram.svg
├── open-questions.md
└── ai-agent-notes.md
```

---

## โครงสร้างไฟล์

```
senior-architect-agent/
├── README.md / SKILL.md / INSTALL.md / CHANGELOG.md / LICENSE
├── assets/visuals/       # infographic, workflow GIF, Mermaid source
├── scripts/              # build tooling (build_core_flow_gif.py)
├── agents/               # interface metadata (openai.yaml)
├── adapters/             # AGENTS.example.md
├── docs/                 # philosophy, workflow, output-spec, diagram-guidelines, model-requirements, anti-patterns
├── rules/                # 7 rule files (inspection, question, assessment, documentation, diagram, anti-overengineering, agent-handoff)
├── templates/            # 11 output templates
└── examples/             # basic-web-app output
```

---

## ข้อกำหนดโมเดล

ต้องการ long context (128K+ ปกติ, 200K+ สำหรับ multi-service) และ instruction following ที่แข็งแรง 32K พอสำหรับ Scan Mode

ดู [Model Requirements](docs/model-requirements.md)

---

## การติดตั้ง

ดู [INSTALL.md](INSTALL.md) สำหรับ Codex, Claude Code, Antigravity, AGENTS.md, และ manual

```txt
aetox-skills/senior-architect-agent
```

---

## License

MIT
