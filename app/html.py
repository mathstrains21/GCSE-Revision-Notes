from app import env

def render_template(template_name, **context):
    template = env.get_template(template_name)
    return template.render(**context)

def render_data(data):
    return render_template('base.html', **data)
