from pathlib import Path
import re
root = Path('g:/Programming/HTML_Programming/IDK')
button_re = re.compile(r'<button(?![^>]*\bclass=)([^>]*)>', re.IGNORECASE)
updated_html = []
for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    new_text = button_re.sub(r'<button class="cta-button"\1>', text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        updated_html.append(path.name)

css_path = root / 'style.css'
css_text = css_path.read_text(encoding='utf-8')
css_text_new = css_text
css_text_new = css_text_new.replace('.btn-seg button,\n.hero-btn button {', '.btn-seg button,\n.hero-btn button,\n.cta-button {')
css_text_new = css_text_new.replace('.btn-seg button:hover,\n.btn-seg button:focus-visible,\n.hero-btn button:hover,\n.hero-btn button:focus-visible {', '.btn-seg button:hover,\n.btn-seg button:focus-visible,\n.hero-btn button:hover,\n.hero-btn button:focus-visible,\n.cta-button:hover,\n.cta-button:focus-visible {')
css_text_new = css_text_new.replace('.btn-seg button:focus-visible,\n.hero-btn button:focus-visible {', '.btn-seg button:focus-visible,\n.hero-btn button:focus-visible,\n.cta-button:focus-visible {')
updated_css = False
if css_text_new != css_text:
    css_path.write_text(css_text_new, encoding='utf-8')
    updated_css = True

print('updated_html=', updated_html)
print('updated_css=', updated_css)
