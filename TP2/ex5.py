class Animal:
    def faire_du_bruit(self):
        pass
class Chat:
    def faire_du_bruit(self):
        return "Meow Meow!"
class Chien:
    def faire_du_bruit(self):
        return "Woof Woof!"
        
# Test
chien = Chien()
chat = Chat()
print (chien.faire_du_bruit())
print (chat.faire_du_bruit())