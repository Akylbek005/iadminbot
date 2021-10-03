from aiogram import types

from data import config
from loader import dp, bot
from keyboards.inline.link_inline import link_panel


@dp.message_handler(commands=['post'])
async def post_command(message: types.Message):
    config.IS_POSTING_REQUESTEQ = True
    await message.answer('Пришлите текст поста или без!')


@dp.message_handler(commands=['setlink'])
async def setlink_command(message: types.Message):
    with open('link.txt', 'w') as f:
        f.write(message.text.replace('/setlink', ' ').strip())
        f.close()

    await message.answer('Ссылка успешно сохранена!')


@dp.message_handler(commands=['getlink'])
async def getlink_command(message: types.Message):
    with open('link.txt', 'r') as f:
        content = f.readlines()
        if not content:
            content = 'Ссылка еще не добавлена'
        else:
            content = f'Текущая ссылка {content[0]}'
        f.close()
    await message.answer(content.strip())


@dp.message_handler()
async def message_handler(message: types.Message):
    if config.IS_POSTING_REQUESTEQ:
        config.IS_POSTING_REQUESTEQ = False
        await message.bot.send_message(config.CHANNEL_ID, message.text, reply_markup=link_panel)
        await message.answer('Пост опубликован')


@dp.callback_query_handler(lambda c: c.data == 'get_link_button')
async def process_callback_get_link_button(c: types.CallbackQuery):
    member = await bot.get_chat_member(config.CHANNEL_ID, c.from_user.id)
    if member['status'] in ['member', 'creator', 'administrator']:
        with open('link.txt', 'r') as f:
            content = f.readlines()
            f.close()
        await bot.answer_callback_query(c.id, f'Ссылка {content[0].strip()}', show_alert=True)
    else:
        await bot.answer_callback_query(c.id, 'Сначала подпишись на канал', show_alert=True)
