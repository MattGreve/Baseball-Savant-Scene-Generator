# =========================
# material_utils.py
# =========================

"""
Material utility functions for Baseball Savant Scene Generator.
"""

import maya.cmds as cmds


def create_material(
    name="default_material",
    color=(1, 1, 1)
):
    """
    Creates a lambert material.

    Returns:
        str: Material name.
    """
    pass


def assign_material(
    material,
    object_name
):
    """
    Assigns material to object.

    Returns:
        None
    """
    pass


def create_gradient_material(
    low_color=(0, 0, 1),
    high_color=(1, 0, 0)
):
    """
    Creates a gradient-based material setup.

    Returns:
        str: Material name.
    """
    pass


def assign_material_by_value(
    value=0
):
    """
    Assigns material based on stat value.

    Returns:
        str: Material name.
    """
    pass
