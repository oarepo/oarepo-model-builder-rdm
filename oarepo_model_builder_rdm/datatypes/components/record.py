from oarepo_model_builder.datatypes import ModelDataType
from oarepo_model_builder.datatypes.components import RecordModelComponent
from oarepo_model_builder.datatypes import DataTypeComponent
from oarepo_model_builder_drafts.datatypes.components import DraftRecordModelComponent

class RDMRecordModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [RecordModelComponent, DraftRecordModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if datatype.root.profile == "draft":
            datatype.definition["record"]["base-classes"] = ["invenio_rdm_records.records.api.RDMDraft"]
        elif datatype.root.profile == "record":
            datatype.definition["record"]["base-classes"] = ["invenio_rdm_records.records.api.RDMRecord"]
