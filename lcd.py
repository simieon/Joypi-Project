#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# define LCD rows and cols.
lcd_columns = 16
lcd_rows    = 2

# initialising an I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# initialising of lcd variable
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

degree_symbol = (
	0b00111,
	0b00101,
	0b00111,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
)
# Store the custom character in CGRAM location 0
lcd.create_char(0, degree_symbol)

def shutdown_lcd():
    lcd.clear()
    lcd.message = "Shutting down..."
    time.sleep(1)
    lcd.clear()
    lcd.backlight = False

def show_data_on_lcd(temperature: int, humidity: int):
    # turn on Backlight
    lcd.backlight = True

    lcd.message = f"Temperatur:{temperature}\x00C\nFeuchtigkeit:{humidity}%"
