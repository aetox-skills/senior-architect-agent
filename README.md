# senior-architect-agent

รุ่นปัจจุบัน: `v1.1.0 — Right-Sized Architecture Passes`

**นี่ไม่ใช่เครื่องมือทำเอกสาร มันคือ cognitive framework ที่เปลี่ยน AI agents ให้เป็น senior architects — บังคับ evidence-first thinking, ความไม่แน่นอนที่ซื่อสัตย์, และความเข้าใจระบบอย่างลึกซึ้งก่อนลงมือ**

Senior Architect Agent คือชั้นระเบียบวินัยทางความคิดสำหรับ AI agents มันเปลี่ยน agents ให้เป็น architects ที่เข้าใจระบบจริงๆ และเขียนความเข้าใจนั้นออกมา — แยกสิ่งที่รู้กับสิ่งที่ inferred, ตั้งชื่อความไม่แน่นอนแทนที่จะซ่อนมัน, และสร้าง maps ที่มนุษย์และ AI agents ในอนาคตสามารถ trust ได้

โปรเจกต์นี้เป็น AI agent skill ที่ใช้ซ้ำได้ — บังคับให้ agent inspect, เข้าใจ, ตั้งคำถาม, map, document, และ validate ระบบซอฟต์แวร์หรือไอเดียระบบดิบๆ ก่อนจะเสนอการเปลี่ยนแปลงสถาปัตยกรรมหรือแก้โค้ด

คำค้นที่ Repository นี้ตั้งใจรองรับ: `Senior Architect Agent`, `AI architecture skill`, `architecture mapping`, `existing system mapping`, `software architecture documentation`, `Mermaid architecture diagram`, `AI agent handoff`, `AI architecture reasoning`, `evidence-first AI`, `cognitive framework for AI agents`

สโลแกนหลัก:

> สถาปนิกที่เข้าใจระบบจริงๆ และเขียนมันลงไป  
> ไม่ใช่เครื่องสร้างเอกสาร — มันคือ cognitive framework ที่ทำให้ AI อ่านก่อนวาด

ทิศทางขยาย:

> Skill นี้ช่วยให้ AI agents คลี่คลายระบบที่มีอยู่และไอเดียดิบๆ ออกมาเป็น architecture maps ที่มนุษย์และ AI agents ในอนาคตสามารถเข้าใจ ตรวจสอบ และต่อยอดได้

<p align="center">
  <a href="assets/visuals/from_powerful_models_to_elite_architects.png">
    <img src="assets/visuals/from_powerful_models_to_elite_architects.png" alt="From powerful models to elite senior architect infographic แสดงโมเดลที่สวม Senior Architect cognitive framework" width="980">
  </a>
  <br>
  <strong>From powerful models to elite senior architects</strong>: skill เพิ่มชั้น cognitive framework ที่มีระเบียบวินัยรอบโมเดลที่มีความสามารถ
</p>

<p align="center">
  <a href="assets/visuals/senior_architect_agent_workflow_infographic.png">
    <img src="assets/visuals/senior_architect_agent_workflow_infographic.png" alt="Senior Architect Agent workflow infographic ครอบคลุม core workflow, mode selector, evidence gate, repository anatomy, output overview, และ core flow animation" width="980">
  </a>
  <br>
  <strong>Full workflow infographic</strong>: core flow, mode selection, evidence gates, repository anatomy, และ expected outputs
</p>

<p align="center">
  <a href="assets/visuals/senior_architect_agent_core_flow.gif">
    <img src="assets/visuals/senior_architect_agent_core_flow.gif" alt="Senior Architect Agent animated core flow: intake, mode selection, inspection, classification, questioning, mapping, documentation, validation, และ reporting" width="920">
  </a>
  <br>
  <strong>Core flow animation</strong>: inspect evidence, classify claims, ask before mapping, แล้ว deliver traceable architecture output
</p>

## จุดประสงค์

AI agents มักแก้โค้ดก่อนเข้าใจสถาปัตยกรรม และเปลี่ยนไอเดียดิบๆ เป็นดีไซน์ที่ confident เร็วเกินไป

Skill นี้เพิ่มชั้นระเบียบวินัย:

1. ตรวจสอบระบบจริงก่อน
2. รักษาเจตนาของผู้ใช้เมื่อยังไม่มีระบบ
3. แยก confirmed facts, proposed architecture, assumptions, inferences, open questions, risks, และ decisions
4. ถามคำถามที่มีผลต่อสถาปัตยกรรมก่อนสรุป
5. สร้าง Markdown และ Mermaid architecture maps ที่มีประโยชน์
6. ทิ้ง handoff notes ที่ AI agents ในอนาคตใช้ได้ทันที
7. หลีกเลี่ยง unsupported claims, decorative documentation, และ overengineering

