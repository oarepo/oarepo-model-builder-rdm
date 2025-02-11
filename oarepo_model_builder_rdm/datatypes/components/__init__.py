from .service import RDMServiceComponent
from .record import RDMRecordModelComponent
from .ext_resource import RDMExtResourceModelComponent
from .draft_record import RDMDraftParentComponent
from .marshmallow import RDMMarshmallowModelComponent
from .search_options import RDMSearchOptionsModelComponent

RDM_COMPONENTS = [
    RDMServiceComponent,
    RDMRecordModelComponent,
    RDMExtResourceModelComponent,
    RDMDraftParentComponent,
    RDMMarshmallowModelComponent,
    RDMSearchOptionsModelComponent
]
