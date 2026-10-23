import flet as ft

CARD_WIDTH = 70
CARD_HEIGHT = 100
DROP_PROXIMITY = 20
CARD_OFFSET = 20


class Card(ft.GestureDetector):
    def __init__(self, solitaire, image_path: str):
        super().__init__()
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.left = None
        self.top = None
        self.solitaire = solitaire
        self.slot = None
        self.card_offset = CARD_OFFSET
        self.image_path = image_path

        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            content=ft.Image(
                src=self.image_path,
                fit="contain",
            ),
        )
        self.draggable_pile = [self]

    def move_on_top(self):
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    def bounce_back(self):
        for card in self.draggable_pile:
            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            card.left = card.slot.left
        self.solitaire.update()

    def place(self, slot):
        for card in self.draggable_pile:
            card.top = slot.top + len(slot.pile) * CARD_OFFSET
            card.left = slot.left

            if card.slot is not None:
                card.slot.pile.remove(card)

            card.slot = slot
            slot.pile.append(card)

        self.solitaire.update()

    def get_draggable_pile(self):
        if self.slot is not None:
            self.draggable_pile = self.slot.pile[self.slot.pile.index(self) :]
        else:
            self.draggable_pile = [self]

    def start_drag(self, e: ft.DragStartEvent):
        self.get_draggable_pile()
        self.move_on_top()
        self.solitaire.update()

    def drag(self, e: ft.DragUpdateEvent):
        for card in self.draggable_pile:
            card.top = (
                max(0, self.top + e.local_delta.y)
                + self.draggable_pile.index(card) * CARD_OFFSET
            )
            card.left = max(0, self.left + e.local_delta.x)
            self.solitaire.update()

    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET))
                < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                self.solitaire.update()
                return

        self.bounce_back()