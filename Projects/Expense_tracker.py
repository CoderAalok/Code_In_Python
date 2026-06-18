
""""
Personal Expense Tracker
==========================
## Features:
- Add new expense intractively
- View total spent records (Category and monthly trend line)
- Visualization: Pie, Bar charts and graph(tends)
"""

import pandas as pd
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import os
from pathlib import Path
from datetime import datetime


#─────────────────* Config *────────────────────────#
FILE = "expenses.csv"
BASE_DIR = Path(__file__).parent # current working directory path
CSV_FILE = BASE_DIR / FILE
CATEGORIES = ["Food", "Health", "Entertainment", "Transport", "Utilities", "Other"]
COLORS = ["#56C591", "#F4845F", "#4C9BE8", "#D1A842", "#A78BFA", "#94A3B8"]


#─────────────────* Data analysis & update record *─────────────────#
def load_file():
    # load previous expenses, create empty dataframe if doesn't exits
    Is_exits = os.path.exists(CSV_FILE)
    
    if not Is_exits:
        df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
        df.to_csv(CSV_FILE, index=False)
        print(f"✔ Sucessfully! CSV file created: {CSV_FILE}")
    
    # if file does exits but empty
    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["Date"])
        
    except Exception:
        df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
        df.to_csv(CSV_FILE, index=False)
        print(f"✔ Sucessfully! CSV file created: {CSV_FILE}")
        
    return df


def add_expenses(df):
    # add current date
    date_str = datetime.today().strftime("%Y-%m-%d")
    date = pd.to_datetime(date_str)
    
    # add category
    print(f"\n✦ CATEGORIES 🛍️  :\n●", "\n● ".join(CATEGORIES))
    print("──────────────────────────────────")
    category = input("\n⤷ Category 🛍️ : ").strip().title()
    
    if category not in CATEGORIES:
        category = 'Other'
    
    # add description
    description = input("⤷ Description 📝: ").strip().title()
    
    if not description:
        description = "Unknown"
    
    # add amount
    try:
        amount = float(input("⤷ Amount 💸: ").strip())
        
    except ValueError:
        print("❌ Invalid amount. Expenses not added.")
        return df

    # formating new data
    new_data = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }])
    
    # concatenate old and new data
    df = pd.concat([df, new_data], ignore_index=True)
    
    # save all
    save_data(df)
    print(f"\n✔ Successfully added 🗃️.\nCategory 🛍️ : {category} ➜  Description 📝: {description} ➜  Amount 💸: 💲{amount:.2f}")
    return df


#─────────────────* Save new dataframe as CSV file *─────────────────#
def save_data(df):
    # Save new data 
    df.to_csv(CSV_FILE, index=False)


#─────────────────* Expenses analysis *─────────────────#
def spending_per_category(df):
    "Return total spending per category"
    return (
        df.groupby('Category')['Amount']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"Amount": "Total"})
    )


def spending_per_month(df):
    "Return total spending per month"
    df = df.copy()
    df['Month'] = df['Date'].dt.to_period("M")
    
    return (
        df.groupby('Month')['Amount']
        .sum()
        .reset_index()
        .rename(columns={"Amount": "Total"})
    )


def display_records(df):
    # load data categories wise
    catg = spending_per_category(df)
    
    print("\n ════════════════ Spending per Category 🛍️  ═════════════════")
    for _, row in catg.iterrows():
        print(f"  {row["Category"]:<15} | 💲{row["Total"]:>8.2f}")
    

    # load data month wise
    month = spending_per_month(df)
    print("\n ════════════════ Spending per Month 📅 ════════════════")
    
    for _, row in month.iterrows():
        print(f"  {str(row["Month"]):<15} | 💲{row["Total"]:>8.2f}")
    
    # total amount
    total = df["Amount"].sum()
    print("\n-----------------------------------------------------")
    print(f" ➤ Total spent 💸: 💲{total}")
    print("-----------------------------------------------------")


#────────────────* Plotting charts and graph *────────────────

