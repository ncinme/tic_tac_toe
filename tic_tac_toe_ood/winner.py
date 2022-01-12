from bot import Bot
bot = Bot()


class Winner:
    """Checks if there is a winner after a player's or bot's response"""
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self. winning_combination = bot.winning_combination
        self.got_winner = False

    def decide_winner(self, player, count, player1_selection, player2_selection, chart):
        self.got_winner = False
        for item in self.winning_combination:
            if set(item).issubset(set(player1_selection)) or set(item).issubset(set(player2_selection)):
                chart.print_ttt()
                if player == 1:
                    self.player1_score += 1
                else:
                    self.player2_score += 1
                print(f"Game Over!! Player {player} is the winner!!")
                print(f"Score: Player1 = {self.player1_score} ; Player2 = {self.player2_score}")
                self.got_winner = True
                return self.got_winner

        if count == 9 and not self.got_winner:
            chart.print_ttt()
            print(f"It's a Draw!!")
            print(f"Score: Player1 = {self.player1_score} ; Player2 = {self.player2_score}")
            self.got_winner = True

        return self.got_winner
