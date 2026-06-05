# แกนกลางโปรเจค `senior-architect-agent`

> เอกสารนี้คือ Directional Source of Truth ของโปรเจค `senior-architect-agent`
> ใช้เพื่อคุมทิศทาง วิสัยทัศน์ ขอบเขต และหลักคิดระยะยาวของโปรเจค
> ก่อนแก้ไขเชิงกลยุทธ์ในโปรเจคนี้ ควรอ่านเอกสารนี้ก่อนเสมอ

---

## 1. ภาพรวมของโปรเจค

`senior-architect-agent` คือสกิลสำหรับ AI Agent
ที่มีหน้าที่ช่วยกางระบบซอฟต์แวร์หรือไอเดียดิบออกมาเป็นสถาปัตยกรรมที่มนุษย์และ AI เข้าใจร่วมกันได้

โปรเจคนี้ไม่ได้เป็นเพียงเครื่องมือสร้าง diagram  
ไม่ได้เป็นเพียงระบบทำเอกสาร  
และไม่ได้เป็นเพียงกฎบังคับให้ AI อ่านโค้ดก่อนแก้

แก่นแท้ของโปรเจคนี้คือ:

> ทำให้ AI Agent คิดและทำงานในบทบาทของ Senior Software Architect ก่อนจะลงมือออกแบบ แก้ไข
> หรือสร้างระบบ

AI Agent ที่ใช้สกิลนี้ต้องไม่รีบทำงานแบบช่างโค้ดที่พุ่งไปแก้ไฟล์ทันที แต่ต้องหยุดอ่าน วิเคราะห์
ตั้งคำถาม กำหนดขอบเขต แยกข้อเท็จจริงออกจากข้อสันนิษฐาน และสร้างแผนที่ระบบที่ตรวจสอบได้ก่อน

เป้าหมายสูงสุดคือทำให้ระบบที่ซับซ้อน หรือไอเดียที่ยังคลุมเครือ ถูกกางออกมาเป็นภาพรวมที่ชัดเจน
เป็นเอกสารที่ใช้ต่อได้ และเป็นบริบทที่ AI รอบถัดไปสามารถเข้าใจได้ทันที

---

## 2. ปัญหาที่โปรเจคนี้ต้องการแก้

AI Agent จำนวนมากมีความสามารถสูงในการเขียนโค้ด แก้บั๊ก สร้างไฟล์ และเสนอ architecture
แต่ปัญหาหลักคือ AI มักทำงานเร็วเกินไปก่อนจะเข้าใจระบบจริง

ปัญหาที่พบได้บ่อยคือ:

- AI แก้โค้ดก่อนเข้าใจ architecture
- AI เดาโครงสร้างระบบจากชื่อไฟล์หรือบริบทบางส่วน
- AI สร้างไฟล์ใหม่โดยไม่ตรวจว่าของเดิมมีอะไรอยู่แล้ว
- AI ผสมข้อเท็จจริงกับข้อสันนิษฐาน
- AI เสนอ architecture เหมือนเป็นความจริง ทั้งที่เป็นเพียง proposal
- AI ทำเอกสารเยอะ แต่เอกสารไม่ช่วยให้คนหรือ AI รอบถัดไปทำงานต่อได้
- AI วาด diagram สวย แต่ไม่สะท้อนระบบจริง
- AI ไม่ถามคำถามสำคัญก่อนออกแบบ
- AI ทำงานจบในรอบเดียว แต่ไม่ทิ้ง handoff context สำหรับรอบถัดไป

โปรเจคนี้จึงเกิดขึ้นเพื่อสร้างวินัยให้ AI Agent ทำงานแบบสถาปนิกก่อนทำงานแบบช่างเขียนโค้ด

---

## 3. วิสัยทัศน์หลัก

วิสัยทัศน์ของ `senior-architect-agent` คือ:

> AI Agent ต้องสามารถกางระบบเดิมหรือไอเดียดิบออกมาเป็นสถาปัตยกรรมที่ตรวจสอบได้ เข้าใจได้
> และใช้ต่อได้ ทั้งสำหรับมนุษย์และ AI Agent รอบถัดไป

โปรเจคนี้ต้องทำให้ AI สามารถทำได้สองทาง:

1. อ่านระบบที่มีอยู่จริง แล้วกางออกมาเป็นแผนที่ architecture
2. รับไอเดียดิบ แล้วแตกออกมาเป็น architecture proposal ที่มีเหตุผล คำถาม ขอบเขต ความเสี่ยง
   และทางเลือก

ทั้งสองทางต้องไม่ปนกัน

