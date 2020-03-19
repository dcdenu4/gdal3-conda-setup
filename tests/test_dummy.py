import time
import tempfile
import os
import unittest
import unittest.mock
import shutil
import types
import importlib

from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import numpy
import scipy.ndimage
import shapely.geometry

print("ENV: ", os.environ)

class MyTests(unittest.TestCase):

    def setUp(self):
        """Create a temporary workspace that's deleted later."""
        self.workspace_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up remaining files."""
        shutil.rmtree(self.workspace_dir)

    def test_dummy(self):
        # Create polygon shapefile to reproject
        # add comment for push
        # another COMMENT, come on
        base_srs = osr.SpatialReference()
        base_srs.ImportFromEPSG(3157) # NAD83(CSRS) / UTM zone 10N

        target_reference = osr.SpatialReference()
        target_reference.ImportFromEPSG(3116) # UTM zone 18N

        self.assertTrue(
            osr.SpatialReference(target_reference.ExportToWkt()).IsSame(
                osr.SpatialReference(target_reference.ExportToWkt())))

