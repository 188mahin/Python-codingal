class spain():
    def capital(self):
        print("the capital of Spain is Madrid")
    def language(self):
        print("the most widely spoken language in Spain is Spanish")
    def type(self):
        print("Spain is highy developed country")
class argentina():
    def capital(self):
        print("the capital of Argentina is Buenos Aires")
    def language(self):
        print("the most widely spoken language in Argentina is Spanish")
    def type(self):
        print("Argentina is a developing country")
obj=spain()
ob=argentina()
for countries in (obj,ob):
    countries.capital()
    countries.language()
    countries.type()