from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

relay_pin = 14  

GPIO.setmode(GPIO.BCM)    
GPIO.setup(relay_pin, GPIO.OUT)

kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500, 2500) 
current_angle = 90
min_angle, max_angle = 0, 180
kit.servo[0].angle = current_angle

def fire():
	GPIO.output(relay_pin, GPIO.HIGH)  
	time.sleep(0.5)                    
	GPIO.output(relay_pin, GPIO.LOW)   
		
try:
	GPIO.output(relay_pin, GPIO.LOW)
			

	app = Flask(__name__)

	@app.route("/")
	def home():
		return render_template("index.html")

	@app.route("/move")
	def move():
		global current_angle
		direction = request.args.get("dir")
		print(f"Move command received: {direction}")
		if direction == 'right':
			current_angle += 10
			if min_angle <= current_angle <= max_angle:
				kit.servo[0].angle = current_angle
				kit.servo[0].angle = current_angle
			else: current_angle -= 10
		elif direction == 'left':
			current_angle -= 10
			if min_angle <= current_angle <= max_angle:
				kit.servo[0].angle = current_angle
				kit.servo[0].angle = current_angle
			else: current_angle += 10
		return f"Moved {direction}"

	@app.route("/fire")
	def fire_gun():
		print("FIRE command received")
		GPIO.output(relay_pin, GPIO.HIGH)
		return "FIRING"

	@app.route("/stopFire")
	def stop_gun():
		print("STOP command recieved")
		GPIO.output(relay_pin, GPIO.LOW)
		return "STOPPED"

	if __name__ == "__main__":
		app.run(host="0.0.0.0", port=5000) 
finally:
	GPIO.cleanup()
