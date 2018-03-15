
import json
import inspect
import copy
from functools import wraps
import traceback
import warnings
from six import string_types

from collections import (
    Counter,
    defaultdict
)

from ..version import __version__
from .util import DotDict, recursively_convert_to_json_serializable, parse_result_format

import re
from datetime import datetime
from functools import wraps
import jsonschema

from numbers import Number

import numpy as np
import pandas as pd
from dateutil.parser import parse
from scipy import stats
from six import string_types

from .base import DataSet
from .util import DocInherit, parse_result_format, \
        is_valid_partition_object, is_valid_categorical_partition_object, is_valid_continuous_partition_object


class MetaFileSystemDataSet(DataSet):

    def __init__(self, filepath=None, *args, **kwargs):
        super(MetaFileSystemDataSet, self).__init__(*args, **kwargs)
        self.filepath = filepath

    @classmethod
    def row_map_expectation(cls, func):
        """Constructs an expectation using row-map semantics.

        """
        raise NotImplementedError


class FileSystemDataSet(MetaFileSystemDataSet):

    def __init__(self, *args, **kwargs):
        super(FileSystemDataSet, self).__init__(*args, **kwargs)

    @DataSet.expectation(['filename'])
    def expect_file_to_be_csv_parseable(self,
        filename,
        result_format=None, include_config=False, catch_exceptions=None, meta=None
    ):
        """
        #FIXME: Needs a docstring.
        """

        try:
            pd.read_csv(self.filepath+filename)
            return {
                "success" : True
            }

        except:
            return {
                "success" : False
            }


    @DataSet.expectation(['filename'])
    def expect_file_to_be_excel_parseable(self,
        filename,
        result_format=None, include_config=False, catch_exceptions=None, meta=None
    ):
        """
        #FIXME: Needs a docstring.
        """

        try:
            pd.read_excel(self.filepath+filename)
            return {
                "success" : True
            }

        except:
            return {
                "success" : False
            }


