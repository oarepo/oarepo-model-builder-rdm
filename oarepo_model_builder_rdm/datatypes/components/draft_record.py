from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder_drafts.datatypes.components import DraftParentComponent

class RDMDraftParentComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DraftParentComponent]

    def process_mb_invenio_drafts_parent_additional_fields(
        self, datatype, section, **kwargs
    ):
        obj = section.config.setdefault("additional-fields", {})
        if 'owners' in obj and obj['owners'] == '{{oarepo_runtime.records.systemfields.owner.OwnersField}}()':
            del obj['owners']


    def before_model_prepare(self, datatype, *, context, **kwargs):
        if "draft-parent-record" in datatype.definition:
            datatype.definition["draft-parent-record"]["base-classes"] = ["invenio_rdm_records.records.api.RDMParent"]