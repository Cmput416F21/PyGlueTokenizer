def msg(s, ch):
  if has_win(s, 'x'): return('x has won')
  elif has_win(s, 'o'): return('o has won')
  else:
    wm, calls = win_move(s, ch)
    out = '\n' + ch + '-to-move: '
    out += (ch if wm else oppCH(ch)) + ' wins'
    out += (' ... ' if wm else ' ') + wm + '\n'
    out += str(calls) + ' calls\n'
    return out