ถ้าเป็นระบบที่มีอยู่จริง AI ต้องยึดหลักฐานเป็นหลัก  
ถ้าเป็นไอเดียใหม่ AI ต้องยึดเจตนาของผู้ใช้ ตั้งคำถามสำคัญ และประกาศทุกอย่างที่ออกแบบว่าเป็น proposal
ไม่ใช่ fact

---

## 4. Operating Modes

โปรเจคนี้มีสองโหมดหลัก

---

### 4.1 Existing System Mapping Mode

ใช้เมื่อมีระบบจริงให้ตรวจ เช่น codebase, folder structure, documentation, configuration, API,
database schema หรือไฟล์โปรเจคที่มีอยู่แล้ว

เป้าหมายของโหมดนี้คือ:

> อ่านของจริงก่อน แล้วกางระบบที่มีอยู่ให้เห็นชัด

AI ต้องตรวจสอบสิ่งที่มีอยู่จริงก่อน เช่น:

- โครงสร้างโฟลเดอร์
- frontend
- backend
- database
- configuration
- routing
- API
- authentication
- external services
- infrastructure
- naming conventions
- existing documentation
- module boundaries
- duplicated responsibilities
- unclear ownership

ผลลัพธ์ที่ควรได้จากโหมดนี้ เช่น:

- architecture overview
- system boundary
- module map
- data flow
- workflow map
- file responsibility map
- open questions
- risk register
- AI agent handoff notes
- Mermaid diagram
- SVG visual artifact เมื่อ diagram ซับซ้อนและต้องใช้สำหรับการนำเสนอหรือรีวิว

กฎสำคัญของโหมดนี้:

- ห้ามออกแบบจากจินตนาการถ้ายังไม่ได้อ่านของจริง
- ห้ามบอกว่าส่วนใดมีอยู่จริงถ้าไม่มีหลักฐาน
- ต้องแยก confirmed facts, reasonable inferences, open questions, risks และ decisions
- ถ้า backend, database, AI service หรือ external service ไม่ถูกพบ ต้องระบุว่า `not observed` หรือ
  `unknown`
- diagram ต้องสะท้อนสิ่งที่ตรวจพบ ไม่ใช่ architecture ในอุดมคติ

---

### 4.2 Idea-to-Architecture Mode

ใช้เมื่อผู้ใช้ให้ไอเดีย แนวคิด product concept, feature request หรือ business/system goal
โดยยังไม่มีระบบจริงให้ตรวจ

เป้าหมายของโหมดนี้คือ:

> รับไอเดียดิบ แล้วแตกออกมาเป็น architecture proposal ที่ตรวจสอบได้

AI ต้องทำหน้าที่เหมือน Senior Architect ที่ช่วยคิดระบบจากศูนย์ แต่ต้องไม่มั่ว ไม่ทับเจตนาของผู้ใช้
และไม่พูดเหมือนสิ่งที่เสนอเป็นความจริงแล้ว

AI ต้องทำสิ่งเหล่านี้:

- จับแก่นของไอเดีย
- แยก user roles หรือ actors
- ตั้งคำถามที่กระทบ architecture
- ระบุ assumptions
- ออกแบบ proposed system boundary
- เสนอ module structure
- เสนอ data model draft
- เสนอ workflow
- เสนอ integration points
- ระบุ risks และ tradeoffs
- ระบุ decisions ที่ต้องให้ผู้ใช้อนุมัติ
- สร้าง diagram ที่บอกชัดว่าเป็น proposed architecture

ผลลัพธ์ที่ควรได้จากโหมดนี้ เช่น:

- idea brief
- architecture proposal
- module proposal
- workflow proposal
- data model draft
- decision options
- open questions
- risk register
- AI agent notes
- Mermaid diagram
- SVG visual artifact เมื่อ architecture map มีความซับซ้อนและต้องใช้เพื่อการนำเสนอ

กฎสำคัญของโหมดนี้:

- ทุก architecture ที่เสนอถือเป็น proposal จนกว่าจะได้รับการอนุมัติ
- ต้อง preserve user intent
- ต้องไม่เปลี่ยนไอเดียของผู้ใช้เป็นระบบอีกแบบโดยไม่บอก
- ต้องแยก assumptions ออกจาก decisions
- ต้องถามคำถามที่กระทบ architecture จริง ไม่ถามจุกจิกจนงานหยุด
- ถ้าข้อมูลไม่ครบ ให้สร้าง first draft จาก assumptions ที่ประกาศชัด
- ต้องอธิบาย tradeoffs เมื่อมีทางเลือกสำคัญ

---

### 4.3 หมายเหตุเรื่อง skill ลูกเฉพาะทาง

