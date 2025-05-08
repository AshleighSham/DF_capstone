

def genres_by_year_query(schema):
    query = f"""SELECT
    album_year,
    pop_count as "Pop",
    rock_count as "Rock",
    hip_hop_count as "Hip-Hop",
    electronic_count as "Electronic",
    rnb_soul_count as "R&B/soul",
    folk_count as "Folk",
    country_count as "Country",
    ska_count as "Ska",
    dance_disco_count as "Disco/Dance",
    indie_alt_count as "Indie/Alternative",
    retro_vintage_count as "Retro/Vintage",
    novelty_count as "Novelty",
    easy_listening_count as "Easy Listening",
    cultural_count as "Cultural"
    FROM {schema}.as_genres_by_year"""
    return query
