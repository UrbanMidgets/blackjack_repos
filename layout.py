### layout.py ###
from dash import html, dcc


def create_layout():
    return html.Div([
        html.H1("Blackjack Game", style={"textAlign": "center", "fontSize": "48px"}),

        # Bet input and new game button
        html.Div([
            html.H4("Place Your Bet:", style={"textAlign": "center", "fontSize": "24px"}),
            dcc.Input(id="bet-input", type="number", min=1, placeholder="Enter bet", style={"fontSize": "20px"}),
            html.Button("New Game", id="new-game-button", n_clicks=0, style={"fontSize": "20px", "marginTop": "10px"}),
        ], style={"textAlign": "center", "marginBottom": "10px"}),

        # Balance display
        html.Div([
            html.H4("Balance:", style={"textAlign": "center", "fontSize": "24px"}),
            html.Div(id="balance-display", style={"fontSize": "24px"}),
        ], style={"textAlign": "center", "marginBottom": "20px"}),

        # Game area
        html.Div([
            html.Div([
                html.H3("Your Hand", style={"fontSize": "24px"}),
                dcc.Markdown(id="player-hand", style={"fontSize": "20px"}),
                html.H4("Total: ", id="player-total", style={"fontSize": "24px"}),
                html.Button("Hit", id="hit-button", n_clicks=0, style={"fontSize": "20px", "marginRight": "10px"}),
                html.Button("Stay", id="stay-button", n_clicks=0, style={"fontSize": "20px"}),
            ], style={"flex": "1", "padding": "20px"}),

            html.Div([
                html.H3("Dealer's Hand", style={"fontSize": "24px"}),
                dcc.Markdown(id="dealer-hand", style={"fontSize": "20px"}),
                html.H4("Total: ", id="dealer-total", style={"fontSize": "24px"}),
            ], style={"flex": "1", "padding": "20px"}),
        ], style={"display": "flex", "justifyContent": "space-between"}),

        # Game status
        html.Div([
            html.H3("Game Status", style={"textAlign": "center", "fontSize": "28px"}),
            html.Div(id="game-result", style={"fontSize": "24px", "color": "red"}),
        ], style={"textAlign": "center", "marginTop": "20px"}),
    ])
