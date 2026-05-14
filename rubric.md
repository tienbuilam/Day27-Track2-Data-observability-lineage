# Scoring Rubric

Total: 10 points

## 1. DAG Structure - 2 points

- 2: DAG is valid, named correctly, and can be triggered manually.
- 1: DAG exists but has minor configuration issues.
- 0: DAG missing or unusable.

## 2. CSV Ingestion - 2 points

- 2: Reads the input CSV correctly and handles all rows.
- 1: Reads data partially or with small mistakes.
- 0: Cannot read the dataset.

## 3. Validation Logic - 3 points

- 3: Correctly checks missing `customer_id`, invalid `amount`, and invalid `status`.
- 2: Two rules work correctly.
- 1: One rule works correctly.
- 0: Validation is incorrect or missing.

## 4. Output JSON - 1 point

- 1: Generates `validation_summary.json` with the correct counts and status.
- 0: Output file missing or incorrect.

## 5. Discord Alert - 1 point

- 1: Sends a meaningful success/failure alert through the webhook.
- 0: Alert missing or broken.

## 6. Failure Handling - 1 point

- 1: Pipeline stops when validation fails and still preserves the summary file.
- 0: Pipeline continues incorrectly or loses the failure summary.
