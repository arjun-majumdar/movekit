# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

from .io import *  # noqa: E402
from .preprocess import preprocessing_methods  # noqa: E402
from .feature_extraction import compute_absolute_features  # noqa: E402
from .feature_extraction import time_series_analyis  # noqa: E402
