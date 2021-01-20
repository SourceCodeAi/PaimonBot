from dhooks import Webhook

def send(url, content):
    hook = Webhook(url)
    hook.send(content)