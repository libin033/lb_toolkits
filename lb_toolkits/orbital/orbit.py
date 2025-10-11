# coding:utf-8
'''
@Project: WordUtil.py
-------------------------------------
@File   : orbital.py
-------------------------------------
@Modify Time      @Author    @Version    
--------------    -------    --------
2022/1/7 15:15     Lee        1.0         
-------------------------------------
@Desciption
-------------------------------------

'''

import datetime
import numpy as np

from .tlefile import read

Deg2Rad = 0.0174532925199433     #/*:  角度转弧度*/
Rad2Deg	= 57.29577951308232	     #/*:  弧度转角度 */
AE = 6378.137   		         # 标准地球赤道半径(公里)WGS84标准  */

J2 =-.0010826517		     # 地球带谐项                     */
J3 = .0000025450306   		 # 地球带谐项                     */
J4 = .0000016714987		     # 地球带谐项                     */
J5 = .00000020672093		 # 地球带谐项                     */

GME = 398601.80          	# 引力常数GM(m**3/(s**2))        */
E21 = .9933056
E2 = 0.0066943800699785	   # 地球偏心率平方                 */
E2E21 = .006739502
TWOPI = 2* np.pi
PI = np.pi



class orbit():

    def __init__(self, satellite, tle_file=None, line1=None, line2=None):
        satellite = satellite.upper()
        self.satellite_name = satellite
        self.tle = read(satellite, tle_file=tle_file,
                        line1=line1, line2=line2)
    def calorbit(self, nowdate):
        # self.epoch = tle.epoch
        # self.excentricity = tle.excentricity
        # self.inclination = np.deg2rad(tle.inclination)
        # self.right_ascension = np.deg2rad(tle.right_ascension)
        # self.arg_perigee = np.deg2rad(tle.arg_perigee)
        # self.mean_anomaly = np.deg2rad(tle.mean_anomaly)
        tle = self.tle
        orbittime = tle.epoch_time
        # print(orbittime)
        dOrbitNum = tle.mean_motion
        dOrbitT = 24.0 / dOrbitNum * 60 * 60

        dOrbitSemiAxis = np.power(((398613.52 * dOrbitT * dOrbitT) / (4 * np.pi * np.pi)), 1.0/3.0)
        # dSatHeight = dOrbitSemiAxis - AE
        tleinfo = {
            'dOrbitSemiAxis' : dOrbitSemiAxis,                # 轨道半长轴
            'dOrbitEccentricity': tle.excentricity,            # 轨道偏心率
            'dOrbitInclination': tle.inclination,         # 轨道倾角
            'dAscendLongitude' : tle.right_ascension,         # 升交点赤道经度
            'dPerigeeDegree'  : tle.arg_perigee,          # 近地点俯角
            'dMeanPerigee' :  tle.mean_anomaly,         # 平近地点
            'dOrbitT' :   dOrbitT,                # 每圈周期时间
            # 'dSatHeight' :dSatHeight,         # 卫星高度
            'TotalOrbit' :  tle.orbit,         # 卫星高度
        }
        TPixel = 2048

        StpAng = 0.0541
        StpTim = 0.000025

        # nowdate = datetime.datetime.utcnow()
        TimeCal = TIMEZ(nowdate.year, nowdate.month, nowdate.day, nowdate.hour, nowdate.minute, nowdate.second)

        # print(TimeCal)
        PIXEL = 1
        #!调用程序SatAEL 计算第一个象元点（PIXEL=1）所对应的经纬度
        FLAT1, FLONG1 = TNLOC(TimeCal, PIXEL, StpAng, StpTim, TPixel, tleinfo, orbittime)

        #!调用程序SatAEL 计算最后一个象元点（PIXEL=TPixel）所对应的经纬度
        PIXEL = TPixel
        FLAT2, FLONG2 = TNLOC(TimeCal, PIXEL, StpAng, StpTim, TPixel, tleinfo, orbittime)

        return FLONG1, FLAT1, FLONG2, FLAT2


def ZSODSRadto2Pai(dRad) :

    dresult = dRad - TWOPI * ((int)(dRad / TWOPI))
    if (dRad < 0.0) :
        dresult += TWOPI
    
    return dresult

