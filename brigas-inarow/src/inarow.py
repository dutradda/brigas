class TurnError(Exception):
  def __str__(self):
    return 'Is not the turn of this player'

class FieldError(Exception):
  def __str__(self):
    return 'This field has been played'

class GameOverError(Exception):
  def __init__(self, winner):
    self.winner = winner

  def __str__(self):
    return 'Game Over! The Winner is #%d' % self.winner

class InaRow():
  def __init__(self, game_size, num_players, row_size):
    self.matrix = [[-1 for i in range(game_size)] for i in range(game_size)]
    self.players = [i for i in range(num_players)]
    self.row_size = row_size
    self.player_turn = 0
    self.game_over = False

  def allocate_field(self, player_id, y):
    for x in range(len(self.matrix)-1, -1, -1):
      if self.matrix[x][y] == -1:
        self.matrix[x][y] = player_id
        return x
    return None

  def play(self, player_id, y):
    if not self.game_over:
      if player_id == self.player_turn:
        x = self.allocate_field(player_id, y)
        if x is not None:
          self.game_over = self._process_move(x, y)
          self.winner = self.player_turn
          self.player_turn = (self.player_turn + 1) % len(self.players)
          if not self.game_over:
            return None
          return self.winner
        else:
          raise FieldError()
      else:
        raise TurnError()
    else:
      raise GameOverError(self.winner)

  def _process_move(self, x, y):
    if self._count_line(x, y) != self.row_size:
      if self._count_column(x, y) != self.row_size:
        if self._count_diagonal_up(x, y) != self.row_size:
          if self._count_diagonal_down(x, y) != self.row_size:
            return False
    return True

  def _count_line(self, x, y):
    count = 1
    try:
      i = x + 1
      while self.matrix[x][y] == self.matrix[i][y]:
        count += 1
        i += 1
    except IndexError:
      pass
    return count

  def _count_column(self, x, y):
    count = 1
    try:
      i = y + 1
      while self.matrix[x][y] == self.matrix[x][i]:
        count += 1
        i += 1
      i = y - 1
      while self.matrix[x][y] == self.matrix[x][i]:
        count += 1
        i -= 1
    except IndexError:
      pass
    return count

  def _count_diagonal_up(self, x, y):
    count = 1
    try:
      i = x + 1
      j = y - 1
      while self.matrix[x][y] == self.matrix[i][j]:
        count += 1
        i += 1
        j -= 1
    except IndexError:
      pass
    return count

  def _count_diagonal_down(self, x, y):
    count = 1
    try:
      i = x + 1
      j = y + 1
      while self.matrix[x][y] == self.matrix[i][j]:
        count += 1
        i += 1
        j += 1
    except IndexError:
      pass
    return count

