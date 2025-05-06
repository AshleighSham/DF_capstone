SELECT
    album_year,
    avg_danceability as "Danceability",
    avg_energy as "Energy",
    avg_loudness as "Loundness",
    avg_speechiness as "Speechiness",
    avg_instrumentalness as "Instrumentalness",
    avg_liveness as "liveness",
    avg_valence as "Valence",
    avg_tempo as "Tempo"
FROM c12de.as_properties_by_year