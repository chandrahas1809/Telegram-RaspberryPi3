import time, datetime
import telepot
import time 
import os 
from telepot.loop import MessageLoop
# Receiving command from Telegram app

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: %s' % command)
    
# Applying condition for coomand

    if (command == 'Hi'):
    # Send back message for hi command
        telegram_bot.sendMessage (chat_id, str("hi Chandrahas"));
        
    # Take a iamge using webcam and send back to Telegram
    
    elif (command == 'Image'):
        os.system('fswebcam -r 320x240 /home/pi/test.jpg');
        #time.sleep(1);
        telegram_bot.sendPhoto (chat_id, photo=open('/home/pi/test.jpg'));
# Authorizing the token number
telegram_bot = telepot.Bot('------- Use here your Token Number -------');
print (telegram_bot.getMe());

MessageLoop(telegram_bot, action).run_as_thread();
print ('Up and Running....')

while 1:
    time.sleep(10)
