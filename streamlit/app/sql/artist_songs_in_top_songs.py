
def find_artist_songs(artist_id):
    query = f"""WITH
        artist_songs
        as
        (
            SELECT
                UNNEST(string_to_array(artist_id, ',')) AS artist_id,
                as_capstone.track_id
            FROM
                as_capstone
            WHERE artist_id = '{artist_id}'
        )
    SELECT
        album_name,
        disc_number,
        track_number,
        album_release_date,
        track_name,
        artist_names,
        track_duration_ms,
        explicit,
        popularity,
        album_image_url
    FROM as_capstone
        inner JOIN artist_songs ON as_capstone.track_id = artist_songs.track_id;"""
    return query
