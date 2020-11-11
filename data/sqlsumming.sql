SELECT county.county_nam, sum(ST_LENGTH(ST_Intersection(county.geom,class1_trout.geom))*10)
FROM county, class1_trout
WHERE ST_Intersects(county.geom, class1_trout.geom)
GROUP BY county.county_nam
ORDER BY sum DESC;
