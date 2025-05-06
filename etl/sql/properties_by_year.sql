CREATE OR REPLACE VIEW as_properties_by_year AS
SELECT
    DATE_PART('YEAR', album_release_date) AS album_year,
    AVG(danceability) AS avg_danceability,
    AVG(energy) AS avg_energy,
    AVG(key) AS avg_key,
    AVG(loudness) AS avg_loudness,
    AVG(speechiness) AS avg_speechiness,
    AVG(acousticness) AS avg_acousticness,
    AVG(instrumentalness) AS avg_instrumentalness,
    AVG(liveness) AS avg_liveness,
    AVG(valence) AS avg_valence,
    AVG(tempo) AS avg_tempo
FROM
    as_capstone
GROUP BY
    album_year
ORDER BY
    album_year;
