# terminal command:
#     ls
#     cd
#     unzip
#     poweroff
#     reboot
#     cat
#     nano
#     rm
#     mv


class A:
    def a(self):
        return "a"


class C:
    def a(self):
        return "c"


class B(A , C):
    pass

