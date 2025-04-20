'''
1). Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

CREATE OR REPLACE FUNCTION find_records_by_pattern(pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(20)
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.last_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern || '%'
       OR p.last_name ILIKE '%' || pattern || '%'
       OR p.phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
'''



'''
2).Create procedure to insert new user by name and phone, update phone if user already exists

CREATE OR REPLACE PROCEDURE insert_or_update_user(
    in_first_name VARCHAR(255),
    in_last_name VARCHAR(255),
    in_phone VARCHAR(20)
)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = in_first_name AND last_name = in_last_name) THEN
        UPDATE phonebook
        SET phone = in_phone
        WHERE first_name = in_first_name AND last_name = in_last_name;
    ELSE
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (in_first_name, in_last_name, in_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
'''

'''
3).Create function to querying data from the tables with pagination (by limit and offset)

CREATE OR REPLACE FUNCTION get_paginated_data(
    p_limit INTEGER,
    p_offset INTEGER
)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(20)
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id,
        p.first_name,
        p.last_name,
        p.phone
    FROM
        phonebook AS p  
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


'''

'''
4).Implement procedure to deleting data from tables by username or phone

CREATE OR REPLACE PROCEDURE delete_data(
    p_username TEXT,
    p_phone INTEGER
)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_username OR last_name = p_username OR phone = p_phone;
END;
$$ LANGUAGE plpgsql;

'''