-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
    FROM metal_bands
    GROUP BY band_name
    WHERE style LIKE 'Glam rock%'
    ORDER BY lifespan DESC;
