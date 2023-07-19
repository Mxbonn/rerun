// NOTE: This file was autogenerated by re_types_builder; DO NOT EDIT.
// Based on "crates/re_types/definitions/rerun/testing/components/fuzzy.fbs"

#pragma once

#include <cstdint>
#include <string>
#include <utility>
#include <vector>

namespace rr {
    namespace components {
        struct AffixFuzzer12 {
            std::vector<std::string> many_strings_required;

            AffixFuzzer12(std::vector<std::string> many_strings_required)
                : many_strings_required(std::move(many_strings_required)) {}
        };
    } // namespace components
} // namespace rr