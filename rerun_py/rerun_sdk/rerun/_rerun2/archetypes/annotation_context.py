# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/archetypes/annotation_context.fbs".

# You can extend this class by creating a "AnnotationContextExt" class in "annotation_context_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import (
    Archetype,
)

__all__ = ["AnnotationContext"]


@define(str=False, repr=False)
class AnnotationContext(Archetype):
    """
    The `AnnotationContext` provides additional information on how to display entities.

    Entities can use `ClassId`s and `KeypointId`s to provide annotations, and
    the labels and colors will be looked up in the appropriate
    `AnnotationContext`. We use the *first* annotation context we find in the
    path-hierarchy when searching up through the ancestors of a given entity
    path.

    Example
    -------
    ```python
    import rerun as rr
    import rerun.experimental as rr2

    rr.init("rerun_example_annotation_context_rects", spawn=True)

    # Log an annotation context to assign a label and color to each class
    rr2.log("/", rr2.AnnotationContext([(1, "red", (255, 0, 0)), (2, "green", (0, 255, 0))]))

    # Log a batch of 2 rectangles with different `class_ids`
    rr2.log("detections", rr2.Boxes2D(mins=[[-2, -2], [0, 0]], sizes=[[3, 3], [2, 2]], class_ids=[1, 2]))

    # Log an extra rect to set the view bounds
    rr2.log("bounds", rr2.Boxes2D(half_sizes=[2.5, 2.5]))
    ```
    """

    # You can define your own __init__ function as a member of AnnotationContextExt in annotation_context_ext.py

    context: components.AnnotationContextArray = field(
        metadata={"component": "required"},
        converter=components.AnnotationContextArray.from_similar,  # type: ignore[misc]
    )
    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
