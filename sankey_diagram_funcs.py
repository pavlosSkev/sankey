import plotly.graph_objects as go

def create_sankey(df, columns, title="Sankey Diagram"):
    """
    Creates a Sankey diagram from a given DataFrame and a list of columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): Ordered list of column names to be used in the flow.
    title (str): Title of the Sankey diagram.

    Returns:
    None: Displays the Sankey diagram.
    """

    # Convert DataFrame to Pandas if needed
    if not isinstance(df, pd.DataFrame):
        df = df.toPandas()

    source = []
    target = []

    # Construct source and target lists dynamically
    for i in range(len(columns) - 1):
        source += df[columns[i]].tolist()
        target += df[columns[i + 1]].tolist()

    # Create unique labels and index mapping
    labels = sorted(set(source + target))
    label_index_map = {label: i for i, label in enumerate(labels)}

    # Convert source and target to indices
    source_indices = [label_index_map[label] for label in source]
    target_indices = [label_index_map[label] for label in target]

    # Assign uniform values for the links (weights)
    values = [1] * len(source_indices)

    # Create the Sankey diagram
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=values
        )
    ))

    # Update layout
    fig.update_layout(
        title_text=title,
        font_size=14,
        width=1200,
        height=800 * 2
    )

    # Show the diagram
    fig.show()

# Example: create_sankey(pdf, ["table_input", "project_name", "job_name", "table_output"], title="Input Tables to Job Overview")
