// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/re_types/definitions/rerun/testing/components/fuzzy.fbs".

#![allow(trivial_numeric_casts)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::iter_on_single_items)]
#![allow(clippy::map_flatten)]
#![allow(clippy::match_wildcard_for_single_variants)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]
#![allow(clippy::unnecessary_cast)]

#[derive(Clone, Debug, Default, PartialEq)]
pub struct AffixFuzzer6(pub Option<crate::testing::datatypes::AffixFuzzer1>);

impl<T: Into<Option<crate::testing::datatypes::AffixFuzzer1>>> From<T> for AffixFuzzer6 {
    fn from(v: T) -> Self {
        Self(v.into())
    }
}

impl std::borrow::Borrow<Option<crate::testing::datatypes::AffixFuzzer1>> for AffixFuzzer6 {
    #[inline]
    fn borrow(&self) -> &Option<crate::testing::datatypes::AffixFuzzer1> {
        &self.0
    }
}

impl std::ops::Deref for AffixFuzzer6 {
    type Target = Option<crate::testing::datatypes::AffixFuzzer1>;

    #[inline]
    fn deref(&self) -> &Option<crate::testing::datatypes::AffixFuzzer1> {
        &self.0
    }
}

impl<'a> From<AffixFuzzer6> for ::std::borrow::Cow<'a, AffixFuzzer6> {
    #[inline]
    fn from(value: AffixFuzzer6) -> Self {
        std::borrow::Cow::Owned(value)
    }
}

impl<'a> From<&'a AffixFuzzer6> for ::std::borrow::Cow<'a, AffixFuzzer6> {
    #[inline]
    fn from(value: &'a AffixFuzzer6) -> Self {
        std::borrow::Cow::Borrowed(value)
    }
}

impl crate::Loggable for AffixFuzzer6 {
    type Name = crate::ComponentName;

    #[inline]
    fn name() -> Self::Name {
        "rerun.testing.components.AffixFuzzer6".into()
    }

    #[allow(unused_imports, clippy::wildcard_imports)]
    #[inline]
    fn arrow_datatype() -> arrow2::datatypes::DataType {
        use ::arrow2::datatypes::*;
        DataType::Struct(vec![
            Field {
                name: "single_float_optional".to_owned(),
                data_type: DataType::Float32,
                is_nullable: true,
                metadata: [].into(),
            },
            Field {
                name: "single_string_required".to_owned(),
                data_type: DataType::Utf8,
                is_nullable: false,
                metadata: [].into(),
            },
            Field {
                name: "single_string_optional".to_owned(),
                data_type: DataType::Utf8,
                is_nullable: true,
                metadata: [].into(),
            },
            Field {
                name: "many_floats_optional".to_owned(),
                data_type: DataType::List(Box::new(Field {
                    name: "item".to_owned(),
                    data_type: DataType::Float32,
                    is_nullable: false,
                    metadata: [].into(),
                })),
                is_nullable: true,
                metadata: [].into(),
            },
            Field {
                name: "many_strings_required".to_owned(),
                data_type: DataType::List(Box::new(Field {
                    name: "item".to_owned(),
                    data_type: DataType::Utf8,
                    is_nullable: false,
                    metadata: [].into(),
                })),
                is_nullable: false,
                metadata: [].into(),
            },
            Field {
                name: "many_strings_optional".to_owned(),
                data_type: DataType::List(Box::new(Field {
                    name: "item".to_owned(),
                    data_type: DataType::Utf8,
                    is_nullable: false,
                    metadata: [].into(),
                })),
                is_nullable: true,
                metadata: [].into(),
            },
            Field {
                name: "flattened_scalar".to_owned(),
                data_type: DataType::Float32,
                is_nullable: false,
                metadata: [].into(),
            },
            Field {
                name: "almost_flattened_scalar".to_owned(),
                data_type: <crate::testing::datatypes::FlattenedScalar>::arrow_datatype(),
                is_nullable: false,
                metadata: [].into(),
            },
            Field {
                name: "from_parent".to_owned(),
                data_type: DataType::Boolean,
                is_nullable: true,
                metadata: [].into(),
            },
        ])
    }

    #[allow(unused_imports, clippy::wildcard_imports)]
    fn to_arrow_opt<'a>(
        data: impl IntoIterator<Item = Option<impl Into<::std::borrow::Cow<'a, Self>>>>,
    ) -> crate::SerializationResult<Box<dyn ::arrow2::array::Array>>
    where
        Self: Clone + 'a,
    {
        use crate::{Loggable as _, ResultExt as _};
        use ::arrow2::{array::*, datatypes::*};
        Ok({
            let (somes, data0): (Vec<_>, Vec<_>) = data
                .into_iter()
                .map(|datum| {
                    let datum: Option<::std::borrow::Cow<'a, Self>> = datum.map(Into::into);
                    let datum = datum
                        .map(|datum| {
                            let Self(data0) = datum.into_owned();
                            data0
                        })
                        .flatten();
                    (datum.is_some(), datum)
                })
                .unzip();
            let data0_bitmap: Option<::arrow2::bitmap::Bitmap> = {
                let any_nones = somes.iter().any(|some| !*some);
                any_nones.then(|| somes.into())
            };
            {
                _ = data0_bitmap;
                crate::testing::datatypes::AffixFuzzer1::to_arrow_opt(data0)?
            }
        })
    }

    #[allow(unused_imports, clippy::wildcard_imports)]
    fn from_arrow_opt(
        arrow_data: &dyn ::arrow2::array::Array,
    ) -> crate::DeserializationResult<Vec<Option<Self>>>
    where
        Self: Sized,
    {
        use crate::{Loggable as _, ResultExt as _};
        use ::arrow2::{array::*, buffer::*, datatypes::*};
        Ok(
            crate::testing::datatypes::AffixFuzzer1::from_arrow_opt(arrow_data)
                .with_context("rerun.testing.components.AffixFuzzer6#single_optional")?
                .into_iter()
                .map(Ok)
                .map(|res| res.map(|v| Some(Self(v))))
                .collect::<crate::DeserializationResult<Vec<Option<_>>>>()
                .with_context("rerun.testing.components.AffixFuzzer6#single_optional")
                .with_context("rerun.testing.components.AffixFuzzer6")?,
        )
    }
}
