********************************************************************************

README for the Himawari L1 Gridded Data 
 through the JAXA's P-Tree System

Prepared by Earth Observation Research Center (EORC),
            Space Technology Directorate I,
            Japan Aerospace Exploration Agency (JAXA).

Aug.31,2016: Himawari L1 Gridded Data are released.

********************************************************************************

In this directory, the Himawari L1 Gridded Data provided by JAXA/EORC
from the Himawari Standard Data is available in near-real-time. 

********************************************************************************

# Available Himawari  L1 Gridded Data 

## Full-disk
 Projection: EQR
 Observation area: 60S-60N, 80E-160W
 Temporal resolution: 10-minutes
 Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)
                     2km (Pixel number: 6001, Line number: 6001)
 Data: albedo(reflectance*cos(SOZ) of band01~band06)
       Brightness temperature of band07~band16
       satellite zenith angle, satellite azimuth angle, 
       solar zenith angle, solar azimuth angle, observation hours (UT)

## Japan Area
 Projection: EQR
 Observation area: 24N-50N, 123E-150E
 Temporal resolution: 10-minutes
 Spatial resolution: 1km (Pixel number: 2701, Line number: 2601)
 Data: albedo(reflectance*cos(SOZ) of band01~band06)
       Brightness temperature of band07, 14, 15
       satellite zenith angle, satellite azimuth angle, 
       solar zenith angle, solar azimuth angle, observation hours (UT)

********************************************************************************

# TOP FTP Directory

 /jma/

********************************************************************************

# Structure of FTP Directories

 /jma/netcdf
       +---/[YYYYMM]
              +---/[DD]
                     +---/[hh]

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline; and
       hh: 2-digit hour of timeline.

********************************************************************************

# File Naming Convention

## Full-disk
 NC_H08_YYYYMDD_hhmm_Rbb_FLDK.xxxxx_yyyyy.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       bb: 2-digit band number (varies from "01" to "16");
       xxxxx: pixel number; ("2401": 5km resolution, 
                             "6001": 2km resolution, )
       yyyyy: line number; ("2401": 5km resolution, 
                             "6001": 2km resolution, )

 Example: 
   NC_H08_20160831_0000_R21_FLDK.02401_02401.nc
   NC_H08_20160831_0000_R21_FLDK.06001_06001.nc

## Japan Area
 NC_H08_YYYYMMDD_hhmm_rbb_FLDK.xxxxx_yyyyy.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       bb: 2-digit band number (fixed to "14");
       xxxxx: pixel number; (fixed to "2701" : 1km resolution)
       yyyyy: line number; (fixed to "2601" : 1km resolution)

 Example: 
   NC_H08_20160831_0000_r14_FLDK.02701_02601.nc

********************************************************************************

# Format

 All data is netCDF4 format.

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
