from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()
print(drone.get_battery())
drone.move_up(50)

for i in range(2):
    drone.rotate_clockwise(360)
    drone.rotate_counter_clockwise(1080)
    drone.move_down(50)
    drone.move_up(50)


print(drone.get_battery())
drone.land()

drone.end()