def shows_chart_graph(df):
    # load data
    month = spending_per_month(df)
    catg = spending_per_category(df)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    fig.suptitle("Personal Expense Tracker", fontsize=16, fontweight="bold")
    fig.patch.set_facecolor('#F8FAFC')
    
    # set face color each axes
    for ax in axes:
        ax.set_facecolor('#F8FAFC')
    
    #────────────────* Pie chart by category *────────────────
    ax1 = axes[0]
    weights, texts, autotexts = ax1.pie(
        catg["Total"],
        labels=catg["Category"],
        autopct="%1.1f%%",
        colors=COLORS[: len(catg)],
        startangle=140,
        pctdistance=0.87,
        wedgeprops={"linewidth": 1.5, "edgecolor": "white"}
    )
    
    for text in autotexts:
        text.set_fontsize(10)
        text.set_color("white")
        text.set_fontweight("bold")
    
    ax1.set_title("Spending per Category", fontsize=14, fontweight="bold", pad=15)
    
    
    #────────────────* Horizontal chart by category *────────────────
    ax2 = axes[1]
    bars = ax2.barh(
        catg['Category'],
        catg["Total"],
        color=COLORS[: len(catg)],
        linewidth=1.4,
        edgecolor="white",
        height=0.4
    )
    
    #────────────────* style and artist add *────────────────
    ax2.set_title("Amount per Category", fontsize=13, fontweight="bold", pad=12)
    ax2.set_xlabel("Total spent (💲)", fontsize=10)
    ax2.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f"))
    ax2.invert_yaxis()
    ax2.spines[["top", "right", "left"]].set_visible(False)
    ax2.grid(axis="x", linestyle="--", alpha=0.5)
    ax2.tick_params(axis="y", length=0)
    
    #────────────────* values label on bar *────────────────
    for bar in bars:
        width = bar.get_width()
        ax2.text(
            width + 2, bar.get_y() + bar.get_height() / 2,
            f"${width:.0f}", va="center", ha="left", fontsize=9, color="#475569",
        )

    
    #────────────────* Month trends graph *────────────────
    ax3 = axes[2]
    months = [str(m) for m in month["Month"]]
    totals = month["Total"].values
    
    #────────────────* Plot *────────────────
    ax3.plot(
        months, totals,
        color="#4C9BE8", linewidth=2.5, marker="o",
        markersize=8, markerfacecolor="white", markeredgewidth=2.5,
    )
    
    #────────────────* style and artist add *────────────────

    ax3.fill_between(months, totals, alpha=0.12, color="#4C9BE8")
    ax3.set_xlabel("Month", fontsize=11)
    ax3.set_ylabel("Total spent ($)", fontsize=11)
    ax3.set_title("Monthly spending trend", fontsize=13, fontweight="bold", pad=14)
    ax3.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.0f"))
    ax3.spines[["top", "right"]].set_visible(False)
    ax3.grid(axis="y", linestyle="--", alpha=0.4)
    
    #────────────────* Annotate each point *────────────────
    for x, y in zip(months, totals):
        ax3.annotate(
            f"${y:.0f}", (x, y),
            textcoords="offset points", xytext=(0, 10),
            ha="center", fontsize=9, color="#475569",
        )
    
    # ────────────────* generate & saved *────────────────
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    
    output_path = BASE_DIR / "expense_records.png"
    
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\n✓ Expense records saved to 📂: {output_path}")
    plt.show()
    

#───────────────── Main menu ─────────────────#
def main():
    # load data 
    df = load_file()
    
    try:
        while True:
            print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            print("════════════════ Expense 💰 Tracker 🔎 ════════════════")
            print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")

            print("1️⃣  Add expenses 💰")
            print("2️⃣  Display records 📑")
            print("3️⃣  Shows charts 📊 and graph 📈")
            print("4️⃣  Recent expense 🕒")
            print("5️⃣  Exit➜🚪")
            
            choose = input("\nEnter any number (1 - 5): ").strip()
            
            if choose == "1":
                df = add_expenses(df)
                            
            elif choose == "2":
                if df.empty:
                    print("No expenses recorded yet!")
                    return
                display_records(df)
            
            elif choose == "3":
                if df.empty:
                    print("No expenses recorded yet!")
                    return
                shows_chart_graph(df)
            
            elif choose == "4":
                recent = df.sort_values("Date", ascending=False).head()
                recent = recent.copy()
                recent['Amount'] = recent["Amount"].map("${:.2f}".format)
                
                print("Here the most recent expense: ")
                print("-"*50)
                print(recent[['Date', 'Category', 'Description', 'Amount']].to_string(index=False))

            else:
                print("\n See you next time 😊 !")
                return
    
    except KeyboardInterrupt:
        return
    
#───────────────── Program driver  ─────────────────#
if __name__ == '__main__':
    main()