ถ้ามี `idea-to-architecture-agent` และงานเป็น raw idea ล้วนโดยไม่มีระบบจริงให้ตรวจ
ให้ prefer skill ลูกตัวนั้นสำหรับ workflow ที่โฟกัสเฉพาะการเปลี่ยนไอเดียเป็น architecture proposal

`senior-architect-agent` ยังต้องรองรับ Idea-to-Architecture Mode ต่อไปในฐานะ core skill
โดยเฉพาะเมื่อไม่มี skill ลูกติดตั้งอยู่ เมื่องานเป็นไอเดียที่ผูกกับระบบเดิม
หรือเมื่องานต้องการ architecture discipline ที่กว้างกว่า เช่น boundary, risk, validation
และ AI handoff

การมี skill ลูกไม่ใช่ dependency ของ `senior-architect-agent`
และไม่เปลี่ยนความหมายหลักของโปรเจคแม่

---

## 5. หลักการกลางของโปรเจค

---

### 5.1 Inspect before design

ถ้ามีระบบจริง ต้องอ่านของจริงก่อนออกแบบ

AI ห้ามออกแบบจากชื่อไฟล์ ความคุ้นเคย หรือ pattern ที่คิดเอาเองโดยไม่ตรวจหลักฐาน

---

### 5.2 Understand before editing

AI ห้ามแก้โค้ดก่อนเข้าใจ architecture, data flow, module boundary และผลกระทบของการแก้ไข

---

### 5.3 Never assume silently

AI สามารถสันนิษฐานได้ แต่ต้องประกาศให้ชัดว่าเป็น assumption หรือ inference

การเดาเงียบคือสิ่งต้องห้าม

---

### 5.4 Separate truth from proposal

Existing system คือสิ่งที่ตรวจพบ  
Idea-to-Architecture คือสิ่งที่เสนอ

สองอย่างนี้ต้องไม่ปนกัน

AI ต้องไม่เอา proposal ไปพูดเหมือนเป็น fact  
และต้องไม่เอา fact ไป redesign โดยไม่บอกว่ากำลังเสนอการเปลี่ยนแปลง

---

### 5.5 Ask architecture-impacting questions

AI ต้องถามคำถามที่มีผลต่อโครงสร้างระบบ เช่น:

- user roles มีอะไรบ้าง
- system boundary อยู่ตรงไหน
- data ต้องเก็บที่ไหน
- ต้องมี backend หรือไม่
- authentication จำเป็นแค่ไหน
- payment หรือ external service ต้องใช้จริงหรือไม่
- workflow หลักคืออะไร
- ส่วนไหนต้อง real-time
- ส่วนไหนเป็น core domain
- ส่วนไหนเป็น feature เสริม
- decision ใดต้องให้ผู้ใช้อนุมัติ

แต่ AI ไม่ควรถามมากจนงานหยุด  
ถ้าคำถามไม่ block architecture หลัก ให้ตั้ง assumption แล้วเดินต่อ

---

### 5.6 Make architecture visible

สถาปัตยกรรมที่ดีต้องเห็นภาพได้

AI ต้องสามารถทำให้ระบบหรือไอเดียถูกกางออกมาเป็นแผนที่ เช่น:

- system overview
- module map
- data flow
- workflow
- file responsibility map
- proposed architecture diagram
- integration map
- risk map

เป้าหมายไม่ใช่ภาพสวย  
เป้าหมายคือภาพที่ทำให้คนและ AI เข้าใจตรงกัน

---

### 5.7 Documentation must reduce confusion

เอกสารที่ดีต้องลดความสับสน ไม่ใช่เพิ่มพิธีกรรม

ทุกไฟล์ควรมีหน้าที่จริง เช่น:

- ช่วยเข้าใจระบบ
- ช่วยตัดสินใจ
- ช่วยตรวจสอบ assumptions
- ช่วยวาง architecture
- ช่วย AI รอบหน้าทำงานต่อ
- ช่วยลดการเดาซ้ำ

ถ้าเอกสารไม่ช่วยสิ่งเหล่านี้ ควรตัดหรือรวม

---

### 5.8 Handoff is part of architecture

AI Agent รอบถัดไปไม่ควรเริ่มจากศูนย์

ทุก output สำคัญควรมี handoff notes ที่บอกว่า:

- รู้อะไรแล้ว
- ยังไม่รู้อะไร
- อะไรเป็น fact
- อะไรเป็น assumption
- อะไรเป็น proposed decision
- จุดไหนเสี่ยง
- ห้าม assume อะไร
- ควร inspect อะไรต่อ
- safe edit zone อยู่ตรงไหน
- risky edit zone อยู่ตรงไหน

