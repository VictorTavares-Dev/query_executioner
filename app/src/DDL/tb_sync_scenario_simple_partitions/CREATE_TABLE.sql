CREATE EXTERNAL TABLE IF NOT EXISTS `tb_sync_scenario_simple_partitions`(
  `col_1` string,
  `col_2` string
)
PARTITIONED BY (`anomesdia` string)
STORED AS PARQUET
LOCATION 's3://test-spark-470085096987/tb_sync_scenario_simple_partitions/'
TBLPROPERTIES ("parquet.compression"="SNAPPY")