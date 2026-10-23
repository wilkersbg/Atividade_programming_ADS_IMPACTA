import flet as ft
from card import Card
from slot import Slot

SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500


class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()
        self.controls = []
        self.slots = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        card1 = Card(self, image_path="Captura de tela 2026-10-22 215825.png")
        card2 = Card(self, image_path="WhatsApp Image 2026-10-22 at 21.57.33.jpeg")
        card3 = Card(self, image_path="WhatsApp Image 2026-10-22 at 22.13.45.jpeg")
        self.cards = [card1, card2, card3]

    def create_slots(self):
        self.slots.append(Slot(top=0, left=0))
        self.slots.append(Slot(top=0, left=200))
        self.slots.append(Slot(top=0, left=300))
        self.controls.extend(self.slots)
        self.update()

    def deal_cards(self):
        self.controls.extend(self.cards)

        for card in self.cards:
            card.place(self.slots[0])
        self.update()