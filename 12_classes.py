class myClass:

    def __init__(self, fan, table):
        self.fan = fan
        self.table = table

    def give_me_the_count_of_table_fan(self):
        return f"Count of table {self.table} and count of fan {self.fan}"
    
    def _hello(self):
        return "hello"
    
    def __bye(self):
        return "Bye"


oneIns = myClass(5, 50)
print(oneIns.give_me_the_count_of_table_fan())
print(oneIns._hello())
print(oneIns.__bye())
