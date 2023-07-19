// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/components/radius.fbs"

#pragma once

#include <cstdint>
#include <utility>

namespace rr {
    namespace components {
        /// A Radius component.
        struct Radius {
            float value;

            Radius(float value) : value(std::move(value)) {}
        };
    } // namespace components
} // namespace rr