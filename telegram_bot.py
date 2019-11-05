import requests
from bottle import Bottle, response, request as bottle_request


class BottleHandlerMixing:
    BOT_URL = None

    def get_chat_id(self, data):
        chat_id = data['message']['chat']['id']

        return chat_id

    def get_message(self, data):
        message_text = data['message']['text']

        return message_text

    def send_message(self, prepared_data):
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)


class TelegramBot(BottleHandlerMixing, Bottle):
    BOT_URL = 'https://api.telegram.org/bot1032773380:AAEnx75tFJd9R659Erx9js-J--bIuUrIAiU/'

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")

    def change_text_message(self, text):
        return text[::-1]

    def prepare_data_for_answer(self, data):
        json_data = {
            'chat_id': '',
            'text': '',
            }

        return json_data

    def post_handler(self):

        return response


if __name__ == '__main__':
    app = TelegramBot()
    app.run(host='localhost', port=8080, debug=True)