## ใช้เมื่อ

- AI agent ต้อง map existing codebase หรือระบบซอฟต์แวร์
- โปรเจกต์ต้องการ architecture documentation ก่อนแก้โค้ด
- ทีมต้องการ module maps, workflow maps, data-flow notes, หรือ Mermaid diagrams
- AI agent ในอนาคตต้องการ handoff notes, risks, unknowns, และ safe next actions
- ไอเดียดิบๆ เชื่อมโยงกับระบบที่มีอยู่หรือการ review สถาปัตยกรรมในวงกว้าง

## **ไม่** ใช้เมื่อ

- งานเป็นไอเดียดิบๆ ล้วนๆ ที่ไม่มี implementation และมี `$idea-to-architecture-agent` อยู่
- ผู้ใช้ต้องการแค่ implementation fix เล็กๆ ที่ไม่มีผลต่อสถาปัตยกรรม
- Output จะกลายเป็น decorative documentation แทนที่จะเป็น context ที่มีประโยชน์

## โหมดการทำงาน

### Existing System Mapping Mode

ใช้เมื่อมี project files, codebase structure, หรือเอกสารที่มีอยู่

Agent inspect สิ่งที่มี, map boundaries และ responsibilities ที่แท้จริง, และ mark ความไม่แน่นอนแทนที่จะ invent สถาปัตยกรรมที่หายไป

### Idea-to-Architecture Mode

ใช้เมื่อผู้ใช้ให้ไอเดียดิบ, product concept, feature request, หรือเป้าหมายธุรกิจ/ระบบ ที่ยังไม่มี implementation

Agent ถามคำถามที่มีผลต่อสถาปัตยกรรม, รักษาเจตนาของผู้ใช้, ระบุ assumptions, และสร้าง proposal ที่ตรวจสอบได้ ทุก module, workflow, data model, และ integrations ยังคงเป็น "เสนอ" จนกว่าจะได้รับการอนุมัติ

## การเลือกใช้ Skill ที่เกี่ยวข้อง

