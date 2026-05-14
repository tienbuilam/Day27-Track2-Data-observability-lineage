"""
Step-by-step implementation checklist in Python form.
Replace TODOs with real code in the student's project.
"""

STEP_1 = "Create dags/, src/, data/, and output/ folders."
STEP_2 = "Put orders_failed.csv and orders_passed.csv in data/."
STEP_3 = "Create config constants for valid statuses, input path, output path, and webhook."
STEP_4 = "Read CSV rows with csv.DictReader."
STEP_5 = "Count invalid rows for customer_id, amount, and status."
STEP_6 = "Build a summary dictionary and save it as JSON."
STEP_7 = "Send the summary to Discord."
STEP_8 = "Raise an exception when validation_status == 'failed'."
STEP_9 = "Wrap the validation function inside an Airflow PythonOperator."
STEP_10 = "Run both datasets and compare output with the expected summaries."
STEP_11 = "Use a mock webhook first if the real Discord webhook is not stable."


def implementation_checklist() -> list[str]:
    return [
        STEP_1,
        STEP_2,
        STEP_3,
        STEP_4,
        STEP_5,
        STEP_6,
        STEP_7,
        STEP_8,
        STEP_9,
        STEP_10,
        STEP_11,
    ]


def print_checklist() -> None:
    for index, step in enumerate(implementation_checklist(), start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    print_checklist()