def ICGS( RX, Sth, Cth, SCNLAT):
    '''
    !  RX(3)(R*8) : 卫星空间位置矢量（x,y,z)
    !  Sth (R*8)  :  观测点SIN(S) S:观测点的地方恒星时
    !  Cth        :	 观测点COS(S)
    !  Glat		  :  观测点的纬度[弧度]
    !  输出参数
    !  azgs	 	  :	 TIME时刻的卫星相对观测站的方位角
    !  elgs	      :	 TIME时刻的卫星相对观测站的仰角    */
    '''

    HGT = 50.0 / 6378137.0
    Sla = np.sin(SCNLAT)
    Cla = np.cos(SCNLAT)
    RE2 = AE / np.sqrt(1.0 - E2 * Sla * Sla)
    Gxic = (RE2 + HGT) * Cla * Cth
    Gyic = (RE2 + HGT) * Cla * Sth
    Gzic = (RE2 * (1.0 - E2) + HGT) * Sla
    Rhx = RX[0] - Gxic
    Rhy = RX[1] - Gyic
    Rhz = RX[2] - Gzic
    Rht = Cth * Rhx + Sth * Rhy
    Rxgs = Cth * Rhy - Sth * Rhx
    Rygs = Cla * Rhz - Sla * Rht
    Rzgs = Cla * Rht + Sla * Rhz

    Azgs = np.arctan2(Rxgs, Rygs)
    if (Azgs < 0.0) :
        Azgs = Azgs + TWOPI
    Elgs = np.arctan(Rzgs / np.sqrt(Rxgs * Rxgs + Rygs * Rygs))

    return Azgs, Elgs

def TNSUB(RSAT, SINP, COSP, SINI, COSI, COST) :
    RX = RSAT * COSP
    RZ = RSAT * SINP
    rzcrx2 = RZ / RX
    X = AE / np.sqrt(1.0 + (rzcrx2 * rzcrx2) / E21)
    for i in range(100) :
        XO = X
        rzx2 = RZ / (RX - E2 * XO)
        X = AE / np.sqrt(1.0 + E21 * (rzx2 * rzx2))

        dxi = (X - XO) / X
        if (dxi < 0) : dxi = -dxi
        if (dxi <= 1.0e-6) : break

    Z = E21 * (RZ * X / (RX - E2 * X))
    HX = X - RX
    HZT = Z - RZ
    HSAT = np.sqrt(HX * HX + HZT * HZT)
    HBAR = (COSP * HZT - SINP * HX) / COSP
    TDOTH = COST * SINI * HBAR
    ZDOTH = COSI * HBAR
    
    SINB = TDOTH / (HSAT)
    COSB = 1.0 - .5 * (SINB) * (SINB)
    
    SINA = ZDOTH / ((HSAT) * (COSB))
    COSA = np.sqrt(1.0 - (SINA) * (SINA))
    
    return SINA, COSA, SINB, COSB, HSAT

def KEPLR(L, E) :
        
    COSL = np.cos(L)
    SINL = np.sin(L)
    EPS0 = np.arctan(E * SINL / (1.0 - E * COSL))
    ETA = np.sqrt(1.0 - E * (2.0 * COSL - E))
    ESINL = E * np.sin(L + EPS0)
    ESINL2 = ESINL * ESINL
    ESINL3 = ESINL * ESINL2
    EPSLON = EPS0 - np.arcsin(ESINL3 * (1.0 - ESINL2 / 20.0) / (6.0 * ETA))
    EA = L + EPSLON

    return EA

