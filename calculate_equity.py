from treys import Card, Deck, Evaluator
import time

if __name__ == '__main__':
    start_time = time.time()
    evaluator = Evaluator()
    deck = Deck()
    for i in range(10):
        hand = deck.deal_hand()
        print(hand)
        for card in hand:
            print(Card.int_to_str(card))
        print(Card.ints_to_pretty_str(hand))
        print(deck)
    # player1_hand = deck.draw(2)
    # player2_hand = deck.draw(2)
    # Card.print_pretty_cards(player1_hand)
    # Card.print_pretty_cards(player2_hand)
    # Card.print_pretty_cards(board)
    # p1_score = evaluator.evaluate(board, player1_hand)
    # p2_score = evaluator.evaluate(board, player2_hand)
    # p1_class = evaluator.get_rank_class(p1_score)
    # p2_class = evaluator.get_rank_class(p2_score)
    # print("Player 1 hand rank = %d (%s)\n" %
    #       (p1_score, evaluator.class_to_string(p1_class)))
    # print("Player 2 hand rank = %d (%s)\n" %
    #       (p2_score, evaluator.class_to_string(p2_class)))
    # hands = [player1_hand, player2_hand]
    # evaluator.hand_summary(board, hands)
    # end_time = time.time()
    # print(f"cost time {end_time - start_time}s")
