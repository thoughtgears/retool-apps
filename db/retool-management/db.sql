-- retool-management.sql

CREATE TABLE retool_configuration (
    id SERIAL PRIMARY KEY,
    space_id TEXT NOT NULL,
    space_name TEXT NOT NULL,
    space_domain TEXT NOT NULL,
    retool_api_resource_id TEXT
);