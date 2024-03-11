import random
import string
import pyfiglet
import hashlib
from hashlib import pbkdf2_hmac


bvn = pyfiglet.figlet_format("Bienvenue")
print(bvn)
print("Bienvenue sur le générateur de mot de passe sécurisé pour système d'exploitation. \n ")

def windows_site():
	#while True:
		try:
			choix = int(input("merci de choisir le nombre de caractère du mot de passe (entre 10 et 100)  : \n \n "))
		except ValueError as e :
			print("Merci d'entrer une valeur numérique.")
		else:
			if 10 <= choix <=  100 :
				taille = choix
				caracteres = "~,@,_,/,+,:"
				mdp = string.ascii_letters + string.digits + caracteres*3
				mdp_genere = ''.join(random.choice(mdp) for i in range(choix))
				print("Voici votre nouveau mot de passe :" ,mdp_genere)



				#break
			else:
				if choix < 10 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE SUPÉRIEUR À 10.")
				elif choix > 100 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE INFÉRIEUR À 100")

def linux():
	#while True:
		try:
			choix = int(input("merci de choisir le nombre de caractère du mot de passe (entre 10 et 100)  : \n \n "))
		except ValueError as e :
			print("Merci d'entrer une valeur numérique.")
		else:
			if 10 <= choix <=  100 :
				taille = choix 



				#break
			else:
				if choix < 10 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE SUPÉRIEUR À 10.")
				elif choix > 100 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE INFÉRIEUR À 100")
def hashage():
	choix = input("Merci d'entrer le mot de passe à hacher  : \n \n ")
	choix_encodage = choix.encode('utf-8')
	salt = '393848492dkfdfj4994'.encode()
	our_app_iters = 500_000
	mdp = hashlib.pbkdf2_hmac('sha256',choix_encodage,salt,our_app_iters)
	hachage = mdp.hex()



	print("Voici votre hash :",hachage)






def debut():
	try:
		choix = int(input("Merci de préciser si vous voulez générer un mot de passe pour linux , ou un mot de passe pour windows et sites webs, ou activer le mode hashe  \n \n TAPEZ 1 POUR UN MOT DE PASSE WINDOWS ET SITES WEBS, TAPEZ 2 POUR MOT DE PASSE LINUX, TAPEZ 3 POUR LE MODE HASHE : \n \n"))
	except ValueError as e :
		print("Erreur")
	else:
		if choix > 3 or choix < 1 :
			print("Vous devez choisir une valeur entre 1 et 3")
		elif choix == 1 :
			windows_site()
		elif choix == 2 :
			linux()
		else :
			hashage()


debut()





