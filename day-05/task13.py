
class Message:
    def display(self):
        print("Displaying a simple message.")


class WhatsAppMessage(Message):
    def display(self):
        print("Displaying message through WhatsApp.")


class TelegramMessage(Message):
    def display(self):
        print("Displaying message through Telegram.")


messages = [
    Message(),
    WhatsAppMessage(),
    TelegramMessage(),
    WhatsAppMessage(),
    TelegramMessage()
]

for msg in messages:
    msg.display()
