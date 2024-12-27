********************************************************************************

README for the Model Output through the JAXA's P-Tree System

Prepared by Earth Observation Research Center (EORC),
            Japan Aerospace Exploration Agency (JAXA).

Oct.31,2018: Aerosol Model product (Ver. beta), and Sea Surface Temperature 
             Model product (Ver. 20170705) are released.

********************************************************************************

In this directory, the Geophysical Parameter Data estimated from 
the geostationary Himawari-8 Standard Data and Model Paramteters are 
available in near-real-time. 
You can also download the past period data of the Geophysical Parameter Data
since Mar.20, 2015.

Please note that past period data of the JAXA Geophysical Parameter Data
will be uploaded to the ftp site upon completion of its processing.

********************************************************************************

# Model Outputs
 
## Aerosol Property by MRI/JMA
 Latest version: Beta Version
 Area: Global
 Temporal resolution: 1-hour (Level 4)
 Spatial resolution: Longitude 0.375 deg., Latitude 0.37147 to 0.37461 deg. (Gaussian)
 (Pixel number: 960, Line number: 480)
 NOTE: This product is the forecast (every one hour) of aerosol properties by
       the MRI/JMA global aerosol model called Model of Aerosol Species IN the Global
       AtmospheRe (MASINGAR). This product is assimilated by Himawari L3 aerosol
       optical depth at 00, 03, 06, and 09UTC. The opposite side of the Himawari
       observation area is assimilated at 12 and 18UTC using MODIS/Terra+Aqua L3
       Value-added Aerosol Optical Depth - NRT dataset due to lack of aerosol
       retrievals by Himawari.(As for the image on the top page, there are cases
       where preliminary forecast is displayed that was derived by assimilating
       observation data before the previous day.)
       Please refer to the reference below for the assimilation method etc. 
       The aerosol data assimilation system based on MASINGER was developed 
       by Meteorological Research Institute and Kyushu University. 
       The products are produced at Meteorological Research Institute, and provided 
       by JAXA P-Tree System, Japan Aerospace Exploration Agency (JAXA). 

 Acknowledgements: 
    MODIS/Terra+Aqua L3 Value-added Aerosol Optical Depth - NRT datasets
    were acquired from the Level-1 and Atmosphere Archive & Distribution System
    (LAADS) Distributed Active Archive Center (DAAC), located in the Goddard Space
    Flight Center in Greenbelt, Maryland (https://ladsweb.nascom.nasa.gov/).

## Sea Surface Temperature by JAXA/JAMSTEC
 Latest version: v20170705
 Area: Around Japan (117E-150E, 17N-50N)
 Temporal resolution: 1-hour (Level 4)
 Spatial resolution: About 3km (1/36 deg.) (Pixel number: 1190, Line number: 1190)
 NOTE: This research is JAXA-JAMSTEC joint research and a part of the Japan Coastal 
       Ocean Predictability Experiment (JCOPE).
       This product is constructed by data assimilation using high resolution 
       regional ocean model "JCOPE-T" developed by JAMSTEC and observation data 
       including the 4 types satellite SST data provided by JAXA. 
       When we do the data assimilation, we do the bias correction of satellite 
       SST data using GCOM-W/AMSR2 SST data as refer to reference value, 
       because the bias in observation data is undesirable for data assimilation. 
       Near Real-Time data (analysis and forecast) and Best Estimate data are 
       included in this product. 

       Update frequency and period are follow.

       Near Real-Time data: Every day except Saturdays.
        - Analysis (ANAL): 5-days (replaced every update)
        - Forecast (FCST): 16-days (replaced every update)
       Best Estimate data: Every week
        (update in the beginning of the week; Sunday or Monday)
        - This is delay mode data which is provided about two weeks late.
        - 7-days data are added every update.

********************************************************************************

# TOP FTP Directory

 /pub/

********************************************************************************

# Structure of FTP Directories

### Level 4 (model parameters) 
### Aerosol Property Level 4
 /pub/model
        +---/ARP
             +---/MS
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]

 where VER: algorithm version;
       YYYY: 4-digit year observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline; and
       hh: 2-digit hour of timeline.

