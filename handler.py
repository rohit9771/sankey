import plotly.graph_objects as go

# Define the values for the nodes
revenue_operations = 3359.58
other_income = 86.09
medical_consumables = 426.97
employee_benefits = 434.25
finance_costs = 142.62
depreciation_amortization = 276.60
professional_fees_doctors = 772.11
other_expenses = 545.47
total_income = revenue_operations + other_income
total_expenses = medical_consumables + employee_benefits + finance_costs + depreciation_amortization + professional_fees_doctors + other_expenses
profit_before_tax = total_income - total_expenses
current_tax = 235.67
deferred_tax = -13.75
total_tax_expense = current_tax + deferred_tax
profit_for_period = profit_before_tax - total_tax_expense
other_comprehensive_income = 1.46
total_comprehensive_income = profit_for_period + other_comprehensive_income

# Define the Sankey diagram data
data = go.Sankey(
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=[
            "Revenue from Operations", "Other Income", "Total Income",
            "Medical Consumables", "Employee Benefits", "Finance Costs",
            "Depreciation & Amortization", "Professional Fees to Doctors", "Other Expenses",
            "Total Expenses", "Profit Before Tax", "Current Tax", "Deferred Tax",
            "Profit for Period", "Other Comprehensive Income", "Total Comprehensive Income"
        ],
        color="blue"
    ),
    link=dict(
        source=[0, 1, 2, 2, 2, 2, 2, 2, 9, 10, 10, 11, 12, 13],
        target=[2, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 13, 14],
        value=[
            revenue_operations, other_income, medical_consumables, employee_benefits, finance_costs,
            depreciation_amortization, professional_fees_doctors, other_expenses, profit_before_tax,
            current_tax, deferred_tax, profit_for_period, other_comprehensive_income, total_comprehensive_income
        ],
        label=[
            str(revenue_operations), str(other_income), str(medical_consumables), str(employee_benefits), 
            str(finance_costs), str(depreciation_amortization), str(professional_fees_doctors), str(other_expenses), 
            str(profit_before_tax), str(current_tax), str(deferred_tax), str(profit_for_period), 
            str(other_comprehensive_income), str(total_comprehensive_income)
        ]
    )
)

# Define the layout of the diagram
layout = go.Layout(
    title=dict(
        text="Sankey Diagram for Rainbow Children's Medicare Limited Income Statement",
        font=dict(size=16)
    )
)

# Create the figure
fig = go.Figure(data=[data], layout=layout)

# Show the figure
fig.show()