---

### 5.9 Source of truth hierarchy

ลำดับความจริงของ output ในโปรเจคนี้คือ:

1. Markdown documentation คือแหล่งอธิบายความจริง ขอบเขต เหตุผล ความเสี่ยง และ decision
2. Mermaid คือ diagram source ที่อ่านง่าย แก้ไขง่าย และใช้ version control ได้ดี
3. SVG คือ visual artifact สำหรับการนำเสนอ การฝังใน README การรีวิวระบบซับซ้อน
   หรือการสื่อสารกับคนที่ต้องเห็นภาพชัด

SVG มีประโยชน์และควรมีได้เมื่อเหมาะสม  
แต่ SVG ไม่ควรแทนที่ Markdown และ Mermaid ที่เป็น editable source of truth

claim สำคัญควรมี evidence strength:

- `Direct`: มาจากไฟล์ เอกสารเดิม หรือ user-provided fact โดยตรง
- `Inferred`: สรุปจาก evidence แต่ยังไม่ยืนยันตรงๆ
- `Assumed`: premise ชั่วคราวที่ประกาศไว้เพื่อเดินงานต่อ
- `Unverified`: ยังไม่มี source ต้อง verify, label หรือถอดออกก่อนใช้ตัดสินใจ

ถ้า claim ใดควรถูกตรวจซ้ำก่อนใช้ ให้ระบุ `Verify first: Yes`

---

## 6. ขอบเขตของโปรเจค

---

### 6.1 สิ่งที่อยู่ในขอบเขต

`senior-architect-agent` ควรครอบคลุมสิ่งเหล่านี้:

- codebase architecture mapping
- project structure inspection
- idea-to-architecture proposal
- system boundary definition
- module responsibility mapping
- data flow mapping
- workflow mapping
- file responsibility mapping
- open questions
- risk register
- architecture decision notes
- AI handoff notes
- Markdown documentation templates
- Mermaid diagrams
- SVG visual artifacts เมื่อจำเป็นต่อการอธิบายระบบที่ซับซ้อน
- rules against fake certainty
- rules against overengineering
- rules for separating facts, assumptions, proposals, and decisions

---

### 6.2 ขอบเขตของ Core Skill

แกนหลักของ repository นี้ควรคมและเล็กพอที่จะใช้งานได้จริง:

- `SKILL.md`
- Markdown architecture docs
- Mermaid diagram sources
- optional SVG visual artifacts
- rules
- templates
- examples ที่พิสูจน์สอง operating modes
- validation guidance ที่เบาและตรวจสอบได้

ข้อสำคัญ:

> การมีไฟล์ SVG เป็น output ไม่ได้ขัดกับขอบเขตของโปรเจค  
> สิ่งที่ต้องรักษาคือ Mermaid เป็น source of truth และ SVG เป็น artifact

เหตุผลคือ core skill ต้องรักษาความคมของการเป็น architecture skill ก่อน
และไม่ขยายจนขอบเขตเบลอ

---

## 7. ระดับของผลลัพธ์ที่ต้องการ

โปรเจคนี้ควรสร้างผลลัพธ์ได้หลายระดับ

---

### 7.1 Human-readable output

เอกสารที่มนุษย์อ่านแล้วเข้าใจระบบ เช่น:

- overview
- boundary
- workflow
- risks
- decisions
- architecture proposal

---

### 7.2 AI-readable output

เอกสารที่ AI รอบถัดไปอ่านแล้วทำงานต่อได้ เช่น:

- ai-agent-notes
- file responsibility map
- assumptions
- unknowns
- safe/risky areas
- next inspection targets

---

### 7.3 Visual output

แผนภาพที่ช่วยให้เห็นระบบ เช่น:

- Mermaid diagram
- architecture map
- data flow
- workflow flowchart
- SVG visual artifact สำหรับระบบที่ซับซ้อนหรืองานนำเสนอ

Mermaid ควรเป็น source of truth ก่อน SVG เพราะอ่านง่าย แก้ง่าย diff ง่าย และ version control
ง่ายกว่า

SVG ควรเป็น export artifact หรือ presentation artifact ที่ช่วยให้คนเห็นภาพชัดขึ้น โดยเฉพาะเมื่อ
diagram ซับซ้อนมาก

---

### 7.4 Decision output

เอกสารที่ช่วยตัดสินใจ เช่น:

- open questions
- decision options
- tradeoffs
- risk register
- approval-required decisions

---

## 8. หลักการเรื่อง Diagram และ Visual Export

Diagram ในโปรเจคนี้ไม่ใช่ของตกแต่ง

