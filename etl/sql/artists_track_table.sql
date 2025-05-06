CREATE OR REPLACE VIEW artists_track AS
SELECT
    track_id,
    UNNEST(STRING_TO_ARRAY(artist_id, ',')) AS artist_id
FROM
    as_capstone;
