# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/archetypes/boxes2d.fbs".

# You can extend this class by creating a "Boxes2DExt" class in "boxes2d_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import (
    Archetype,
)
from .boxes2d_ext import Boxes2DExt

__all__ = ["Boxes2D"]


@define(str=False, repr=False, init=False)
class Boxes2D(Boxes2DExt, Archetype):
    """
    A batch of 2d boxes with half-extents and optional center, rotations, rotations, colors etc.

    Example
    -------
    Simple 2D boxes:
    ```python
    import rerun as rr
    import rerun.experimental as rr2

    rr.init("rerun_example_box2d", spawn=True)

    rr2.log("simple", rr2.Boxes2D(mins=[-1, -1], sizes=[2, 2]))

    # Log an extra rect to set the view bounds
    rr2.log("bounds", rr2.Boxes2D(sizes=[4.0, 3.0]))
    ```
    """

    # __init__ can be found in boxes2d_ext.py

    half_sizes: components.HalfSizes2DArray = field(
        metadata={"component": "required"},
        converter=components.HalfSizes2DArray.from_similar,  # type: ignore[misc]
    )
    """
    All half-extents that make up the batch of boxes.
    """

    centers: components.Position2DArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.Position2DArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional center positions of the boxes.
    """

    radii: components.RadiusArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.RadiusArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional radii for the lines that make up the boxes.
    """

    colors: components.ColorArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional colors for the boxes.
    """

    labels: components.TextArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional text labels for the boxes.
    """

    draw_order: components.DrawOrderArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.DrawOrderArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    An optional floating point value that specifies the 2D drawing order.
    Objects with higher values are drawn on top of those with lower values.

    The default for 2D boxes is 10.0.
    """

    class_ids: components.ClassIdArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ClassIdArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Optional `ClassId`s for the boxes.

    The class ID provides colors and labels if not specified explicitly.
    """

    instance_keys: components.InstanceKeyArray | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.InstanceKeyArray.optional_from_similar,  # type: ignore[misc]
    )
    """
    Unique identifiers for each individual boxes in the batch.
    """

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