Diagram ต้องเป็นแผนที่ที่ตรวจสอบได้

กฎของ diagram คือ:

- ต้องบอกได้ว่าอะไร confirmed
- ต้องบอกได้ว่าอะไร inferred
- ต้องบอกได้ว่าอะไร assumed
- ต้องบอกได้ว่าอะไร proposed
- ต้องไม่สร้าง fantasy architecture
- ต้องไม่แสดง backend, database หรือ service เป็นของจริงถ้าไม่พบหลักฐาน
- ต้องใช้ label ที่ชัดและ render-safe
- ต้องอ่าน raw source ได้
- ต้องใช้ Mermaid เป็น diagram source หลัก
- diagram หนึ่งควรตอบคำถาม architecture หนึ่งเรื่องให้ชัด
- ถ้า diagram ใหญ่จนอ่านยาก ให้แยกเป็น boundary, module, workflow หรือ data-flow view
- SVG ใช้เป็น visual artifact เมื่อมีประโยชน์ต่อการนำเสนอ การรีวิว หรือการสื่อสารภาพรวม

หลักที่ต้องจำ:

> Mermaid มีไว้ให้แก้และตรวจสอบ  
> Markdown มีไว้เก็บความจริงของระบบ  
> SVG มีไว้ให้เห็นภาพชัดเมื่อต้องสื่อสารระบบที่ซับซ้อน

SVG ไม่ควรเป็นแหล่งความจริงหลัก  
แต่ SVG เป็น output ที่ควรมีได้เมื่อช่วยให้ระบบเข้าใจง่ายขึ้น

---

## 9. หลักการเรื่องการออกแบบจากไอเดีย

เมื่อ AI รับไอเดียดิบมา AI ต้องไม่รอให้ข้อมูลครบทุกจุดก่อนเริ่มคิด

AI ควรทำ first draft ได้ โดยประกาศ assumptions ให้ชัด

กระบวนการที่ถูกต้องคือ:

1. จับแก่นไอเดีย
2. ระบุ actors
3. ระบุ core workflows
4. ตั้งคำถามที่กระทบ architecture
5. ตั้ง assumptions สำหรับส่วนที่ไม่ block
6. เสนอ architecture draft
7. แยก module responsibilities
8. ร่าง data model
9. ระบุ tradeoffs
10. ระบุ risks
11. ระบุ decisions requiring approval
12. สร้าง Mermaid diagram
13. สร้าง SVG visual artifact ถ้าระบบซับซ้อนพอและช่วยให้เห็นภาพชัดขึ้น
14. เขียน handoff notes

สิ่งที่ต้องระวังคือ AI ต้องไม่ “ฉลาดแทนเจ้าของไอเดีย” จนเปลี่ยนแก่นของระบบ

AI ต้องช่วยขยายไอเดีย ไม่ใช่กลืนไอเดีย

---

## 10. หลักการเรื่องการอ่านระบบเดิม

เมื่อ AI อ่านระบบเดิม AI ต้องทำงานเหมือนนักสำรวจ ไม่ใช่นักแต่งเรื่อง

กระบวนการที่ถูกต้องคือ:

1. อ่านโครงสร้างไฟล์
2. อ่านเอกสารที่มีอยู่
3. ระบุ technology stack
4. ระบุ entry points
5. ระบุ module boundaries
6. ระบุ data flow เท่าที่พบ
7. ระบุ external services เท่าที่พบ
8. ระบุ unknowns
9. ระบุ risks
10. ระบุสิ่งที่ต้อง inspect ต่อ
11. สร้าง architecture map
12. สร้าง Mermaid diagram
13. สร้าง SVG visual artifact ถ้าจำเป็นต่อการรีวิวระบบซับซ้อน
14. สร้าง handoff notes

สิ่งที่ต้องระวังคือ AI ต้องไม่เอา best practice ทั่วไปมายัดใส่ระบบเดิมโดยไม่มีหลักฐาน

---

## 11. นิยามคำสำคัญ

### Confirmed Fact

สิ่งที่ตรวจพบจากไฟล์ โค้ด เอกสาร หรือข้อมูลที่ผู้ใช้ระบุชัดเจน

### Reasonable Inference

ข้อสันนิษฐานที่มีเหตุผลจากหลักฐาน แต่ยังไม่ใช่ความจริงที่ยืนยันแล้ว

### Assumption

สิ่งที่ AI ใช้เป็นฐานชั่วคราวเพื่อเดินงานต่อ โดยต้องประกาศให้ชัด

### Open Question

คำถามที่ต้องการคำตอบเพื่อให้ architecture ชัดขึ้น

### Risk

