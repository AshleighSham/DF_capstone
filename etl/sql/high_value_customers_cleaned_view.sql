CREATE OR REPLACE VIEW high_value_customers_filtered AS
SELECT
    customer_id,
    name,
    age,
    country,
    is_active,
    total_amount,
    average_transaction_amount
FROM
    high_value_customers
WHERE
    age IS NOT NULL
    AND
    country IS NOT NULL;
