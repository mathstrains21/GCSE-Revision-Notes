import re

def convert_to_markdown(text: str) -> str:
    return text.strip()

def get_data(text: str) -> str:
    return [get_section_data(section) for section in text.strip().split('\n\n')]

def get_section_data(text: str) -> str:
    if text.startswith('#'):
        return get_heading_data(text)
    elif text.startswith('|'):
        return get_table_data(text)
    elif re.match(r'^([-_*])\1{2,}$', text):
        return {"type": "hr"}
    else:
        return get_paragraph_data(text)

def get_heading_data(text: str) -> str:
    heading, content = text.split(' ',1)
    size = len(heading)
    content = get_inline_data(content)
    return {
        "type": "heading",
        "size": size,
        "content": content,
    }

def get_table_data(text: str) -> str:
    head, _, *body = text.split('\n')
    head_data = get_table_head_data(head)
    body_data = [get_table_body_row_data(row) for row in body]
    return {
        "type": "table",
        "head": head_data,
        "body": body_data,
    }

def get_table_head_data(text: str) -> str:
    headings = [get_inline_data(heading) for heading in text.split('|') if heading != '']
    return {
        "type": "table_head",
        "content": headings,
    }

def get_table_body_row_data(text: str) -> str:
    cells = [get_inline_data(cell) for cell in text.split('|') if cell != '']
    return {
        "type": "table_row",
        "content": cells,
    }

def get_paragraph_data(text: str) -> str:
    return {
        "type": "paragraph",
        "content": get_inline_data(text),
    }

def get_inline_data(text: str) -> str:
    text = text.strip()
    if text == '':
        return []
    # Bold and Italic
    if match := re.match(r'(?P<before>.*?)\*\*\*(?P<bold_italic>.*?)\*\*\*(?P<after>.*)', text):
        return [
            *get_inline_data(match.group('before')),
            {"type": "bold", "content": [{"type": "italic", "content": get_inline_data(match.group('bold_italic'))}]},
            *get_inline_data(match.group('after')),
        ]
    # Bold
    if match := re.match(r'(?P<before>.*?)\*\*(?P<bold>.*?)\*\*(?P<after>.*)', text):
        return [
            *get_inline_data(match.group('before')),
            {"type": "bold", "content": get_inline_data(match.group('bold'))},
            *get_inline_data(match.group('after')),
        ]
    # Italic
    if match := re.match(r'(?P<before>.*?)\*(?P<italic>.*?)\*(?P<after>.*)', text):
        return [
            *get_inline_data(match.group('before')),
            {"type": "italic", "content": get_inline_data(match.group('italic'))},
            *get_inline_data(match.group('after')),
        ]
    # Inline Code
    if match := re.match(r'(?P<before>.*?)`(?P<code>.*?)`(?P<after>.*)', text):
        return [
            *get_inline_data(match.group('before')),
            {"type": "code", "content": match.group('code')},
            *get_inline_data(match.group('after')),
        ]
    return [{"type": "text", "content": text}]
