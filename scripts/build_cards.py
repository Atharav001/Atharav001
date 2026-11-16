"""Build the small editorial project cards used by the profile README."""
from pathlib import Path
from html import escape

root = Path(__file__).resolve().parents[1] / 'assets'
projects = [
    ('research', '01', 'RESEARCH SYSTEMS', 'Agentic Deep', 'Research', 'Hybrid retrieval / cited synthesis', '#9dbca7', '''<circle cx="310" cy="167" r="54" fill="none" stroke="#9dbca7" stroke-opacity=".38"/><circle cx="310" cy="167" r="24" fill="none" stroke="#9dbca7" stroke-opacity=".3"/><path d="M252 133L310 167L348 113M310 167L363 206M310 167L260 210" fill="none" stroke="#9dbca7" stroke-opacity=".44"/><g fill="#c7ddca"><circle cx="252" cy="133" r="4"/><circle cx="348" cy="113" r="4"/><circle cx="363" cy="206" r="4"/><circle cx="260" cy="210" r="4"/></g>'''),
    ('router', '02', 'INTELLIGENT ROUTING', 'WhatsApp', 'Message Router', 'Multimodal signals / safety controls', '#9cbbd1', '''<path d="M274 167H313M313 167L345 125M313 167L345 167M313 167L345 209" fill="none" stroke="#9cbbd1" stroke-width="2" stroke-opacity=".55"/><circle cx="270" cy="167" r="8" fill="#9cbbd1"/><g fill="none" stroke="#9cbbd1" stroke-opacity=".65"><circle cx="348" cy="125" r="8"/><circle cx="348" cy="167" r="8"/><circle cx="348" cy="209" r="8"/></g>'''),
    ('pipeline', '03', 'MULTIMODAL INFERENCE', 'Two-Step', 'Pipeline', 'Blind perception / grounded decisions', '#c5ad98', '''<circle cx="278" cy="167" r="42" fill="none" stroke="#c5ad98" stroke-opacity=".55"/><circle cx="346" cy="167" r="42" fill="none" stroke="#c5ad98" stroke-opacity=".55"/><path d="M293 167H330" stroke="#c5ad98" stroke-width="2"/><path d="M323 161L331 167L323 173" fill="none" stroke="#c5ad98" stroke-width="2"/><circle cx="278" cy="167" r="5" fill="#d8c1ad"/><circle cx="346" cy="167" r="5" fill="#d8c1ad"/>'''),
]
for filename, number, category, line1, line2, note, color, motif in projects:
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="390" height="260" viewBox="0 0 390 260" role="img" aria-label="{escape(line1+' '+line2)}">
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#182027"/><stop offset="1" stop-color="#111b1d"/></linearGradient><pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#e0eee4" opacity=".08"/></pattern></defs>
<rect x="1" y="1" width="388" height="258" rx="17" fill="url(#bg)" stroke="{color}" stroke-opacity=".38"/>
<path d="M28 39H362" stroke="{color}" stroke-opacity=".24"/>
<path d="M28 39H72" stroke="{color}" stroke-width="2"/>
<rect x="1" y="1" width="388" height="258" rx="17" fill="url(#dots)"/>
<text x="28" y="27" fill="{color}" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700" letter-spacing="2.3">{category}</text>
<text x="362" y="27" fill="#92a59a" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="11" letter-spacing="1.5">{number} / 03</text>
<text x="28" y="120" fill="#f1f3ee" font-family="Arial, Helvetica, sans-serif" font-size="29" font-weight="600" letter-spacing="-.7">{line1}</text>
<text x="28" y="154" fill="#f1f3ee" font-family="Arial, Helvetica, sans-serif" font-size="29" font-weight="600" letter-spacing="-.7">{line2}</text>
{motif}
<path d="M28 219H362" stroke="{color}" stroke-opacity=".25"/>
<text x="28" y="240" fill="#b4c5bb" font-family="Arial, Helvetica, sans-serif" font-size="11" letter-spacing=".4">{note}</text>
<path d="M344 231h14m-6-6 6 6-6 6" fill="none" stroke="{color}" stroke-width="1.5"/>
</svg>'''
    (root / f'{filename}.svg').write_text(svg)
