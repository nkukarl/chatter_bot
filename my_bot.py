from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'Muhammad Li',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database_li.json',
)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')

while True:
    try:
        bot_input = bot.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
