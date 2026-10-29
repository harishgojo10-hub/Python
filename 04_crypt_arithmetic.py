from itertools import permutations

def solve_send_more_money():
    # SEND + MORE = MONEY
    for digits in permutations(range(10), 8):
        S, E, N, D, M, O, R, Y = digits
        if S == 0 or M == 0:
            continue
        send = 1000*S + 100*E + 10*N + D
        more = 1000*M + 100*O + 10*R + E
        money = 10000*M + 1000*O + 100*N + 10*E + Y
        if send + more == money:
            return S, E, N, D, M, O, R, Y, send, more, money
    return None

answer = solve_send_more_money()
print("Crypt-Arithmetic: SEND + MORE = MONEY")
if answer:
    S, E, N, D, M, O, R, Y, send, more, money = answer
    print(f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
    print(f"{send} + {more} = {money}")
else:
    print("No solution found")