def EARTH(TIME) :
    PHIGRN = [1.739935890,628.33195070,.000006754947810]
    CHIMS = [4.881633570, 628.3319487050, 1.4468088e-10]
    MEARTH = [6.256581470, 628.3019468590, -7.1676766e-11]
    OMEGA = [4.523636080, -33.7571619360, 9.9285594E-10]
    EPSLON = [.40936890950, -2.27232172336e-4]
    KAPPA = .0335020
    DELPSI = [8.35465e-5, .61712e-5]
    DELEPS = [4.46513e-5, .26771e-5]
    ZERO80 = 29219.50
    CENTCT = 36525.0
    # *** I) IF THIS THE FIRSTCALL TO EARTH THEN
    #! ***   A) THE JULIAN DAY NUMBER NEAREST THE INPUT TIME IS DETERMINE
    # !      IF(FIRST.eq. 1.0) then
    DDATE = ZERO80 + TIME / 86400.0
    IDATE2 = 2. * DDATE
    if ((IDATE2 % 2) == 0) : IDATE2 = IDATE2 - 1
    DATE = IDATE2 * .50
    if (DDATE - DATE > .50) : DATE = DATE + 1.0
    EPTIME = (DATE - ZERO80) * 86400.0
    CENTNO = DATE / CENTCT
    #  ***    B) THE HOUR ANGLE (ALPHA), NUTATION (ANUT),LONGITUDE OF THE
    # ! ***       SUN (CHI) AND OBLIQUITY OF THE ECLIPTIC (EPSLN) AND THEI
    # ***       DERIVATIVES AT THE EPOCH TID5 ARE DETERMINED. \
    ALPHA0 = ZSODSRadto2Pai(PHIGRN[0] + \
                            ZSODSRadto2Pai(CENTNO * (PHIGRN[1] + CENTNO * PHIGRN[2])))
    DADT = (TWOPI + (PHIGRN[1] + 2. * CENTNO * PHIGRN[2]) / CENTCT) / 86400.
    CHIMO = ZSODSRadto2Pai(CHIMS[0] +
                           ZSODSRadto2Pai(CENTNO * (CHIMS[1] + CENTNO * CHIMS[2])))
    DXMDT = (CHIMS[1] + 2. * CENTNO * CHIMS[2]) / (86400.0 * CENTCT)
    MANOM0 = ZSODSRadto2Pai(MEARTH[0] +
                            ZSODSRadto2Pai(CENTNO * (MEARTH[1] + CENTNO * MEARTH[2])))
    DMDT = (MEARTH[1] + 2. * CENTNO * MEARTH[2]) / (86400.0 * CENTCT)
    OMEGA0 = ZSODSRadto2Pai(OMEGA[0] +
                            ZSODSRadto2Pai(CENTNO * (OMEGA[1] + CENTNO * OMEGA[2])))
    DWDT = (OMEGA[1] + 2. * CENTNO * OMEGA[2]) / (86400.0 * CENTCT)
    EPSLN0 = EPSLON[0] + CENTNO * EPSLON[1]
    DEDT = EPSLON[1] / (86400.0 * CENTCT)
    DELP0 = DELPSI[0] * np.sin(OMEGA0) + DELPSI[1] * np.sin(2.0 * CHIMO)
    DDPDT = DELPSI[0] * np.cos(OMEGA0) * DWDT + DELPSI[1] * np.cos(2. * CHIMO) \
            * 2.0 * DXMDT
    DELE0 = DELEPS[0] * np.cos(OMEGA0) + DELEPS[1] * np.cos(2.0 * CHIMO)
    DDEDT = -DELEPS[0] * np.sin(OMEGA0) * DWDT - \
            DELEPS[1] * np.sin(2.0 * CHIMO) * 2.0 * DXMDT
    CHI0 = CHIMO + KAPPA * np.sin(MANOM0)
    DXDT = DXMDT + KAPPA * np.cos(MANOM0) * DMDT
    ANUT0 = DELP0 * np.cos(EPSLN0 + DELE0)
    DANDT = DDPDT * ANUT0 / DELP0 - DELP0 * np.sin(EPSLN0 + DELE0) * (DEDT + DDEDT)
    Dtime = TIME - EPTIME
    ALPHA = ZSODSRadto2Pai(ALPHA0 + ANUT0 + (DADT + DANDT) * Dtime)
    ALPDOT = DADT + DANDT
    CHISUN = ZSODSRadto2Pai(CHI0 + DXDT * Dtime)
    OBLIQE = EPSLN0 + DELE0 + (DEDT + DDEDT) * Dtime

    return ALPHA, ALPDOT, CHISUN, OBLIQE

