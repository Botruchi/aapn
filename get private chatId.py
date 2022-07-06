import amino
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.BLUE)
print(Style.NORMAL)
print(pyfiglet.figlet_format("Tcxeh", font="slant"))
print(pyfiglet.figlet_format("Private ChatId", font="small"))
client = amino.Client()
email = "iqqbu6epv2zl@1secmail.org"
password = "Tcxeh6"
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]
print(f"""
⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　
Community comId >> {communityid}

_________________________________

ChatId >> {chatx}
⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　⋇⋆✦⋆⋇　
"""
)