# DESCRIPTION
#       Agilepy software
#
# NOTICE
#      Any information contained in this software
#      is property of the AGILE TEAM and is strictly
#      private and confidential.
#      Copyright (C) 2005-2020 AGILE Team.
#          Baroncelli Leonardo <leonardo.baroncelli@inaf.it>
#          Addis Antonio <antonio.addis@inaf.it>
#          Bulgarelli Andrea <andrea.bulgarelli@inaf.it>
#          Parmiggiani Nicolò <nicolo.parmiggiani@inaf.it>
#      All rights reserved.

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import shutil
import unittest
from pathlib import Path
from time import sleep

from agilepy.utils.AstroUtils import AstroUtils
from agilepy.utils.AgilepyLogger import AgilepyLogger
from agilepy.utils.PlottingUtils import PlottingUtils
from agilepy.config.AgilepyConfig import AgilepyConfig

class AgilepyUtilsUT(unittest.TestCase):

    def setUp(self):
        self.currentDirPath = Path(__file__).parent.absolute()
        self.agilepyconfPath = os.path.join(self.currentDirPath,"conf/agilepyconf.yaml")

        self.config = AgilepyConfig()
        self.config.loadConfigurations(self.agilepyconfPath, validate=False)

        self.agilepyLogger = AgilepyLogger()

        self.agilepyLogger.initialize(self.config.getConf("output","outdir"), self.config.getConf("output","logfilenameprefix"), self.config.getConf("output","verboselvl"))

        self.datadir = os.path.join(self.currentDirPath,"data")

        self.outDir = Path(self.config.getOptionValue("outdir"))

        if self.outDir.exists() and self.outDir.is_dir():
            shutil.rmtree(self.outDir)

    def tearDown(self):
        self.agilepyLogger.reset()

    def test_display_sky_map(self):

        pu = PlottingUtils(self.config, self.agilepyLogger)

        smooth = True
        sigma = 4
        fileFormat = ".png"
        title = "testcase"
        cmap = "CMRmap"
        regFilePath = self.config._expandEnvVar("$AGILE/catalogs/2AGL_2.reg")


        file = pu.displaySkyMap(
                    self.datadir+"/testcase_EMIN00100_EMAX00300_01.cts.gz", \
                    smooth = smooth,
                    sigma = sigma,
                    fileFormat = fileFormat,
                    title = title,
                    cmap = cmap,
                    regFilePath = regFilePath,
                    saveImage=True)

        self.assertEqual(True, os.path.isfile(file))


    def test_display_sky_map_single_mode(self):

        pu = PlottingUtils(self.config, self.agilepyLogger)

        smooth = True
        sigma = 4
        fileFormat = ".png"
        title = "testcase"
        cmap = "CMRmap"
        regFilePath = self.config._expandEnvVar("$AGILE/catalogs/2AGL_2.reg")
        img = self.datadir+"/testcase_EMIN00100_EMAX00300_01.cts.gz"

        file = pu.displaySkyMapsSingleMode(
                    [img, img, img], \
                    outfilename = "pippo",
                    smooth = smooth,
                    sigma = sigma,
                    fileFormat = fileFormat,
                    titles = [title+"_1", title+"_2", title+"_3"],
                    cmap = cmap,
                    regFilePath = regFilePath,
                    saveImage=True)

        self.assertEqual(True, os.path.isfile(file))

    def test_initialize_logger_verboselvl_2(self):
        sleep(1.0)
        self.agilepyLogger.reset()
        self.config.setOptions(force=True, verboselvl=2)

        logfilePath = self.agilepyLogger.initialize(self.config.getOptionValue("outdir"), self.config.getOptionValue("logfilenameprefix"), self.config.getOptionValue("verboselvl"))

        self.assertEqual(True, logfilePath.is_file())

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(1, linesNumber)

        self.agilepyLogger.debug(self, "%s %s", "Debug", "message")
        self.agilepyLogger.info(self, "%s %s", "Info", "message")
        self.agilepyLogger.warning(self, "%s %s", "Warning", "message")
        self.agilepyLogger.critical(self, "%s %s", "Critical", "message")

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(5, linesNumber)


    def test_initialize_logger_verboselvl_1(self):
        sleep(1.0)
        self.agilepyLogger.reset()
        self.config.setOptions(force=True, verboselvl=1)

        logfilePath = self.agilepyLogger.initialize(self.config.getOptionValue("outdir"), self.config.getOptionValue("logfilenameprefix"), self.config.getOptionValue("verboselvl"))

        self.assertEqual(True, logfilePath.is_file())

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(1, linesNumber)

        self.agilepyLogger.debug(self, "%s %s", "Debug", "message")
        self.agilepyLogger.info(self, "%s %s", "Info", "message")
        self.agilepyLogger.warning(self, "%s %s", "Warning", "message")
        self.agilepyLogger.critical(self, "%s %s", "Critical", "message")

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(5, linesNumber)


    def test_initialize_logger_verboselvl_0(self):
        sleep(1.0)
        self.agilepyLogger.reset()
        self.config.setOptions(force=True, verboselvl=0)

        logfilePath = self.agilepyLogger.initialize(self.config.getOptionValue("outdir"), self.config.getOptionValue("logfilenameprefix"), self.config.getOptionValue("verboselvl"))

        self.assertEqual(True, logfilePath.is_file())

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(1, linesNumber)

        self.agilepyLogger.debug(self, "%s %s", "Debug", "message")
        self.agilepyLogger.info(self, "%s %s", "Info", "message")
        self.agilepyLogger.warning(self, "%s %s", "Warning", "message")
        self.agilepyLogger.critical(self, "%s %s", "Critical", "message")

        with open(logfilePath, "r") as f:
            linesNumber = len(f.readlines())
            self.assertEqual(5, linesNumber)







    """
    Time conversions
        # https://tools.ssdc.asi.it/conversionTools
        # https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl?time_in_i=&time_in_c=&time_in_d=&time_in_j=&time_in_m=58871.45616898&time_in_sf=&time_in_wf=&time_in_sl=&time_in_sni=&time_in_snu=&time_in_s=&time_in_h=&time_in_sz=&time_in_ss=&time_in_sn=&timesys_in=u&timesys_out=u&apply_clock_offset=yes
    """
    def test_astro_utils_time_mjd_to_tt(self):
        sec_tolerance = 0.001
        tt = AstroUtils.time_mjd_to_tt(58871.45616898) # 506861812.99987227
        self.assertEqual(True, abs(506861813-tt) <= sec_tolerance)

    def test_astro_utils_time_tt_to_mjd(self):
        sec_tolerance = 0.0000001
        mjd = AstroUtils.time_tt_to_mjd(507391426.9447)
        self.assertEqual(True, abs(58877.58595999 - mjd) <= sec_tolerance)



    """
    TODO !! it should be 2020, 1, 23)
    def test_astro_utils_time_jd_to_civil(self):

        civ = AstroUtils.jd_to_civil(2458871.95616898)
        self.assertEqual(civ, (2020, 1, 22.956168979872018))





    def test_astro_utils_time_utc_to_tt(self):

        tt = AstroUtils.time_utc_to_tt("2020-01-23T10:56:53")
        self.assertEqual(tt, 506861813)


    def test_astro_utils_time_tt_to_utc(self):

        utc = AstroUtils.time_tt_to_utc(506861813)
        self.assertEqual(utc, "2020-01-23T10:56:53")
    """



    """
    def test_astro_utils_time_mjd_to_utc(self):
        utc = AstroUtils.time_mjd_to_utc(58871.45616898)
        self.assertEqual(utc, "2020-01-23T10:56:53")

    def test_astro_utils_time_utc_to_mjd(self):

        mjd = AstroUtils.time_utc_to_mjd("2020-01-23T10:56:53")
        self.assertEqual(mjd, 58871.45616898)
    """

if __name__ == '__main__':
    unittest.main()
