
class Smartphone:
    def __init__(self, brand, model, price):
        # Encapsulation: price is private
        self.brand = brand
        self.model = model
        self.__price = price  

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} - Price: ${self.__price}"


class GamingSmartphone(Smartphone):

    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"🎮 Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU!")

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition) - GPU: {self.gpu}, Price: ${self.get_price()}"



if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S21", 999)
    print(phone1)
    phone1.make_call("123-456-789")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1200, "Adreno 730")
    print(gaming_phone)
    gaming_phone.play_game("PUBG Mobile")
