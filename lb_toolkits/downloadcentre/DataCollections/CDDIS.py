from lb_toolkits.downloadcentre.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionCDDIS : 
    CDDIS_CDDIS_GNSS_products_IGS20_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_IGS20_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_IGS20",
            version="1",
            description="CDDIS GNSS ITRF2020 IGS products (IGS20) version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_daily_tropo_delay_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_daily_tropo_delay_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_daily_tropo_delay",
            version="1",
            description="CDDIS SESES MEaSUREs GNSS products daily tropospheric delay version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_daily_time_series_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_daily_time_series_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_daily_time_series",
            version="1",
            description="CDDIS SESES MEaSUREs products daily GNSS geodetic displacement time series version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_earthquake_displacement_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_earthquake_displacement_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_earthquake_displacement",
            version="1",
            description="CDDIS SESES MEaSUREs products highrate earthquake displacement version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_transients_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_transients_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_transients",
            version="1",
            description="CDDIS SESES MEaSUREs products plate boundary aseismic transient deformation version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_strain_rate_grids_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS MEASURES products strain rate grids_1",
            provider="CDDIS", 
            shortname="CDDIS MEASURES products strain rate grids",
            version="1",
            description="CDDIS SESES MEaSUREs products strain rate grids version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_water_storage_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_water_storage_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_water_storage",
            version="1",
            description="CDDIS SESES MEaSUREs products total water storage time series version: 1"
        )

    CDDIS_CDDIS_MEaSURES_products_velocities_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS MEaSURES products velocities_1",
            provider="CDDIS", 
            shortname="CDDIS MEaSURES products velocities",
            version="1",
            description="CDDIS SESES MEaSUREs products velocities version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_coseismic_offsets_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_coseismic_offsets_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_coseismic_offsets",
            version="1",
            description="CDDIS SESES MEaSUREs products weekly coseismic offset time series version: 1"
        )

    CDDIS_CDDIS_MEASURES_products_discplacement_grids_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MEASURES_products_discplacement_grids_1",
            provider="CDDIS", 
            shortname="CDDIS_MEASURES_products_discplacement_grids",
            version="1",
            description="CDDIS SESES MEaSUREs products weekly displacement grids time series version: 1"
        )

    CDDIS_CDDIS_SLR_products_ITRF2020_REPRO2020_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_products_ITRF2020_REPRO2020_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_products_ITRF2020_REPRO2020",
            version="1",
            description="CDDIS SLR products ITRF2020 Station Positions and Earth Orientation Parameters Time Series REPRO2020 version: 1"
        )

    CDDIS_CDDIS_VLBI_data_aux_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_aux_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data_aux",
            version="1",
            description="CDDIS VLBI Auxilliary Files version: 1"
        )

    CDDIS_CDDIS_VLBI_product_EOPI_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_product_EOPI_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_product_EOPI",
            version="1",
            description="CDDIS VLBI Intensive Earth Orientation Parameter (EOPI) products version: 1"
        )

    CDDIS_CDDIS_VLBI_data_ngs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_ngs_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data_ngs",
            version="1",
            description="CDDIS VLBI NGS data version: 1"
        )

    CDDIS_CDDIS_VLBI_data_SWIN_V1A = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_SWIN_1A",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data_SWIN",
            version="1A",
            description="CDDIS VLBI SWIN data version: 1A"
        )

    CDDIS_CDDIS_VLBI_data_db_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_db_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data_db",
            version="1",
            description="CDDIS VLBI data DB version: 1"
        )

    CDDIS_CDDIS_VLBI_data_vgosDB_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_vgosDB_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data_vgosDB",
            version="1",
            description="CDDIS VLBI level 2 vgosDB format data version: 1"
        )

    CDDIS_CDDIS_VLBI_product_trf_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_product_trf_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_product_trf",
            version="1",
            description="CDDIS VLBI products Terrestrial Reference Frame version: 1"
        )

    CDDIS_CDDIS_DORIS_data_cycle_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_data_cycle_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_data_cycle",
            version="1",
            description="CDDIS_DORIS_data_cycle version: 1"
        )

    CDDIS_CDDIS_DORIS_data_rinex_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_data_rinex_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_data_rinex",
            version="1",
            description="CDDIS_DORIS_data_rinex version: 1"
        )

    CDDIS_CDDIS_DORIS_products_geocenter_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_geocenter_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_geocenter",
            version="1",
            description="CDDIS_DORIS_products_geocenter version: 1"
        )

    CDDIS_CDDIS_DORIS_products_ionosphere_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_ionosphere_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_ionosphere",
            version="1",
            description="CDDIS_DORIS_products_ionosphere version: 1"
        )

    CDDIS_CDDIS_DORIS_products_orbit_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_orbit_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_orbit",
            version="1",
            description="CDDIS_DORIS_products_orbit version: 1"
        )

    CDDIS_CDDIS_DORIS_products_positions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_positions_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_positions",
            version="1",
            description="CDDIS_DORIS_products_positions version: 1"
        )

    CDDIS_CDDIS_DORIS_products_quaternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_quaternions_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_quaternions",
            version="1",
            description="CDDIS_DORIS_products_quaternions version: 1"
        )

    CDDIS_CDDIS_DORIS_products_stcd_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_products_stcd_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_products_stcd",
            version="1",
            description="CDDIS_DORIS_products_stcd version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data",
            version="1",
            description="CDDIS_GNSS_highrate_data version: 1"
        )

    CDDIS_CDDIS_GNSS_products_clocks_final_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_clocks_final_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_clocks_final",
            version="1",
            description="CDDIS_GNSS_products_clocks_final version: 1"
        )

    CDDIS_CDDIS_GNSS_products_clocks_rapid_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_clocks_rapid_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_clocks_rapid",
            version="1",
            description="CDDIS_GNSS_products_clocks_rapid version: 1"
        )

    CDDIS_CDDIS_GNSS_products_clocks_realtime_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_clocks_realtime_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_clocks_realtime",
            version="1",
            description="CDDIS_GNSS_products_clocks_realtime version: 1"
        )

    CDDIS_CDDIS_GNSS_products_erp_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_erp_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_erp",
            version="1",
            description="CDDIS_GNSS_products_erp version: 1"
        )

    CDDIS_CDDIS_GNSS_products_ionosphere_final_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_ionosphere_final_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_ionosphere_final",
            version="1",
            description="CDDIS_GNSS_products_ionosphere_final version: 1"
        )

    CDDIS_CDDIS_GNSS_products_ionosphere_predicted_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_ionosphere_predicted_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_ionosphere_predicted",
            version="1",
            description="CDDIS_GNSS_products_ionosphere_predicted version: 1"
        )

    CDDIS_CDDIS_GNSS_products_ionosphere_rapid_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_ionosphere_rapid_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_ionosphere_rapid",
            version="1",
            description="CDDIS_GNSS_products_ionosphere_rapid version: 1"
        )

    CDDIS_CDDIS_GNSS_products_orbit_rapid_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_orbit_rapid_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_orbit_rapid",
            version="1",
            description="CDDIS_GNSS_products_orbit_rapid version: 1"
        )

    CDDIS_CDDIS_GNSS_products_orbit_realtime_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_orbit_realtime_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_orbit_realtime",
            version="1",
            description="CDDIS_GNSS_products_orbit_realtime version: 1"
        )

    CDDIS_CDDIS_GNSS_products_orbit_ultrarapid_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_orbit_ultrarapid_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_orbit_ultrarapid",
            version="1",
            description="CDDIS_GNSS_products_orbit_ultrarapid version: 1"
        )

    CDDIS_CDDIS_GNSS_products_positions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_positions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_positions",
            version="1",
            description="CDDIS_GNSS_products_positions version: 1"
        )

    CDDIS_CDDIS_GNSS_products_troposphere_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_troposphere_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_troposphere",
            version="1",
            description="CDDIS_GNSS_products_troposphere version: 1"
        )

    CDDIS_CDDIS_GNSS_satellite_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_satellite_data_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_satellite_data",
            version="1",
            description="CDDIS_GNSS_satellite_data version: 1"
        )

    CDDIS_CDDIS_LLR_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_LLR_data_1",
            provider="CDDIS", 
            shortname="CDDIS_LLR_data",
            version="1",
            description="CDDIS_LLR_data version: 1"
        )

    CDDIS_CDDIS_MISC_information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_MISC_information_1",
            provider="CDDIS", 
            shortname="CDDIS_MISC_information",
            version="1",
            description="CDDIS_MISC_information version: 1"
        )

    CDDIS_CDDIS_SLR_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data",
            version="1",
            description="CDDIS_SLR_data version: 1"
        )

    CDDIS_CDDIS_SLR_predictions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_predictions_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_predictions",
            version="1",
            description="CDDIS_SLR_predictions version: 1"
        )

    CDDIS_CDDIS_SLR_products_poseop_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_products_poseop_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_products_poseop",
            version="1",
            description="CDDIS_SLR_products_poseop version: 1"
        )

    CDDIS_CDDIS_VLBI_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_data_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_data",
            version="1",
            description="CDDIS_VLBI_data version: 1"
        )

    CDDIS_CDDIS_VLBI_products_crf_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_products_crf_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_products_crf",
            version="1",
            description="CDDIS_VLBI_products_crf version: 1"
        )

    CDDIS_CDDIS_VLBI_products_eop_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_products_eop_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_products_eop",
            version="1",
            description="CDDIS_VLBI_products_eop version: 1"
        )

    CDDIS_CDDIS_VLBI_products_positions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_products_positions_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_products_positions",
            version="1",
            description="CDDIS_VLBI_products_positions version: 1"
        )

    CDDIS_CDDIS_VLBI_products_troposphere_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_products_troposphere_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_products_troposphere",
            version="1",
            description="CDDIS_VLBI_products_troposphere version: 1"
        )

    CDDIS_DORIS_DATA_RINEX_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_DORIS_DATA_RINEX_1",
            provider="CDDIS", 
            shortname="DORIS_DATA_RINEX",
            version="1",
            description="DORIS_DATA_RINEX version: 1"
        )

    CDDIS_CDDIS_SLR_SLRF2020_DHF_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_SLRF2020_DHF_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_SLRF2020_DHF",
            version="1",
            description="Data Handling File for the International Laser Ranging Service (ILRS) extension of the International Terrestrial Reference Frame 2020 (ITRF2020) TRF Model with additional SLR sites version: 1"
        )

    CDDIS_CDDIS_IERSrspcEOP_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_IERSrspcEOP_product_1",
            provider="CDDIS", 
            shortname="CDDIS_IERSrspcEOP_product",
            version="1",
            description="EOP products from the IERS Rapid Service/Prediction Center at USNO (updated sub-daily) made available from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_General_Information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_General_Information_1",
            provider="CDDIS", 
            shortname="CDDIS_General_Information",
            version="1",
            description="General Archive Information from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACclockFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACclockFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACclockFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Final Clock Product (daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACERPFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACERPFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACERPFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Final Earth Rotation Parameters Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACorbitFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACorbitFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACorbitFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Final Orbit Product (daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACsummaryFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACsummaryFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACsummaryFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Final Orbit/Reference Frame Product Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACRFfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACRFfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACRFfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Final Station Positions/Velocities Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACTroposphereZPD_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACTroposphereZPD_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACTroposphereZPD_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Analysis Center Troposphere Zenith Path Delay (ZPD) product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSclockComparisonFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSclockComparisonFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSclockComparisonFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Combined Final Clock Solution Comparison Summary Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSclockComparisonRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSclockComparisonRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSclockComparisonRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Combined Rapid Clock Solution Comparison Summary Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRTStreamClock_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRTStreamClock_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRTStreamClock_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Decoded Real-Time Clock Solution from IGS Real-Time Product Streams from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRTStreamOrbit_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRTStreamOrbit_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRTStreamOrbit_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Decoded Real-Time Orbit Solution from IGS Real-Time Product Streams from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACRFSSCfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACRFSSCfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACRFSSCfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Analysis Center Station Positions/Velocities (no covariance matrix) Product from NASA CDDIS - Cloned version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSclock30Final_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSclock30Final_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSclock30Final_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Clock Product (30 second resolution, daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSclock5Final_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSclock5Final_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSclock5Final_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Clock Product (5 minute resolution, daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFSSCfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFSSCfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFSSCfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Combined Station Positions/Velocities (no covariance matrix) Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Combined Station Positions/Velocities Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFResidualsFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFResidualsFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFResidualsFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Combined Station Positions/Velocities Residual Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFITRResidualsFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFITRResidualsFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFITRResidualsFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Combined Station Positions/Velocities Residuals (between AC solutions and current RF) Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFSummaryFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFSummaryFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFSummaryFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Combined Station Positions/Velocities Summary Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFcumlativeFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFcumlativeFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFcumlativeFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Cumulative Combined Station Positions/Velocities Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSERPRFcumulativeFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSERPRFcumulativeFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSERPRFcumulativeFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Cumulative Earth Rotation Parameters Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFcumulativeSSCfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFcumulativeSSCfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFcumulativeSSCfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Cumulative Station Positions/Velocities (no covariance matrix) Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRFcumlativeResidualsFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRFcumlativeResidualsFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRFcumlativeResidualsFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Cumulative Station Positions/Velocities Residual Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSERPFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSERPFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSERPFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Earth Rotation Parameters Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSorbitFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSorbitFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSorbitFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Orbit Product (daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_products_orbit_final_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_products_orbit_final_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_products_orbit_final",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Orbit Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSsummaryFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSsummaryFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSsummaryFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Orbit/Reference Frame Product Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSERPRFcombinedFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSERPRFcombinedFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSERPRFcombinedFinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Final Weekly Combined Earth Rotation Parameters Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRTClock_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRTClock_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRTClock_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) IGS Clock Combination Product from Real-Time AC Submissions from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSMGEX_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSMGEX_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSMGEX_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) IGS Multi-GNSS Products from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRTSummary_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRTSummary_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRTSummary_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) IGS Real-Time Combination Solution Summary of Real-Time AC Submissions from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSHRIonosphereVTEC_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSHRIonosphereVTEC_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSHRIonosphereVTEC_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere High-Rate Vertical Total Electron Content (VTEC) Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACIonosphereVTEC_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACIonosphereVTEC_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACIonosphereVTEC_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Analysis Center Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSACIonosphereVTECRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSACIonosphereVTECRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSACIonosphereVTECRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Analysis Center Rapid Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSDailyIonosphereVTECcomparison_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSDailyIonosphereVTECcomparison_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSDailyIonosphereVTECcomparison_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Comparison Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSIonosphereVTECfinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSIonosphereVTECfinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSIonosphereVTECfinal_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Final Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSIonosphereVTECflux_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSIonosphereVTECflux_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSIonosphereVTECflux_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Fluctuation Measurement Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSIonosphereVTECPredicted_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSIonosphereVTECPredicted_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSIonosphereVTECPredicted_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Predicted Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSIonosphereVTECRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSIonosphereVTECRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSIonosphereVTECRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Rapid Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSIonosphereVTECvalidation_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSIonosphereVTECvalidation_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSIonosphereVTECvalidation_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Validation Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSclockRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSclockRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSclockRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Rapid Clock Product (30 second resolution, daily files, generated daily) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSERPRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSERPRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSERPRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Rapid Earth Rotation Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSorbitRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSorbitRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSorbitRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Rapid Orbit Product (daily files, generated daily) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSsummaryRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSsummaryRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSsummaryRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Rapid Orbit/Clock/ERP Product Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSRTRapidComparisonSummary_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSRTRapidComparisonSummary_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSRTRapidComparisonSummary_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Real-Time and Rapid Orbit and Clock Comparison Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSTroposphereZPDv1_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSTroposphereZPDv1_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSTroposphereZPDv1_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Troposphere Zenith Path Delay (ZPD) product (Version 1) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSTroposphereZPD_product_V2 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSTroposphereZPD_product_2",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSTroposphereZPD_product",
            version="2",
            description="Global Navigation Satellite System (GNSS) Troposphere Zenith Path Delay (ZPD) product from NASA CDDIS version: 2"
        )

    CDDIS_CDDIS_GNSS_IGSERPUltraRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSERPUltraRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSERPUltraRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ultra-Rapid Earth Rotation Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSorbitUltraRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSorbitUltraRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSorbitUltraRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ultra-Rapid Orbit Product (sub-daily files, generated 4 times/day) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSCMPsummaryUltraRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSCMPsummaryUltraRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSCMPsummaryUltraRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ultra-Rapid Orbit/Clock/ERP Product Comparison Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSsummaryUltraRapid_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSsummaryUltraRapid_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSsummaryUltraRapid_product",
            version="1",
            description="Global Navigation Satellite System (GNSS) Ultra-Rapid Orbit/Clock/ERP Product Summary from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDScumulativePositions_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDScumulativePositions_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDScumulativePositions_product",
            version="1",
            description="Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Cumulative Station Position Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSEOP_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSEOP_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSEOP_product",
            version="1",
            description="Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Earth Orientation Parameters Time Series Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSgeocenter_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSgeocenter_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSgeocenter_product",
            version="1",
            description="Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Geocenter Time Series Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSionosphere_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSionosphere_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSionosphere_product",
            version="1",
            description="Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Ionospheric Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSdpod_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSdpod_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSdpod_product",
            version="1",
            description="Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Station Position Product for Precise Orbit Determination from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_data_daily_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_data_daily_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_data_daily",
            version="1",
            description="Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_data_multiday_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_data_multiday_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_data_multiday",
            version="1",
            description="Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Data (multi-day files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSorbit_products_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSorbit_products_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSorbit_products",
            version="1",
            description="Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Satellite Orbit Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDStimeseriesPositions_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDStimeseriesPositions_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDStimeseriesPositions_product",
            version="1",
            description="Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Station Position Time Series Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_IDSweeklyPositions_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_IDSweeklyPositions_product_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_IDSweeklyPositions_product",
            version="1",
            description="Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Weekly Station Position Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_beidounav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_beidounav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_beidounav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_beidounav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_beidounav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_beidounav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_beidounav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_beidounav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_beidounav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_combinednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_combinednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_combinednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Combined Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_compactobs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_compactobs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_compactobs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Compact Observation Data (1-second sampling, sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_compactobs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_compactobs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_compactobs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Compact Observation Data (30-second sampling, daily, 24 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_compactobs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_compactobs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_compactobs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Compact Observation Data (30-second sampling, hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_glonassnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_glonassnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_glonassnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_glonassnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_glonassnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_glonassnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_glonassnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_glonassnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_glonassnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GLONASS_POD_30sec_Attitude_Quaternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GLONASS_POD_30sec_Attitude_Quaternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GLONASS_POD_30sec_Attitude_Quaternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GLONASS_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GLONASS_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GLONASS_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Clock Corrections (1-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GLONASS_POD_60sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GLONASS_POD_60sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GLONASS_POD_60sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Clock Corrections (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GLONASS_POD_60sec_orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GLONASS_POD_60sec_orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GLONASS_POD_60sec_orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Orbits (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_gpsnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_gpsnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_gpsnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_gpsnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_gpsnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_gpsnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_gpsnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_gpsnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_gpsnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GPS_POD_30sec_Attitude_Quaternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GPS_POD_30sec_Attitude_Quaternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GPS_POD_30sec_Attitude_Quaternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GPS_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GPS_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GPS_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS real-time POD Clock Corrections (1-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GPS_POD_60sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GPS_POD_60sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GPS_POD_60sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS real-time POD Clock Corrections (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GPS_POD_60sec_orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GPS_POD_60sec_orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GPS_POD_60sec_orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) GPS real-time POD Orbits (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_galileonav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_galileonav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_galileonav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_galileonav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_galileonav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_galileonav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_galileonav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_galileonav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_galileonav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_Galileo_POD_30sec_Attitude_Quaternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_Galileo_POD_30sec_Attitude_Quaternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_Galileo_POD_30sec_Attitude_Quaternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_Galileo_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_Galileo_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_Galileo_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Clock Corrections (1-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_Galileo_POD_60sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_Galileo_POD_60sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_Galileo_POD_60sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Clock Corrections (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_Galileo_POD_60sec_orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_Galileo_POD_60sec_orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_Galileo_POD_60sec_orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Orbits (60-second sampling, 60-second files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_EOP_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_EOP_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_EOP",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS Earth Orientation Parameters (1-day sampling, 7-day files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_30sec_Attitude_Quarternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_30sec_Attitude_Quarternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_POD_30sec_Attitude_Quarternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily accumulated real-time POD Attitude Quaternions (30-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily accumulated real-time POD Clock Corrections (1-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily accumulated real-time POD Clock Corrections (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_Orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_Orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_POD_60sec_Orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily accumulated real-time POD orbits (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Centers_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Centers_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Centers",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily antenna phase centers (24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Map_Meta_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Map_Meta_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GLONASS_Daily_Antenna_Phase_Map_Meta",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS daily antenna phase maps (meta data, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_EOP_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_EOP_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_EOP",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS Earth Orientation Parameters (1-day sampling, 7-day files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_30sec_Attitude_Quarternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_30sec_Attitude_Quarternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_POD_30sec_Attitude_Quarternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily accumulated real-time POD Attitude Quaternions (30-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily accumulated real-time POD Clock Corrections (1-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_60sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_60sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_POD_60sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily accumulated real-time POD Clock Corrections (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_60sec_Orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_POD_60sec_Orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_POD_60sec_Orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily accumulated real-time POD orbits (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Centers_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Centers_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Centers",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily antenna phase centers (24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Map_Meta_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Map_Meta_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_GPS_Daily_Antenna_Phase_Map_Meta",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian GPS daily antenna phase maps (meta data, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_EOP_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_EOP_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_EOP",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo Earth Orientation Parameters (1-day sampling, 7-day files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_30sec_Attitude_Quarternions_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_30sec_Attitude_Quarternions_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_POD_30sec_Attitude_Quarternions",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Attitude Quaternions (30-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_1sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_1sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_POD_1sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (1-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_60_sec_clk_corr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_60-sec_clk_corr_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_POD_60-sec_clk_corr",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_60sec_Orbits_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_POD_60sec_Orbits_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_POD_60sec_Orbits",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD orbits (60-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Centers_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Centers_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Centers",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily antenna phase centers (24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Map_Meta_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Map_Meta_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Galileo_Daily_Antenna_Phase_Map_Meta",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily antenna phase maps (meta data, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_GD_Daily_Ionosphere_TEC_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_GD_Daily_Ionosphere_TEC_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_GD_Daily_Ionosphere_TEC",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Guardian near-real-time Ionospheric Total Electron Count (5-second sampling, 24-hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_irnssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_irnssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_irnssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) IRNSS Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_irnssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_irnssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_irnssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) IRNSS Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_irnssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_irnssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_irnssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) IRNSS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_mixednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_mixednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_mixednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Mixed Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_obs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_obs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_obs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Observation Data (1-second sampling, sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_obs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_obs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_obs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Observation Data (30-second sampling, daily, 24 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_obs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_obs_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_obs",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) Observation Data (30-second sampling, hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_qzssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_qzssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_qzssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_qzssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_qzssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_qzssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_qzssnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_qzssnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_qzssnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_sbasnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_sbasnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_sbasnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) SBAS Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_sbasnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_sbasnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_sbasnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) SBAS Broadcast Ephemeris Data (hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_sbasnav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_sbasnav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_sbasnav",
            version="1",
            description="Ground-Based Global Navigation Satellite System (GNSS) SBAS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_combinednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_combinednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_combinednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System Combined Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_realtime_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_realtime_data_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_realtime_data",
            version="1",
            description="Ground-Based Global Navigation Satellite System Data (1-second sampling, real-time streams) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data",
            version="1",
            description="Ground-Based Global Navigation Satellite System Data (30-second sampling, 1 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data",
            version="1",
            description="Ground-Based Global Navigation Satellite System Data (30-second sampling, 24 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_IGSDCB_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_IGSDCB_product_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_IGSDCB_product",
            version="1",
            description="Ground-Based Global Navigation Satellite System Differential Code Bias Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GLONASS_daily_data_combinednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GLONASS_daily_data_combinednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GLONASS_daily_data_combinednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Combined Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GLONASS_daily_data_compactobs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GLONASS_daily_data_compactobs_1",
            provider="CDDIS", 
            shortname="CDDIS_GLONASS_daily_data_compactobs",
            version="1",
            description="Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Compact Observation Data (30-second sampling, daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GLONASS_daily_data_obs_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GLONASS_daily_data_obs_1",
            provider="CDDIS", 
            shortname="CDDIS_GLONASS_daily_data_obs",
            version="1",
            description="Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Observation Data (30-second sampling, daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GLONASS_daily_data_sum_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GLONASS_daily_data_sum_1",
            provider="CDDIS", 
            shortname="CDDIS_GLONASS_daily_data_sum",
            version="1",
            description="Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Summary Data (30-second sampling, daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_mixednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_mixednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_mixednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System Mixed Broadcast Ephemeris Data (daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_mixednav_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_mixednav_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_mixednav",
            version="1",
            description="Ground-Based Global Navigation Satellite System Mixed Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_sum_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_sum_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_sum",
            version="1",
            description="Ground-Based Global Navigation Satellite System Observation Summary Data (30-second sampling, daily files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_daily_data_met_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_daily_data_met_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_daily_data_met",
            version="1",
            description="Ground-Based Meteorological Data (daily, 24 hour files) from Co-Located Global Navigation Satellite System (GNSS) Receivers from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GLONASS_daily_data_met_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GLONASS_daily_data_met_1",
            provider="CDDIS", 
            shortname="CDDIS_GLONASS_daily_data_met",
            version="1",
            description="Ground-Based Meteorological Data (daily, 24 hour files) from Co-Located Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Receivers from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_hourly_data_met_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_hourly_data_met_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_hourly_data_met",
            version="1",
            description="Ground-Based Meteorological Data (hourly files) from Co-Located Global Navigation Satellite System (GNSS) Receivers from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_highrate_data_met_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_highrate_data_met_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_highrate_data_met",
            version="1",
            description="Ground-Based Meteorological Data (sub-hourly files) from Co-Located Global Navigation Satellite System (GNSS) Receivers from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_daily_fr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_daily_fr_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_daily_fr",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data (full-rate, daily, 24 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_monthly_fr_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_monthly_fr_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_monthly_fr",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data (full-rate, monthly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_daily_npt_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_daily_npt_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_daily_npt",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data (normal points, daily, 24 hour files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_hourly_npt_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_hourly_npt_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_hourly_npt",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data (normal points, hourly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_monthly_npt_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_monthly_npt_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_monthly_npt",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data (normal points, monthly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_data_monthlysum_npt_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_data_monthlysum_npt_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_data_monthlysum_npt",
            version="1",
            description="Ground-Based Satellite Laser Ranging (SLR) Observation Data Summary (normal points, monthly files) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_LROLR_LOLA_full_rate_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_LROLR_LOLA_full_rate_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_LROLR_LOLA_full_rate",
            version="1",
            description="Lunar Orbiter Laser Altimeter (LOLA) one-way Laser Ranging Full Rate Data (all ranges collected, ground stations, aggregate of normal points daily) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_ILRSorbitAC_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_ILRSorbitAC_product_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_ILRSorbitAC_product",
            version="1",
            description="Satellite Laser Ranging (SLR) AC Orbit Product (daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_ILRSpositionERPAC_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_ILRSpositionERPAC_product_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_ILRSpositionERPAC_product",
            version="1",
            description="Satellite Laser Ranging (SLR) AC Station Position and ERP Product (daily files, generated daily) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_ILRSorbitFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_ILRSorbitFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_ILRSorbitFinal_product",
            version="1",
            description="Satellite Laser Ranging (SLR) Final Orbit Product (daily files, generated weekly) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_ILRSpositionERPFinal_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_ILRSpositionERPFinal_product_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_ILRSpositionERPFinal_product",
            version="1",
            description="Satellite Laser Ranging (SLR) Final Station Position and ERP Product (daily files, generated daily) from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_ILRSpredictedOrbit_product_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_ILRSpredictedOrbit_product_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_ILRSpredictedOrbit_product",
            version="1",
            description="Satellite Laser Ranging (SLR) Predicted Orbit Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_Mail_ILRS_info_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_Mail_ILRS_info_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_Mail_ILRS_info",
            version="1",
            description="Satellite Laser Ranging Mail exploder distributing information about ILRS activities to the ILRS community, each message automatically numbered sequentially and archived for reference. version: 1"
        )

    CDDIS_CDDIS_SLR_Report_ILRS_reports_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_Report_ILRS_reports_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_Report_ILRS_reports",
            version="1",
            description="Satellite Laser Ranging Report exploder distributing mission related reports, each message automatically numbered sequentially and archived for reference. version: 1"
        )

    CDDIS_CDDIS_SLR_products_orbit_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_products_orbit_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_products_orbit",
            version="1",
            description="Satellite Laser Ranging Satellite Orbit Product from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_DORIS_information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_DORIS_information_1",
            provider="CDDIS", 
            shortname="CDDIS_DORIS_information",
            version="1",
            description="Supporting Information for Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Data and Products from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_GNSS_information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_GNSS_information_1",
            provider="CDDIS", 
            shortname="CDDIS_GNSS_information",
            version="1",
            description="Supporting Information for Global Navigation Satellite System (GNSS) Data and Products from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_information_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_information",
            version="1",
            description="Supporting Information for Satellite Laser Ranging (SLR) Data and Products from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_VLBI_information_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_VLBI_information_1",
            provider="CDDIS", 
            shortname="CDDIS_VLBI_information",
            version="1",
            description="Supporting Information for Very Long Baseline Interferometry (VLBI) Data and Products from NASA CDDIS version: 1"
        )

    CDDIS_CDDIS_SLR_SLRF2020_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="CDDIS_CDDIS_SLR_SLRF2020_1",
            provider="CDDIS", 
            shortname="CDDIS_SLR_SLRF2020",
            version="1",
            description="The International Laser Ranging Service (ILRS) extension of the International Terrestrial Reference Frame 2020 (ITRF2020) TRF Model with additional SLR sites at NASA CDDIS version: 1"
        )

