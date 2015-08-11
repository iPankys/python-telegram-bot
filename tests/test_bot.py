#!/usr/bin/env python
# encoding: utf-8
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].


import os
import telegram
import unittest


class BotTest(unittest.TestCase):
    def setUp(self):
        bot = telegram.Bot(token=os.environ.get('TOKEN'))
        self._bot = bot
        print('Testing the Bot API class')

    def testGetMe(self):
        '''Test the telegram.Bot getMe method'''
        print('Testing getMe')
        bot = self._bot.getMe()
        self.assertEqual(120405045, bot.id)
        self.assertEqual('Toledo\'s Palace Bot', bot.first_name)
        self.assertEqual(None, bot.last_name)
        self.assertEqual('ToledosPalaceBot', bot.username)

    def testSendMessage(self):
        '''Test the telegram.Bot sendMessage method'''
        print('Testing sendMessage')
        message = self._bot.sendMessage(chat_id=12173560,
                                        text='Моё судно на воздушной подушке полно угрей')
        self.assertEqual(u'Моё судно на воздушной подушке полно угрей', message.text)

    def testGetUpdates(self):
        '''Test the telegram.Bot getUpdates method'''
        print('Testing getUpdates')
        updates = self._bot.getUpdates()
        self.assertIsInstance(updates[0], telegram.Update)

    def testForwardMessage(self):
        '''Test the telegram.Bot forwardMessage method'''
        print('Testing forwardMessage')
        message = self._bot.forwardMessage(chat_id=12173560,
                                           from_chat_id=12173560,
                                           message_id=138)
        self.assertEqual('Oi', message.text)
        self.assertEqual('leandrotoledo', message.forward_from.username)

    def testSendPhoto(self):
        '''Test the telegram.Bot sendPhoto method'''
        print('Testing sendPhoto - File')
        message = self._bot.sendPhoto(photo=open('tests/telegram.png', 'rb'),
                                      caption='testSendPhoto',
                                      chat_id=12173560)
        self.assertEqual(1451, message.photo[0].file_size)
        self.assertEqual('testSendPhoto', message.caption)

    def testResendPhoto(self):
        '''Test the telegram.Bot sendPhoto method'''
        print('Testing sendPhoto - Resend')
        message = self._bot.sendPhoto(photo=str('AgADAQADr6cxGzU8LQe6q0dMJD2rHYkP2ykABFymiQqJgjxRGGMAAgI'),
                                      chat_id=12173560)
        self.assertEqual('AgADAQADr6cxGzU8LQe6q0dMJD2rHYkP2ykABFymiQqJgjxRGGMAAgI', message.photo[0].file_id)

    def testSendURLPhoto(self):
        '''Test the telegram.Bot sendPhoto method'''
        print('Testing sendPhoto - URL')
        message = self._bot.sendPhoto(photo=str('http://dummyimage.com/600x400/000/fff.jpg&text=telegram'),
                                      chat_id=12173560)
        self.assertEqual(822, message.photo[0].file_size)

    def testSendAudio(self):
        '''Test the telegram.Bot sendAudio method'''
        print('Testing sendAudio - File')
        message = self._bot.sendAudio(audio=open('tests/telegram.ogg', 'rb'),
                                      chat_id=12173560)
        self.assertEqual(9199, message.audio.file_size)

    def testResendAudio(self):
        '''Test the telegram.Bot sendAudio method'''
        print('Testing sendAudio - Resend')
        message = self._bot.sendAudio(audio=str('AwADAQADIQEAAvjAuQABSAXg_GhkhZcC'),
                                      chat_id=12173560)
        self.assertEqual('AwADAQADIQEAAvjAuQABSAXg_GhkhZcC', message.audio.file_id)

    def testSendDocument(self):
        '''Test the telegram.Bot sendDocument method'''
        print('Testing sendDocument - File')
        message = self._bot.sendDocument(document=open('tests/telegram.png', 'rb'),
                                         chat_id=12173560)
        self.assertEqual(12948, message.document.file_size)

    def testResendDocument(self):
        '''Test the telegram.Bot sendDocument method'''
        print('Testing sendDocument - Resend')
        message = self._bot.sendDocument(document=str('BQADAQADHAADNTwtBxZxUGKyxYbYAg'),
                                         chat_id=12173560)
        self.assertEqual('BQADAQADHAADNTwtBxZxUGKyxYbYAg', message.document.file_id)

    def testSendVideo(self):
        '''Test the telegram.Bot sendVideo method'''
        print('Testing sendVideo - File')
        message = self._bot.sendVideo(video=open('tests/telegram.mp4', 'rb'),
                                      caption='testSendVideo',
                                      chat_id=12173560)
        self.assertEqual(326534, message.video.file_size)
        self.assertEqual('testSendVideo', message.caption)

    def testResendVideo(self):
        '''Test the telegram.Bot sendVideo method'''
        print('Testing sendVideo - Resend')
        message = self._bot.sendVideo(video=str('BAADAQADIgEAAvjAuQABOuTB937fPTgC'),
                                      chat_id=12173560)
        self.assertEqual(4, message.video.duration)

    def testResendSticker(self):
        '''Test the telegram.Bot sendSticker method'''
        print('Testing sendSticker - Resend')
        message = self._bot.sendSticker(sticker=str('BQADAQADHAADyIsGAAFZfq1bphjqlgI'),
                                        chat_id=12173560)
        self.assertEqual(39518, message.sticker.file_size)

    def testSendLocation(self):
        '''Test the telegram.Bot sendLocation method'''
        print('Testing sendLocation')
        message = self._bot.sendLocation(latitude=-23.558873,
                                         longitude=-46.659732,
                                         chat_id=12173560)
        self.assertEqual(-23.558873, message.location.latitude)
        self.assertEqual(-46.659732, message.location.longitude)

    def testSendChatAction(self):
        '''Test the telegram.Bot sendChatAction method'''
        print('Testing sendChatAction - ChatAction.TYPING')
        self._bot.sendChatAction(action=telegram.ChatAction.TYPING,
                                 chat_id=12173560)

    def testGetUserProfilePhotos(self):
        '''Test the telegram.Bot getUserProfilePhotos method'''
        print('Testing getUserProfilePhotos')
        upf = self._bot.getUserProfilePhotos(user_id=12173560)
        self.assertEqual(6547, upf.photos[0][0].file_size)
