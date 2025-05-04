CREATE OR REPLACE VIEW high_value_customers AS
SELECT
    sub.customer_id,
    sub.name,
    sub.age,
    sub.country,
    sub.is_active,
    sub.total_amount,
    sub.average_transaction_amount
FROM (
    SELECT
        tbc.customer_id,
        tbc.name,
        tbc.age,
        tbc.country,
        tbc.is_active,
        SUM(tbc.amount) OVER (
            PARTITION BY tbc.customer_id
        ) AS total_amount,
        AVG(tbc.amount) OVER (
            PARTITION BY tbc.customer_id
        ) AS average_transaction_amount
    FROM
        transactions_by_customers AS tbc
) AS sub
WHERE
    sub.total_amount >:total_spend_threshold;
