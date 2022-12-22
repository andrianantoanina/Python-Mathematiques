
#programmation orientée objet 
class CompteBancaire:
    def __init__(self, nom_titulaire, solde=0):
        self.nom_titulaire = nom_titulaire
        self.solde = solde

    def ajouter_argent(self, montant):
        self.solde += montant

    def retirer_argent(self, montant):
        self.solde -= montant

    def __str__(self):
        return f"Le titulaire du compte est {self.nom_titulaire} et il a {self.solde}€ sur son compte."

compte1 = CompteBancaire("Marie", 1000)
compte2 = CompteBancaire("Jean", 2000)

print(compte1)
print(compte2)

compte1.ajouter_argent(500)
compte2.retirer_argent(500)

print(compte1)
print(compte2)

#Ce programme définit une classe CompteBancaire avec trois méthodes :

#__init__ : constructeur de la classe, qui initialise les attributs nom_titulaire et solde lorsqu'un nouvel objet de la classe est créé.
#ajouter_argent : qui permet d'ajouter de l'argent au solde du compte.
#retirer_argent : qui permet de retirer de l'argent du solde du compte.
#Il y a également une méthode __str__ qui permet de personnaliser la façon dont l'objet est affiché lorsqu'on utilise la fonction print().

#Le programme crée deux objets de la classe CompteBancaire, compte1 et compte2, et affiche leur état initial. Ensuite, il ajoute de l'argent au compte de Marie et retire de l'argent du compte de Jean, et affiche à nouveau l'état de chaque compte.