def BLORB(TIME, tleinfo, nowdate) :

    eptime = TIMEZ(nowdate.year, nowdate.month, nowdate.day,
                   nowdate.hour, nowdate.minute, nowdate.second+nowdate.microsecond/1000)

    eporbt = tleinfo['TotalOrbit'] # 发星以来飞行圈数

    epelem = np.zeros(shape=(6), dtype=np.float32)
    epelem[0] = tleinfo['dOrbitSemiAxis']                  # 轨道半长轴
    epelem[1] = tleinfo['dOrbitEccentricity']              # 轨道偏心率
    epelem[2] = tleinfo['dOrbitInclination'] * Deg2Rad     # 轨道倾角
    epelem[3] = tleinfo['dAscendLongitude'] * Deg2Rad      # 升交点赤道经度
    epelem[4] = tleinfo['dPerigeeDegree'] * Deg2Rad        # 近地点俯角
    epelem[5] = tleinfo['dMeanPerigee'] * Deg2Rad          # 平近地点
    
    BKSUBC = .010

    # *** THE ACTION INDICATED BY IOPTN IS PERFORMED:
    # *** I) (IOPTN=0) THE ORBIT GECERATOR IS INTIALIZED WITH THE
    #     BROUWER MEAN ELEMENTS IN ORBEL AT TIME AND ORBIT NUMBER
    #     IN TIME AND IORBIT. */

    ORBEL = epelem # 全局历元轨道根数变量
    ADP = ORBEL[0] / AE
    ADP2 = ADP * ADP
    ADP3 = ADP2 * ADP
    EK = np.sqrt(GME / (AE * AE * AE))
    ANU = np.sqrt(1.0 / ADP3)
    EDP = ORBEL[1]
    EDP2 = EDP * EDP
    ETA2 = 1.0 - EDP2
    ETA = np.sqrt(ETA2)
    ETA3 = ETA2 * ETA
    ETA6 = ETA3 * ETA3

    IDP = ORBEL[2]
    COSI = np.cos(IDP)
    SINI = np.sin(IDP)
    COSI2 = COSI * COSI
    CSI321 = 3.0 * COSI2 - 1.0
    COSI4 = COSI2 * COSI2
    SINI2 = SINI * SINI
    COSID2 = np.cos(0.5 * IDP)
    SINID2 = np.sin(0.5 * IDP)
    TANID2 = SINID2 / COSID2

    H0 = ORBEL[3]
    HDP = H0
    G0 = ORBEL[4]
    GDP = G0
    L0 = ORBEL[5]
    LDP = L0
    ETA22 = ETA2 * ETA2
    ETA23 = ETA22 * ETA2
    GM2 = -.50 * J2 / ADP2
    GMP2 = GM2 / ETA22
    GM3 = J3 / ADP3
    GMP3 = GM3 / ETA23
    GM4 = .3750 * J4 / (ADP2 * ADP2)
    GMP4 = GM4 / (ETA22 * ETA22)

    GM5 = J5 / (ADP2 * ADP3)

    GMP5 = GM5 / (ETA22 * ETA23)
    G3DG2 = GMP3 / GMP2
    G4DG2 = GMP4 / GMP2
    G5DG2 = GMP5 / GMP2

    # 计算轨道一阶变化率 LDOT,GDOT,HDOT I
    LDOT = ETA * ANU * (GMP2 * (1.50 * CSI321 + 3.0 / 32.0 * GMP2 * ((-15.0 +
                                                                      16.0 * ETA + 25.0 * ETA2) + COSI2 * (30.0 - 96.0 * ETA - 90.0 * ETA2) +
                                                                     COSI4 * (105.0 + 144.0 * ETA + 25.0 * ETA2))) + 15.0 / 16.0 * EDP2 * GMP4 *
                        (3.0 + 35.0 * COSI4 - 30.0 * COSI2))
    GDOT = ANU * (5.0 / 16.0 * GMP4 * (COSI4 * (385.0 - 189.0 * ETA2)
                                       - COSI2 * (270.0 - 126.0 * ETA2) + (21.0 - 9.0 * ETA2))
                  + GMP2 * (3.0 / 32.0 * GMP2 * (COSI4 * (385.0 + 360.0 * ETA +
                                                          45.0 * ETA2) + COSI2 * (90.0 - 192.0 * ETA - 126.0 * ETA2) + (-35.0 +
                                                                                                                        24.0 * ETA + 25.0 * ETA2)) + 1.50 * (5.0 * COSI2 - 1.0)))

    HDOT = COSI * ANU * (1.250 * GMP4 * (3.0 - 7.0 * COSI2) * (5.0 - 3.0 * ETA2)
                         - GMP2 * (3.0 - .3750 * GMP2 * ((-5.0 + 12.0 * ETA + 9.0 * ETA2)
                                                         - COSI2 * (35.0 + 36.0 * ETA + 5.0 * ETA2))))

    ISUBC = (25.0 * COSI4 * COSI * GMP2 * EDP2) / ((5.0 * COSI2 - 1.0) * (5.0 * COSI2 - 1.0))
    A1P = 1.0 / (5.0 * COSI2 - 1.0)
    A1 = .1250 * GMP2 * ETA2 * (1.0 - 11.0 * COSI2 + 40.0 * A1P * COSI4)
    A2P = 3.0 * COSI2 - 8.0 * A1P * COSI4
    A2 = 5.0 / 12.0 * G4DG2 * ETA2 * (1.0 - A2P)
    A3 = G5DG2 * (3.0 * EDP2 + 4.0)
    A4 = G5DG2 * (1.0 - 3.0 * A2P)
    A5 = A3 * (1.0 - 3.0 * A2P)
    A6 = .250 * G3DG2
    A10 = ETA2 * SINI
    A7 = A6 * A10
    A8P = G5DG2 * EDP * (1.0 - 5.0 * COSI2 + 16.0 * A1P * COSI4)
    A8 = A8P * EDP
    B13 = EDP * (A1 - A2)
    B14 = A7 + (5.0 / 64.0) * A5 * A10
    B15 = (35.0 / 384.0) * A8 * A10

    #   COMPUTE A11-A27
    A11 = 2.0 + EDP2
    A12 = 3.0 * EDP2 + 2
    A13 = COSI2 * A12
    A14 = -(5.0 * EDP2 + 2.0) * COSI4 * A1P
    A15 = EDP2 * COSI4 * COSI2 * A1P * A1P
    A16 = -COSI2 * A1P
    A17 = A16 * A16
    A18 = EDP * SINI
    A19 = A18 / (1.0 + ETA)
    A21 = EDP * COSI
    A22 = EDP * A21
    A26 = 16.0 * A16 + 40.0 * A17 + 3.0
    A27 = .1250 * A22 * (11.0 + 200.0 * A17 + 80.0 * A16)
    #  COMPUTE B1-B12
    B1 = ETA * (A1 - A2) + (5.0 / 24.0) * G4DG2 * ((((2.0 * A22 * A26 - 80.0 * A15) -
                                                     8.0 * A14) - 3.0 * A13) + A11) - (GMP2 / 16.0) * (A11 + (-(400.0 * A15 + 40.0
                                                                                                                * A14 + 11.0 * A13) + 2.0 * A22 * (11.0 + (200.0 * A17 + 80.0 * A16))))

    B2 = A6 * A19 * (2.0 + ETA - EDP2) + A6 * A21 * TANID2 + (5.0 / 64.0) * \
    (A5 * A19 * ETA2 + A4 * A18 * (26.0 - 6.0 * ETA3 + 9.0 * EDP2)
     + A21 * (A5 * TANID2 + 6.0 * A3 * A26 * SINI * (1.0 - COSI)))

    B3 = (35.0 / 1152.0) * (2.0 * G5DG2 * EDP * SINI * (COSI - 1.0) * A22 *
                            (80.0 * A17 + 5.0 + 32.0 * A16) - A8P * (A22 * TANID2 + (2.0 * EDP2
                                                                                     + 3.0 * (1.0 - ETA3)) * SINI))

    B4 = ETA * EDP * (A1 - A2)
    B5 = ETA * ((5.0 / 64.0) * A4 * A10 * (9.0 * EDP2 + 4.0) + A7)
    B6 = (35.0 / 384.0) * ETA3 * A8 * SINI
    B7 = ETA2 * A18 * A1P * ((5.0 / 12.0) * G4DG2 * (1.0 - 7.0 * COSI2)
                             - .1250 * GMP2 * (1.0 - 15.0 * COSI2))
    B8 = ETA2 * ((5.0 / 64.0) * (1.0 - 9.0 * COSI2 + 24.0 * A1P * COSI4) * A3 + A6)
    B9 = (35.0 / 384.0) * ETA2 * A8
    B10 = SINI * ((5.0 / 12.0) * A22 * A26 * G4DG2 - A27 * GMP2)
    B11 = A21 * ((5.0 / 64.0) * (A5 + 6.0 * A3 * A26 * SINI2) + A6)
    B12 = -(35.0 / 1152.0) * (A8 * A21 + 2.0 * G5DG2 * EDP * SINI2 * A22 *
                              (80.0 * A17 + 32.0 * A16 + 5.0))

    THETA = ORBEL[4] + ORBEL[5] + 2.0 * ORBEL[1] * np.sin(ORBEL[5])
    THETA = ZSODSRadto2Pai(THETA)
    # 计算瞬时轨道的轨道数EPORB
    EPORB = eporbt + THETA / TWOPI# eporbt 全局变量历元轨道数

    DTIME = EK * (TIME - eptime)  # eptime 全局变量历元轨道时间
    HDP = ZSODSRadto2Pai((HDOT * DTIME) + H0)
    GDP = ZSODSRadto2Pai(ZSODSRadto2Pai(GDOT * DTIME) + G0)
    LDP = ZSODSRadto2Pai(ZSODSRadto2Pai((LDOT + ANU) * DTIME) + L0)
    #  计算瞬时轨道的轨道数*Piorbit
    Piorbit = EPORB + (LDOT + GDOT + ANU) * DTIME / TWOPI

    # 调用KEPLR程序求解开普勒方程计算片近点角&EADP
    EADP = KEPLR(LDP, EDP)

    SINEAD = np.sin(EADP)
    COSEAD = np.cos(EADP)
    DADR = 1.0 / (1.0 - EDP * COSEAD)
    SINFDP = ETA * SINEAD * DADR
    COSFDP = (COSEAD - EDP) * DADR
    FDP = np.arctan2(SINFDP, COSFDP)
    if (FDP < 0.0) : FDP = FDP + TWOPI
    DADR2 = DADR * DADR
    DADR3 = DADR * DADR2
    ECOSF = EDP * COSFDP
    DAR3N6 = ECOSF * (3.0 + ECOSF * (3.0 + ECOSF)) / ETA6
    DAR3N4 = DAR3N6 + EDP2 / ETA6
    DAR3N3 = DAR3N6 + EDP2 * (ETA + 1.0 / (1.0 + ETA)) / ETA6
    D1 = DADR2 * ETA2 + DADR
    D1M1 = D1 - 1.0
    D1P13 = D1 + 1.0 / 3.0
    D1P1 = D1 + 1.0
    CS2GFD = np.cos(2.0 * (GDP + FDP))
    COSFD2 = COSFDP * CS2GFD
    SN2GFD = np.sin(2.0 * (GDP + FDP))
    SNF2GD = np.sin(2.0 * GDP + FDP)
    CSF2GD = np.cos(2.0 * GDP + FDP)
    SIN2GD = np.sin(2.0 * GDP)
    COS2GD = np.cos(2.0 * GDP)
    SIN3GD = np.sin(3.0 * GDP)
    COS3GD = np.cos(3.0 * GDP)
    SN3FGD = np.sin(3.0 * FDP + 2.0 * GDP)
    CS3FGD = np.cos(3.0 * FDP + 2.0 * GDP)
    SINGDP = np.sin(GDP)
    COSGDP = np.cos(GDP)

    D2 = SN3FGD * D1P13 - SNF2GD * D1M1
    D3 = 3.0 * SN2GFD + EDP * (3.0 * SNF2GD + SN3FGD)

    D4 = EDP * SINEAD * (2 + ETA * DADR + .50 * EDP *
    (COSEAD + EDP * (1.0 + 2.0 * (COSEAD * COSEAD)) / 3.0))
    if (ISUBC > BKSUBC) :
        DLT1E = 0.0
        BLGHP = 0.0
        EDPDL = 0.0
        DLTI = 0.0
        SINDH = 0.0
    else :
        DLT1E = B14 * SINGDP + B13 * COS2GD - B15 * SIN3GD
        BLGHP = ZSODSRadto2Pai(B3 * COS3GD + B1 * SIN2GD + B2 * COSGDP + HDP + GDP + LDP)
        EDPDL = B4 * SIN2GD - B5 * COSGDP + B6 * COS3GD
        - .250 * GMP2 * ETA * ETA2 * (2.0 * CSI321 * D1P1 * SINFDP + 3.0 * SINI2 * D2)
        DLTI = .50 * COSI * GMP2 * SINI * (EDP * CS3FGD + 3.0 * (EDP * CSF2GD + CS2GFD))
        - EDP * COSI / ETA2 * (B7 * COS2GD + B8 * SINGDP - B9 * SIN3GD)
        SINDH = .50 / COSID2 * (B12 * COS3GD + B11 * COSGDP + B10 * SIN2GD
        - .50 * COSI * GMP2 * SINI * (6.0 * D4 - D3))

    BLGH = BLGHP + .250 * EDP * GMP2 * ETA2 / (1.0 + ETA) * (3.0 * SINI2 * D2
                                                             + 2. * SINFDP * CSI321 * D1P1) + 1.5 * GMP2 * (5. * COSI2 - 2. * COSI - 1.) * D4 \
           + .250 * GMP2 * (3.0 + 2.0 * COSI - 5.0 * COSI2) * D3

    DLTE = DLT1E + .50 * ETA2 / EDP * (3.0 * GM2 * SINI2 * CS2GFD * DAR3N4
                                       - GMP2 * SINI2 * EDP * (3.0 * CSF2GD + CS3FGD) + GM2 * CSI321 * DAR3N3)
    A = ADP * (1.0 + GM2 * (CSI321 * DAR3N3 + 3.0 * SINI2 * CS2GFD * DADR3))
    E = np.sqrt(EDPDL * EDPDL + (EDP + DLTE) * (EDP + DLTE))
    COSDH = .50 * COSID2 * DLTI + SINID2
    Inc = ZSODSRadto2Pai(2.0 * np.arcsin(np.sqrt(SINDH * SINDH + COSDH * COSDH)))
    # *** COMPUTE MEAN ANOMALY (L).
    if (E == 0.0) :
        L = 0.0
    else :
        SINLDP = np.sin(LDP)
        COSLDP = np.cos(LDP)
        SINHDP = np.sin(HDP)
        COSHDP = np.cos(HDP)
        ARG1 = EDPDL * COSLDP + (EDP + DLTE) * SINLDP
        ARG2 = (EDP + DLTE) * COSLDP - (EDPDL * SINLDP)
        L = ZSODSRadto2Pai(np.arctan2(ARG1, ARG2))


    # COMPUTE LONGITUDE OF ASCENDING NODE (H)
    if (Inc == 0.00) :
        H = 0.00
    else :
        ARG1 = SINDH * COSHDP + SINHDP * COSDH
        ARG2 = COSHDP * COSDH - SINDH * SINHDP
        H = ZSODSRadto2Pai(np.arctan2(ARG1, ARG2))

    G = ZSODSRadto2Pai(BLGH - L - H)
    # 调用KEPLR程序求解开普勒方程计算片近点角&EADP
    EA = KEPLR(L, E)
    ARG1 = np.sin(EA) * np.sqrt(1.0 - E * E)
    ARG2 = np.cos(EA) - E
    R = A * (1.0 - E * np.cos(EA))
    F = ZSODSRadto2Pai(np.arctan2(ARG1, ARG2))

    orbosele = np.zeros(shape=(8), dtype=np.float32)
    orbosele[0] = A * AE
    orbosele[1] = E
    orbosele[2] = Inc
    orbosele[3] = H
    orbosele[4] = G
    orbosele[5] = L
    orbosele[6] = R * AE
    orbosele[7] = F

    return orbosele

