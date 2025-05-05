CREATE OR REPLACE VIEW artists_track AS
SELECT
    UNNEST(string_to_array(artist_id, ',')) AS artist_id,
    track_id
FROM
    as_capstone;