จุดที่อาจทำให้ระบบผิดทิศ พัง บวม ซ้ำซ้อน หรือเข้าใจผิด

### Decision

สิ่งที่ต้องเลือกและมีผลต่อ architecture

### Proposed Architecture

สถาปัตยกรรมที่ AI เสนอจากไอเดียหรือข้อมูลที่ยังไม่ใช่ระบบจริง

### Mermaid Diagram

diagram source ที่อ่าน แก้ไข diff และ version control ได้ง่าย

### SVG Visual Artifact

ไฟล์ภาพที่ใช้สำหรับการนำเสนอ การรีวิว หรือการสื่อสารระบบที่ซับซ้อน  
ไม่ใช่ source of truth หลักของ architecture

### Handoff Notes

บริบทสรุปสำหรับ AI หรือมนุษย์ที่มาทำงานต่อในรอบถัดไป

---

## 12. แนวทางการพัฒนาเวอร์ชัน

---

### v0.1.0 - Foundation Map

เป้าหมายคือทำให้แกนของสกิลชัดและมีตัวอย่าง end-to-end

ควรมี:

- `SKILL.md` ที่อธิบายสองโหมดหลัก
- `README.md` ที่อธิบายภาพรวมและคุณค่าของโปรเจค
- rules สำหรับกัน AI ทำงานมั่ว
- templates สำหรับ output หลัก
- example สำหรับ Existing System Mapping
- example สำหรับ Idea-to-Architecture
- Mermaid diagram ที่อ่านง่ายแบบ line-by-line
- SVG visual artifact ตัวอย่างอย่างน้อยหนึ่งชิ้น
  ถ้าช่วยให้เห็นภาพรวมของโปรเจคหรือระบบซับซ้อนได้ชัดขึ้น
- AI handoff notes
- risk register
- open questions
- evidence / assumption / proposal separation
- readable output package

v0.1.0 ยังควรเน้น readable Markdown/Mermaid output package ก่อน

---

### v0.2.0 - Workflow Mapping Upgrade

เน้น workflow ให้ลึกขึ้น เช่น:

- user journey
- backend request lifecycle
- decision points
- failure paths
- permission flow
- async jobs
- error handling flow

---

### v0.3.0 - Codebase Inspection Upgrade

เน้นการอ่าน codebase จริงลึกขึ้น เช่น:

- routing map
- API map
- data model map
- dependency map
- file ownership map
- duplication map
- boundary violation map

---

### v0.4.0 - Agent Handoff Standard

เน้นมาตรฐานการส่งต่องานให้ AI รอบถัดไป เช่น:

- known facts
- unknown areas
- assumptions
- forbidden assumptions
- safe edit zones
- risky edit zones
- decisions
- pending questions
- next inspection targets

---

### v0.5.0 - Visual Output Refinement

เน้นมาตรฐาน diagram และ visual artifact ให้คมขึ้น เช่น:

- Mermaid diagram convention
- render-safe labels
- visual status labels
- SVG artifact guidelines
- README-embeddable architecture maps
- diagram examples สำหรับระบบซับซ้อน

เวอร์ชันนี้เน้นมาตรฐาน visual output ให้ชัดและไม่มั่ว

---

### v1.0.0 - Flagship Content Readiness / Stable Architecture Discipline Standard

เป้าหมายคือทำให้ core skill พร้อมรีวิวและพร้อม tag ในฐานะ flagship content
ที่สามารถนำไปใช้กับโปรเจคจริงได้อย่างมั่นใจ

ควรมี:

- `SKILL.md` ที่คุมสองโหมดได้ชัด
- operating modes ที่ชัด
- operational docs ภาษาอังกฤษที่อ่านแล้วใช้งานได้ทันที
- เอกสารแกนกลางภาษาไทยเป็น directional source of truth
- templates ที่แยก fact, inference, assumption, proposal, unknown, risk
  และ decision ได้ชัด
- examples สำหรับทั้ง Existing System Mapping และ Idea-to-Architecture
- Mermaid diagrams ที่อ่าน raw source ได้และ render-safe
- SVG visual artifacts เมื่อช่วย review, presentation, README embedding,
  หรือ human-facing explanation
- Mermaid/SVG checks ที่พอใช้สำหรับตรวจ diagram artifacts
- AI handoff notes
- risk register
- open questions
- changelog
- clear scope
- practical README

v1.0.0 ต้องรักษา Markdown เป็น documentation source of truth,
Mermaid เป็น editable diagram source, และ SVG เป็น visual artifact เท่านั้น

