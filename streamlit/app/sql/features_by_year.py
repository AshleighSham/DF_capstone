

def features_by_year_query(schema):
    query = f"""SELECT
    album_year,
    avg_danceability as "Danceability",
    avg_energy as "Energy",
    avg_loudness as "Loundness",
    avg_speechiness as "Speechiness",
    avg_instrumentalness as "Instrumentalness",
    avg_liveness as "Liveness",
    avg_valence as "Valence",
    avg_tempo as "Tempo"
    FROM {schema}.as_properties_by_year"""
    return query
