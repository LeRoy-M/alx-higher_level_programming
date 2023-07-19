## 0x0E. SQL - More queries

**0. My privileges!** `[0-privileges.sql]` >> Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on ones server (in `localhost`).

**1. Root user** `[1-create_user.sql]` >> Script that creates the MySQL server user `user_0d_1` with all MySQL server privileges and `user_0d_1` password should be set to `user_0d_1_pwd`.

**2. Read user** `[2-create_read_user.sql]` >> Script that creates the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privilege in the database, and password set to `user_0d_2_pwd`.

**3. Always a name** `[3-force_name.sql]` >> Script that creates the table `force_name` with description `id` INT and `name` VARCHAR(256) (which cannot be null) on ones MySQL server.

**4. ID can't be null** `[4-never_empty.sql]` >> Script that creates the table called `id_not_null` with description `id` INT (default value set to `1`) and `name` VARCHAR(256) on ones MySQL server.

**5. Unique ID** `[5-unique_id.sql]` >> Script that creates the table `unique_id` with description `id` INT (default value set to `1` and each is unique) and `name` VARCHAR(256) on ones MySQL server.

**6. States table** `[6-states.sql]` >> Script that creates the database `hbtn_0d_usa` and the table `states` with description `id` INT (which is unique, auto-generated, cannot be null and is a primary key) and `name` VARCHAR(256) (which cannot be null) in the created database on ones MySQL server.

**7. Cities table** `[7-cities.sql]` >> Script that creates the database `hbtn_0d_usa` and the table `cities` with description `id` INT (which is unique, auto-generated, cannot be null and is a primary key), `state_id` INT (which also cannot be null and must be a `FOREIGN KEY` that references to `id` of the `states` table) and `name` VARCHAR(256) (which as well cannot be null) in the created database on ones MySQL server.

**8. Cities of California** `[8-cities_of_california_subquery.sql]` >> Script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

**9. Cities by States** `[9-cities_by_state_join.sql]` >> Script that lists all cities contained in the database `hbtn_0d_usa`.

**10. Genre ID by show** `[10-genre_id_by_show.sql]` >> Script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Data imported in `hbtn_0d_tvshows` database from [hbtn_0d_tvshows.sql](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

**11. Genre ID for all shows** `[11-genre_id_all_shows.sql]` >> Script that lists all shows contained in the database `hbtn_0d_tvshows`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**12. No genre** `[12-no_cheating.sql]` >> Script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**13. Number of shows by genre** `[13-count_shows_by_genre.sql]` >> Script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**14. My genres** `[14-my_genres.sql]` >> Script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**15. Only Comedy** `[15-comedy_only.sql]` >> Script that lists all Comedy shows in the database `hbtn_0d_tvshows`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**16. List shows and genres** `[16-shows_by_genre.sql]` >> Script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**17. Not my genre** `[100-not_my_genres.sql]` >> Script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**18. No Comedy tonight!** `[101-not_a_comedy.sql]` >> Script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**19. Rotten tomatoes** `[102-rating_shows.sql]` >> Script that lists all shows from `hbtn_0d_tvshows_rate` by their rating. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.

**20. Best genre** `[103-rating_genres.sql]` >> Script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating. Data imported in `hbtn_0d_tvshows` database is same as that from **task 10**.
