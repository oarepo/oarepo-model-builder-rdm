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
                    name="archive",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["archive"], "read_files"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="archive_media",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["archive_media"], "read_files"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="access_links",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["access_links"], "manage"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="access_grants",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["access_grants"], "manage"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="access_users",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["access_users"], "manage"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="access_groups",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["access_groups"], "manage"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="access",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["access"], "manage"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
                Link(
                    name="communities-suggestions",
                    link_class="PermissionRequiringLink",
                    link_args=[
                        'supercls_links["communities-suggestions"], "add_community"',
                    ],
                    imports=[
                        Import("oarepo_runtime.services.records.links.PermissionRequiringLink"),
                    ],
                ),
            ]