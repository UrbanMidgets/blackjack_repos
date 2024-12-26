import dash
from dash import Input, Output, State
import blackjack_logic as game_logic
from blackjack_logic import start_new_game, player_hit, player_stay


def register_callbacks(app):
    @app.callback(
        [Output("player-hand", "children"),
         Output("dealer-hand", "children"),
         Output("player-total", "children"),
         Output("dealer-total", "children"),
         Output("game-result", "children"),
         Output("balance-display", "children")],
        [Input("new-game-button", "n_clicks"),
         Input("hit-button", "n_clicks"),
         Input("stay-button", "n_clicks")],
        [State("bet-input", "value")]
    )
    def update_game(new_game_clicks, hit_clicks, stay_clicks, bet_value):
        ctx = dash.callback_context
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None

        if triggered_id == "new-game-button":
            if not bet_value:
                return ("Invalid bet. Please enter a bet amount.",
                        "", "Total: --", "Total: --",
                        "Game not started.", f"Balance: ${start_new_game.balance}")
            return start_new_game(bet_value)

        elif triggered_id == "hit-button":
            return player_hit()

        elif triggered_id == "stay-button":
            return player_stay()

        return ("", "", "Total: --", "Total: --", "Awaiting action.", f"Balance: ${game_logic.balance}")  # Access balance directly from the game logic module
