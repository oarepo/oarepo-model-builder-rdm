from oarepo_model_builder.datatypes import ModelDataType
from oarepo_model_builder_drafts.datatypes.components import PublishedServiceComponent
from oarepo_model_builder.datatypes import DataTypeComponent

class RDMPublishedServiceComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [PublishedServiceComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        pass
        # datatype.definition["published-service"]["base-classes"] = ["invenio_rdm_records.services.services.RDMRecordService"]
        # datatype.definition["published-service-config"]["base-classes"] = [
        #     "oarepo_runtime.services.config.service.PermissionsPresetsConfigMixin",
        #     "invenio_rdm_records.services.config.RDMRecordServiceConfig"]