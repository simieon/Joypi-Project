#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Festlegen des LCDs in die Variable LCD
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

while True:

    try:
        # Hintergrundbeleuchtung einschalten
        lcd.backlight = True

        lcd.message = f"Temperatur:{1}\x00C\nFeuchtigkeit:{1}%"
    except KeyboardInterrupt:
        # LCD ausschalten.
        lcd.clear()
        lcd.message = "ERROR..."
        time.sleep(2.0)
        lcd.backlight = False
