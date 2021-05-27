import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(receiver, subject, message ):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('techboxx7@gmail.com', 'techyy131')
    email = EmailMessage()
    email['From'] = 'techboxx7@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'friend 1': 'asmajain789@gmail.com',
    'friend 2': 'ajayjainaj014@gmail.com',
    'friend 3': 'brainogenous@gmail.com',
    'friend 4': 'amankumarjagdev@gmail.com',
    'friend 5': 'mittalvertika1@gmail.com',
    'friend 6': 'jatinjp@gmail.com',
    'friend 7': 'thakurpalak729@gmail.com'
}


def get_email_info():
    talk('To whom you want to send email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is your email's subject?")
    subject = get_info()
    talk("Speak the message that you want to send")
    message = get_info()

    send_email(receiver, subject, message)

    talk('email sent!')
    talk('Do you want to send more emails?')
    more_email = get_info()
    if 'yes' in more_email:
        get_email_info()


get_email_info()



