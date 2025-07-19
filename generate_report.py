import pandas as pd
from fpdf import FPDF

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Analyze data
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()
top_student = df.loc[df["Score"].idxmax(), "Name"]

# Step 3: Generate PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Student Performance Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_analysis(self, avg, high, low, top):
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Average Score: {avg:.2f}", ln=True)
        self.cell(0, 10, f"Highest Score: {high}", ln=True)
        self.cell(0, 10, f"Lowest Score: {low}", ln=True)
        self.cell(0, 10, f"Top Performer: {top}", ln=True)
        self.ln(10)

    def add_table(self, data_frame):
        self.set_font("Arial", "B", 12)
        self.cell(50, 10, "Name", 1)
        self.cell(50, 10, "Score", 1)
        self.ln()
        self.set_font("Arial", size=12)
        for index, row in data_frame.iterrows():
            self.cell(50, 10, row["Name"], 1)
            self.cell(50, 10, str(row["Score"]), 1)
            self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.add_analysis(average_score, highest_score, lowest_score, top_student)
pdf.add_table(df)

# Save the PDF
pdf.output("sample_report.pdf")

print("Report generated: sample_report.pdf")