def TNLOC(STTIME, PIXLE, STPANG, STPTIM, TPixel, tleinfo, nowdate) :

    # 视场角的一半
    HLFANG = -0.5 * STPANG * Deg2Rad

    # 视场角FOV
    ANGL = -STPANG * Deg2Rad
    SPIX = PIXLE

    SIGMA = ANGL * (SPIX - (float(TPixel) / 2 + 1)) + HLFANG
    TIME = STTIME + (SPIX - 1) * STPTIM

    #计算瞬时轨道根数
    orbosele = BLORB(TIME, tleinfo, nowdate)

    ATTERR = np.zeros(shape=(3), dtype=np.float32)      #  卫星姿态参数误差 （滚动角、俯仰角、偏航角）[弧度]
    
    CA = np.cos(ATTERR[0])
    SA = np.sin(ATTERR[0])
    CB = np.cos(ATTERR[1])
    SB = np.sin(ATTERR[1])
    COSG = np.cos(ATTERR[2])
    SING1 = -np.sin(ATTERR[2])
    # 计算格林尼治恒星时PHIG和太阳黄经CHISUN及黄赤交角EPSLON
    PHIG, DPHIDT, CHISUN, EPSLON = EARTH(TIME)

    RSOL = 149600881.0
    COSX = np.cos(CHISUN)
    SINX = np.sin(CHISUN)
    COSE = np.cos(EPSLON)
    SINE = np.sin(EPSLON)
    # 计算太阳位置矢量SLP
    SLP = np.full(shape=(3), fill_value=0,dtype=np.float32)
    SLP[0] = RSOL * COSX
    SLP[1] = RSOL * (SINX * COSE)
    SLP[2] = RSOL * (SINX * SINE)

    # *** THE INPUT ORBITAL PARAMETERS ARE ASSIGNED TO COMMON /SCCOM/.
    RSAT = orbosele[6]
    COSI = np.cos(orbosele[2])
    SINI = np.sin(orbosele[2])
    COSO = np.cos(orbosele[3])
    SINO = np.sin(orbosele[3])
    THETA = orbosele[4] + orbosele[7]
    COST = np.cos(THETA)
    SINT = np.sin(THETA)
    SINP = SINT * SINI
    COSP = np.sqrt(1.0 - SINP * SINP)
    COSS = np.cos(SIGMA)
    SINS = np.sin(SIGMA)

    # 调用TNSUB程序计算卫星垂直高度HSAT和初始姿态COSA,COSB,SINA,SINB
    SINA, COSA, SINB, COSB, HSAT = TNSUB(RSAT, SINP, COSP, SINI, COSI, COST)

    TEMP = COSA * CA + SINA * SA
    SINA = SINA * CA - COSA * SA
    COSA = TEMP
    TEMP = COSB * CB + SINB * SB
    SINB = SINB * CB - COSB * SB
    COSB = TEMP

    # 计算卫星轨道坐标系三个分量,径向,横向,轨道面法向
    RSDXE = COST * COSO - SINT * COSI * SINO
    TSDXE = -SINT * COSO - COST * COSI * SINO
    ZSDXE = SINI * SINO
    RSDYE = COST * SINO + SINT * COSI * COSO
    TSDYE = -SINT * SINO + COST * COSI * COSO
    ZSDYE = -SINI * COSO
    RSDZE = SINT * SINI
    TSDZE = COST * SINI
    ZSDZE = COSI

    SIGR = SINA * COSG * SINS + COSA * COSB * COSS
    SIGT = COSB * SING1 * SINS - SINB * COSS
    SIGZ = COSA * COSG * SINS - SINA * COSB * COSS
    # 计算地心惯性坐标系三个分量

    SIGXE = SIGR * RSDXE + SIGT * TSDXE + SIGZ * ZSDXE
    SIGYE = SIGR * RSDYE + SIGT * TSDYE + SIGZ * ZSDYE
    SIGZE = SIGR * RSDZE + SIGT * TSDZE + SIGZ * ZSDZE

    # 计算扫描点斜距LAMBDA(点到卫星距离)
    A0 = 1.0
    A1 = SIGZE * SIGZE
    B0 = SIGR
    B1 = SINP * SIGZE
    C0 = 1.0 - (AE * AE) / (RSAT * RSAT)
    C1 = SINP * SINP
    B2MAC = ((B0 * B0 - A0 * C0) + ((B0 * B1 - A0 * C1) + (B0 * B1 - A1 * C0)) * E2E21) + \
            ((B1 * B1 - A1 * C1) * E2E21 * E2E21)
    LAMBDA = RSAT * ((B0 - np.sqrt(B2MAC)) + B1 * E2E21) / (A0 + A1 * E2E21)
    # =================================================================

    # 计算椭球面坐标系三个分量
    SMAG = np.sqrt(RSAT * (RSAT - 2.0 * LAMBDA * SIGR) + LAMBDA * LAMBDA)
    SP = np.zeros(shape=(3), dtype=np.float32)

    SP[0] = RSAT * RSDXE
    SP[1] = RSAT * RSDYE
    SP[2] = RSAT * RSDZE
    SDOTX = SP[0] - LAMBDA * SIGXE
    SDOTY = SP[1] - LAMBDA * SIGYE
    SDOTZ = SP[2] - LAMBDA * SIGZE
    # 计算扫描点经度和纬度
    SINL = SDOTZ / SMAG
    COSL = np.sqrt(1.0 - SINL * SINL)
    COSM = SDOTX / (SMAG * COSL)
    SINM = SDOTY / (SMAG * COSL)
    SCNLAT = np.arctan(SINL / (COSL * E21))
    SCNLON = np.arctan2(SINM, COSM) - PHIG

    #     THE ZENITH ANGLE IS COMPUTED BASED ON FLAG ANGTYP.
    if (SCNLON > np.pi)  :
        SCNLON = SCNLON - TWOPI
    if (SCNLON <= -np.pi) : SCNLON = SCNLON + TWOPI

    FLAT = SCNLAT * Rad2Deg
    FLON = SCNLON * Rad2Deg

    return FLAT, FLON

    # 计算太阳高度角和方位角
    SOLAZ, SOLELV = ICGS(SLP, SINM, COSM, SCNLAT)

    # 计算卫星高度角
    SATAZ, SATELV = ICGS(SP, SINM, COSM, SCNLAT)
    # 计算天顶角和方位角
    SOLZEN = 0.50 * PI - SOLELV
    SATZEN = 0.50 * PI - SATELV

    # 计算太阳相对卫星方位角
    SSAZ = SOLAZ - SATAZ
    if (SSAZ <= 0) : SSAZ = SSAZ + TWOPI
    HEIGHT = HSAT



def TIMEZ(nry, NMON, NDAY, NHR, NMIN, SEC) :
    MON = [ 31,59,90,120,151,181,212,243,273,304,334,365 ]

    if (nry >= 2000 | nry <= 90) :
        iyr0 = nry % 100
        iyr = 100 + iyr0
    else:
        iyr = nry % 100
    
    if (iyr >= 80) : MDAYS = 365. * (iyr - 80) + (iyr - 77) / 4
    if (iyr < 80) : MDAYS = 365. * (iyr - 80) + (iyr - 80) / 4
    
    if (NMON != 1) : MDAYS = MDAYS + MON[NMON - 2]
    if ((NMON > 2) & ((iyr % 4) == 0)) : MDAYS = MDAYS + 1

    TIMEZT = 86400.0 * (MDAYS + NDAY - 1) + 3600.0 * NHR + 60 * NMIN + SEC

    return TIMEZT



