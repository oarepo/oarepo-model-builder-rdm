from oarepo_model_builder.datatypes import DataTypeComponent
from oarepo_model_builder.datatypes.components.model import ServiceModelComponent
from oarepo_model_builder.datatypes.model import ModelDataType
from oarepo_model_builder.datatypes.components.model.utils import set_default

class RDMServiceComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [ServiceModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        components_to_remove = [
            '{{oarepo_runtime.services.files.FilesComponent}}',
            '{{invenio_drafts_resources.services.records.components.DraftFilesComponent}}'
        ]
        datatype.service_config["components"] = [
            component for component in datatype.service_config["components"]
            if component not in components_to_remove
        ]

        if not datatype.profile in ["record", "draft"]:
            return

        datatype.definition["service"]["base-classes"] = ["invenio_rdm_records.services.services.RDMRecordService"]
        datatype.definition["service-config"]["base-classes"] = ["oarepo_runtime.services.config.service.PermissionsPresetsConfigMixin",
                                                                 "invenio_rdm_records.services.config.RDMRecordServiceConfig"]