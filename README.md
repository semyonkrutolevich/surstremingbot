
# Surstreming Telegram Bot

It's a simple telegram bot that fetches prices from API and send it to you as a telegram message.

**Hours spent: 0.8h** (0.6h was spent to write README)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`TOKEN` - required

`CHAT_ID` - required

`CURRENCIES` - default: BTC,ETH

`PRICE_CURRENCY` - default: USD

`TIMEOUT` - fetch timeout in minutes, default: 60 min


## Run Locally

Clone the project

```bash
  git clone https://github.com/semyonkrutolevich/surstremingbot
```

Go to the project directory

```bash
  cd surstremingbot
```

Create and fill .env
```bash
```


Install dependencies

```bash
  pip install -r requirements.txt
```

Start the worker

```bash
  python3 main.py
```

## Run with docker-compose

```bash
  git clone https://github.com/semyonkrutolevich/surstremingbot
```

Go to the project directory

```bash
  cd surstremingbot
```

Create and fill .env
```bash
```

Start the worker

```bash
  docker-compose up --build -d
```

## Acknowledgements

 - [Crypto Prices API](https://min-api.cryptocompare.com/documentation)
 - [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)


## Roadmap(probably never)

- Add coins to fetch via telegram commands

- Add portfolio

- Add statistics


## Surströmming
I know that I spell it wrong, whatever...

Surströmming (pronounced [ˈsʉ̂ːˌʂʈrœmːɪŋ]; Swedish for 'sour herring') is lightly salted, fermented Baltic Sea herring traditional to Swedish cuisine since at least the 16th century. It is distinct from fried or pickled herring.