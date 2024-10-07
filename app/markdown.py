def convert_to_markdown(text: str) -> str:
    return text.strip()

def get_data(text: str) -> str:
    return [get_section_data(section) for section in text.strip().split('\n\n')]

def get_section_data(text: str) -> str:
    if text.startswith('#'):
        return get_heading_data(text)
    elif text.startswith('|'):
        return get_table_data(text)
    else:
        return get_paragraph_data(text)

def get_heading_data(text: str) -> str:
    heading, content = text.split(' ',1)
    size = len(heading)
    content = get_inline_html(content)
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
    headings = [get_inline_html(heading) for heading in text.split('|') if heading != '']
    return {
        "type": "table_head",
        "content": headings,
    }

def get_table_body_row_data(text: str) -> str:
    cells = [get_inline_html(cell) for cell in text.split('|') if cell != '']
    return {
        "type": "table_row",
        "content": cells,
    }

def get_paragraph_data(text: str) -> str:
    return {
        "type": "paragraph",
        "content": get_inline_html(text),
    }

def get_inline_html(text: str) -> str:
    return text.strip().replace('\n', ' ')
