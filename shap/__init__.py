# flake8: noqa

import warnings
import sys

__version__ = '0.41.0'

# check python version
if (sys.version_info < (3, 0)):
    warnings.warn("As of version 0.29.0 shap only supports Python 3 (not 2)!")

from ._explanation import Explanation, Cohorts

# explainers
from .explainers._explainer import Explainer
from .explainers._tree import Tree as TreeExplainer
from .explainers._gpu_tree import GPUTree as GPUTreeExplainer

_no_matplotlib_warning = "matplotlib is not installed so plotting is not available! Run `pip install matplotlib` " \
                         "to fix this."


# plotting (only loaded if matplotlib is present)
def unsupported(*args, **kwargs):
    warnings.warn(_no_matplotlib_warning)


class UnsupportedModule(object):
    def __getattribute__(self, item):
        raise ValueError(_no_matplotlib_warning)


try:
    import matplotlib
    have_matplotlib = True
except ImportError:
    have_matplotlib = False
else:
    summary_plot = unsupported
    decision_plot = unsupported
    multioutput_decision_plot = unsupported
    dependence_plot = unsupported
    force_plot = unsupported
    initjs = unsupported
    save_html = unsupported
    image_plot = unsupported
    monitoring_plot = unsupported
    embedding_plot = unsupported
    partial_dependence_plot = unsupported
    bar_plot = unsupported
    waterfall_plot = unsupported
    text_plot = unsupported
    # If matplotlib is available, then the plots submodule will be directly available.
    # If not, we need to define something that will issue a meaningful warning message
    # (rather than ModuleNotFound).
    plots = UnsupportedModule()


# other stuff :)
from . import datasets
from . import utils
from . import links

from .utils._legacy import kmeans
from .utils import sample, approximate_interactions
