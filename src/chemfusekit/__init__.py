"""__init__.py file for the library"""
from beartype import BeartypeConf
from beartype.claw import beartype_this_package
beartype_this_package(conf=BeartypeConf(violation_type=TypeError))

from . import _base
from . import df
from . import knn
from . import lda
from . import lr
from . import pca
from . import plsda
from . import svm
from . import _utils