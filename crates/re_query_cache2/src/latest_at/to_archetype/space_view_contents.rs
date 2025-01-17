// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/rust/to_archetype.rs

#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]

use crate::CachedLatestAtResults;
use re_query2::{PromiseResolver, PromiseResult};
use re_types_core::{Archetype, Loggable as _};
use std::sync::Arc;

impl crate::ToArchetype<re_types::blueprint::archetypes::SpaceViewContents>
    for CachedLatestAtResults
{
    #[inline]
    fn to_archetype(
        &self,
        resolver: &PromiseResolver,
    ) -> PromiseResult<crate::Result<re_types::blueprint::archetypes::SpaceViewContents>> {
        re_tracing::profile_function!(<re_types::blueprint::archetypes::SpaceViewContents>::name());

        // --- Required ---

        // --- Recommended/Optional ---

        use re_types::blueprint::components::QueryExpression;
        let query = match self
            .get_or_empty(<QueryExpression>::name())
            .to_dense::<QueryExpression>(resolver)
        {
            PromiseResult::Pending => return PromiseResult::Pending,
            PromiseResult::Error(promise_err) => return PromiseResult::Error(promise_err),
            PromiseResult::Ready(query_res) => match query_res {
                Ok(data) => data.to_vec(),
                Err(query_err) => return PromiseResult::Ready(Err(query_err)),
            },
        };

        // ---

        let arch = re_types::blueprint::archetypes::SpaceViewContents { query };

        PromiseResult::Ready(Ok(arch))
    }
}
