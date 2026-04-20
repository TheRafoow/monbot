nom = "MrBot"
version = "1.0"
print(f"Je suis {nom} version {version}")
print("Prêt à devenir un bot Telegram 🤖")
prenom = input("C'est quoi ton prénom ? ")
print(f"Bonjour {prenom} ! Je suis {nom} 🤖")
if prenom == "Raphaël":
    print("Tiens, c'est toi le créateur ! 👑")
else:
    print(f"Bienvenue {prenom} sur {nom} !")
while True:
    message = input("Dis quelque chose à MrBot : ")
    if message == "stop":
        print("À bientôt ! 👋")
        break
    print(f"MrBot reçoit : {message}")