### Sea Surface Temperature Level 4
 /pub/model
       +---/SST
              +---/JCPT_DA
                   +---/[VER]
                          +---/FCST
                          +---/ANAL
                          +---/BEST
                              +---/[YYYYMM]
                                     +---/[DD]
 where VER: algorithm version;
       YYYY: 4-digit year observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline; and
       hh: 2-digit hour of timeline.

 FCST: Near Real-Time data (Forecast)
 ANAL: Near Real-Time data (Analysis)
 BEST: Best Estimate data 

********************************************************************************

# File Naming Convention

## Level 4 (model parameters) 
### Aerosol Property

 H08_YYYYMMDD_hhmm_MSARPVER_ANL.xxxxx_yyyyy.nc

where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       VER: algorithm version;
       xxxxx: pixel number; and
       yyyyy: line number.

Example:  H08_20180727_0000_MSARPbet_ANL.00960_00480.nc

### Sea Surface Temperature
 JCPT_DA_JPN03_SST_YYYYMMDD_hhmm.nc

where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;

Example: JCPT_DA_JPN03_SST_20181024_1200.nc

********************************************************************************

# Format

  All data is in NetCDF4 format. 

********************************************************************************

# Documents

## Operational schedule of Himawari-8
 Operational schedule of the geostationary Himawari-8 is available from
 the JMA's web site;
 http://www.data.jma.go.jp/mscweb/en/operation8/bulletin_list_H8.html

# Timetable of Himawari-8 Imaging
 The Himawari-8 Imaging Schedule is available from the JMA's web site.
 Please note that no observations are planned at 0240-0250UTC and 1440-1450UTC
 everyday for house-keeping of the Himawai-8 satellite.
 http://www.data.jma.go.jp/mscweb/en/operation8/Himawari-8%20Imaging%20Schedule.pdf

********************************************************************************

# References

# About Sea Surface Temperature Model:
 (Ocean model)
 Varlamov, S. M., X. Guo, T. Miyama, K. Ichikawa, T. Waseda, and Y. Miyazawa, 2015: 
 M2 baroclinic tide variability modulated by the ocean circulation south of Japan, 
 J. Geophys. Res. Oceans, 120, 3681-3710. DOI:10.1002/2015JC010739.
 https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JC010739.

 (Data assimilation method)
 Miyazawa, Y., S. M. Varlamov, T. Miyama, Y. Kurihara, H. Murakami, M. Kachi, 2021:
 A Nowcast/Forecast System for Japan’s Coasts Using Daily Assimilation of Remote Sensing 
 and In Situ Data. Remote Sens., 13, 2431.
 https://doi.org/10.3390/rs13132431

 Miyazawa, Y., S. M. Varlamov, T. Miyama, X. Guo, T. Hihara, K. Kiyomatsu, M. Kachi, 
 Y. Kurihara, H. Murakami, Assimilation of high-resolution sea surface temperature data 
 into an operational nowcast/forecast system around Japan using a multi-scale 
 three-dimensional variational scheme, Ocean Dyn., 67, 713-728. DOI: 10.1007/s10236-017-1056-1.
 https://link.springer.com/article/10.1007/s10236-017-1056-1.

# About Aerosol Model:
 (assimilation method)
 Yumimoto, K., T. Y. Tanaka, N. Oshima, and T. Maki, 2017: JRAero: the Japanese Reanalysis 
 for Aerosol v1.0, Geosci. Model Dev., 10, 3225-3253
 https://doi.org/10.5194/gmd-10-3225-2017.

 (assimilation with Himawari-8 Aerosol optical properties)
 Yumimoto, K., T. Y. Tanaka, M. Yoshida, M. Kikuchi, T. M. Nagao, H. Murakami, and T. Maki, 
 2018: Assimilation and forecasting experiment for heavy Siberian wildfire smoke in May 2016
 with Himawari-8 aerosol optical thickness. J. Meteor. Soc. Japan, 96B
 http://jmsj.metsoc.jp/GA/JMSJ2018-035.html.

 (quotation for MODIS assimilation)
 MODIS/Terra+Aqua Near Real Time value-added Aerosol Optical Depth
 Product, 6.1NRT, L2 Swath 1 km and 5 km, C6, NASA Level-1 and Atmosphere
 Archive & Distribution System (LAADS) Distributed Active Archive Center
 (DAAC), Goddard Space Flight Center, Greenbelt, MD.
 http://dx.doi.org/10.5067/MODIS/MCDAODHD.NRT.061
 

********************************************************************************

