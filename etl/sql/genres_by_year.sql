CREATE OR REPLACE VIEW genres_by_year AS
SELECT
	date_part('year', to_date(album_release_date, 'DD/MM/YYY')) AS album_year,
	count(pop) FILTER
(
	WHERE "pop") AS pop_count,
	count
(rock) FILTER
(
	WHERE "rock") AS rock_count,
	count
(hip_hop) FILTER
(
	WHERE "hip_hop") AS hip_hop_count,
	count
(electronic) FILTER
(
	WHERE "electronic") AS electronic_count,
	count
(rnb_soul) FILTER
(
	WHERE "rnb_soul") AS rnb_soul_count,
	count
(folk) FILTER
(
	WHERE "folk") AS folk_count,
	count
(country) FILTER
(
	WHERE "country") AS country_count,
	count
(ska) FILTER
(
	WHERE "ska") AS ska_count,
	count
(dance_disco) FILTER
(
	WHERE "dance_disco") AS dance_disco_count,
	count
(indie_alt) FILTER
(
	WHERE "indie_alt") AS indie_alt_count,
	count
(retro_vintage) FILTER
(
	WHERE "retro_vintage") AS retro_vintage_count,
	count
(novelty) FILTER
(
	WHERE "novelty") AS novelty_count,
	count
(easy_listening) FILTER
(
	WHERE "easy_listening") AS easy_listening_count,
	count
(cultural) FILTER
(
	WHERE "cultural") AS cultural_count,
	count
(jazz) FILTER
(
	WHERE "jazz") AS jazz_count
FROM
	as_capstone
GROUP BY
	album_year
ORDER BY
	album_year;
