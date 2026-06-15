CREATE DATABASE IF NOT EXISTS telecom_db;

USE telecom_db;

CREATE TABLE IF NOT EXISTS telecom_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT,
    fixed_tel_subs BIGINT,
    fixed_tel_penetration DECIMAL(10,2),
    fixed_bb_subs BIGINT,
    fixed_bb_penetration DECIMAL(10,2),
    mobile_tel_subs BIGINT,
    mobile_tel_penetration DECIMAL(10,2),
    mobile_bb_subs BIGINT,
    mobile_bb_penetration DECIMAL(10,2)
);