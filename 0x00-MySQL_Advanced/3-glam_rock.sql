-- a SQL script that lists all bands with Glam rock 
-- as their main style, ranked by their longevity

SELECT band_name,
       IF(splitted.lifespan_end = 0,
	0,
	splitted.lifespan_end - formed.year) AS lifespan
FROM bands
JOIN styles ON bands.id = styles.band_id
JOIN (
    SELECT band_id,
           MAX(CASE WHEN attribute = 'formed' THEN CAST(value AS UNSIGNED) END) AS year,
           MAX(CASE WHEN attribute = 'split' THEN CAST(value AS UNSIGNED) END) AS lifespan_end
    FROM attributes
    WHERE attribute IN ('formed', 'split')
    GROUP BY band_id
) AS splitted ON bands.id = splitted.band_id
WHERE styles.style = 'Glam rock'
ORDER BY lifespan DESC, band_name;
