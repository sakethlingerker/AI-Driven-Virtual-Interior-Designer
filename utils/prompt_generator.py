from jinja2 import Template
 
template_str = """
High quality interior render of a {{ adjective }} {{ room | lower }}, in {{ architecture }} architecture,
with {{ theme }} style, painted in {{ wall }} with {{ color }} accents, {{ wood }} wood finishes,
and {{ tile }} flooring.
"""

def generate_prompt(room, adjective, architecture, theme, color, wood, wall, tile):
    template = Template(template_str)
    return template.render(
        room=room,
        adjective=adjective,
        architecture=architecture,
        theme=theme,
        color=color,
        wood=wood,
        wall=wall,
        tile=tile
    )
