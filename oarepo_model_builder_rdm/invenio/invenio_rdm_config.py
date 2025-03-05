from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioConfigBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_rdm_config"
    section = "config"
    template = "rdm-config"