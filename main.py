import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# customers = pd.read_sql("""
#                         SELECT *
#                         FROM customers;
#                         """, conn)

# print(customers)


# Group by Country
# q = """
# SELECT country, COUNT(*) AS customer_count
# FROM customers
# GROUP BY country;
# """
# GROUP BY allows us to specify the column that we are grouping by numerically, in this case column 1 (index starts at 1)

# AGGREGATES
q = """
SELECT customerNumber,
COUNT(*) AS number_of_payments,
MIN(CAST(amount AS FLOAT)) AS min_purchase,
MAX(CAST(amount AS FLOAT)) AS max_purchase,
AVG(CAST(amount AS FLOAT)) AS avg_purchase,
SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
WHERE CAST(amount AS FLOAT) > 50000
GROUP BY customerNumber
HAVING number_of_payments >= 2
ORDER BY total_spent
LIMIT 1;
"""

results = pd.read_sql(q, conn).head(10)
print(results)

conn.close()