ขอบเขตของ v1.0.0 คือ skill package ที่อ่าน ใช้ รีวิว และส่งต่อได้:
Markdown docs, Mermaid sources, SVG artifacts ที่มีที่มา, rules, templates,
examples, และ handoff context

---

## 13. สิ่งที่ต้องระวังระยะยาว

---

### 13.1 อย่าให้กลายเป็น diagram generator

Diagram เป็น output สำคัญ แต่ไม่ใช่แก่นของโปรเจค

แก่นคือการกางระบบหรือไอเดียให้ตรวจสอบได้

---

### 13.2 อย่าให้กลายเป็นเอกสารกองโต

เอกสารต้องช่วยลดความสับสน

ถ้าเอกสารเพิ่มภาระโดยไม่เพิ่มความเข้าใจ ต้องตัดหรือรวม

ให้เริ่มจาก architecture pass ที่เล็กที่สุดแต่ยังปลอดภัยต่อความเข้าใจ:

- Scan Mode สำหรับงานเล็ก งานสำรวจ หรืองานความเสี่ยงต่ำ
  ใช้ compact architecture note ที่ยังแยก fact, inference, assumption,
  unknown, risk และ decision ได้ชัด
- Focus Mode สำหรับ module, workflow, subsystem หรือ boundary ที่เจาะจง
- Full Mode สำหรับ whole-system mapping, handoff ให้ AI รอบถัดไป,
  boundary ไม่ชัด, 3+ modules ที่มี interaction จริง, persistence,
  integration, payment/billing, authentication/authorization, security,
  deployment หรือ workflow ใหญ่

เริ่มจาก pass ที่เล็กที่สุดก่อน แล้วค่อย promote เมื่อ scope, evidence,
risk หรือ handoff need ทำให้ pass เดิมไม่พอ

ถ้าไม่แน่ใจ ให้ inspect แคบก่อน บันทึกว่าเช็กอะไรแล้ว และอย่า promote
เป็น full output package เพียงเพราะ uncertainty

---

### 13.3 อย่าให้ AI เสนอ architecture แบบมั่นใจเกินจริง

โดยเฉพาะ Idea-to-Architecture Mode ต้องประกาศว่าอะไรเป็น proposal, assumption, risk และ decision
requiring approval

---

### 13.4 อย่าให้ AI ถามเยอะจนงานหยุด

คำถามต้องสำคัญต่อ architecture

เรื่องที่ไม่ block ให้ตั้ง assumption แล้วเดินต่อ

---

### 13.5 อย่าให้ AI แก้ของจริงก่อนเข้าใจของจริง

Existing System Mapping Mode ต้อง evidence-first เสมอ

---

### 13.6 อย่าให้ validation เป็น checklist ลอยๆ

ก่อน Report ต้องตอบ validation gate 3 ข้อ:

1. claim สำคัญทุกข้อมีที่มาหรือไม่
   ถ้าไม่มี source ให้ mark เป็น `Unverified`, `Assumed` หรือถอดออก
2. final scope ตรงกับ intake scope หรือไม่
   ถ้าขยาย ต้องบอกว่าเพิ่มอะไร เพราะอะไร และอนุมัติแล้วหรือยัง
3. handoff มี unknowns และ safe next actions หรือไม่
   ถ้าไม่มี ให้เขียน `None identified` อย่างชัดเจน

---

### 13.7 อย่าให้โปรเจคขยายเร็วกว่าแกน

แกนหลักควรเป็น skill package ที่คุมวินัย architecture ได้ชัด:
Markdown docs, Mermaid sources, optional SVG visual artifacts, rules,
templates, examples, และ validation guidance แบบเบา

SVG visual artifact อยู่ในขอบเขตได้เมื่อช่วยให้เห็นภาพชัด  
แต่ Mermaid/SVG checks ควรอยู่ในรูปแบบที่เบาและตรวจสอบได้

---

## 14. หลักคิดการทำงานของโปรเจคนี้

สูตรการพัฒนาที่เหมาะกับโปรเจคนี้คือ:

1. ทำให้ภาพใหญ่ครบก่อน
2. ตรวจว่าแก่นไม่หลุด
3. ตัดส่วนซ้ำและส่วนบวม
4. ทำเอกสารให้คม
5. ทำตัวอย่างให้พิสูจน์ตัวเอง
6. ค่อย release

ไม่ควร polish ก่อนที่ภาพใหญ่จะครบ  
แต่ก็ไม่ควรขยายจนเกินแก่นเดิม

หลักที่ควรยึดคือ:

> สร้างภาพเต็มก่อน แล้วค่อยลับคม  
> แต่ภาพเต็มต้องอยู่ในรั้วของเจตนาเดิม

---

## 15. ขอบเขตของ Core Skill

