CREATE OR REPLACE VIEW genres_by_year AS
SELECT
    DATE_PART('year', album_release_date) AS album_year,
    COUNT(pop) FILTER(WHERE pop) AS pop_count,
    COUNT(rock) FILTER(WHERE rock) AS rock_count,
    COUNT(hip_hop) FILTER(WHERE hip_hop) AS hip_hop_count,
    COUNT(electronic) FILTER(WHERE electronic) AS electronic_count,
    COUNT(rnb_soul) FILTER(WHERE rnb_soul) AS rnb_soul_count,
    COUNT(folk) FILTER (WHERE folk) AS folk_count,
    COUNT(country) FILTER (WHERE country) AS country_count,
    COUNT(ska) FILTER (WHERE ska) AS ska_count,
    COUNT(dance_disco) FILTER (WHERE dance_disco) AS dance_disco_count,
    COUNT(indie_alt) FILTER(WHERE indie_alt) AS indie_alt_count,
    COUNT(retro_vintage) FILTER(WHERE retro_vintage) AS retro_vintage_count,
    COUNT(novelty) FILTER(WHERE novelty) AS novelty_count,
    COUNT(easy_listening) FILTER(WHERE easy_listening) AS easy_listening_count,
    COUNT(cultural) FILTER(WHERE cultural) AS cultural_count,
    COUNT(jazz) FILTER(WHERE jazz) AS jazz_count
FROM
    as_capstone
GROUP BY
    album_year
ORDER BY
    album_year;
