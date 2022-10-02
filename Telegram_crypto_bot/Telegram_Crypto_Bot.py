#pycoingecko is used to interact witk CoinGeckoAPI
from pycoingecko import CoinGeckoAPI
import logging
from aiogram import Bot,Dispatcher,executor,types
from Config import API_TOKEN
#CoinGeckoAPI
cg = CoinGeckoAPI()

#Telegram Bot

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello!I am Crypto Bot!"
    "\nHere you can get rates for certain cryptocurrencies."
    "\nHere is list of commands you can use:"
    "\n/BTC for Bitcoin rate"
    "\n/ETH for Ethereum rate"
    "\n/USDT for Tether rate"
    "\n/USDC for USD-Coin rate"
    "\n/BNB for Binancecoin rate"
    "\n/XPR for Ripple(XPR) rate"
    "\n/BUSD for Binance USD rate"
    "\n/ADA for Cordano(ADA) rate"
    "\n/SOL for Solano(SOL) rate"
    "\n/DOGE for Dogecoin rate")
    

#BITCOIN
@dp.message_handler(commands = ['BTC','Bitcoin','bitcoin'])
async def bitcoin_rate(message: types.Message):
    data = cg.get_price(ids='bitcoin',vs_currencies='usd')
    await message.reply('\U000020BF BITCOIN\n' + str(data['bitcoin']['usd']) + ' ' +'USD 💵')
    

#ETHEREUM
@dp.message_handler(commands=['ETH','Ethereum','ethereum'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='ethereum',vs_currencies='usd')
    await message.reply('⟠ ETHEREUM\n' + str(data['ethereum']['usd']) + ' ' +'USD 💵')


#TETHER
@dp.message_handler(commands=['USDT','Tether','tether'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='tether',vs_currencies='usd')
    await message.reply('₮ TETHER\n' + str(data['tether']['usd']) + ' ' +'USD 💵')


#USD-COIN
@dp.message_handler(commands=['USDC','USDCoin','USD Coin','USD-Coin'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='usd-coin',vs_currencies='usd')
    await message.reply('USD-Coin\n' + str(data['usd-coin']['usd']) + ' ' +'USD 💵')

#BINANCECOIN
@dp.message_handler(commands=['BNB','Binancecoin','binancecoin'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='binancecoin',vs_currencies='usd')
    await message.reply('BNB\n' + str(data['binancecoin']['usd']) + ' ' +'USD 💵')

#XPR
@dp.message_handler(commands=['XPR','Ripple','ripple'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='ripple',vs_currencies='usd')
    await message.reply('XPR\n' + str(data['ripple']['usd']) + ' ' +'USD 💵')


#Binance USD
@dp.message_handler(commands=['BUSD','Binance-USD','binance-usd'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='binance-usd',vs_currencies='usd')
    await message.reply('Binance USD\n' + str(data['binance-usd']['usd']) + ' ' +'USD 💵')


#Cardano(ADA)
@dp.message_handler(commands=['ADA','Cardano','cardano'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='cardano',vs_currencies='usd')
    await message.reply('Cardano(ADA)\n' + str(data['cardano']['usd']) + ' ' +'USD 💵')


#Solano(SOL)
@dp.message_handler(commands=['SOL','Solano','solano'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='solano',vs_currencies='usd')
    await message.reply('Solano(SOL)\n' + str(data['solano']['usd']) + ' ' +'USD 💵')


#Dogecoin(DOGE)
@dp.message_handler(commands=['DOGE','Dogecoin','dogecoin'])
async def ethereum_rate(message: types.Message):
    data = cg.get_price(ids='dogecoin',vs_currencies='usd')
    await message.reply('Dogecoin(DOGE)\n' + str(data['dogecoin']['usd']) + ' ' +'USD 💵')    


executor.start_polling(dp,skip_updates=True)