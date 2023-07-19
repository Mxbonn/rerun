// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/testing/components/fuzzy.fbs"

#pragma once

#include <cstdint>
#include <optional>
#include <utility>
#include <vector>

namespace rr {
    namespace components {
        struct AffixFuzzer11 {
            std::optional<std::vector<float>> many_floats_optional;

            AffixFuzzer11(std::optional<std::vector<float>> many_floats_optional)
                : many_floats_optional(std::move(many_floats_optional)) {}
        };
    } // namespace components
} // namespace rr