CREATE OR REPLACE VIEW properties_by_year AS
SELECT
    DATE_PART('YEAR', TO_DATE(album_release_date, 'DD/MM/YYY')) AS album_year,
    AVG(danceability) AS avg_danceability,
    AVG(energy) AS avg_energy,
    AVG(key) AS avg_key,
    AVG(loudness) AS avg_loudness,
    AVG(speechiness) AS avg_speechiness,
    AVG(acouticness) AS avg_acouticness,
    AVG(instrumentalness) AS vg_instumentalness,
    AVG(liveness) AS avg_liveness,
    AVG(valence) AS avg_valence,
    AVG(tempo) AS avg_tempo
FROM
    as_capstone
GROUP BY
    album_year
ORDER BY
    album_year;
