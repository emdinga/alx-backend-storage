-- a SQL script that ranks country origins of bands, 
--ordered by the number of (non-unique) fans

SELECT origin, COUNT(DISTINCT band_id) AS nb_fans
FROM fans
JOIN bands ON fans.band_id = bands.id
GROUP BY origin
ORDER BY nb_fans DESC;

