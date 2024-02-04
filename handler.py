import plotly.graph_objects as go

# Define the labels for the nodes
labels = [
    'Revenue from operations',  # 0
    'Other Income',             # 1
    'Total Income',             # 2
    'Total Expenses',           # 3
    'Profit before Tax',        # 4
    'Medical Consumables',      # 5
    'Employee Benefits',        # 6
    'Finance Costs',            # 7
    'Depreciation',             # 8
    'Professional Fees',        # 9
    'Other Expenses',           # 10
    'Current Tax',              # 11
    'Deferred Tax',             # 12
    'Profit for Period'         # 13
]

# Define the flows (source to target)
links = {
    'source': [0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4],  # Indices of the source nodes
    'target': [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], # Indices of the target nodes
    'value':  [
        3359.58,  # Revenue from operations to Total Income
        86.09,    # Other Income to Total Income
        2598.02,  # Total Income to Total Expenses
        847.65,   # Total Income to Profit before Tax
        426.97,   # Total Expenses to Medical Consumables
        434.25,   # Total Expenses to Employee Benefits
        142.62,   # Total Expenses to Finance Costs
        276.60,   # Total Expenses to Depreciation
        772.11,   # Total Expenses to Professional Fees
        545.47,   # Total Expenses to Other Expenses
        235.67,   # Profit before Tax to Current Tax
        13.75,    # Profit before Tax to Deferred Tax
        598.23    # Profit before Tax to Profit for Period (Assuming this is the remainder after taxes)
    ]
}

# Define nodes for the Sankey diagram
nodes = {
    'label': labels,
    'pad': 50,  # Padding between nodes
    'thickness': 15  # Thickness of the nodes
}

# Create the Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node=nodes,
    link=links
)])

# Update the layout of the figure
fig.update_layout(
    title_text="Financial Sankey Diagram for Q3 FY24",
    font_size=10
)

# Show the figure
fig.show()
