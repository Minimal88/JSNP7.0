## Copyright (C) GNSS ACADEMY 
##
## Name          : Posunctions.py
## Purpose       : Satellite Analyses functions
## Project       : WP0-JSNP
## Component     : 
## Author        : GNSS Academy
## Creation date : 2021
## File Version  : 1.0
## Version date  : 
##

import sys, os
from pandas import unique
from interfaces import LOS_IDX, POS_IDX
sys.path.append(os.getcwd() + '/' + \
    os.path.dirname(sys.argv[0]) + '/' + 'COMMON')
from COMMON import GnssConstants
from COMMON.Plots import generatePlot
import numpy as np
# from pyproj import Transformer
from COMMON.Coordinates import xyz2llh

# T6.1 Satellites Used in PVT
def plotNumberOfSats(PosData):
    print( 'Ploting the Satellites Used in PVT image ...')

    # Extract number of satellites information
    num_sats = PosData[POS_IDX["NSATS"]]     
    
    # Plot settings
    PlotConf = {}

    PlotConf["Type"] = "Lines"
    PlotConf["FigSize"] = (16.8, 15.2)
    PlotConf["Title"] = "Number of Satellites in PVT vs Time from TLSA on Year 2015 DoY 006 "

    PlotConf["yLabel"] = "Number of Satellites"
    PlotConf["yTicks"] = range(0,14)
    PlotConf["yLim"] = [0,14]

    PlotConf["xLabel"] = "Hour of DoY 006"
    PlotConf["xTicks"] = range(0, 25)
    PlotConf["xLim"] = [0, 24]

    PlotConf["Grid"] = True
    PlotConf["Marker"] = '.'
    PlotConf["LineWidth"] = 2

    PlotConf["xData"] = {}
    PlotConf["yData"] = {}

    Label = 0
    PlotConf["xData"][Label] = PosData[POS_IDX["SOD"]] / GnssConstants.S_IN_H  # Converting to hours
    PlotConf["yData"][Label] = num_sats

    PlotConf["Path"] = sys.argv[1] + '/OUT/POS/POS/' + 'POS_SATS_vs_TIME_TLSA_D006Y15.png'  

    # Generate plot
    generatePlot(PlotConf) 
