class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

#recursive function
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users=group.get_users()
    if user in users:
        return True
    else:
        groups=group.get_groups()
        for x in groups:
            if is_user_in_group(user,x):
                return True
    return False


#Given Testcase 1----------------------
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

#check
print("Sub_child_user is in {} - {} ".format(parent.get_name(),is_user_in_group("sub_child_user",parent)))

#given Testcase2
#My test cases
root=Group('root')
TANK=Group("TANK")
besties=Group('besties')
best1=Group('best1')
best2=Group('best2')
user1="Alok"
user2="Brij"
user3="Kriti"
user4="Deepak"
user5="Ajay"
user6="Praveen"
user7="Nidhi"
user8="Anu"
user9="Tanu"
user10="Shivam"
root.add_group(TANK)
TANK.add_user(user9)
TANK.add_user(user7)
TANK.add_user(user3)
root.add_group(besties)
besties.add_group(best1)
besties.add_group(best2)
best1.add_user(user1)
best1.add_user(user2)
best1.add_user(user4)
best1.add_user(user5)
best2.add_user(user6)
best2.add_user(user10)

#check1
print("Ayush is in {} - {} ".format(root.get_name(),is_user_in_group("Ayush",root)))
#check2
print("Alok is in {} - {} ".format(TANK.get_name(),is_user_in_group("Alok",TANK)))
#check3
print("Alok is in {} - {} ".format(best2.get_name(),is_user_in_group("Alok",best2)))
#check4
print("Alok is in {} - {} ".format(besties.get_name(),is_user_in_group("Alok",besties)))