เมื่อมี [`$idea-to-architecture-agent`](https://github.com/aetox-skills/idea-to-architecture-agent) อยู่ ให้ใช้มันสำหรับไอเดียดิบๆ ที่ไม่มี implementation context

ใช้ skill นี้สำหรับระบบที่มีอยู่, งานผสม existing-system และ proposal, architecture boundaries, risk review, handoff notes, หรือเมื่อ dedicated idea skill ไม่ได้ติดตั้ง

Skill ที่เกี่ยวข้อง:

- [`idea-to-architecture-agent`](https://github.com/aetox-skills/idea-to-architecture-agent): proposal discipline สำหรับไอเดียดิบ, product concepts, feature requests, และเป้าหมายธุรกิจ/ระบบที่ไม่มี implementation

## ทิศทาง Release

`v1.0.0` สร้าง content readiness หลัก:

1. กำหนด `SKILL.md` ที่เข้มงวดและใช้งานได้จริงสำหรับทั้งสองโหมด
2. มี operating workflow ครอบคลุม intake, mode selection, inspection หรือ idea extraction, classification, questioning, mapping, documentation, validation, และ reporting
3. เพิ่ม rule files ขนาดกะทัดรัดที่ป้องกัน failure modes ทั่วไปของ AI agents
4. เพิ่ม templates ที่ใช้ซ้ำได้สำหรับ architecture outputs
5. มีตัวอย่างเล็กๆ สำหรับ existing-system mapping และ idea-to-architecture proposal
6. มี optional skill interface metadata โดยไม่ทำให้ core skill พึ่งพามัน
7. รวม SVG visual artifacts ที่สร้างจาก Mermaid example diagrams

`v1.1.0` เพิ่ม right-sized architecture pass control:

- `Scan Mode` สำหรับ architecture notes แบบกะทัดรัด
- `Focus Mode` สำหรับงาน scoped module, workflow, subsystem, หรือ boundary
- `Full Mode` สำหรับการ mapping ทั้งระบบ, future-agent handoff, ความเป็นเจ้าของไม่ชัดเจน, 3+ modules ที่ interact กัน, persistence, integrations, payment, authentication, security, deployment, หรือ major workflow changes

Skill เริ่มจาก smallest safe pass และเลื่อนระดับเมื่อ scope, evidence, risk, หรือ handoff needs ต้องการ

## โครงสร้างไฟล์

```txt
senior-architect-agent/
  README.md
  SKILL.md
  INSTALL.md
  LICENSE
  CHANGELOG.md

  assets/
    visuals/
      from_powerful_models_to_elite_architects.png
      senior_architect_agent_workflow_infographic.png
      senior_architect_agent_core_flow.gif
      01_core_workflow.mmd

  scripts/
    build_core_flow_gif.py

  agents/
    openai.yaml

  adapters/
    agents-md/
      AGENTS.example.md

  docs/
    philosophy.md
    workflow.md
    output-spec.md
    diagram-guidelines.md
    question-framework.md
    anti-patterns.md
    model-requirements.md
    project-core-th-final.md

  rules/
    inspection-rules.md
    question-rules.md
    documentation-rules.md
    diagram-rules.md
    anti-overengineering-rules.md
    agent-handoff-rules.md

  templates/
    architecture-overview.md
    system-boundary.md
    module-map.md
    data-flow.md
    workflow-map.md
    file-responsibility-map.md
    open-questions.md
    risk-register.md
    ai-agent-notes.md
    decision-record.md
    idea-brief.md
    architecture-proposal.md
    module-proposal.md
    workflow-proposal.md
    data-model-draft.md
    decision-options.md

  examples/
    basic-web-app/
      input-context.md
      output/
        architecture-overview.md
        system-boundary.md
        module-map.md
        data-flow.md
        workflow-map.md
        file-responsibility-map.md
        risk-register.md
        diagram.mmd
        diagram.svg
        open-questions.md
        ai-agent-notes.md
    idea-to-architecture/
      input-context.md
      output/
        idea-brief.md
        open-questions.md
        architecture-proposal.md
        module-proposal.md
        workflow-proposal.md
        data-model-draft.md
        risk-register.md
        diagram.mmd
        diagram.svg
        ai-agent-notes.md
```

## วิธีใช้

ใช้ skill นี้เมื่อ AI agent ถูกขอให้เข้าใจ codebase, วางแผนการเปลี่ยนแปลงสถาปัตยกรรม, ตรวจสอบโครงสร้างระบบ, ทำเอกสารสถาปัตยกรรม, สร้าง handoff notes, เสนอ redesign, หรือเปลี่ยนไอเดียดิบเป็น architecture proposal

เมื่อมีไฟล์อยู่ agent ไม่ควรเริ่มด้วยการแก้โค้ด ควร inspect โปรเจกต์, classify สิ่งที่มี, ถามคำถามสำคัญ, map ระบบ, document confirmed facts และ uncertainty, แล้วรายงาน safe next steps

Agents อาจใช้ inspection tools เช่น file search, file tree inspection, git history, validators, และ Mermaid checks Tool output เป็น evidence ที่ต้องตีความ ไม่ใช่สถาปัตยกรรมในตัวมันเอง

เมื่อมีแค่ไอเดีย agent ไม่ควรทำเป็นว่าระบบมีอยู่ ควร clarify intent, mark assumptions, propose architecture, ระบุ tradeoffs, และแจกแจง decisions ที่ต้องได้รับการอนุมัติ

## ข้อกำหนดโมเดล

Skill นี้เหมาะกับโมเดลที่สามารถ hold long context, follow instructions ผ่านหลาย gates, และ reasoning ผ่าน evidence ก่อนรายงาน

สำหรับการใช้งานปกติ แนะนำโมเดลที่มี context อย่างน้อย 128K และ instruction following ที่แข็งแรง ใช้ 32K สำหรับ `Scan Mode` เล็กๆ เท่านั้น ใช้ 200K+ สำหรับระบบ multi-service หรือ multi-repo ขนาดใหญ่

Skill นี้ถูกออกแบบมาสำหรับโมเดลที่สามารถคิดผ่าน architecture gates ไม่ใช่แค่ produce quick summaries ดู [Model Requirements](docs/model-requirements.md)

## Output ที่แนะนำ

ใช้ Markdown ก่อน ใช้ Mermaid diagrams เมื่อ diagram ช่วยได้

Mermaid เป็น editable source of truth สำหรับ diagrams

SVG visual artifacts อาจรวมเมื่อทำให้สถาปัตยกรรมตรวจสอบหรือนำเสนอได้ง่ายขึ้น SVG files เป็น generated artifacts และต้องไม่แทนที่ Markdown และ Mermaid ในฐานะ source of truth

`agents/openai.yaml` เป็นแค่ lightweight interface metadata เท่านั้น core skill ไม่ได้พึ่งพามัน

## ตัวอย่าง Output

- Existing system example: [`examples/basic-web-app/output/`](examples/basic-web-app/output/)
- Idea-to-architecture example: [`examples/idea-to-architecture/output/`](examples/idea-to-architecture/output/)

## การติดตั้ง

ดู [INSTALL.md](INSTALL.md) สำหรับ Codex, Claude Code, Antigravity, AGENTS.md, และ manual installation

ติดตั้ง Codex skill นี้จาก:

```txt
aetox-skills/senior-architect-agent
```

## License

MIT
