
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
