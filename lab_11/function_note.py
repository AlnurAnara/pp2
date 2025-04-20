
#####1.FUNCTION#####
#\df list all funcs

'''
✅1).CREATE OR REPLACE FUNCTION get_discount(price NUMERIC, discount NU
MERIC)
RETURNS NUMERIC AS $$
Lecture 14: Advanced SQL 1
BEGIN
 RETURN price - (price * discount / 100);
END;
$$ LANGUAGE plpgsql;

#this code is used in postgres not database

✅2).SELECT get_discount(100, 10);   this step is to run and return 
'''

'''
✅3).CASE WHEN as SQL's version of if...else . 

CASE WHEN condition1 THEN result1
WHEN condition2 THEN result2
ELSE result3
END;

|
|
|

e.g.
CREATE TABLE students (
 name TEXT,
 score INT
);
INSERT INTO students VALUES
('Alice', 85),
('Bob', 67),
('Charlie', 92),
('Diana', 45);

|
|
11111. for select 
SELECT
 name,
 score,
 CASE
 WHEN score >= 90 THEN 'A'
 WHEN score >= 80 THEN 'B'
 WHEN score >= 70 THEN 'C'
 WHEN score >= 60 THEN 'D'
 ELSE 'F'
 END AS grade
FROM students;

|
|
|

Expected Output:
name score grade
Alice 85 B
Bob 67 D
Charlie 92 A
Diana 45 F


one more example:
CREATE OR REPLACE FUNCTION grade_comment(score INT)
RETURNS TEXT AS $$
BEGIN
 RETURN
 CASE
 WHEN score >= 90 THEN 'Excellent'
 WHEN score >= 70 THEN 'Good'
 WHEN score >= 50 THEN 'Average'
 ELSE 'Needs Improvement'
 END;
END;
$$ LANGUAGE plpgsql;

SELECT grade_comment(85);



22222. for update
UPDATE students
SET score =
 CASE
 WHEN score < 70 THEN score + 5
 ELSE score
 END;



'''


'''
✅4). use conditions and loops inside your functions/procedures.
CREATE OR REPLACE FUNCTION check_age(age INT)
RETURNS TEXT AS $$
BEGIN
 IF age < 18 THEN
 RETURN 'Minor';
 ELSE
 RETURN 'Adult';
 END IF;
END;
$$ LANGUAGE plpgsql;

SELECT check_age(25);

'''


### the differences between function and procedure
### function has return value,procedure do not need to return value

'''
Feature Function Procedure
Returns Value Yes (mandatory) Optional
Can be used in SELECT Yes No
Modifies Data Usually No Yes
Error Handling Limited Flexible

'''
