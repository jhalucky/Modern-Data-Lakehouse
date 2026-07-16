USE ROLE ACCOUNTADMIN;

USE DATABASE RETAIL_ANALYTICS;
USE SCHEMA PUBLIC;

CREATE OR REPLACE STAGE published_stage
    URL = 's3://modern-retail-lakehouse-lucky/published/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = (
        TYPE = PARQUET
    );

LIST @published_stage;