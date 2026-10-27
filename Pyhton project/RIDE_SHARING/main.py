from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing('Niye Jao')
robin = Rider("Robin", "robin@gmail.com", 236362234, "Gazipur", 1300)
niye_jao.add_rider(robin)

chobir = Driver("Cobir", "cobir@gmail.com", 456455725, "Mirpur")
niye_jao.add_driver(chobir)

robin.request_ride(niye_jao, 'Uttara', "car")
robin.show_current_ride()
chobir.reach_destination(robin.current_ride)
print(niye_jao)


