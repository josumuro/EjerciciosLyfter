from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def get_rol(self):
     pass

    @abstractmethod
    def has_permission(self,permission):
       rol=self.get_rol()
       if rol =="AdminUser":
          return True
       elif rol=="RegularUser" and permission in ["read"]:
          return True
       return False
    

class AdminUser(User):
    def get_rol(self):
        return "AdminUser"


class RegularUser(User):
    def get_rol(self):
        return "RegularUser"
admin=AdminUser("juan")
regular=RegularUser("pedro")

print(admin.has_permission("delete"))  # Output: True
print(regular.has_permission("delete"))  # Output: False