### app.py ###
from dash import Dash
from layout import create_layout
from callbacks import register_callbacks

app = Dash(__name__)
app.title = "Blackjack"

# Set up layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
