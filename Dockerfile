FROM python:3

WORKDIR /home/user/app
COPY . .
RUN pip install requests==2.31.0 pyTelegramBotAPI==4.16.1
RUN useradd -u 1000 user
USER user