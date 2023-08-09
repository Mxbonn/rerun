#include "recording_stream.hpp"

#include <rerun.h>

#include <arrow/buffer.h>
#include <vector>

namespace rerun {
    static int32_t store_kind_to_c(StoreKind store_kind) {
        switch (store_kind) {
            case StoreKind::Recording:
                return RERUN_STORE_KIND_RECORDING;

            case StoreKind::Blueprint:
                return RERUN_STORE_KIND_BLUEPRINT;
        }
    }

    RecordingStream::RecordingStream(const char* app_id, StoreKind store_kind)
        : _store_kind(store_kind) {
        rr_store_info store_info;
        store_info.application_id = app_id;
        store_info.store_kind = store_kind_to_c(store_kind);

        this->_id = rr_recording_stream_new(&store_info);
    }

    RecordingStream::~RecordingStream() {
        rr_recording_stream_free(this->_id);
    }

    void RecordingStream::set_global() {
        rr_recording_stream_set_global(_id, store_kind_to_c(_store_kind));
    }

    void RecordingStream::set_thread_local() {
        rr_recording_stream_set_thread_local(_id, store_kind_to_c(_store_kind));
    }

    RecordingStream& RecordingStream::current(StoreKind store_kind) {
        switch (store_kind) {
            case StoreKind::Recording: {
                static RecordingStream current_recording(
                    RERUN_REC_STREAM_CURRENT_RECORDING,
                    StoreKind::Recording
                );
                return current_recording;
            }
            case StoreKind::Blueprint: {
                static RecordingStream current_blueprint(
                    RERUN_REC_STREAM_CURRENT_BLUEPRINT,
                    StoreKind::Blueprint
                );
                return current_blueprint;
            }
        }
    }

    void RecordingStream::connect(const char* tcp_addr, float flush_timeout_sec) {
        rr_recording_stream_connect(_id, tcp_addr, flush_timeout_sec);
    }

    void RecordingStream::save(const char* path) {
        rr_recording_stream_save(_id, path);
    }

    void RecordingStream::flush_blocking() {
        rr_recording_stream_flush_blocking(_id);
    }

    void RecordingStream::log_data_row(
        const char* entity_path, size_t num_instances, size_t num_data_cells,
        const DataCell* data_cells
    ) {
        // Map to C API:
        std::vector<rr_data_cell> c_data_cells;
        c_data_cells.reserve(num_data_cells);
        for (size_t i = 0; i < num_data_cells; ++i) {
            c_data_cells.push_back({
                .component_name = data_cells[i].component_name,
                .num_bytes = static_cast<uint64_t>(data_cells[i].buffer->size()),
                .bytes = data_cells[i].buffer->data(),
            });
        }

        const rr_data_row c_data_row = {
            .entity_path = entity_path,
            .num_instances = static_cast<uint32_t>(num_instances),
            .num_data_cells = static_cast<uint32_t>(num_data_cells),
            .data_cells = c_data_cells.data(),
        };

        rr_log(_id, &c_data_row, true);
    }
} // namespace rerun