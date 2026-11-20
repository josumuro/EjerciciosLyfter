

class Notifier:
    def send(self,message):
        raise NotImplementedError("Subclasses must implement this method")
    
class EmailNotifier(Notifier):
    def send(self,message):
        print(f"Sending email: {message}")

class SMSNotifier(Notifier):
    def send(self,message):
        print(f"Sending SMS:{message}")

class WhatsAppNotifier(Notifier):
    def send(self,message):
        print(f"Sending WhatsApp message: {message}")

def broadcast(notifiers, message):
        for notifer in notifiers:
            notifer.send(message)
# Demo
notifiers = [EmailNotifier(), SMSNotifier(), WhatsAppNotifier()]
broadcast(notifiers, "Hola mundo")

