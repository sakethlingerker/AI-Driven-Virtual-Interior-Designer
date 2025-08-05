def get_selected_cost_links(accent_color, wood_finish, wall_color, tiles):
    base_url = "https://materialdepot.in"
    return f"""
    <ul>
    <li><b>Accent Color</b> ({accent_color}): <a href='{base_url}/primary%20color%20{accent_color.replace(" ", "%20")}-search' target='_blank'>View Materials</a></li>
    <li><b>Wood Finish</b> ({wood_finish}): <a href='{base_url}/wood%20finish%20{wood_finish.replace(" ", "%20")}-search' target='_blank'>View Materials</a></li>
    <li><b>Wall Color</b> ({wall_color}): <a href='{base_url}/wall%20color%20{wall_color.replace(" ", "%20")}-search' target='_blank'>View Materials</a></li>
    <li><b>Tiles</b> ({tiles}): <a href='{base_url}/tiles%20{tiles.replace(" ", "%20")}-search' target='_blank'>View Materials</a></li>
    </ul>
    """
