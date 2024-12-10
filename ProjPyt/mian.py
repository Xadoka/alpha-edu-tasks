import logging
import pandas as pd
import matplotlib.pyplot as plt
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from io import BytesIO
import matplotlib.patches as patches

# Ваш Telegram токен
TOKEN = '7503616880:AAGEp_uEt5a-BR9Ntsz4H6a2GANpHdJtLTI'

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработчик документов
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handle_document(message: types.Message):
    # Получаем документ, который был отправлен пользователем
    document = message.document

    # Загружаем файл Excel
    file_info = await bot.get_file(document.file_id)
    file_path = file_info.file_path
    file = await bot.download_file(file_path)

    # Конвертируем файл Excel в CSV
    try:
        # Считываем файл Excel в DataFrame с помощью pandas
        excel_file = BytesIO(file.getvalue())
        df = pd.read_excel(excel_file, engine='openpyxl')
        df = df.drop(['Тема','Наименование бизнес процесса','Тема.1','Автор.2','Организация','Описание'], axis = 1)
        df= df.rename(columns={'ID задачи': 'id',
                       'Дата': 'date',
                       'Автор.1': 'dzo',
                       'Статус': 'status',
                       'Автор': 'author',
                       'Ответственный':'liable',
                       'Исполнитель':'executor',
                       'Информационная система/Сервис':'service'})
        
        groupedData = df.groupby('date').size().sort_index()
        groupedStatus = df.groupby('status').size().sort_index()
        groupedService = df.groupby('service').size().sort_index()
        groupedDzo = df.groupby('dzo').size().sort_index()
        
        buf_list = []

        fig, ax = plt.subplots()
        bars = ax.bar(groupedData.index, groupedData.values, width=0.5)
        ax.set_xticks(groupedData.index)

        for bar in bars:
            height = bar.get_height()  # Высота столбца
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # Центр столбца
                height,  # Высота текста равна высоте столбца
                f'{int(height)}',  # Текст (значение) над баром
                ha='center',  # Горизонтальное выравнивание
                va='bottom',  # Вертикальное выравнивание
                fontsize=10,  # Размер шрифта
                color='black'  # Цвет текста
            )

        ax.set_title('По дням', fontsize=14, fontweight='bold')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.grid(True)
        buf = BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        buf.seek(0)
        buf_list.append(buf)

        # График для количества запросов по статусам
        fig, ax1 = plt.subplots()
        ax1.plot(groupedStatus.index, groupedStatus.values, marker='o')
        ax1.set_title('Количество запросов по статусам')
        ax1.set_xlabel('Статус')
        ax1.set_ylabel('Количество запросов')
        ax1.grid(True)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        buf_list.append(buf)
        
        fig, ax2 = plt.subplots(figsize=(16, 10), facecolor='white', dpi=80)
        
        # Строим вертикальные линии для количества запросов
        ax2.vlines(groupedService.index, ymin=0, ymax=groupedService.values, color='firebrick', alpha=0.7, linewidth=20)

        # Добавляем текстовые метки на график
        for i, val in enumerate(groupedService.values):
            ax2.text(i, val + 0.5, round(val, 1), horizontalalignment="center")

        # Настройки графика
        ax2.set_title('Количество запросов по сервисам', fontdict={'size':22})
        ax2.set_ylabel('Количество запросов')
        ax2.set_xlabel('Сервис')
        ax2.grid(True)

        # Добавляем цветные прямоугольники на график (как пример)
        p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
        p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
        fig.add_artist(p1)
        fig.add_artist(p2)

        # Сохраняем график в байтовый поток
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        buf_list.append(buf)


        # График для количества запросов по DZO
        fig, ax3 = plt.subplots()
        ax3.plot(groupedDzo.index, groupedDzo.values, marker='o')
        ax3.set_title('Количество запросов по DZO')
        ax3.set_xlabel('DZO')
        ax3.set_ylabel('Количество запросов')
        ax3.grid(True)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        buf_list.append(buf)

        # Отправляем все графики обратно пользователю
        await message.answer("Вот несколько графиков по вашим данным:")

        # Отправляем каждый график по очереди
        for buf in buf_list:
            await message.answer_photo(photo=buf)

        # pd.DataFrame(df.groupby('date').size().sort_index(), columns=['count']).reset_index().to_csv(csv_file, index=False)
        # pd.DataFrame(df.groupby('status').size(), columns=['count']).reset_index().sort_values(by='count', ascending=False).to_csv(csv_file, index=False, encoding='utf-8-sig')
        # pd.DataFrame(df.groupby('service').size().sort_index(), columns=['count']).reset_index().sort_values(by='count', ascending=False).to_csv('./output/03.csv', index=False, encoding='utf-8-sig')
        # pd.DataFrame(df.groupby('dzo').size().sort_index(), columns=['count']).reset_index().to_csv('./output/04.csv', index=False, encoding='utf-8-sig')
        # pd.DataFrame(df.groupby('executor').size().sort_index(), columns=['count']).reset_index().assign(executor=lambda x: x['executor'].apply(lambda name: f"{name.split()[0]} {name.split()[1][0]}." if len(name.split()) > 1 else name)).sort_values(by='count', ascending=False).to_csv('./output/05.csv', index=False, encoding='utf-8-sig')
				
    except Exception as e:
        await message.answer(f"Произошла ошибка при обработке файла: {str(e)}")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
