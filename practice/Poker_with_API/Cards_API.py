import requests
import json


class Card:
    apicem_ip = "http://deckofcardsapi.com/api/deck"

    # Shuffle the Cards: https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
    def __init__(self, deck_count=1):
        """
        shuffle
        :param deck_count: the integer number of decks we want  to use
        """
        shuffle_url = f"{Card.apicem_ip}/new/shuffle/"
        params = {"deck_count": deck_count}
        response = requests.get(url=shuffle_url, params=params, verify=True)
        self.r_dict = response.json()
        self.deck_id = self.r_dict["deck_id"]
        print(self.r_dict)

    # Draw a Card: https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2
    def draw_card(self, count=1):
        """
        :param count: the number of cards to draw from the deck
        :return:
        """
        draw_card_url = f"{Card.apicem_ip}/{self.deck_id}/draw/"
        params = {"count": count}
        response = requests.get(url=draw_card_url, params=params, verify=True)
        r_dict = response.json()
        print(r_dict)
        cards_list = []
        for item in r_dict['cards']:
            cards_list.append(item['code'])
        return cards_list

    # Reshuffle the Cards: https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/
    def reshuffle(self):
        reshuffle_url = f"{Card.apicem_ip}/{self.deck_id}/shuffle"
        response = requests.get(url=reshuffle_url, verify=True)
        r_dict = response.json()
        print(r_dict)

    # A Brand New Deck: https://deckofcardsapi.com/api/deck/new/
    def a_brand_new_deck(self):
        new_deck_url = f"{Card.apicem_ip}/new/"
        params = {"jokers_enabled": True}
        response = requests.get(url=new_deck_url, params=params, verify=True)
        r_dict = response.json()  # dictionary
        r_dict["deck_id"] = self.deck_id
        return r_dict

    # A partial Deck: https://deckofcardsapi.com/api/deck/new/shuffle/?cards=AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH
    def a_partial_deck(self, cards_str):
        """
        :param cards_str: a string of card names you need, etc,"AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH"
        :return:
        """
        partial_deck_url = f"{Card.apicem_ip}/new/shuffle/"
        params = {"cards": cards_str}
        response = requests.get(url=partial_deck_url, params=params, verify=True)
        r_dict = response.json()
        r_dict["deck_id"] = self.deck_id
        return r_dict

    # Adding to Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/add/?cards=AS,2S
    def adding_to_piles(self, count):
        """
        :param count: number of cards drawn from deck
        :return:
        """
        discard = ",".join(self.draw_card(count))
        print(discard)
        to_piles_url = f"{Card.apicem_ip}/{self.deck_id}/pile/discard/add/"
        params = {"cards": discard}
        response = requests.get(url=to_piles_url, params=params, verify=True)
        r_dict = response.json()
        return r_dict

    # Shuffle Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/shuffle/
    def shuffle_piles(self):
        shuffle_piles_url = f"{Card.apicem_ip}/{self.deck_id}/pile/discard/shuffle/"
        response = requests.get(url=shuffle_piles_url, verify=True)
        r_dict = response.json()
        print(r_dict)

    # Listing Cards in Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/list/
    def listing_cards(self):
        listing_cards_url = f"{Card.apicem_ip}/{self.deck_id}/pile/discard/list/"
        response = requests.get(url=listing_cards_url, verify=True)
        r_dict = response.json()
        print(r_dict)

    # Drawing from Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?cards=AS
    # Drawing from Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?count=2
    # Drawing from Piles: https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/bottom/
    def drawing_from_piles(self, count):
        drawing_from_piles_url01 = f"{Card.apicem_ip}/{self.deck_id}/pile/discard/draw/"
        discard = ",".join(self.draw_card(count))
        params01 = {"cards": discard}
        response01 = requests.get(url=drawing_from_piles_url01, params=params01, verify=True)
        drawing_from_piles_url02 = f"{Card.apicem_ip}/{self.deck_id}/pile/discard/draw/"
        params02 = {"count": 1}
        response02 = requests.get(url=drawing_from_piles_url02, params=params02, verify=True)
        r_dict01 = response01.json()
        r_dict02 = response02.json()
        # r_dict = r_dict01+r_dict02
        print(r_dict01, r_dict02)


class PokerHand(Card):
    def suit_hist(self,count):
        self.suits = {}
        for card in Card.adding_to_piles(3):
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False




card = Card()
r = card.a_partial_deck("AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH")
print(r)
a = card.adding_to_piles(2)
print(a)
card.shuffle_piles()
card.listing_cards()
card.drawing_from_piles(1)
