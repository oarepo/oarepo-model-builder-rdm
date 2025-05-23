from oarepo_model_builder.datatypes import DataTypeComponent
from oarepo_model_builder.datatypes.components.model import ResourceModelComponent
from oarepo_model_builder.datatypes.model import ModelDataType

class RDMResourceComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [ResourceModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):

        if datatype.profile not in ["record", "draft"]:
            return
        datatype.definition["resource"]["base-classes"].insert(0, "oarepo_runtime.resources.resource.SearchAllResourceMixin")