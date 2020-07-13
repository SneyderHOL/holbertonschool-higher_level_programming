-- list the number of records with the same score in the table named 'second_table' from database hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
