# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadERA5.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
下载ERA5 再分析廓线数据和地面分析资料
'''
import sys
import os
import cdsapi
import datetime

import numpy as np
from dateutil.relativedelta import relativedelta


class downloadERA5(object):
    def __init__(self, key=None, url='https://cds.climate.copernicus.eu/api'):
        self.url = url
        self.key = key

        self.checkkeys(self.url, self.key)

    def searchfile(
            self,
            startDate,
            endDate=None,
            dataset="reanalysis-era5-pressure-levels",
            variable=["temperature"],
            bbox=None,
            pressure_level=["1", "2", "3", "5", "7", "10",
                "20", "30", "50", "70", "100", "125",
                "150", "175", "200", "225", "250", "300",
                "350", "400", "450", "500", "550", "600",
                "650", "700", "750", "775", "800", "825",
                "850", "875", "900", "925", "950", "975", "1000"],
            format='netcdf',
            compressed=False,
            everyday=False,
    ):
        urls = []

        nowdate = startDate
        while nowdate <= endDate:
            hours = [np.min([startDate.hour, endDate.hour]),
                     np.max(startDate.hour, endDate.hour)]


            downinfo = {}

            downinfo['product_type'] = ['reanalysis']
            downinfo['variable'] = variable


            if bbox is None :
                downinfo['area'] = [90, -180, -90, 180]
            else:
                downinfo['area'] = [bbox[3], bbox[0], bbox[1], bbox[2]]

            if format.lower() in ['netcdf']:
                downinfo['data_format'] = 'netcdf'
            else:
                downinfo['data_format'] = 'grib'

            if compressed :
                downinfo["download_format"] = "zip"
            else:
                downinfo["download_format"] = "unarchived"

            if everyday :
                hours = np.arange(hours[0], hours[1]+1)
                for hour in hours :
                    downinfo['year']  = [nowdate.strftime('%Y')]
                    downinfo['month'] = [nowdate.strftime('%m')]
                    downinfo['day']   = [nowdate.strftime('%d')]
                    downinfo['time']  = ['%02d:00' %(hour) ]

                    if format.lower() in ['netcdf']:
                        target = '%s_%02d0000.nc' %(nowdate.strftime('%Y%m%d'), hour)
                    else:
                        target = '%s_%02d0000.grib' %(nowdate.strftime('%Y%m%d'), hour)

                    urls.append({
                        'dataset' : dataset,
                        'request' : downinfo,
                        'target' :  target}
                    )
                nowdate += relativedelta(days=1)
            else:
                downinfo['year']  = [nowdate.strftime('%Y')]
                downinfo['month'] = [nowdate.strftime('%m')]
                downinfo['day']   = [nowdate.strftime('%d')]
                downinfo['time']  = ['%02d:00' %(nowdate.hour) ]

                if format.lower() in ['netcdf']:
                    target = '%s_%02d0000.nc' %(nowdate.strftime('%Y%m%d'), nowdate.hour)
                else:
                    target = '%s_%02d0000.grib' %(nowdate.strftime('%Y%m%d'), nowdate.hour)

                urls.append({
                    'dataset' : dataset,
                    'request' : downinfo,
                    'target' :  target}
                )
                nowdate += relativedelta(hours=1)

        return urls

    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False, cover=False, continuing=True, **kwargs):

        self.m_client = cdsapi.Client(timeout=timeout, retry_max=tries, sleep_max=60)

        for url1 in url :
            if 'target' in url1 :
                target = os.path.join(outdir, url1['target'])
            else:
                target = None
            print(url1)
            self.m_client.retrieve(url1['dataset'], url1['request']).download(target)

    def checkkeys(self, url, key) :
        ''' 检查密钥 '''

        keyfile = os.environ.get("CDSAPI_RC", os.path.expanduser("~/.cdsapirc"))
        tempfile = os.environ.get("CDSAPI_RC", os.path.expanduser("~/temp.txt"))
        if not os.path.isfile(keyfile):
            print('【%s】不存在，将创建它' %(keyfile))
            if url is None or key is None :
                raise Exception('请输入cdsapi账号的链接和密钥')

            fp = open(tempfile, 'w')
            fp.write('url: %s\n' %(url))
            fp.write('key: %s\n' %(key))
            fp.close()
            os.rename(tempfile, keyfile)
        else:
            if key is not None :
                fp = open(tempfile, 'w')
                fp.write('url: %s\n' %(url))
                fp.write('key: %s\n' %(key))
                fp.close()
                os.remove(keyfile)
                os.rename(tempfile, keyfile)
            with open(keyfile) as fp :
                lines = fp.readlines()
                fp.close()
                print(lines)


if __name__ == '__main__':
    downloader = downloadERA5(url='https://cds.climate.copernicus.eu/api', key='f974adde-3b12-4fbb-9c02-1ff21851e234')
    urls = downloader.searchfile(
        startDate=datetime.datetime(2025, 1, 26),
        endDate=datetime.datetime(2025, 1, 26),
        dataset='reanalysis-era5-single-levels',
        variable=[
            '100m_u_component_of_wind',
            '100m_v_component_of_wind',
            '10m_u_component_of_neutral_wind',
                  '10m_u_component_of_wind',
            '10m_v_component_of_neutral_wind',
            '10m_v_component_of_wind',
                  # '10m_wind_gust_since_previous_post_processing',
            '2m_dewpoint_temperature',
            '2m_temperature',
                  'air_density_over_the_oceans', 'altimeter_corrected_wave_height', 'altimeter_range_relative_correction',
                  'altimeter_wave_height', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography',
                  'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height',
                  'charnock', 'clear_sky_direct_solar_radiation_at_surface', 'cloud_base_height',
                  'coefficient_of_drag_with_waves', 'convective_available_potential_energy', 'convective_inhibition',
                  'convective_precipitation', 'convective_rain_rate', 'convective_snowfall',
                  'convective_snowfall_rate_water_equivalent', 'downward_uv_radiation_at_the_surface', 'duct_base_height',
                  'eastward_gravity_wave_surface_stress', 'eastward_turbulent_surface_stress', 'evaporation',
                  'forecast_albedo', 'forecast_logarithm_of_surface_roughness_for_heat', 'forecast_surface_roughness',
                  'free_convective_velocity_over_the_oceans', 'friction_velocity', 'gravity_wave_dissipation',
                  'high_cloud_cover', 'high_vegetation_cover', 'ice_temperature_layer_1',
                  'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4',
                  'instantaneous_10m_wind_gust',
            # 'instantaneous_eastward_turbulent_surface_stress',
                  'instantaneous_large_scale_surface_precipitation_fraction',
                  'instantaneous_moisture_flux',
            # 'instantaneous_northward_turbulent_surface_stress',
                  'instantaneous_surface_sensible_heat_flux',
                  'k_index', 'lake_bottom_temperature', 'lake_cover',
                  'lake_depth', 'lake_ice_depth', 'lake_ice_temperature',
                  'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor',
                  'lake_total_layer_temperature', 'land_sea_mask', 'large_scale_precipitation',
                  'large_scale_precipitation_fraction', 'large_scale_rain_rate', 'large_scale_snowfall',
                  'large_scale_snowfall_rate_water_equivalent', 'leaf_area_index_high_vegetation',
                  'leaf_area_index_low_vegetation',
                  'low_cloud_cover', 'low_vegetation_cover',
            # 'maximum_2m_temperature_since_previous_post_processing',
                  'maximum_individual_wave_height',
            # 'maximum_total_precipitation_rate_since_previous_post_processing',
                  'mean_boundary_layer_dissipation',
                  'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate', 'mean_direction_of_total_swell',
                  'mean_direction_of_wind_waves',
            # 'mean_eastward_gravity_wave_surface_stress',
            #       'mean_eastward_turbulent_surface_stress',
                  'mean_evaporation_rate', 'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction',
                  'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate',
                  # 'mean_northward_gravity_wave_surface_stress',
                  # 'mean_northward_turbulent_surface_stress',
            'mean_period_of_total_swell', 'mean_period_of_wind_waves',
                  'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_sea_level_pressure',
                  'mean_snow_evaporation_rate', 'mean_snowfall_rate', 'mean_snowmelt_rate',
                  'mean_square_slope_of_waves', 'mean_sub_surface_runoff_rate',
                  'mean_surface_direct_short_wave_radiation_flux',
                  'mean_surface_direct_short_wave_radiation_flux_clear_sky',
                  'mean_surface_downward_long_wave_radiation_flux',
                  'mean_surface_downward_long_wave_radiation_flux_clear_sky',
                  'mean_surface_downward_short_wave_radiation_flux',
                  'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux',
                  'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux',
                  'mean_surface_net_long_wave_radiation_flux_clear_sky',
                  'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky',
                  'mean_surface_runoff_rate',
                  'mean_surface_sensible_heat_flux', 'mean_top_downward_short_wave_radiation_flux',
                  'mean_top_net_long_wave_radiation_flux',
                  'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux',
                  'mean_top_net_short_wave_radiation_flux_clear_sky',
                  'mean_total_precipitation_rate', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer',
                  'mean_vertically_integrated_moisture_divergence',
                  'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition',
                  'mean_wave_direction_of_second_swell_partition',
                  'mean_wave_direction_of_third_swell_partition', 'mean_wave_period',
                  'mean_wave_period_based_on_first_moment',
                  'mean_wave_period_based_on_first_moment_for_swell',
                  'mean_wave_period_based_on_first_moment_for_wind_waves',
                  'mean_wave_period_based_on_second_moment_for_swell',
                  'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition',
                  'mean_wave_period_of_second_swell_partition',
                  'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period', 'medium_cloud_cover',
                  # 'minimum_2m_temperature_since_previous_post_processing',
                  # 'minimum_total_precipitation_rate_since_previous_post_processing',
                  'minimum_vertical_gradient_of_refractivity_inside_trapping_layer',
                  'model_bathymetry', 'near_ir_albedo_for_diffuse_radiation', 'near_ir_albedo_for_direct_radiation',
                  'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves',
                  'normalized_stress_into_ocean',
                  'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress',
                  'ocean_surface_stress_equivalent_10m_neutral_wind_direction',
                  'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'orography', 'peak_wave_period',
                  'period_corresponding_to_maximum_individual_wave_height', 'potential_evaporation', 'precipitation_type',
                  'runoff', 'sea_ice_cover', 'sea_surface_temperature',
                  'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell',
                  'significant_height_of_wind_waves',
                  'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition',
                  'significant_wave_height_of_third_swell_partition',
                  'skin_reservoir_content', 'skin_temperature', 'slope_of_sub_gridscale_orography',
                  'snow_albedo', 'snow_density', 'snow_depth',
                  'snow_evaporation', 'snowfall', 'snowmelt',
                  'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3',
                  'soil_temperature_level_4', 'soil_type', 'standard_deviation_of_filtered_subgrid_orography',
                  'standard_deviation_of_orography', 'sub_surface_runoff', 'surface_latent_heat_flux',
                  'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 'surface_net_thermal_radiation',
                  'surface_net_thermal_radiation_clear_sky', 'surface_pressure', 'surface_runoff',
                  'surface_sensible_heat_flux', 'surface_solar_radiation_downward_clear_sky',
                  'surface_solar_radiation_downwards',
                  'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards',
                  'temperature_of_snow_layer',
                  'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky',
                  'top_net_thermal_radiation', 'top_net_thermal_radiation_clear_sky', 'total_cloud_cover',
                  'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_ozone',
                  'total_column_rain_water', 'total_column_snow_water', 'total_column_supercooled_liquid_water',
                  'total_column_water', 'total_column_water_vapour', 'total_precipitation',
                  'total_sky_direct_solar_radiation_at_surface', 'total_totals_index', 'trapping_layer_base_height',
                  'trapping_layer_top_height', 'type_of_high_vegetation', 'type_of_low_vegetation',
                  'u_component_stokes_drift', 'uv_visible_albedo_for_diffuse_radiation',
                  'uv_visible_albedo_for_direct_radiation',
                  'v_component_stokes_drift', 'vertical_integral_of_divergence_of_cloud_frozen_water_flux',
                  'vertical_integral_of_divergence_of_cloud_liquid_water_flux',
                  'vertical_integral_of_divergence_of_geopotential_flux',
                  'vertical_integral_of_divergence_of_kinetic_energy_flux',
                  'vertical_integral_of_divergence_of_mass_flux',
                  'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux',
                  'vertical_integral_of_divergence_of_thermal_energy_flux',
                  'vertical_integral_of_divergence_of_total_energy_flux',
                  'vertical_integral_of_eastward_cloud_frozen_water_flux',
                  'vertical_integral_of_eastward_cloud_liquid_water_flux',
                  'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux',
                  'vertical_integral_of_eastward_kinetic_energy_flux',
                  'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux',
                  'vertical_integral_of_eastward_total_energy_flux',
                  'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion',
                  'vertical_integral_of_kinetic_energy',
                  'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency',
                  'vertical_integral_of_northward_cloud_frozen_water_flux',
                  'vertical_integral_of_northward_cloud_liquid_water_flux',
                  'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux',
                  'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux',
                  'vertical_integral_of_northward_ozone_flux',
                  'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux',
                  'vertical_integral_of_potential_and_internal_energy',
                  'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature',
                  'vertical_integral_of_thermal_energy',
                  'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence',
                  'volumetric_soil_water_layer_1',
                  'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
                  'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell',
                  'wave_spectral_directional_width_for_wind_waves',
                  'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness',
                  'zero_degree_level',
            ],
        bbox=[100, 0, 160, 60]
    )

    downloader.download(outdir=r'D:\DATA\ERA5', url=urls)