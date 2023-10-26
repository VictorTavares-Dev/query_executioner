ALTER TABLE test_database.tb_sync_scenario_simple_partitions ADD PARTITION (anomesdia='0');


--------------------------
DECLARE @i INT = 1;
DECLARE @max INT = 10000;

WHILE (@i <= @max)
BEGIN
    ALTER TABLE tb_sync_scenario_simple_partitions ADD PARTITION (PARTITION p_{{i}} VALUES LESS THAN ({{i}}));
    SET @i = @i + 1;
END;

-- Check https://stackoverflow.com/questions/37320137/declare-variable-in-sql-hive