# class MyString:
#     def __init__(self, value: str):
#         self.value = value

#     def add_exclamation(self) -> 'MyString':
#         self.value += ".....!"
#         return self

#     def make_upper(self) -> 'MyString':
#         self.value = self.value.upper()
#         return self

# my_string = MyString("hello")
# my_string.add_exclamation().make_upper()

# print(my_string.value) # output: "HELLO!"


# class Person:
#     def __init__(self, name: str):
#         self.name = name
#         self.name_length = None
#         self.email = None

#     def set_name_length(self) -> "Person":
#         self.name_length = len(self.name)
#         return self

#     def create_email(self, surname: str) -> "Person":
#         DEFAULT_EMAIL_PROVIDER = "@gmail.com"
#         self.email = self.name + "." + surname + DEFAULT_EMAIL_PROVIDER
#         return self

#     def get_name(self) -> str:
#         return self.name


# person = Person("Jonas")
# person.set_name_length().create_email(surname="Jonaitis")
# print(f"Email: {person.email}\nName length: {person.name_length}")


class A:
    def __init__(self, value: int) -> None:
        self.value = value

    def increment(self) -> None:
        self.value += 1


class C:
    def __init__(self, lempa) -> None:
        self.lempa = lempa


class B(A, C):
    def __init__(self, value: int, step: int) -> None:
        super().__init__(value=value)
        C.__init__(self, lempa=step)
        self.step = step

    def increment(self) -> None:
        super().increment()
        self.value += self.step


b = B(5, 3)
b.increment()
print(b.value)  # output: 9



#offtopic
# class A:
#     def __init__(self, value: int) -> None:
#         self.value = value


# print(dir(A))
# for x in dir(A):
#     print(x)
