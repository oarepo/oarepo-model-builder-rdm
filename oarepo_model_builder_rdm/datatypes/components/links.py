import marshmallow as ma
from oarepo_model_builder.datatypes import (
    DataType,
    DataTypeComponent,
    ModelDataType,
    Section,
)
from oarepo_model_builder.datatypes.components import DefaultsModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.datatypes.model import Link
from oarepo_model_builder.utils.links import url_prefix2link
from oarepo_model_builder.utils.python_name import Import

class RDMLinksComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [DefaultsModelComponent]

    def process_links(self, datatype, section: Section, **kwargs):

        if datatype.root.profile == "record":
            section.config.setdefault("links_item", {})
            section.config["links_item"] += [
                Link(
                    name="access_request",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access/request"',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                    ],
                ),
                Link(
                    name="access_links",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access/links"',
                        'when=has_permission("manage")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                        Import("oarepo_runtime.services.config.has_permission"),
                    ],
                ),
                Link(
                    name="access_grants",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access/grants"',
                        'when=has_permission("manage")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                        Import("oarepo_runtime.services.config.has_permission"),
                    ],
                ),
                Link(
                    name="access_users",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access/users"',
                        'when=has_permission("manage")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                        Import("oarepo_runtime.services.config.has_permission"),
                    ],
                ),
                Link(
                    name="access_groups",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access/groups"',
                        'when=to_oarepo_condition(_groups_enabled) & has_permission("manage")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                        Import("oarepo_runtime.services.config.has_permission"),
                        Import("invenio_rdm_records.services.config._groups_enabled"),
                        Import("oarepo_runtime.services.config.link_conditions.to_oarepo_condition")
                    ],
                ),
                Link(
                    name="access",
                    link_class="RecordLink",
                    link_args=[
                        '"{+api}/records/{id}/access"',
                        'when=has_permission("manage")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.RecordLink"),
                        Import("oarepo_runtime.services.config.has_permission"),
                    ],
                ),
            ]