โปรเจคนี้ควรรักษาแกนหลักของ `senior-architect-agent` ให้ชัดและไม่บวม

แกนหลักของโปรเจคนี้คือ:

- Markdown documentation
- Mermaid diagrams
- SVG visual artifacts เมื่อจำเป็นต่อการสื่อสารภาพรวม
- Mermaid/SVG checks เพื่อรักษาความถูกต้องของ diagram artifacts
- architecture mapping
- idea-to-architecture proposal
- evidence and assumption discipline
- AI handoff context

เหตุผลคือโปรเจคนี้ต้องรักษาความคมของการเป็น architecture skill

### 15.1 Model Fit

สกิลนี้เหมาะกับ model ที่ถือ context ได้ยาว ทำตาม instruction ได้สม่ำเสมอ
และ reasoning หลายขั้นได้จริง

model ที่ใช้กับสกิลนี้ควรจำ intake scope, classification, evidence,
assumptions, checkpoint gates และ validation gate ได้ตลอดงาน

สกิลนี้ถูกออกแบบมาสำหรับ model ที่ “คิดได้” ไม่ใช่ model ที่แค่ “ตอบได้”

model เล็กอาจใช้กับ Scan Mode หรืองานเล็กมากได้ แต่ไม่ควรถูกใช้เป็นตัวหลัก
สำหรับ full architecture mapping ของระบบกลางหรือใหญ่

---

## 16. ประโยคหลักของโปรเจค

ประโยคหลักที่ใช้คุมทิศทางคือ:

> This skill does not make AI code faster. It makes AI understand before it acts.

แต่เมื่อขยาย vision ให้ครบขึ้น สามารถใช้ประโยคนี้เป็นแกนใหม่ได้:

> This skill helps AI agents unfold existing systems and raw ideas into architecture maps that
> humans and future AI agents can understand, review, and continue from.

แปลความหมาย:

> สกิลนี้ช่วยให้ AI Agent กางระบบเดิมและไอเดียดิบออกมาเป็นแผนที่สถาปัตยกรรมที่มนุษย์และ AI
> รอบถัดไปสามารถเข้าใจ ตรวจสอบ และทำงานต่อได้

---

## 17. คำตัดสินเชิงทิศทาง

`senior-architect-agent` ควรเป็นสกิลระดับ flagship ของ `aetox-skills`

ไม่ใช่เพราะมันทำเอกสารได้  
ไม่ใช่เพราะมันวาด diagram ได้  
แต่เพราะมันแก้ปัญหาหลักของ AI Agent ยุคนี้:

> AI มีพลังมากพอจะสร้างและแก้ระบบได้เร็ว  
> แต่ยังต้องการวินัยในการเข้าใจ อธิบาย ตั้งคำถาม และส่งต่อบริบทก่อนลงมือ

โปรเจคนี้จึงควรเป็นเหมือน “สติทางสถาปัตยกรรม” ของ AI Agent

ถ้าทำสำเร็จ มันจะช่วยให้ AI ไม่ใช่แค่ทำงานเร็วขึ้น แต่ทำงานอย่างมีทิศทาง มีหลักฐาน มีขอบเขต
และมีความรับผิดชอบต่อระบบที่มันกำลังแตะ

---

## 18. สรุปสุดท้าย

ปลายทางของ `senior-architect-agent` คือ:

- AI อ่านระบบซับซ้อนแล้วกางออกมาเป็นแผนที่ที่เข้าใจได้
- AI รับไอเดียดิบแล้วแตกออกมาเป็น architecture proposal ที่ตรวจสอบได้
- AI แยก fact, inference, assumption, proposal, risk และ decision ได้ชัด
- AI สร้างเอกสารที่มนุษย์และ AI รอบถัดไปใช้ต่อได้
- AI วาด diagram ที่สะท้อนความจริงหรือ proposal อย่างซื่อสัตย์
- AI สร้าง SVG visual artifact ได้เมื่อช่วยอธิบาย architecture ที่ซับซ้อน
- AI ตั้งคำถามที่จำเป็นต่อ architecture โดยไม่ทำให้งานหยุด
- AI ไม่มั่ว ไม่เดาเงียบ ไม่สร้างเอกสารบวม และไม่แก้ระบบก่อนเข้าใจระบบ

นี่คือแกนของโปรเจค

> กางระบบให้เห็น  
> กางไอเดียให้เป็นรูป  
> แยกความจริงออกจากข้อเสนอ  
> วาดภาพให้เข้าใจ  
> และส่งต่อบริบทให้ AI รุ่นถัดไปเดินต่อได้โดยไม่โง่ซ้ำ
