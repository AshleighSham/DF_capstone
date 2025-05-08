

def popularity_by_year_query(schema):
    query = f"""SELECT
    year_group,
    bin_0 as "0",
    bin_1_10 as "1-10",
    bin_11_20 as "11-20",
    bin_21_30 as "21-30",
    bin_31_40 as "31-40",
    bin_41_50 as "41_50",
    bin_51_60 as "51_60",
    bin_61_70 as "61-70",
    bin_71_80 as "71-80",
    bin_81_90 as "81-90",
    bin_91_100 as "91-100"
    FROM {schema}.as_popularity_by_year
    ORDER BY year_group"""
    return query
