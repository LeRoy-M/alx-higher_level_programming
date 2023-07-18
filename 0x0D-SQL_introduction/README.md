## 0x0D. SQL - Introduction

**0. List databases** `[0-list_databases.sql]` >> Script that all databases of ones MySQL server.

**1. Create a database** `[1-create_database_if_missing.sql]` >> Script that creates the database `hbtn_0c_0` in ones MySQL server, without making use of `SELECT` or `SHOW` statements to check if it already exists.

**2. Delete a database** `[2-remove_database.sql]` >> Script that deletes the database `hbtn_0c_0` in ones MySQL server, without making use of `SELECT` or `SHOW` statements to check if it already exists.

**3. List tables** `[3-list_tables.sql]` >> Script that lists all the tables of a database in ones MySQL server.

**4. First table** `[4-first_table.sql]` >> Script that creates a table called `first_table` in the current database in ones MySQL server, that has columns `id` INT and `name` VARCHAR(256), without making use of `SELECT` or `SHOW` statements to check if it already exists.

**5. Full description** `[5-full_table.sql]` >> Script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in ones MySQL server, without making use of `DESCRIBE` or `EXPLAIN` statements.

**6. List all in table** `[6-list_values.sql]` >> Script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in ones MySQL server, including all fields.

**7. First add** `[7-insert_value.sql]` >> Script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in ones MySQL server. The record is `id` = `89` and `name` = `Best School`.

**8. Count 89** `[8-count_89.sql]` >> Script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in ones MySQL server.

**9. Full creation** `[9-full_creation.sql]` >> Script that creates a table `second_table` in the database `hbtn_0c_0` in ones MySQL server and add multiples rows, without making use of `SELECT` or `SHOW` statements to check if it already exists. `second_table` description is `id` INT, `name` VARCHAR(256) and `score` INT. The records added are as follows:
- `id` = 1, `name` = “John”, `score` = 10
- `id` = 2, `name` = “Alex”, `score` = 3
- `id` = 3, `name` = “Bob”, `score` = 14
- `id` = 4, `name` = “George”, `score` = 8

**10. List by best** `[10-top_score.sql]` >> Script that lists all records of the table `second_table` of the database `hbtn_0c_0` in ones MySQL server, displaying both the score and the name in descending order of the score.

**11. Select the best** `[11-best_score.sql]` >> Script that lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0` in ones MySQL server, displaying both the score and the name in descending order of the score.

**12. Cheating is bad** `[12-no_cheating.sql]` >> Script that updates the score of Bob to `10` in the table `second_table` using the `name` field.

**13. Score too low** `[13-change_class.sql]` >> Script that removes all records with a score <= 5 in the table `second_table` of the database `hbtn_0c_0` in ones MySQL server.

**14. Average** `[14-average.sql]` >> Script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in ones MySQL server, with the result column name been `average`.

**15. Number by score** `[15-groups.sql]` >> Script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in ones MySQL server, by displaying the `score` and the number of records for this `score` with the label `number` next to it; this in descending order of the `number` field.

**16. Say my name** `[16-no_link.sql]` >> Script that lists all records with a `name` value of the table `second_table` of the database `hbtn_0c_0` in ones MySQL server in descending score.

**17. Go to UTF8** `[100-move_to_utf8.sql]` >> Script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in ones MySQL server. The database `hbtn_0c_0`, table `first_table`, and field `name` in `first_table` are all converted to `UTF8`.

**18. Temperatures #0** `[101-avg_temperatures.sql]` >> Script that displays the average temperature (Fahrenheit) by city ordered by temperature in descending order. Data imported in `hbtn_0c_0` database from [temperatures.sql](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql).

**19. Temperatures #1** `[102-top_city.sql]` >> Script that displays the top 3 of cities temperature during July and August ordered by temperature in descending order. Data imported in `hbtn_0c_0` database is same as that from **task 18**.

**20. Temperatures #2** `[103-max_state.sql]` >> Script that displays the max temperature of each state ordered alphabetically by state name. Data imported in `hbtn_0c_0` database is same as that from **task 18**.
