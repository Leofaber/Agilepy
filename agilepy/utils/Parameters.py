import os

class Parameters:

    datapath = os.path.join(os.environ["AGILE"], "model/scientific_analysis/data")

    _skymap = os.path.join(datapath, "{}_{}.SKY002.SFMG_H0025.disp.conv.sky.gz")
    _mapNamePrefix = "EMIN{}_EMAX{}_{}"

    # constants
    sarmatrix = os.path.join(datapath, "AG_GRID_G0017_SFMG_H0025.sar.gz")
    edpmatrix = os.path.join(datapath, "AG_GRID_G0017_SFMG_H0025.edp.gz")
    psdmatrix = os.path.join(datapath, "AG_GRID_G0017_SFMG_H0025.psd.gz")

    matrixconf = sarmatrix + " " + edpmatrix + " " + psdmatrix

    energybins = [[10000,50000],
                  [1000,3000],
                  [1000,50000],
                  [100,1000],
                  [100,10000],
                  [100,200],
                  [100,300],
                  [100,400],
                  [100,50000],
                  [200,400],
                  [200,50000],
                  [3000,10000],
                  [3000,50000],
                  [300,1000],
                  [300,10000],
                  [300,3000],
                  [300,50000],
                  [30,100],
                  [30,1000],
                  [30,400],
                  [30,50],
                  [30,50000],
                  [400,1000],
                  [400,10000],
                  [400,3000],
                  [400,50000],
                  [50,100],
                  [50,400],
                 ]

    @staticmethod
    def checkEnergyBin(energyBin):
        energyBin = [int(energy) for energy in energyBin]
        if energyBin in Parameters.energybins:
            return True
        return False

    @staticmethod
    def getSkyMap(emin, emax):
        return Parameters._skymap.format(emin, emax)

    @staticmethod
    def getMapNamePrefix(emin, emax, stepi):
        return Parameters._mapNamePrefix.format(emin.zfill(5), emax.zfill(5), str(stepi).zfill(2))