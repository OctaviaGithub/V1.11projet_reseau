##Fichier pour les fonctions d'administrateurs.

import module_chat,module_profil,projet_réseau_principal

class User_Permission():

    def __init__(self):
        self.__profil = projet_réseau_principal.Configuration()
        self.__liste_user=["BasicUser","Moderator","Administrator","Owner"]
        self.__perm = {"Owner,add_salon" : True, "Administrator,add_salon" : False, "Moderator,add_salon" : False, "User,add_salon" : False,\
                       "Owner,change_salon" : True, "Administrator,change_salon" : False, "Moderator,change_salon" : False, "User,change_salon" : False,\
                       "Owner,change_role" : True, "Administrator,change_role": False, "Moderator,change_role" : False, "User,change_role" : False,\
                       "Owner,suppr_message" : True, "Administrator,suppr_message" : False, "Moderator,suppr_message" : False, "User,suppr_message": False}
        ##self.__perm = permission de base des quatre membres principaux du réseau.

    def get_liste_perm(self):
        '''Permet de return pour des tests la liste des permissions TRUE / FALSE.'''
        print(self.__perm)

    def change_permission_add_salon(self,nom_role:str):
        '''Permet de changer le TRUE / FALSE d'une permission d'un role.'''
        if self.__profil.get_role(self.__profil.get_role) == self.__liste_user[3]:
            print("#Console | Permission Accordée")
            for i in self.__perm:
                test = (nom_role+",add_salon")
                if str(i) == test :
                    if self.__perm[str(i)] == True:
                        self.__perm[str(i)] = False
                        return "#Console | Changement effectué !"
                    else:
                        self.__perm[str(i)] = True
                        return "#Console | Changement effectué !"
                else:
                    print("Rien n'a été trouvé.")
        else:
            print("#Console | Permission non Accordée. Vous n'êtes pas l'Owner.")

    def change_permission_change_salon(self,nom_role:str):
        '''Permet de changer le TRUE / FALSE d'une permission d'un role.'''
        if self.__profil.get_role(self.__profil.get_role) == self.__liste_user[3]:
            print("#Console | Permission Accordée")
            for i in self.__perm:
                test = (nom_role+",change_salon")
                if str(i) == test :
                    if self.__perm[str(i)] == True:
                        self.__perm[str(i)] = False
                        return "#Console | Changement effectué !"
                    else:
                        self.__perm[str(i)] = True
                        return "#Console | Changement effectué !"
                else:
                    print("Rien n'a été trouvé.")
        else:
            print("#Console | Permission non Accordée. Vous n'êtes pas l'Owner.")

    def change_permission_change_role(self,nom_role:str):
        '''Permet de changer le TRUE / FALSE d'une permission d'un role.'''
        if self.__profil.get_role(self.__profil.get_role) == self.__liste_user[3]:
            print("#Console | Permission Accordée")
            for i in self.__perm:
                test = (nom_role+",change_role")
                if str(i) == test :
                    if self.__perm[str(i)] == True:
                        self.__perm[str(i)] = False
                        return "#Console | Changement effectué !"
                    else:
                        self.__perm[str(i)] = True
                        return "#Console | Changement effectué !"
                else:
                    print("Rien n'a été trouvé.")
        else:
            print("#Console | Permission non Accordée. Vous n'êtes pas l'Owner.")


    def change_permission_suppr_message(self,nom_role:str):
        '''Permet de changer le TRUE / FALSE d'une permission d'un role.'''
        if self.__profil.get_role(self.__profil.get_role) == self.__liste_user[3]:
            print("#Console | Permission Accordée")
            for i in self.__perm:
                test = (nom_role+",suppr_message")
                if str(i) == test :
                    if self.__perm[str(i)] == True:
                        self.__perm[str(i)] = False
                        return "#Console | Changement effectué !"
                    else:
                        self.__perm[str(i)] = True
                        return "#Console | Changement effectué !"
                else:
                    print("Rien n'a été trouvé.")
        else:
            print("#Console | Permission non Accordée. Vous n'êtes pas l'Owner.")









