# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits
@File     : Scan.py
@Modify Time      @Author    @Version    
--------------    -------    --------    
2022/7/15 9:34      Lee       1.0         
@Description
------------------------------------
 
'''
import os
import sys
import numpy as np
from numpy import *
from config import *


STPANG = 0.054100
PIXLE = 2048

def TNLOC(TIME) :

    # double  SLP[3], SP[3]
    # double CA, SA, CB, SB, COSG
    # double  RSOL, COSX, SINX, COSE, SINE, RSAT, COSI, SINI, COSO, SINO, SING1
    # double THETA, COST, SINT, SINP, COSP, COSS, SINS, TEMP, SINA, COSA, SINB, COSB
    # double RSDXE, TSDXE, ZSDXE, RSDYE, TSDYE, ZSDYE, RSDZE, TSDZE, ZSDZE
    # double SIGR, SIGT, SIGZ, SIGXE, SIGYE, SIGZE
    # double A0, A1, B0, B1, C0, C1, B2MAC, LAMBDA, SMAG, SDOTX, SDOTY, SDOTZ
    # double SINL, COSL, COSM, SINM, HSAT, SOLELV, SATELV, SOLAZ, SATAZ
    # double PHIG, DPHIDT, CHISUN, EPSLON

    HLFANG = -.50 * STPANG * Deg2Rad

    ANGL = -STPANG * Deg2Rad

    # 计算卫星扫描角
    SIGMA = ANGL * (PIXLE - 1025.0) + HLFANG

    ATTERR = np.zeros(shape=(3), dtype=np.float64)
    orbosele = np.zeros(shape=(8), dtype=np.float64)

    CA = np.cos(ATTERR[0])
    SA = np.sin(ATTERR[0])
    CB = np.cos(ATTERR[1])
    SB = np.sin(ATTERR[1])
    COSG = np.cos(ATTERR[2])
    
    SING1 = -np.sin(ATTERR[2])
    #计算格林尼治恒星时PHIG和太阳黄经CHISUN及黄赤交角EPSLON
    PHIG, DPHIDT, CHISUN, EPSLON = EARTH(TIME)
    # 
    RSOL = 149600881.0
    COSX = np.cos(CHISUN)
    SINX = np.sin(CHISUN)
    COSE = np.cos(EPSLON)
    SINE = np.sin(EPSLON)
    # 计算太阳位置矢量SLP

    SLP = np.zeros(shape=(3), dtype=np.float64)
    SLP[0] = RSOL * COSX
    SLP[1] = RSOL * (SINX * COSE)
    SLP[2] = RSOL * (SINX * SINE)
    
    #  *** THE INPUT ORBITAL PARAMETERS ARE ASSIGNED TO COMMON /SCCOM/.
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
    # /***  THE GEODETIC SUBPOINT IS DETERMINED IN TERMS OF DEVIATIONS FRO
    # !     THE GEOCENTRIC SUBPOINT. THESE DEVIATIONS ARE COMBINED WITH TH
    # !     ROLL AND PITCH, PROVIDING A TRANSFOM FROM THE NOMINAL COORDIN
    # !     SYSTEM TO THE ACTUAL SCANNING COORDINATE SYSTEM.   */
                                                   # 调用TNSUB程序计算卫星垂直高度HSAT和初始姿态COSA,COSB,SINA,SINB
    SINA,COSA,SINB,COSB,HSAT = TNSUB(RSAT, SINP, COSP, SINI, COSI, COST)
    # 
    TEMP = COSA * CA + SINA * SA
    SINA = SINA * CA - COSA * SA
    COSA = TEMP
    TEMP = COSB * CB + SINB * SB
    SINB = SINB * CB - COSB * SB
    COSB = TEMP
    #      THE (ROTATING) EARTH COORDINATES OF THE SCAN POINT ARE DETERMI
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
    # ===========================================
    # /* *** II) THE SCAN DIRECTION CECTOR SIGHAT, IS DETERMINED.
    # !        A) IN SATELLITE CYLINDRICAL COORDINATE SYSTEM,
    # !         SIGHAT = -(SIGR*RSHAT+SIGT*TSHAT+SIGZ*ZSHAT).
    # !         (COMPUTATION OF ACTUAL VALUES COMMENTED OUT AND REPLACED
    # !         WITH APPROXIMATE VALUES.)     */
    SIGR = SINA * COSG * SINS + COSA * COSB * COSS
    SIGT = COSB * SING1 * SINS - SINB * COSS
    SIGZ = COSA * COSG * SINS - SINA * COSB * COSS
    #  计算地心惯性坐标系三个分量 \
       #  \
    SIGXE = SIGR * RSDXE + SIGT * TSDXE + SIGZ * ZSDXE
    SIGYE = SIGR * RSDYE + SIGT * TSDYE + SIGZ * ZSDYE
    SIGZE = SIGR * RSDZE + SIGT * TSDZE + SIGZ * ZSDZE
    # /* *** III) THE SCAN VECTOR IS: RSAT*RSHAT+LAMBDA*SIGHAT,
    # !          WHERE LAMBDA PARAMETERIZES THE SCAN VECTOR.
    # !          THE VALUE OF LAMBDA AT THE EARTH,S SURFACE IS DETERMINED.
    # !     A = 1.0+E2E21*SIGZE*SIGZE
    # !     B = RSAT*(SIGR+E2E21*SINP*SIGZE)
    # !     C = RSAT*RSAT*((10-(AE*AE)/(RSAT*RSAT))+E2E21*SINP*SINP)
    # !     LAMBDA=(B-sqrt(B*B-A*C))/A     */
    #              # 计算扫描点斜距LAMBDA(点到卫星距离)
    A0 = 1.0
    A1 = SIGZE * SIGZE
    B0 = SIGR
    B1 = SINP * SIGZE
    C0 = 1.0 - (AE * AE) / (RSAT * RSAT)
    C1 = SINP * SINP
    B2MAC = ((B0 * B0 - A0 * C0) + ((B0 * B1 - A0 * C1) + (B0 * B1 - A1 * C0)) * E2E21) + \
            ((B1 * B1 - A1 * C1) * E2E21 * E2E21)
    LAMBDA = RSAT * ((B0 - sqrt(B2MAC)) + B1 * E2E21) / (A0 + A1 * E2E21)
    # # =================================================================
    # /* *** IV) THE GEOCENTRIC INERTIAL COORDINATES OF THE SCAN POINT ARE
    # !         DETERMINED AND CONVERTED TO RIGHT ASCENSION (COSM,SINM)
    # !         DECLINATION (COSL,SINL).    */
    #           # 计算椭球面坐标系三个分量
    SMAG = np.sqrt(RSAT * (RSAT - 2.0 * LAMBDA * SIGR) + LAMBDA * LAMBDA)
    SP = [RSAT * RSDXE, RSAT * RSDYE, RSAT * RSDZE,]
    SDOTX = SP[0] - LAMBDA * SIGXE
    SDOTY = SP[1] - LAMBDA * SIGYE
    SDOTZ = SP[2] - LAMBDA * SIGZE
    #  计算扫描点经度和纬度
    SINL = SDOTZ / SMAG
    COSL = np.sqrt(1.0 - SINL * SINL)
    COSM = SDOTX / (SMAG * COSL)
    SINM = SDOTY / (SMAG * COSL)
    SCNLAT = np.atan(SINL / (COSL * E21))
    SCNLON = np.atan2(SINM, COSM) - PHIG
    #      THE ZENITH ANGLE IS COMPUTED BASED ON FLAG ANGTYP.
    if (SCNLON > np.pi) :  SCNLON = SCNLON - 2*np.pi
    if (SCNLON <= -np.pi): SCNLON = SCNLON + 2*np.pi
    # =================================================
    
    # /*      write(*,*)'scnlat,scnlon:',scnlat,scnlon
    # !      SIND=SINX*SINE
    # !      CDCH=COSM*COSX+SINM*SINX*COSE
    # !      SOLZEN=DACOS(SINL*SIND+COSL*CDCH)
    # !      ELSE IF(ANGTYP.EQ.2) THEN
    # ! *** SATELLITE ZENITH ANGLE COMPUTATION ***
    # !
    # !      SIND=SINP
    # !      CDCH= COSM*(COST*COSO-SINT*SINO*COSI)+SINM*(COST*SINO+SINT
    #                                                    !     $  *COSO *COSI)
    # !      SATZEN=DACOS(SINL*SIND+COSL*CDCH)+DABS(SIGMA)   */
                  # 计算太阳高度角和方位角
    SOLAZ, SOLELV = ICGS(SLP, SINM, COSM)
    # 计算卫星高度角

    SATAZ, SATELV = ICGS(SP, SINM, COSM, )
    # 计算天顶角和方位角
    SOLZEN = 0.50 * np.pi - SOLELV
    SATZEN = 0.50 * np.pi - SATELV
    #      *SATZEN=*SATZEN+abs(SIGMA) 
    # 计算太阳相对卫星方位角
    SSAZ = SOLAZ - SATAZ# ???????????????????????????????????????
    if (SSAZ <= 0) :
        SSAZ = SSAZ + 2*np.pi
    HEIGHT = HSAT
    return None

# /*
# ! *****************************************************************!
# ! *****  EARTH 计算格林尼治恒星时、太阳真黄经和黄赤交角程序     ***!
# ! *****************************************************************/
# 
# 
# /*
# !  功能: 已知时间，计算格林尼治恒星时、太阳真黄经和黄赤交角
# !
# !  输入参数
# !  TIME  (R*8)     : 时间（1980年起算的秒时间）
# !  输出参数
# !  ALPHA           : 格林尼真治恒星时 [弧度]
# !  ALPDOT          : 格林尼真治恒星时变化率 [弧度/秒]
# !  CHISUN		   : 太阳真黄经		  [弧度]
# !  OBLIQE          : 黄赤交角         [弧度]  */
def EARTH(TIME, ALPHA, ALPDOT, CHISUN, OBLIQE) :
    '''
    # double PHIGRN[3], CHIMS[3], MEARTH[3], OMEGA[3], EPSLON[2], \
    #        DELPSI[2], DELEPS[2]
    # double KAPPA, MANOM0, ZERO80, CENTCT, DDATE, DATE, EPTIME, CENTNO
    # double ALPHA0, DADT, CHIMO, DXMDT, OMEGA0, DMDT, DWDT, EPSLN0, \
    #        DEDT, DELP0, DDPDT, DELE0, DDEDT, CHI0, DXDT, ANUT0, DANDT, Dtime
    # int IDATE2
    :param TIME:
    :param ALPHA:
    :param ALPDOT:
    :param CHISUN:
    :param OBLIQE:
    :return:
    '''
    PHIGRN = np.zeros(shape=(3), dtype=np.float64)
    CHIMS = np.zeros(shape=(3), dtype=np.float64)
    MEARTH = np.zeros(shape=(3), dtype=np.float64)
    OMEGA = np.zeros(shape=(3), dtype=np.float64)
    EPSLON = np.zeros(shape=(2), dtype=np.float64)
    DELPSI = np.zeros(shape=(2), dtype=np.float64)
    DELEPS = np.zeros(shape=(2), dtype=np.float64)

    PHIGRN[0] = 1.739935890
    PHIGRN[1] = 628.33195070
    PHIGRN[2] = .000006754947810
    CHIMS[0] = 4.881633570
    CHIMS[1] = 628.3319487050
    CHIMS[2] = 1.4468088e-10

    MEARTH[0] = 6.256581470
    MEARTH[1] = 628.3019468590
    MEARTH[2] = -7.1676766e-11
    OMEGA[0] = 4.523636080
    OMEGA[1] = -33.7571619360
    OMEGA[2] = 9.9285594E-10
    EPSLON[0] = .40936890950
    EPSLON[1] = -2.27232172336e-4
    KAPPA = .0335020
    DELPSI[0] = 8.35465e-5
    DELPSI[1] = .61712e-5
    DELEPS[0] = 4.46513e-5
    DELEPS[1] = .26771e-5
    ZERO80 = 29219.50
    CENTCT = 36525.0
    # *** I) IF THIS THE FIRSTCALL TO EARTH THEN
    #! ***   A) THE JULIAN DAY NUMBER NEAREST THE INPUT TIME IS DETERMINE
    #!      IF(FIRST.eq. 1.0) then
    DDATE = ZERO80 + TIME / 86400.0
    IDATE2 = 2. * DDATE
    if ((IDATE2 % 2) == 0) :
        IDATE2 = IDATE2 - 1
    DATE = IDATE2 * .50
    if (DDATE - DATE > .50):
        DATE = DATE + 1.0
    EPTIME = (DATE - ZERO80) * 86400.0
    CENTNO = DATE / CENTCT
    # ***    B) THE HOUR ANGLE (ALPHA), NUTATION (ANUT),LONGITUDE OF THE
    #! ***       SUN (CHI) AND OBLIQUITY OF THE ECLIPTIC (EPSLN) AND THEI
    #***       DERIVATIVES AT THE EPOCH TID5 ARE DETERMINED. \

    ALPHA0 = ZSODSRadto2Pai(PHIGRN[0] + \
                            ZSODSRadto2Pai(CENTNO * (PHIGRN[1] + CENTNO * PHIGRN[2])))
    DADT = (2*np.pi + (PHIGRN[1] + 2. * CENTNO * PHIGRN[2]) / CENTCT) / 86400.
    CHIMO = ZSODSRadto2Pai(CHIMS[0] +\
                           ZSODSRadto2Pai(CENTNO * (CHIMS[1] + CENTNO * CHIMS[2])))
    DXMDT = (CHIMS[1] + 2. * CENTNO * CHIMS[2]) / (86400.0 * CENTCT)
    MANOM0 = ZSODSRadto2Pai(MEARTH[0] +\
                            ZSODSRadto2Pai(CENTNO * (MEARTH[1] + CENTNO * MEARTH[2])))
    DMDT = (MEARTH[1] + 2. * CENTNO * MEARTH[2]) / (86400.0 * CENTCT)
    OMEGA0 = ZSODSRadto2Pai(OMEGA[0] +\
                            ZSODSRadto2Pai(CENTNO * (OMEGA[1] + CENTNO * OMEGA[2])))
    DWDT = (OMEGA[1] + 2. * CENTNO * OMEGA[2]) / (86400.0 * CENTCT)
    EPSLN0 = EPSLON[0] + CENTNO * EPSLON[1]
    DEDT = EPSLON[1] / (86400.0 * CENTCT)
    DELP0 = DELPSI[0] * sin(OMEGA0) + DELPSI[1] * sin(2.0 * CHIMO)
    DDPDT = DELPSI[0] * cos(OMEGA0) * DWDT + DELPSI[1] * cos(2. * CHIMO)  * 2.0 * DXMDT
    DELE0 = DELEPS[0] * cos(OMEGA0) + DELEPS[1] * cos(2.0 * CHIMO)
    DDEDT = -DELEPS[0] * sin(OMEGA0) * DWDT - DELEPS[1] * sin(2.0 * CHIMO) * 2.0 * DXMDT
    CHI0 = CHIMO + KAPPA * sin(MANOM0)
    DXDT = DXMDT + KAPPA * cos(MANOM0) * DMDT
    ANUT0 = DELP0 * cos(EPSLN0 + DELE0)
    DANDT = DDPDT * ANUT0 / DELP0 - DELP0 * sin(EPSLN0 + DELE0) * (DEDT + DDEDT)
    Dtime = TIME - EPTIME
    ALPHA = ZSODSRadto2Pai(ALPHA0 + ANUT0 + (DADT + DANDT) * Dtime)
    ALPDOT = DADT + DANDT
    CHISUN = ZSODSRadto2Pai(CHI0 + DXDT * Dtime)
    OBLIQE = EPSLN0 + DELE0 + (DEDT + DDEDT) * Dtime

    return None

def ZSODSRadto2Pai(dRad):

    # double dresult

    dresult = dRad - 2*np.pi * ((int)(dRad / 2*np.pi))
    if (dRad < 0.0) :
        dresult += 2*np.pi

    return dresult


def TNSUB(RSAT, SINP, COSP, SINI, COSI, COST) :

    RX = RSAT * COSP
    RZ = RSAT * SINP
    rzcrx2 = RZ / RX
    X = AE / sqrt(1.0 + (rzcrx2 * rzcrx2) / E21)
    for i in range(100) :
        XO = X
        rzx2 = RZ / (RX - E2 * XO)
        X = AE / sqrt(1.0 + E21 * (rzx2 * rzx2))
        #      X=AE/sqrt(1.0+E21*(RZ/(RX-E2*XO))**2)
        dxi = (X - XO) / X
        if (dxi < 0) : dxi = -dxi

        if (dxi <= 1.0e-6): break

    Z = E21 * (RZ * X / (RX - E2 * X))
    HX = X - RX
    HZT = Z - RZ
    HSAT = sqrt(HX * HX + HZT * HZT)
    HBAR = (COSP * HZT - SINP * HX) / COSP
    TDOTH = COST * SINI * HBAR
    ZDOTH = COSI * HBAR

    SINB = TDOTH / (HSAT)
    COSB = 1.0 - .5 * (SINB) * (SINB)

    SINA = ZDOTH / ((HSAT) * (COSB))
    COSA = sqrt(1.0 - (SINA) * (SINA))

    return SINA, COSA,  SINB, COSB, HSAT


# /* *****************************************************************!
# ! ***  ICGS 计算卫星瞬时轨道相对观测点的位置(方位角和仰角)程序  **!
# ! ******************************************************************/

def ICGS(RX, Sth, Cth) :


    # /*输入参数
    # !  RX(3)(R*8) : 卫星空间位置矢量（x,y,z)
    # !  Sth (R*8)  :  观测点SIN(S) S:观测点的地方恒星时
    # !  Cth        :	 观测点COS(S)
    # !  Glat		  :  观测点的纬度[弧度]
    # !  输出参数
    # !  azgs	 	  :	 TIME时刻的卫星相对观测站的方位角
    # !  elgs	      :	 TIME时刻的卫星相对观测站的仰角    */

    #                        double  Sla, Cla
    # double Gxic, Gyic, Gzic, Rhx, Rhy, Rhz
    # double Rht, Rxgs, Rygs, Rzgs
    # double HGT, RE2
    HGT = 50.0 / 6378137.0
    Sla = sin(SCNLAT)
    Cla = cos(SCNLAT)
    RE2 = AE / sqrt(1.0 - E2 * Sla * Sla)
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

    Azgs = np.atan2(Rxgs, Rygs)
    if (Azgs < 0.0) :
        Azgs = Azgs + 2*np.pi
    Elgs = np.atan(Rzgs / sqrt(Rxgs * Rxgs + Rygs * Rygs))

    #	*Rgs = sqrt(Rhx*Rhx+Rhy*Rhy+Rhz*Rhz)

    return Azgs, Elgs

def TNSUB(RSAT, SINP, COSP, SINI, COSI,  COST, SINA, COSA, SINB, COSB,  HSAT):

    # double RX, RZ, X, XO, Z, HX
    # double HZT, HBAR, TDOTH, ZDOTH, rzx2, dxi
    # double rzcrx2
    # int i
    RX = RSAT * COSP
    RZ = RSAT * SINP
    rzcrx2 = RZ / RX
    X = AE / sqrt(1.0 + (rzcrx2 * rzcrx2) / E21)
    for i in range(100) :
        XO = X
        rzx2 = RZ / (RX - E2 * XO)
        X = AE / sqrt(1.0 + E21 * (rzx2 * rzx2))
        #      X=AE/sqrt(1.0+E21*(RZ/(RX-E2*XO))**2) 
        dxi = (X - XO) / X
        if (dxi < 0) :dxi = -dxi
    
        if (dxi <= 1.0e-6) :break
    
    Z = E21 * (RZ * X / (RX - E2 * X))
    HX = X - RX
    HZT = Z - RZ
    HSAT = sqrt(HX * HX + HZT * HZT)
    HBAR = (COSP * HZT - SINP * HX) / COSP
    TDOTH = COST * SINI * HBAR
    ZDOTH = COSI * HBAR

    SINB = TDOTH / (HSAT)
    COSB = 1.0 - .5 * (SINB) * (SINB)

    SINA = ZDOTH / ((HSAT) * (COSB))
    COSA = sqrt(1.0 - (SINA) * (SINA))

    return SINA,COSA,SINB,COSB,HSAT


