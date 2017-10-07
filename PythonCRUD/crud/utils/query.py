INSERT_QUERY = "INSERT INTO employees(emp_id, first_name, last_name, salary, address) VALUES(%s,%s,%s,%s,%s)"
SELECT_QUERY = "SELECT * FROM employees"
UPDATE_QUERY = "UPDATE employees SET address=%s WHERE emp_id=%s"
DELETE_QUERY = "DELETE FROM employees WHERE id=%s"
