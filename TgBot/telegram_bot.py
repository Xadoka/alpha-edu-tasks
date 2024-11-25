import yfinance as yf
import matplotlib.pyplot as plt
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import io

# Замените 'ВАШ_ТОКЕН' на токен вашего бота
TELEGRAM_TOKEN = 'Your Token'

# Функция для получения цены и графика IXN
async def send_ixn_price_and_chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ticker = yf.Ticker("IXN")
    data = ticker.history(period="1y")

    # Получаем текущую цену
    current_price = data['Close'].iloc[-1]
    message = f"Текущая цена IXN: ${current_price:.2f}"

    # Создаем график
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label='Цена закрытия')
    plt.title('График цены IXN за последний год')
    plt.xlabel('Дата')
    plt.ylabel('Цена (USD)')
    plt.legend()
    plt.grid(True)

    # Сохраняем график в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Отправляем цену и график
    await update.message.reply_text(message)
    await update.message.reply_photo(photo=buf)

# Основная функция для запуска бота
def main():
    # Создаем приложение бота
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Обработчик команды /start для приветствия
    application.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("Привет! Напиши /ixn, чтобы получить цену и график IXN.")))

    # Обработчик команды /ixn для отправки цены и графика
    application.add_handler(CommandHandler("ixn", send_ixn_price_and_chart))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
