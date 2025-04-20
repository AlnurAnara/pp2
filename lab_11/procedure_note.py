'''
result : = ....

2).procedure 
use "call" instead of select
'''
'''
CREATE OR REPLACE PROCEDURE print_numbers()
LANGUAGE plpgsql
AS $$
DECLARE
 i INT := 1;
BEGIN
 WHILE i <= 5 LOOP
 RAISE NOTICE 'Number: %', i;
 i := i + 1;
 END LOOP;
END;
$$;

CALL print_numbers();

--- or

CREATE OR REPLACE PROCEDURE print_numbers(i INT)
LANGUAGE plpgsql
AS $$
DECLARE
j INT :=1;
BEGIN
 WHILE j <= i LOOP
 RAISE NOTICE 'Number: %', j;
 j := j + 1;
 END LOOP;
END;
$$;
Call the procedure with:
Lecture 14: Advanced SQL 6

CALL print_numbers(20);

'''