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
 
 
def create_ground_plane(width=20.0, depth=10.0, name="ground_plane"):
    """
    Create a flat polyPlane to contain the bar graph scene.
 
    Parameters
    ----------
    width : float
        Extent along X, should cover the full width of the graph.
    depth : float
        Extent along Z.
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
    return plane
 
