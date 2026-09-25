# TensorTonic Solutions

Welcome to my TensorTonic solutions repository!

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, automatically synchronized from the platform.

<!-- tensortonic:start -->
# Madan Raj's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/maximus.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| Create Arrays from Lists | Convert a rectangular Python list of lists into a two-dimensional NumPy float64 array. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-create-array |
| Zeros and Ones | Create a two-dimensional float64 NumPy array of a requested shape filled entirely with zeros or ones. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-zeros-ones |
| Create DataFrame from Dict | Create a pandas DataFrame from dictionary data and report its records, shape, and ordered column names. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-read-csv |
| Activation Functions | Implement four common activation functions from scratch using basic PyTorch tensor operations (no torch.nn module). | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-activation-function-from-scratch |
| Basic Autograd | Use PyTorch autograd to evaluate a scalar function and return its derivative at every supplied input value. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-basic-autograd |
| Batch Normalization | Normalize each feature across the batch, then scale and shift using learnable parameters. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-batch-normalization |
| Simple Neural Network | Implement a class SimpleNet subclassing nn.Module with two linear layers and ReLU between them. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-build-simple-nn-from-scratch |
| Custom Linear Layer | Implement a custom linear layer that computes the affine transformation without using any built-in linear layer. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-custom-linear-layer |
| Loss Functions | Implement three common loss functions from scratch using PyTorch tensor operations: mean squared error, cross-entropy, and Huber loss. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-loss-functions |
| Tensor Operations | Perform common element-wise and matrix tensor operations: add, multiply, matmul, power, and max. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-tensor-arithmetic |
| Tensor Factory | Create PyTorch tensors with zeros, ones, or a constant fill value using the requested shape and dtype. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-tensor-creation |
| Tensor Shape Manipulation | Reshape tensors using three common PyTorch operations: flatten to collapse into 1D, squeeze to remove size-1 dimensions. | https://www.tensortonic.com/study-plans/pytorch-basics/pytorch-tensor-reshape |
| Basic SELECT | Write a SQL SELECT query that aliases product names and calculates inventory value from unit price and stock quantity. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-basic-select |
| CASE Statements | Classify user activity and platform type with SQL CASE expressions using session counts and mobile platform values. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-case-statements |
| Conditional Aggregation | Summarize support tickets by department with conditional SQL counts for open, in-progress, and closed statuses. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-conditional-aggregation |
| COUNT, SUM, AVG | Aggregate sales by category with SQL COUNT, SUM, and AVG while handling NULL discounts and deterministic ordering. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-count-sum-avg |
| Cross Join | Generate every segment and metric combination with a SQL CROSS JOIN for a complete reporting grid. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-cross-join |
| Common Table Expressions | Use a SQL CTE to calculate customer order counts and spending, then filter repeat customers by total spend. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-cte |
| Date Functions | Extract signup year, month, quarter, and cohort month with SQL date functions for cohort analysis. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-date-functions |
| DISTINCT Values | Return each customer and their distinct product count with SQL aggregation and deterministic sorting. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-distinct-values |
| GROUP BY | Group orders by customer in SQL to calculate total order count and spending, ordered by highest spend. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-group-by |
| HAVING Clause | Use SQL GROUP BY and HAVING to find customers with at least two orders and summarize their total spending. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-having-clause |
| INNER JOIN | Join employees to matching departments with SQL INNER JOIN and return employee name, salary, and department. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-inner-join |
| LAG and LEAD | Use SQL LAG to compare monthly revenue with the previous month and calculate month-over-month change. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-lag-lead |
| LEFT JOIN | Use SQL LEFT JOIN to include every customer and calculate total spending, returning zero for customers without orders. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-left-join |
| LIMIT and OFFSET | Use SQL ORDER BY, LIMIT, and OFFSET to return the second through fourth highest-revenue sales with tie-breaking. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-limit-offset |
| Multiple Joins | Join users, experiment assignments, and conversion events in SQL to report converted users, variants, and revenue. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-multiple-joins |
| Nested Aggregations | Use a SQL subquery or CTE to compute daily order totals, average daily revenue, and the busiest day. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-nested-aggregations |
| NULL Handling | Handle SQL NULL values with COALESCE and conditional status logic while filtering customers without phone numbers. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-null-handling |
| ORDER BY | Sort student exam results in SQL by descending score and ascending name for deterministic ties. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-order-by |
| RANK and DENSE_RANK | Rank ML models within each dataset using SQL RANK and DENSE_RANK over descending accuracy. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-rank-dense-rank |
| ROW_NUMBER | Assign deterministic per-segment activity ranks with SQL ROW_NUMBER ordered by engagement score and username. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-row-number |
| Running Totals | Compute per-account running transaction totals with a partitioned SQL window ordered by date and transaction ID. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-running-totals |
| Self Join | Use a SQL self join to pair users with their referrers while labeling organic signups without a referral. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-self-join |
| String Functions | Clean survey data with SQL string functions for trimmed lowercase names, answer lengths, and parsed source URLs. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-string-functions |
| Subqueries | Use SQL subqueries to compare product prices with the overall average and include only products with recorded sales. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-subqueries |
| WHERE Clauses | Filter employees by department and salary with SQL WHERE conditions, returning only qualifying names and salaries. | https://www.tensortonic.com/study-plans/sql-basics/sql/sql-where-clauses |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/maximus)
<!-- tensortonic:end -->
