# =================
geometry_utils.py
# =================
import maya.cmds as cmds
 
 
def create_bar(height=1.0, position=(0.0, 0.0, 0.0), width=0.8, depth=0.8, name="stat_bar"):
    """
    Create a single polyCube bar.
 
    Parameters
    ----------
    height : float
    position : tuple of float
    width : float
    depth : float
    name : str
 
    Returns
    -------
    str
        Maya node name of the created polyCube.
    """
    h = max(height, 0.01)
    bar = cmds.polyCube(width=width, height=h, depth=depth, name=name)[0]
    cmds.move(position[0], position[1] + h / 2.0, position[2], bar, absolute=True)
    return bar
 
 
def create_bar_graph(values=None, labels=None, spacing=1.5, bar_width=0.8, bar_depth=0.8):
    """
    Build a row of bars from a list of values.
 
    Parameters
    ----------
    values : list of float
    labels : list of str
    spacing : float
    bar_width : float
    bar_depth : float
 
    Returns
    -------
    list of str
        Maya node names of every created bar.
    """
    if values is None:
        values = [1.0, 2.0, 3.0]
    if labels is None:
        labels = ["bar_{}".format(i) for i in range(len(values))]
 
    max_val = max(values) if max(values) != 0 else 1.0
    bars = []
 
    for i, (val, label) in enumerate(zip(values, labels)):
        norm_height = (val / max_val) * 10.0
        safe_name = label.replace(" ", "_").replace(".", "_") + "_bar"
        bar = create_bar(
            height=norm_height,
            position=(i * spacing, 0.0, 0.0),
            width=bar_width,
            depth=bar_depth,
            name=safe_name
        )
        bars.append(bar)
 
    return bars
 
 
def create_text_label(text="Label", position=(0.0, 0.0, 0.0), scale=0.3, name="text_label"):
    """
    Create a text label using NURBS curves (textCurves).
 
    Parameters
    ----------
    text : str
    position : tuple of float
    scale : float
    name : str
 
    Returns
    -------
    str
        Maya node name of the created group transform.
    """
    grp = cmds.textCurves(font="Arial", text=text, ch=False, name=name)[0]
    cmds.scale(scale, scale, scale, grp)
    cmds.move(position[0], position[1], position[2], grp, absolute=True)
    return grp
 
 
def create_ground_plane(width=20.0, depth=10.0, spacing=1.5, name="ground_plane"):
    """
    Create a flat polyPlane to contain the bar graph scene.
 
    Parameters
    ----------
    width : float
        Extent along X, should cover the full width of the graph.
    depth : float
        Extent along Z.
    spacing : float
        Bar spacing, used to calculate the correct centre offset.
    name : str
 
    Returns
    -------
    str
        Maya node name of the created polyPlane.
    """
    plane = cmds.polyPlane(
        width=width,
        height=depth,
        subdivisionsX=1,
        subdivisionsY=1,
        name=name
    )[0]
    # Center = midpoint between first bar (x=0) and last bar (x=width-spacing)
    cmds.move((width - spacing) / 2.0, 0.0, 0.0, plane, absolute=True)
    return plane
 
 
# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------
 
if __name__ == "__main__":
 
    test_values  = [0.312, 0.285, 0.301, 0.275, 0.330]
    test_labels  = ["Judge", "Ohtani", "Betts", "Acuna", "Freeman"]
    test_spacing = 1.5
 
    # 1. Ground plane
    create_ground_plane(
        width=len(test_values) * test_spacing + test_spacing,
        depth=4.0,
        spacing=test_spacing,
        name="ground_plane"
    )
 
    # 2. Bars
    bars = create_bar_graph(
        values=test_values,
        labels=test_labels,
        spacing=test_spacing
    )
 
    # 3. Value labels above each bar
    max_val = max(test_values)
    for i, (val, label) in enumerate(zip(test_values, test_labels)):
        norm_h = (val / max_val) * 10.0
        create_text_label(
            text=str(round(val, 3)),
            position=(i * test_spacing, norm_h + 0.4, 0.0),
            scale=0.1,
            name="{}_val".format(label)
        )
 
    # 4. Name labels below each bar
    for i, label in enumerate(test_labels):
        create_text_label(
            text=label,
            position=(i * test_spacing, 0.01, 1.5),
            scale=0.1,
            name="{}_name".format(label)
        )
 
    cmds.viewFit(all=True)
    print("Test complete. Bars:", bars)
 
