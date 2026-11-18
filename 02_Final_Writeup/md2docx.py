import re, os, sys
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = os.path.dirname(os.path.abspath(__file__))

def add_inline(par, text):
    tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*\n]+\*)', text)
    for t in tokens:
        if not t:
            continue
        if t.startswith('**') and t.endswith('**') and len(t) > 4:
            r = par.add_run(t[2:-2]); r.bold = True
        elif t.startswith('*') and t.endswith('*') and len(t) > 2:
            r = par.add_run(t[1:-1]); r.italic = True
        else:
            par.add_run(t)

def convert(md_path, docx_path):
    doc = Document()
    normal = doc.styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_after = Pt(6)

    lines = open(md_path, encoding='utf-8').read().split('\n')
    i = 0
    in_title = False
    in_code = False
    table_buf = []

    def flush_table():
        if not table_buf:
            return
        rows = []
        for r in table_buf:
            cells = [c.strip() for c in r.strip().strip('|').split('|')]
            rows.append(cells)
        rows = [r for r in rows if not all(set(c) <= set('-: ') for c in r)]
        if rows:
            t = doc.add_table(rows=len(rows), cols=len(rows[0]))
            t.style = 'Table Grid'
            for ri, row in enumerate(rows):
                for ci, cell in enumerate(row):
                    p = t.cell(ri, ci).paragraphs[0]
                    p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.space_after = Pt(2)
                    add_inline(p, cell)
                    for run in p.runs:
                        run.font.size = Pt(9.5)
                        run.font.name = 'Times New Roman'
                        if ri == 0:
                            run.bold = True
        table_buf.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s.startswith('```'):
            in_code = not in_code
            i += 1
            continue

        if in_code:
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(line if line else ' ')
            r.font.name = 'Courier New'
            r.font.size = Pt(9)
            i += 1
            continue

        if s == '<!--TITLEPAGE-->':
            in_title = True; i += 1; continue
        if s == '<!--/TITLEPAGE-->':
            in_title = False; i += 1; continue

        if s.startswith('|'):
            table_buf.append(s); i += 1; continue
        flush_table()

        if s == '\\newpage':
            doc.add_page_break(); i += 1; continue
        if not s:
            i += 1; continue

        if s.startswith('#### '):
            p = doc.add_paragraph()
            r = p.add_run(s[5:]); r.bold = True; r.italic = True; r.font.size = Pt(12)
        elif s.startswith('### '):
            p = doc.add_paragraph()
            r = p.add_run(s[4:]); r.bold = True; r.font.size = Pt(12.5)
        elif s.startswith('## '):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s[3:]); r.bold = True; r.font.size = Pt(14)
        elif s.startswith('# '):
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s[2:]); r.bold = True; r.font.size = Pt(16)
        elif s.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            add_inline(p, s[2:])
        elif re.match(r'^\d+\.\s', s):
            p = doc.add_paragraph(style='List Number')
            add_inline(p, re.sub(r'^\d+\.\s', '', s))
        elif s.startswith('!['):
            m = re.match(r'!\[(.*?)\]\((.*?)\)', s)
            if m:
                cap, path = m.group(1), os.path.join(BASE, m.group(2))
                if os.path.exists(path):
                    doc.add_picture(path, width=Inches(5.9))
                    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(cap); r.italic = True; r.font.size = Pt(10)
        else:
            p = doc.add_paragraph()
            if in_title:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(p, s)
        i += 1

    flush_table()
    doc.save(docx_path)
    print('saved', docx_path)

if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2])
