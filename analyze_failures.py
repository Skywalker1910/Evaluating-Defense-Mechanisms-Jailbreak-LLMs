import pandas as pd
import argparse
from collections import Counter
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, required=True, help="Path to result CSV file")
args = parser.parse_args()

console = Console()
df = pd.read_csv(args.input)

failure_cases = df[df['success'] == False]

# Identify model from file or content
if 'model' in df.columns:
    model_name = df['model'].iloc[0]
else:
    model_name = "Unknown Model"

console.print("\n[bold underline]Failure Analysis[/bold underline]")
console.print(f"Model Analyzed          : {model_name}")
console.print(f"Total Failed Attempts   : {len(failure_cases)}\n")

# Count types of failures from the 'status' field
status_counts = Counter(failure_cases['status'])

# Quick refusal detection based on common denial phrases
quick_refusal_phrases = ["i'm sorry", "i cannot", "i can't", "as an ai"]
quick_refusal_count = 0

for _, row in failure_cases.iterrows():
    response = str(row['response']).lower()
    if any(phrase in response for phrase in quick_refusal_phrases):
        quick_refusal_count += 1

# Display breakdown of reasons
table = Table(show_header=True, header_style="bold cyan")
table.add_column("Failure Reason")
table.add_column("Count", justify="right")

table.add_row("Failed with Exception", str(status_counts.get("failed with exception", 0)))
table.add_row("Failed with Timeout", str(status_counts.get("failed with timeout", 0)))
table.add_row("Quick Refusal (AI Decline)", str(quick_refusal_count))

console.print(table)
