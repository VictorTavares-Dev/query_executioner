import boto3
import os
import config as cfg
import time
from src.Logger import Logger
from src.query_execution import AthenaQueryExecutor

log = Logger()

# Create connection

# Execute queries
log.info("Creating connection to Athena")
query_executor = AthenaQueryExecutor("test_database", "s3://test-spark-470085096987/query_results/")

# Query 1
def execute_query(query_executor, root_folder, query_file):
    with open(os.path.join(root_folder, query_file), "r") as file:
        query = file.read()
    log.info(f"Executing {os.path.join(root_folder, query_file)}")
    query_id = query_executor.execute_query(query)
    log.info(f"Query ID: {query_id}")


# execute_query(query_executor, cfg.ddl_folder, "tb_sync_scenario_simple_partitions/CREATE_TABLE.sql")
# execute_query(query_executor, cfg.ddl_folder, "tb_sync_scenario_simple_partitions/ADD_PARTITION.sql")
# execute_query(query_executor, cfg.dml_folder, "tb_sync_scenario_simple_partitions/INSERT.sql")
# execute_query(query_executor, cfg.ddl_folder, "tb_sync_scenario_simple_partitions/DROP_TABLE.sql")

# Close connection
