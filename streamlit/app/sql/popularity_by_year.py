

def popularity_by_year_query(schema, group_size):
    query = f"""SELECT
    FLOOR(album_year / {group_size}) * {group_size} AS year_group,
    SUM(bin_0) as "0-0",
    SUM(bin_1_10) as "1-10",
    SUM(bin_11_20) as "11-20",
    SUM(bin_21_30) as "21-30",
    SUM(bin_31_40) as "31-40",
    SUM(bin_41_50) as "41-50",
    SUM(bin_51_60) as "51-60",
    SUM(bin_61_70) as "61-70",
    SUM(bin_71_80) as "71-80",
    SUM(bin_81_90) as "81-90",
    SUM(bin_91_100) as "91-100"
    FROM {schema}.as_popularity_by_year
    GROUP BY year_group
    ORDER BY year_group"""
    return query
