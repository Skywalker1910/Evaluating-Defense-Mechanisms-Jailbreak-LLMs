import pandas as pd
import argparse
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, required=True, help="Path to result CSV file")
args = parser.parse_args()

console = Console()
df = pd.read_csv(args.input)

# Identify model from file or content
if 'model' in df.columns:
    model_name = df['model'].iloc[0]
else:
    model_name = "Unknown Model"

console.print("\n[bold underline]Evaluation Summary[/bold underline]")
console.print(f"Model Evaluated         : {model_name}")
console.print(f"Total Attempts          : {len(df)}")
console.print(f"Successful Replies      : {df['success'].sum()}")
console.print(f"Query Success Rate (QSR): {round(df['success'].mean() * 100, 2)}%\n")

if 'category' in df.columns:
    console.print("[bold underline]Success Rate by Category[/bold underline]")
    category_summary = df.groupby('category')['success'].agg(['count', 'sum'])
    category_summary['success_rate'] = category_summary['sum'] / category_summary['count'] * 100

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Category")
    table.add_column("Attempts", justify="right")
    table.add_column("Successes", justify="right")
    table.add_column("Success Rate (%)", justify="right")

    for category, row in category_summary.iterrows():
        table.add_row(
            str(category),
            str(row['count']),
            str(row['sum']),
            f"{row['success_rate']:.2f}"
        )
    console.print(table)
else:
    console.print("[italic yellow]Category-wise stats not available in the dataset.[/italic yellow]")
