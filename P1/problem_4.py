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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_pool = [group]
    while len(group_pool) != 0:
        item = group_pool.pop()

        users = item.get_users()
        if len(users) != 0:
            if user in users:
                return True

        next_groups = item.get_groups()
        if len(next_groups) != 0:
            group_pool.extend(next_groups)

    return None


if __name__ == "__main__":
    assert is_user_in_group("sub_child_user", parent)
    assert not is_user_in_group("subchild", parent)
    assert not is_user_in_group("children", parent)

