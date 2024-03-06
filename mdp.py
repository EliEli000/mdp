import random
import string
import pyfiglet
import hashlib


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
				caracteres = "~,@,_,/,+,:,;,=,+,.,%,*,^,#"
				mdp = string.ascii_letters + string.digits + caracteres
				mdp_genere = ''.join(random.choice(mdp) for i in range(choix))
				print("Voici votre nouveau mot de passe :" ,mdp_genere)



				#break
			else:
				if choix < 10 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE SUPÉRIEUR À 10.")
				elif choix > 100 :
					print("VOUS DEVEZ CHOISIR UN NOMBRE DE CARACTÈRE INFÉRIEUR À 100")





def debut():
	try:
		choix = int(input("Merci de préciser si vous voulez générer un mot de passe pour linux , ou un mot de passe pour windows et sites webs  \n \n TAPEZ 1 POUR UN MOT DE PASSE WINDOWS ET SITES WEBS, TAPEZ 2 POUR MOT DE PASSE LINUX: \n \n"))
	except ValueError as e :
		print("Erreur")
	else:
		if choix > 2 :
			print("Vous devez choisir une valeur entre 1 et 2")
		elif choix < 1 :
			print("Vous devez choisir une valeur entre 1 et 2")
		elif choix == 1 :
			windows_site()
		elif choix == 2 :
			linux()


debut()




#rajouter moyen de choisir entre mot de passe pour linux (plus de caractères disponibles) et mot de passe pur windows (moins de disponibles) > FAIT
#Rajouter la fonction qui genere aleatoirement mdp pour linux (rajouter donc les caracteres spéciaux) > FAIT

#nouvelles idées ?
#peut être essayer de rajouter un cracker de mdp, ou le moyen de transformer un mot de passe en hashe
#https://docs.python.org/3/library/hashlib.html (lis ça en vrai )
#https://thepythoncode.com/article/crack-hashes-in-python











