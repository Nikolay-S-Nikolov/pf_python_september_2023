def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_side = ticket[10:]
    right_side = ticket[:10]
    winning_symbol = ['@', '#', '$', '^']
    for match_symbol in winning_symbol:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = uninterrupted_match_length * match_symbol
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


collection_tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in collection_tickets:
    print(check_ticket(current_ticket))
